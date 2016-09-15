from dxfwrite import DXFEngine as dxf
from trophy import text_align, draw, save_file
import sys
import os
import csv

# TODO REMOVE! ADD A REFPOINT GENERATOR .FEAT SHOVEL!
refpoints = [
    (0,0),
    (50,0),
    (100,0),
    (150,0),
    (200,0)

]


__author__ = 'Shovel, Jack, and Archie @sydneyboyshigh.com All Rights Unreserved'
__version__ = 'Beta 1.2'
plaque_len = 40
plaque_height = 20
half_len=plaque_len//2

K_NAME = "Plaque Generator"

font_size = 4

def insert_plaque(insertpoint, name, year, drawing):
    x,y = insertpoint
    text_align(str(name), half_len+x, plaque_height//4+y+1, font_size,drawing,mirror=None)
    text_align(str(year), half_len+x, (plaque_height//4)*3+y, font_size, drawing, mirror=None)
    # go up
    draw(x,y,x,y+plaque_height,drawing)
    # go up then right
    draw(x,y+plaque_height,x+plaque_len,y+plaque_height,drawing)
    # then go down
    draw(x+plaque_len,y+plaque_height,x+plaque_len,y,drawing)
    # finally go left
    draw(x+plaque_len,y,x,y,drawing)





def csv_to_plaque(path, filename='output', outpath=''):
    """Reads from a csv, plaquing all of the things"""
    drawing = None
    try:
        with open(os.path.expanduser(path)) as f:
            reader = csv.reader(f)
            drawing_counter = 0
            counter = 0
            for iteration, line in enumerate(reader):
                if line[0].startswith('##') or line[1].startswith('##'): # comment line
                    continue

                if len(line) != 2:  # invalid line
                    print("Line %d is invalid [%s]" % (iteration+1, line))



                else:
                    name, year = line
                    if len(name) == 0 and len(year) == 0: # empty line,created by EXCLE WHEN YOU PRESS ARROW DOWN COMMAND
                        continue

                    if len(name) == 0 or len(year) == 0:
                        print("Length of line %d, is invalid (one entry is 0 length)" % (iteration+1))
                        continue

                    if counter % len(refpoints) == 0: # is start:
                        if drawing:
                            save_file(drawing, filename, outpath, drawing_counter)
                            drawing_counter += 1
                        drawing = dxf.drawing()
                    insert_plaque(refpoints[counter%len(refpoints)], name, year,drawing)


                    counter += 1
            if counter != 0:
                save_file(drawing, filename, outpath, drawing_counter)




    except FileNotFoundError:
        print("file '%s' not found! Aborting"% path)
        sys.exit(-4)



def main(argv):
    arg_delete_csv = False
    arg_filename = ['','output']
    arg_dummy = False

    if len(argv) > 1:

        # there are arguments
        if argv[1] == '--help' or argv[1] == '-help':
            print("USAGE:")
            print("%-30s" % ('\t' + str(K_NAME) + ' [OPTIONS] (CSV)'))
            print("\tCSV - Path to CSV file")
            print('\n')

            print("OPTIONS: (-- and - can be used)")
            print("%-15s %s" % ("\t--interact", "Enable interactive input with automatic formatting, saving as a csv when done"))
            print("%-15s %s" % ("\t--delete-csv", "Deletes the csv file after successful reading"))
            print("%-15s %s" % ("\t--filename (filename)", "Name the output files"))
            print("%-15s %s" % ("\t--fileout (filepath)", "Directory where output is sent"))
            print("%-15s %s" % ("\t--dummy", "Do not create output files"))

            sys.exit(0)
        argv.pop(0)

        while argv:
            i = argv.pop(0)

            if i.startswith('--') or i.startswith('-'):
                if i == '--interact' or i == '-interact': # allows interative input:
                    filepath = input("Enter new csv file path (default temp.csv): ")
                    if not filepath:
                        filepath = 'temp.csv'
                    print("Enter name and year seperated by commas: ")

                    with open(filepath, 'w',encoding='utf8',newline='') as f:
                        csvfile = csv.writer(f)
                        line = input(">> ")
                        while line:
                            if len(line.split(',')) == 2:
                                line = line.replace('\n', '').split(',')
                                csvfile.writerow([' '.join(line[0].title().lstrip().rstrip().split()), line[1].replace(' ', '')])

                            else:
                                print("Invalid input")
                            line = input(">> ")
                    print(filepath)
                    argv.append(filepath)


                elif i == '--delete-csv' or i == '-delete-csv':  # delete csv file
                    arg_delete_csv = True

                elif i == '--filename' or i == '-filename':
                    if arg_filename[1] != 'output':
                        print("Duplicate --filename option")
                        sys.exit(-1)
                    arg_filename[1] = argv.pop(0)

                elif i == '--fileout' or i == '-fileout':
                    if arg_filename[0]:
                        print("Duplicate --fileout option")
                        sys.exit(-1)
                    arg_filename[0] = argv.pop(0)

                elif i == '--dummy' or i == '-dummy':
                    arg_dummy = True



                else:
                    print(i, "is an invalid option")
                    sys.exit(-1)

            else:
                # must be CSV path -- if override is speciifed then use the overide

                if arg_filename[0] and not (arg_filename[0].endswith('\\') or arg_filename[0].endswith('/')):
                    if os.name == 'nt':
                        arg_filename[0] += '\\'
                    else:
                        arg_filename[0] += '/'
                print(i, 'fill')
                print("Reading from '%s'" % (i))
                if arg_dummy:
                    sys.exit(0)
                if os.path.exists(os.path.expanduser(i)):
                    csv_to_plaque(i, filename=''.join(arg_filename))
                    print('Outputing to "%s' % ''.join(arg_filename))
                    if arg_delete_csv:
                        os.remove(i)
                    sys.exit(0)

                else:
                    print("CSV cannot be found")
                    sys.exit(-2)

        # sys.argv finished reading without hitting a csv file at the end

        print("No csv file specified")
        sys.exit(-3)


    # no options at all
    else:
        print("Usage: %s [OPTIONS] CSV" % K_NAME)
        print('Type %s --help to see options' % K_NAME)









if __name__ == "__main__":
    main(sys.argv)

