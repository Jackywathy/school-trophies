from dxfwrite.const import CENTER
import dxfwrite
from dxfwrite import DXFEngine as dxf
import os
import csv
import sys

K_MAX_ITER = 100
K_NAME = 'Trophy'

__author__ = 'Shovel, Jack, and Archie @sydneyboyshigh.com All Rights Unreserved'
__version__ = 'Beta 1.2'

h1=155.5 
h2= 225 
w = 90.4 
BLACK = 250

file_out = []
logo_width = float(40)
logo_height = float(120)

# sum constants
mid_trophy = 45
crest_y = 129
sbhs_y = 120 # sydney boys high
sac_y = 110   # student award scheme
the_y = 91
school_y = 79
trophy_y = 67
awarded_y = 44.5
name_y = 34.5
year_y = 24

#
# Trophy parts are inserted with the midpint being (mid_trophy)
# and the y points being these constants
#

def generate_ref_point(h1,h2,w):
    """
    Shovel's reference point generator: returns a list of 10 reference points
    that each should be the bottom left corner of a trophy
    """
    ref = []
    xgap = (600-(h1+h2+w))/4
    ygap1 = (450-(4*w))/5
    ygap2 = (450-(h1+h2))/3
    # first collumn ref points
    ref.append((xgap,ygap1+w))
    ref.append((xgap,2*ygap1+2*w))
    ref.append((xgap,3*ygap1+3*w))
    ref.append((xgap,4*ygap1+4*w))
    # second collumn ref points
    ref.append((2*xgap+h1+h2,ygap1))
    ref.append((2*xgap+h1+h2,2*ygap1+w))
    ref.append((2*xgap+h1+h2,3*ygap1+2*w))
    ref.append((2*xgap+h1+h2,4*ygap1+3*w))
    # third collumn ref points
    ref.append((3*xgap+h1+h2,ygap2))
    ref.append((3*xgap+h1+h2+w,2*ygap2+h2+h1))
    return ref


def generate_template(h1,h2,w,drawing):
    drawing.add(dxf.line((0, 0), (600,0), color=255, layer='LINES', thickness=0.00))
    drawing.add(dxf.line((600, 0), (600,450), color=255, layer='LINES', thickness=0.00))
    drawing.add(dxf.line((600,450), (0,450), color=255, layer='LINES', thickness=0.00))
    drawing.add(dxf.line((0,450), (0,0), color=255, layer='LINES', thickness=0.00))
    refpoint = generate_ref_point(h1,h2,w)
    for i in refpoint[:4]:
        x,y = i
        draw(x,y,x+h1,y,drawing)
        draw(x,y,x,y-w,drawing)
        draw(x,y-w,x+h2,y-w,drawing)
        draw(x+h1,y,x+h2,y-w,drawing)
    for i in refpoint[4:8]:
        x,y=i
        draw(x,y,x-h1,y,drawing)
        draw(x,y,x,y+w,drawing)
        draw(x,y+w,x-h2,y+w,drawing)
        draw(x-h2,y+w,x-h1,y,drawing)
    x,y = refpoint[-2]
    draw(x,y,x,y+h1,drawing)
    draw(x,y,x+w,y,drawing)
    draw(x+w,y,x+w,y+h2,drawing)
    draw(x+w,y+h2,x,y+h1,drawing)
    x,y = refpoint[-1]
    draw(x,y,x,y-h1,drawing)
    draw(x,y,x-w,y,drawing)
    draw(x-w,y,x-w,y-h2,drawing)
    draw(x-w,y-h2,x,y-h1,drawing)


def draw(x,y,x1,x2,d):
    d.add(dxf.line((x,y),(x1,x2),color=1, layer='LINES',thickness=0.01))


def text_align(text, x_align, y_align, height, d ,style= "TIMES_ITALIC",rotation=0, color=BLACK):
    """Creates text with the middle aligned to x_al. and y_al."""
    text = dxf.text(text, height = height,mirror=dxfwrite.MIRROR_X,halign=CENTER, alignpoint = (x_align,y_align),
                    style=style, layer='LINES', rotation=rotation, color=color, linetype='ByBlock')
    d.add(text)


def add_school_trophy(ref_point, drawing, name, year, long_side_dir):
    x_r, y_r = ref_point
    if long_side_dir == 'down':
        # long side is down!
        rotation = 270
        file_out.append((x_r + crest_y, y_r -mid_trophy, '270'))

        x_sbhs,y_sbhs = x_r + sbhs_y, y_r - mid_trophy
        x_sac, y_sac = x_r + sac_y,  y_r - mid_trophy
        x_the, y_the = x_r + the_y, y_r - mid_trophy
        x_school, y_school = x_r + school_y, y_r - mid_trophy
        x_trophy,y_trophy = x_r + trophy_y, y_r - mid_trophy
        x_awarded, y_awarded = x_r + awarded_y, y_r - mid_trophy
        x_name, y_name = x_r + name_y, y_r - mid_trophy
        x_year, y_year = x_r + year_y, y_r - mid_trophy

    elif long_side_dir == 'up':
        # if trophy is pointing up
        rotation = 90
        file_out.append((x_r - crest_y, y_r + mid_trophy, '090'))

        x_sbhs,y_sbhs = x_r - sbhs_y, y_r + mid_trophy
        x_sac, y_sac = x_r - sac_y,  y_r + mid_trophy
        x_the, y_the = x_r - the_y, y_r + mid_trophy
        x_school, y_school = x_r - school_y, y_r + mid_trophy
        x_trophy,y_trophy = x_r - trophy_y, y_r + mid_trophy
        x_awarded, y_awarded = x_r - awarded_y, y_r + mid_trophy
        x_name, y_name = x_r - name_y, y_r + mid_trophy
        x_year, y_year = x_r - year_y, y_r + mid_trophy

    elif long_side_dir == 'right':
        # if the trophy is straight
        rotation = 0
        file_out.append((x_r+mid_trophy, y_r+crest_y, '000'))
        x_sbhs,y_sbhs = mid_trophy + x_r, sbhs_y + y_r
        x_sac, y_sac  = mid_trophy + x_r, sac_y  + y_r
        x_the, y_the  = mid_trophy + x_r, the_y  + y_r
        x_school, y_school   = mid_trophy + x_r, school_y + y_r
        x_trophy, y_trophy   = mid_trophy + x_r, y_r + trophy_y
        x_awarded, y_awarded = mid_trophy + x_r, y_r + awarded_y
        x_name, y_name= mid_trophy + x_r, y_r + name_y
        x_year, y_year= mid_trophy + x_r, y_r + year_y

    elif long_side_dir == 'left':
        # if it is backwards
        rotation = 180
        file_out.append((x_r-mid_trophy, y_r - crest_y, '180'))
        x_sbhs,y_sbhs = x_r-mid_trophy, y_r  - sbhs_y
        x_sac, y_sac = x_r-mid_trophy,  y_r  - sac_y
        x_the, y_the = x_r-mid_trophy,  y_r  - the_y
        x_school, y_school = x_r-mid_trophy, y_r - school_y
        x_trophy, y_trophy = x_r-mid_trophy, y_r - trophy_y
        x_awarded, y_awarded= x_r-mid_trophy,y_r - awarded_y
        x_name, y_name = x_r-mid_trophy, y_r - name_y
        x_year, y_year = x_r-mid_trophy, y_r - year_y

    else:
        raise ValueError('long side direction must be down, up, right or left')

    if len(name) > 23:
        print("Name must be shorter than 23 letters! Skipping", (name, year, ref_point))
        with open('stderr.txt', 'a') as f:
            print("Name must be shorter than 23 letters! Skipping", (name, year, ref_point), file=f)

    text_align('Sydney Boys High School', x_sbhs, y_sbhs, 4.7, drawing, rotation=rotation)
    text_align('Student Award Scheme', x_sac, y_sac, 5.7,drawing, rotation=rotation)
    text_align("The", x_the, y_the, 10.5, drawing, rotation=rotation)
    text_align("School", x_school, y_school, 10.5, drawing, rotation=rotation)
    text_align("Trophy",x_trophy, y_trophy, 10.5, drawing, rotation=rotation)
    text_align("awarded to", x_awarded, y_awarded, 7, drawing, rotation=rotation)
    text_align(name.upper(), x_name,y_name, 4.5, drawing, style='STANDARD', rotation=rotation)
    text_align(str(year), x_year, y_year, 6, drawing,rotation=rotation)
    
ref_points = (generate_ref_point(h1,h2,w))


def save_file(drawing, filename='output', path = '', start_iter = 1):
    default_iter = start_iter
    path += filename
    if path.endswith('.dxf'):
        path = path[:-4]
    counter = 0
    while True:

        try:
            if counter > K_MAX_ITER:
                input("Over 100 trophies generated: Pausing Until Enter Button is pressed. Please empty out "
                      "the directory/path supplied (%s)" % path)
                start_iter = default_iter
            temp = path + str(start_iter) + '.dxf'
            drawing.saveas(temp)
            break
        except PermissionError:
            start_iter += 1
            continue
        

def write_points():
    with open('logopoints.txt', 'w') as f:
        for iteration, item in enumerate(file_out):
            if iteration >= 10:
                return
            print(str(item[2]), "{0:.2f}".format(item[0]) + ',' + "{0:.2f}".format(item[1]), file = f)

# format of this file
#
# first three letters are 000, 090, 180, 270, sepecifying the rotation
# then the rest is in this form x_cord,ycord
#  Example: 000 100,200
#           180 200,300
# this file only needs to be generated once, and placed in autocad support pat
#
def read_csv(path, filename='output', outpath='', outline=False, logopoints=False):
    """Reads from a csv, trophifying all of the things"""
    with open(path) as f:
        with open('stderr.txt', 'a') as stderr:
            reader = csv.reader(f)
            counter = 0
            drawing_counter = 0
            for iteration, line in enumerate(reader):
                if line[0].startswith('##') or line[1].startswith('##'): # comment line
                    continue

                if len(line) != 2:  # invalid line
                    stderr.write(' '.join(line) + 'Line %d' % iteration+1)
                    print("Error happened on line %d" % iteration+1)

                else:
                    name, year = line

                    if counter == 0:
                        _drawing = dxf.drawing()
                        drawing_counter += 1
                        if outline:
                            generate_template(h1,h2,w,_drawing)

                    if counter <= 3:  # trophies on the left, pointing down
                        add_school_trophy(ref_points[counter], _drawing, name, year, 'down')

                    elif counter <= 7:
                        add_school_trophy(ref_points[counter], _drawing, name, year, 'up')

                    elif counter == 8:
                        add_school_trophy(ref_points[counter], _drawing, name, year, 'right')

                    elif counter == 9:
                        add_school_trophy(ref_points[counter], _drawing, name, year, 'left')
                        counter = -1
                        save_file(_drawing, filename, outpath, drawing_counter)

                    counter += 1
            if counter != 0:
                save_file(_drawing, filename, outpath, drawing_counter)
            if logopoints:
                write_points()


def main():
    arg_outline = False
    arg_gen_points = False
    arg_delete_csv = False

    if len(sys.argv) > 1:
        # there are arguments
        if sys.argv[1] == '--help' or sys.argv[1] == '-help':
            print("USAGE:")
            print("%-30s" % ('\t' + str(K_NAME) + ' [OPTIONS] CSV\n'))

            print("OPTIONS: (-- and - can be used)")
            print("%-30s %s" %("\t--outline", "Draw a outline around the trophy"))
            print("%-30s %s" %("\t--interact", "Enable interactive input with automatic formatting, saving as a csv when done"))
            print("%-30s %s" % ("\t--interact-noformat", "Enable interactive input, saving as a csv when done, without automatic formatting"))
            print("%-30s %s" % ("\t--gen-points", "Also generate a logopoints.txt for usage in LISP"))
            print("%-30s %s" % ("\t--delete-csv", "Deletes the csv file after successful reading"))
            sys.exit(0)

        for i in sys.argv[1:]:
            print(i)
            if i.startswith('--') or i.startswith('-'):
                if i == '--outline' or i == '-outline':  # makes the outline!
                    arg_outline = True
                elif i == '--interact' or i == '-interact': # allows interative input: TODO FINISH!
                    filepath = input("Enter new csv file path (default temp.csv): ")
                    if not filepath:
                        filepath = 'temp.csv'

                    with open(filepath, 'w',encoding='utf8',newline='') as f:
                        csvfile = csv.writer(f)
                        line = input("Enter name and year seperated by commas: ")
                        while line:
                            if len(line.split(',')) == 2:
                                line = line.replace('\n', '').split(',')
                                csvfile.writerow([' '.join(line[0].title().lstrip().rstrip().split()), line[1].replace(' ', '')])

                            else:
                                print("Invalid input")
                            line = input("Enter name and year seperated by commas: ")
                        sys.argv.append(filepath)

                elif i == '--gen-points' or i == '-gen-points': # generate a logopoints.txt
                    arg_gen_points = True

                elif i == '--delete-csv' or i == '-delete-csv':  # delete csv file
                    arg_delete_csv = True

                else:
                    print(i, "is an invalid option")
                    sys.exit(-1)

            else:
                # must be CSV path
                if os.path.exists(i):
                    read_csv(i, outline=arg_outline, logopoints=arg_gen_points)
                    print(sys.path)
                    if arg_delete_csv:
                        os.remove(i)

                    sys.exit(0)

                else:
                    print("csv cannot be found")
                    sys.exit(-2)

        print("No csv file specified")
        sys.exit(1)



    else:
        print("Usage: %s [OPTIONS] CSV" % K_NAME)
        print('Type %s --help to see options' % K_NAME)

if __name__ == "__main__":
    main()

