from dxfwrite.const import CENTER
import dxfwrite
from dxfwrite import DXFEngine as dxf
import os

board_len = 600
board_height = 450
K_MAX_ITER = 100
K_NAME = 'Trophy'

__author__ = 'Shovel, Jack, and Archie @sydneyboyshigh.com All Rights Unreserved'
__version__ = 'Beta 1.3'

h1 = 155.5
h2 = 225
w = 90.4 
K_BLACK = 250

mid_trophy = 45  # middle of trophy, in Y
sbhs_y = 120     # sydney boys high
sac_y = 110      # student award scheme
the_y = 91       # the
school_y = 79    # school
trophy_y = 67    # trophy
awarded_y = 44.5 # awarded to
name_y = 34.5    # NAME
year_y = 24      # YEAR

#
# Trophy parts are inserted with the midpint being (mid_trophy)
# and the y points being these constants
#

def generate_ref_trophy(h1, h2, w):
    """
    Shovel's reference point generator: returns a list of 10 reference points
    that each should be the bottom left corner of a trophy
    0 = bottom left with long edge pointing down
    1-3 = stacked on top of 0
    4 = next to 0, long edge pointing up
    5-7 = stacked on 4
    8 = sharp edge pointing up, bottom right
    9 = sharp edge pointing down, above 8
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


def generate_template_trophy(h1, h2, w, drawing):
    """
    Generates a outline around all the tropies on the drawing given. (c) shovel
    """
    drawing.add(dxf.line((0, 0), (600,0), color=255, layer='LINES', thickness=0.00))
    drawing.add(dxf.line((600, 0), (600,450), color=255, layer='LINES', thickness=0.00))
    drawing.add(dxf.line((600,450), (0,450), color=255, layer='LINES', thickness=0.00))
    drawing.add(dxf.line((0,450), (0,0), color=255, layer='LINES', thickness=0.00))
    refpoint = generate_ref_trophy(h1, h2, w)
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


def draw(x,y,x1,y1,d,color=1):
    """Draws a line from (x,y) to (x1,y1) on drawing d"""
    d.add(dxf.line((x,y),(x1,y1),color=color, layer='LINES',thickness=0.01))


def text_align(text, x_align, y_align, height, d, style= "TIMES_ITALIC", rotation=0, color=K_BLACK, mirror=dxfwrite.MIRROR_X):
    """Creates text with the middle aligned to x_al. and y_al."""
    text = dxf.text(text, height = height,mirror=mirror,halign=CENTER, alignpoint = (x_align,y_align),
                    style=style, layer='LINES', rotation=rotation, color=color, linetype='ByBlock')
    d.add(text)


def add_school_trophy(ref_point, drawing, name, year, long_side_dir):
    x_r, y_r = ref_point
    if long_side_dir == 'down':
        rotation = 270
        x_sbhs,y_sbhs = x_r + sbhs_y, y_r - mid_trophy
        x_sac, y_sac = x_r + sac_y,  y_r - mid_trophy
        x_the, y_the = x_r + the_y, y_r - mid_trophy
        x_school, y_school = x_r + school_y, y_r - mid_trophy
        x_trophy,y_trophy = x_r + trophy_y, y_r - mid_trophy
        x_awarded, y_awarded = x_r + awarded_y, y_r - mid_trophy
        x_name, y_name = x_r + name_y, y_r - mid_trophy
        x_year, y_year = x_r + year_y, y_r - mid_trophy

    elif long_side_dir == 'up':
        rotation = 90
        x_sbhs,y_sbhs = x_r - sbhs_y, y_r + mid_trophy
        x_sac, y_sac = x_r - sac_y,  y_r + mid_trophy
        x_the, y_the = x_r - the_y, y_r + mid_trophy
        x_school, y_school = x_r - school_y, y_r + mid_trophy
        x_trophy,y_trophy = x_r - trophy_y, y_r + mid_trophy
        x_awarded, y_awarded = x_r - awarded_y, y_r + mid_trophy
        x_name, y_name = x_r - name_y, y_r + mid_trophy
        x_year, y_year = x_r - year_y, y_r + mid_trophy

    elif long_side_dir == 'right':
        rotation = 0
        x_sbhs,y_sbhs = mid_trophy + x_r, sbhs_y + y_r
        x_sac, y_sac  = mid_trophy + x_r, sac_y  + y_r
        x_the, y_the  = mid_trophy + x_r, the_y  + y_r
        x_school, y_school   = mid_trophy + x_r, school_y + y_r
        x_trophy, y_trophy   = mid_trophy + x_r, y_r + trophy_y
        x_awarded, y_awarded = mid_trophy + x_r, y_r + awarded_y
        x_name, y_name= mid_trophy + x_r, y_r + name_y
        x_year, y_year= mid_trophy + x_r, y_r + year_y

    elif long_side_dir == 'left':
        rotation = 180
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


REF_POINTS = (generate_ref_trophy(h1, h2, w))



def save_file(drawing, filename='output', path = '', start_iter = 1):
    default_iter = start_iter
    path += filename
    if path.endswith('.dxf'):
        path = path[:-4]
    path = os.path.expanduser(path)

    if os.path.exists(path+'.dxf'):
        # it exists already, try to save with number
        while True:
            if start_iter > K_MAX_ITER:
                input("Over 100 trophies generated: Pausing until RETURN is pressed. Please empty out "
                        "the directory/path (%s)" % path)
                start_iter = default_iter
            temp = path + '_' + str(start_iter) + '.dxf'
            if not os.path.exists(temp):
                drawing.saveas(temp)
                break
            else:
                start_iter += 1
    else:
        drawing.saveas(path+'.dxf')


# format of this file
#
# first three letters are 000, 090, 180, 270, sepecifying the rotation
# then the rest is in this form x_cord,ycord
#  Example: 000 100,200
#           180 200,300
# this file only needs to be generated once, and placed in autocad support pat
#


def csv_to_trophy(csv_stream, filename='output', outpath='', outline=False, logopoints=False, validpoints=(0,1,2,3,4,5,6,7,8,9),debugstring='',simulate=False):
    """Reads from a csv, given a stream, trophifying all the points given, not trophyying the non-validpoints"""
    has_content = False
    if logopoints:
        print("LP is now depreciated! plz dont use")
    current_drawing = dxf.drawing()
    if outline:
        generate_template_trophy(h1, h2, w, current_drawing)

    for iteration, valid in enumerate(validpoints):
        try:
            line = next(csv_stream)
        except StopIteration:
            if has_content and not simulate:
                save_file(current_drawing, filename, outpath)
            raise


        # get next item from stream
        if len(line) != 2:  # invalid line
            print("Line %d is invalid [%s]" % (iteration + 1, line))
        if line[0].startswith('##') or line[1].startswith('##'):  # comment line
            continue
        else:
            print(line)
            name, year = line
            if len(name) == 0 and len(year) == 0:  # empty line,created by EXCLE WHEN YOU PRESS ARROW DOWN COMMAND
                continue
            if len(name) == 0 or len(year) == 0:
                print("Length of line %d, is invalid (one entry is 0 length)" % (iteration + 1))
                continue
            has_content = True
            if valid <= 3:
                add_school_trophy(REF_POINTS[valid], current_drawing, name, year, 'down')
            elif valid <= 7:
                add_school_trophy(REF_POINTS[valid], current_drawing, name, year, 'up')
            elif valid == 8:
                add_school_trophy(REF_POINTS[valid], current_drawing, name, year, 'right')
            elif valid == 9:
                add_school_trophy(REF_POINTS[valid], current_drawing, name, year, 'left')
    if not simulate:
        save_file(current_drawing, filename, outpath)

