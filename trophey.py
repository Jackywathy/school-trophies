from dxfwrite.const import CENTER
import dxfwrite
from dxfwrite import DXFEngine as dxf
import os
__author__ = 'Shovel, Jack, and Archie @sydneyboyshigh.com All Rights Unreserved'
__version__ = 'Pre-Alpha 1.1'

h1=155.5 ################
h2= 225 ################
w = 90.4 #################
mid_trophy = 45
black = 250

file_out = []
# 130, 25 = school trophy insertion point
# the bottom left corner of the trophy from the bottom left of a trophy. TODO PROPERLY FINISH THESE VARS?
# crest = 40, 50
logo_width = float(40)
logo_height = float(120)

drawing1 = dxf.drawing("template.dxf")
drawing_trophy = dxf.drawing('Trophy.dxf')
drawing1.add_layer('dxfwrite')
drawing1.add_layer('LINES')
drawing1.add(dxf.line((0, 0), (600,0), color=255, layer='LINES', thickness=0.00))
drawing1.add(dxf.line((600, 0), (600,450), color=255, layer='LINES', thickness=0.00))
drawing1.add(dxf.line((600,450), (0,450), color=255, layer='LINES', thickness=0.00))
drawing1.add(dxf.line((0,450), (0,0), color=255, layer='LINES', thickness=0.00))

# sum constants
crest_y = 132
sbhs_y = 121 # sydney boys high
sac_y = 111 # student award scheme
the_y = 91
school_y = 79
trophy_y = 67.2
awarded_y = 44.5
name_y = 34.5
year_y = 24




def generate_ref_point(h1,h2,w):
    ref = []
    xgap = (600-(h1+h2+w))/4
    ygap1 = (450-(4*w))/5
    ygap2 = (450-(h1+h2))/3
    #first collumn ref points
    ref.append((xgap,ygap1+w))
    ref.append((xgap,2*ygap1+2*w))
    ref.append((xgap,3*ygap1+3*w))
    ref.append((xgap,4*ygap1+4*w))
    #second collumn ref points
    ref.append((2*xgap+h1+h2,ygap1))
    ref.append((2*xgap+h1+h2,2*ygap1+w))
    ref.append((2*xgap+h1+h2,3*ygap1+2*w))
    ref.append((2*xgap+h1+h2,4*ygap1+3*w))
    #third collumn ref points
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
    drawing.save()
        
def draw(x,y,x1,x2,d):
    d.add(dxf.line((x,y),(x1,x2),color=1, layer='LINES',thickness=0.01))


def text(s,x,y,height,d,style="TIMES_ITALIC"):
    text = dxf.mtext(s,(x,y), height=height,style=style,mirror=dxfwrite.MIRROR_X,layer='LINES')
    d.add(text)
    print("DEPRECIATED-PLEASE USED text_align() !(shovel+archie)")


def text_align(text, x_align,y_align,height, d ,style= "TIMES_ITALIC",rotation=0, color = 250):
    """Creates text with the middle aligned to x_al. and y_al."""
    text = dxf.text(text, height = height,mirror=dxfwrite.MIRROR_X,halign=CENTER, alignpoint = (x_align,y_align), style = style, layer='LINES',rotation=rotation,color=color,linetype='ByBlock')
    d.add(text)
'''

def add_school_trophy_upright(ref_point, drawing, name, year):
    """Adds a trophy to the drawing, where ref_points is the bottom left corner under short side. The trophey should be upgright, with long edge on right"""
    if len(name) > 23:
        return "Name must be shorter than 23 letters! Skipping", (name,year,ref_point)
    x,y = ref_point
    file_out.append((x+mid_trophy, y+crest_y, '000'))
    text_align('Sydney Boys High School',mid_trophy+x,sbhs_y+y,4.7,drawing)
    text_align('Student Award Scheme',mid_trophy+x,sac+y,5.7,drawing)
    text_align("The",mid_trophy+x,the+y,10,drawing)
    text_align("School",mid_trophy+x,school+y,10.5,drawing)
    text_align("Trophy",mid_trophy+x,67.2+y,10.5,drawing)
    text_align("awarded to", mid_trophy+x, 44.5+y,7, drawing)
    text_align(name.upper(),mid_trophy+x,34.5+y,4.5,drawing, style = 'STANDARD')
    text_align(str(year), mid_trophy+x, 24+y,6, drawing)



'''

def add_school_trophy(ref_point, drawing, name, year, long_side_dir):
    x_r,y_r = ref_point

    if long_side_dir == 'down':
        # long side is down!
        rotation = 90
        file_out.append((x_r + mid_trophy, y_r+crest_y, '090'))
        x_sbhs,y_sbhs = x_r - sbhs_y, y_r + mid_trophy
        x_sac, y_sac = x_r - sac_y,  y_r + mid_trophy
        x_the, y_the = x_r - the_y, y_r + mid_trophy
        x_school, y_school = x_r - school_y, y_r + mid_trophy
        x_trophy,y_trophy = x_r - trophy_y, y_r + mid_trophy
        x_awarded, y_awarded = x_r - awarded_y, y_r + mid_trophy
        x_name, y_name = x_r - name_y, y_r + mid_trophy
        x_year, y_year = x_r - year_y, y_r + mid_trophy

        x_trophy, y_trophy = mid_trophy + x_r, y_r + trophy_y
        x_awarded, y_awarded = mid_trophy + x_r, y_r + awarded_y
        x_name, y_name= mid_trophy + x_r, y_r + name_y
        x_year, y_year= mid_trophy + x_r, y_r + year_y


    elif long_side_dir == 'up':
        # if trophy is pointing up (long edge paralel to
        ...

    elif long_side_dir == 'right':
        # if the trophey is straight
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
        raise BaseException('long side direction must be down, up, right or left')





    if len(name) > 23:
        return "Name must be shorter than 23 letters! Skipping", (name,year,ref_point)
    x,y = ref_point

    text_align('Sydney Boys High School', x_sbhs,y_sbhs,4.7,drawing,rotation=rotation)
    text_align('Student Award Scheme',x_sac+x,y_sac,5.7,drawing,rotation=rotation)
    text_align("The",x_the,y_the,10,drawing,rotation=rotation)
    text_align("School",x_school, y_school,10.5,drawing,rotation=rotation)
    text_align("Trophy",x_trophy, y_trophy,10.5,drawing,rotation=rotation)
    text_align("awarded to", x_awarded, y_awarded,7, drawing,rotation=rotation)
    text_align(name.upper(), x_name,y_name,4.5,drawing, style = 'STANDARD',rotation=rotation)
    text_align(str(year), x_year, y_year,6, drawing,rotation=rotation)






def add_school_trophy_top(ref_point, drawing, name, year):
    """Adds a trophy to the drawing, where ref_points is the bottom left corner under short side. Trophy will be lying on the long side down"""
    
    if len(name) > 23:
        return "Name must be shorter than 23 letters! Skipping", (name,year,ref_point)
    x,y = ref_point
    file_out.append((x+crest_y, y-mid_trophy, '270'))
    text_align('Sydney Boys High School', sbhs_y+x, y-mid_trophy,4.7,drawing,rotation=270)
    text_align('Student Award Scheme', sac_y+x, y-mid_trophy,5.7,drawing,rotation=270)
    text_align("The",the_y+x,y-mid_trophy,10,drawing,rotation=270)
    text_align("School",       school_y + x, y-mid_trophy, 10.5, drawing,rotation=270)
    text_align("Trophy",     67.2 + x, y-mid_trophy, 10.5, drawing,rotation=270)
    text_align("awarded to", 44.5 + x, y-mid_trophy, 7,    drawing,rotation=270)
    text_align(name.upper(), 34.5 + x, y-mid_trophy, 4.5,  drawing, style = 'STANDARD',rotation=270)
    text_align(str(year),      24 + x, y-mid_trophy, 6,    drawing,rotation=270)



def add_school_trophy_bottom(ref_point, drawing, name, year):
    '''Adds a trophy into the drawing, where ref point is the bottom left corner under short side. Trophy will have long edge pointing up'''
    if len(name) > 23:
        return "Name must be shorter than 23 letters! Skipping", (name,year,ref_point)
    x,y = ref_point
    file_out.append((x-crest_y, y+mid_trophy, ' 90'))
    text_align('Sydney Boys High School', x-sbhs_y, y+mid_trophy,4.7,drawing,rotation=90)
    text_align('Student Award Scheme', x-sac_y, y+mid_trophy,5.7,drawing,rotation=90)
    text_align("The",  x-the_y ,y+mid_trophy,10,drawing,rotation=90)
    text_align("School",       x-school_y, y+mid_trophy, 10.5, drawing,rotation=90)
    text_align("Trophy",      x-67.2, y+mid_trophy, 10.5, drawing,rotation=90)
    text_align("awarded to",  x-44.5, y+mid_trophy, 7,    drawing,rotation=90)
    text_align(name.upper(),  x-34.5, y+mid_trophy, 4.5,  drawing, style = 'STANDARD',rotation=90)
    text_align(str(year),     x-24, y+mid_trophy, 6,    drawing,rotation=90)

def add_school_trophy_upside_down(ref_point, drawing, name, year):
    '''Adds a trophy into the drawing, where ref point is the bottom left corner under short side. Trophy will be upside down *duh?* '''
    if len(name) > 23:
        return "Name must be shorter than 23 letters! Skipping", (name,year,ref_point)
    x,y = ref_point
    file_out.append((x-mid_trophy, y-crest_y, '180'))
    text_align('Sydney Boys High School',x-mid_trophy,y-sbhs_y,4.7,drawing,rotation = 180)
    text_align('Student Award Scheme',x-mid_trophy,y-sac,5.7,drawing,rotation = 180)
    text_align("The",x-mid_trophy,y-the,10,drawing,rotation = 180)
    text_align("School",x-mid_trophy,y-school,10.5,drawing,rotation = 180)
    text_align("Trophy",x-mid_trophy,y-67.2,10.5,drawing,rotation = 180)
    text_align("awarded to", x-mid_trophy, y-44.5,7, drawing,rotation = 180)
    text_align(name.upper(),x-mid_trophy,y-34.5,4.5,drawing, style = 'STANDARD',rotation = 180)
    text_align(str(year), x-mid_trophy, y-24,6, drawing,rotation = 180)



drawing = dxf.drawing()
ref_points = (generate_ref_point(h1,h2,w))

generate_template(h1,h2,w,drawing)
filename = None
counter = 1
while True:

    filename = 'output' + str(counter) + '.dxf'
    try:
        drawing.saveas(filename)
        break
    except PermissionError:
        counter += 1
        continue


os.startfile(filename)

with open('logopoints.txt', 'w') as f:
    for item in file_out:
        print(str(item[2]) + "{0:.2f}".format(item[0]) + ',' + "{0:.2f}".format(item[1]), file = f)


# format of this file

# first three letters are 000, 090, 180, 270, sepecifying the rotation
# then the rest is in this form x_cord,ycord
#  Example: 000100,200
#           180200,300
