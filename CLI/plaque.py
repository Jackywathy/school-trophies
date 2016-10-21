from dxfwrite import DXFEngine as dxf

from CLI.trophy import text_align, draw, save_file, board_len, board_height

__author__ = 'Shovel, Jack, and Archie @sydneyboyshigh.com All Rights Unreserved'
__version__ = 'Beta 1.3'
K_NAME = "plaque"

plaque_len = 40
plaque_height = 20
half_len=plaque_len//2
half_height = plaque_height//2

total_plaque = 154
PLAQUE_DEFAULT = tuple(range(total_plaque))

space = 10 # the start point from top left
tolerance = 5
def generate_ref_plaque(s,h=plaque_height,w=plaque_len):
    """
    PlaQue Stuffz # SHOVEL @)!^1
    :retu,color=255rn: list of ref points
    """
    ref = []
    y,y_next = s+h,s+h+s+h
    x,x_next = s,s+w+s
    while (y_next) <= board_height:
        while (x_next) <= board_len:
            ref.append((x,y))
            x,x_next = x_next, x_next+s + w
        y,y_next = y_next, y_next+s+h
        x, x_next = s, s+w+s
    return ref

refpoints = generate_ref_plaque(s=space)
font_size = 4
def insert_plaque(insertpoint, name, year, drawing, plaque_len=plaque_len,plaque_height=plaque_height):
    x,y = insertpoint
    text_align(str(name), half_len+x, y - plaque_height//4*3, font_size,drawing,mirror=None)
    text_align(str(year), half_len+x, y - plaque_height//4, font_size, drawing, mirror=None)
    draw(x,y,x,y-plaque_height,drawing)
    draw(x,y-plaque_height,x+plaque_len,y-plaque_height,drawing)
    draw(x+plaque_len,y-plaque_height,x+plaque_len,y,drawing)
    draw(x+plaque_len,y,x,y,drawing)


def generate_template_plaque(drawing,h=plaque_height,w=plaque_len):
    draw(0,0,600,0,drawing,color=255)
    draw(600,0, 600,450,drawing,color=255)
    draw(600,450, 0,450,drawing,color=255)
    draw(0,450, 0,0,drawing,color=255)
    for i,each in enumerate(generate_ref_plaque(space)):
        insert_plaque(each, i,'',drawing,w,h)
    return drawing


def csv_to_plaque(csv_stream, filename='output', outpath='', outline=False, logopoints=False, validpoints=(0,1,2,3,4,5,6,7,8,9),debugstring='',simulate=False, do_corners=False):
    """Reads from a csv, plaquing all of the things"""
    has_content = False
    if logopoints:
        print("LOGOPOJTS IS DEPRECIATED")
    if do_corners:
        print("not yet implemented! do_corners (plaque)")
    current_drawing = dxf.drawing()
    if outline:
        generate_template_plaque(drawing=current_drawing)
        for iteration,valid in enumerate(validpoints):
            try:
                line = next(csv_stream)
            except StopIteration:
                if has_content and not simulate:
                    save_file(current_drawing, filename, outpath)
                raise
            # line is next item
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

                else:
                    insert_plaque(refpoints[iteration%len(refpoints)], name, year, current_drawing)
                    has_content = True
        if has_content and not simulate:
            save_file(current_drawing, filename,outpath)

if __name__ == "__main__":
    save_file(generate_template_plaque(dxf.drawing()), 'template')
    print(refpoints)

