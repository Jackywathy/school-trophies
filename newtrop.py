from dxfwrite.const import CENTER
import dxfwrite
from dxfwrite import DXFEngine as dxf
import os
__author__ = 'Shovel, Jack, and Archie @sydneyboyshigh.com?'
__version__ = '-1.1'

h1=155.5 ################
h2= 225 ################
w = 90.4 #################
mid_trophy = 45
black = 250



drawing1 = dxf.drawing("template.dxf")
drawing_trophy = dxf.drawing('Trophy.dxf')
drawing1.add_layer('dxfwrite')
drawing1.add_layer('LINES')
drawing1.add(dxf.line((0, 0), (600,0), color=255, layer='LINES', thickness=0.00))
drawing1.add(dxf.line((600, 0), (600,450), color=255, layer='LINES', thickness=0.00))
drawing1.add(dxf.line((600,450), (0,450), color=255, layer='LINES', thickness=0.00))
drawing1.add(dxf.line((0,450), (0,0), color=255, layer='LINES', thickness=0.00))

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

def text_align(text, x_align,y_align,height, d ,style= "TIMES_ITALIC",rotation=0):
    """Creates text with the middle aligned to x_al. and y_al."""
    text = dxf.text(text, height = height,mirror=dxfwrite.MIRROR_X,halign=CENTER, alignpoint = (x_align,y_align), style = style, layer='LINES',rotation=rotation)
    d.add(text)

def add_school_trophy_upright(ref_point, drawing, name, year):
    """Adds a trophy to the drawing, where ref_points is the bottom left corner under short side. The trophey should be upgright, with long edge on right"""
    if len(name) > 23:
        return "Name must be shorter than 23 letters! Skipping", (name,year,ref_point)
    x,y = ref_point
    text_align('Sydney Boys High School',mid_trophy+x,122+y,4.7,drawing)
    text_align('Student Award Scheme',mid_trophy+x,112+y,5.7,drawing)
    text_align("The",mid_trophy+x,92+y,10,drawing)
    text_align("School",mid_trophy+x,80+y,10.5,drawing)
    text_align("Trophy",mid_trophy+x,67.2+y,10.5,drawing)
    text_align("awarded to", mid_trophy+x, 44.5+y,7, drawing)
    text_align(name.upper(),mid_trophy+x,34.5+y,4.5,drawing, style = 'STANDARD')
    text_align(str(year), mid_trophy+x, 24+y,6, drawing)


def add_school_trophy_top(ref_point, drawing, name, year):
    """Adds a trophy to the drawing, where ref_points is the bottom left corner under short side. Trophy will be lying on the long side down"""
    if len(name) > 23:
        return "Name must be shorter than 23 letters! Skipping", (name,year,ref_point)
    x,y = ref_point
    text_align('Sydney Boys High School', 122+x, y-mid_trophy,4.7,drawing,rotation=270)
    text_align('Student Award Scheme', 112+x, y-mid_trophy,5.7,drawing,rotation=270)
    text_align("The",92+x,y-mid_trophy,10,drawing,rotation=270)
    text_align("School",       80 + x, y-mid_trophy, 10.5, drawing,rotation=270)
    text_align("Trophy",     67.2 + x, y-mid_trophy, 10.5, drawing,rotation=270)
    text_align("awarded to", 44.5 + x, y-mid_trophy, 7,    drawing,rotation=270)
    text_align(name.upper(), 34.5 + x, y-mid_trophy, 4.5,  drawing, style = 'STANDARD',rotation=270)
    text_align(str(year),      24 + x, y-mid_trophy, 6,    drawing,rotation=270)



def add_school_trophy_bottom(ref_point, drawing, name, year):
    '''Adds a trophy into the drawing, where ref point is the bottom left corner under short side. Trophy will have long edge pointing up'''
    if len(name) > 23:
        return "Name must be shorter than 23 letters! Skipping", (name,year,ref_point)
    x,y = ref_point
    text_align('Sydney Boys High School', x-122, y+mid_trophy,4.7,drawing,rotation=90)
    text_align('Student Award Scheme', x-112, y+mid_trophy,5.7,drawing,rotation=90)
    text_align("The",  x-92 ,y+mid_trophy,10,drawing,rotation=90)
    text_align("School",       x-80, y+mid_trophy, 10.5, drawing,rotation=90)
    text_align("Trophy",      x-67.2, y+mid_trophy, 10.5, drawing,rotation=90)
    text_align("awarded to",  x-44.5, y+mid_trophy, 7,    drawing,rotation=90)
    text_align(name.upper(),  x-34.5, y+mid_trophy, 4.5,  drawing, style = 'STANDARD',rotation=90)
    text_align(str(year),     x-24, y+mid_trophy, 6,    drawing,rotation=90)

def add_school_trophy_upside_down(ref_point, drawing, name, year):
    '''Adds a trophy into the drawing, where ref point is the bottom left corner under short side. Trophy will be upside down *duh?* '''
    if len(name) > 23:
        return "Name must be shorter than 23 letters! Skipping", (name,year,ref_point)
    x,y = ref_point
    text_align('Sydney Boys High School',x-mid_trophy,y-122,4.7,drawing,rotation = 180)
    text_align('Student Award Scheme',x-mid_trophy,y-112,5.7,drawing,rotation = 180)
    text_align("The",x-mid_trophy,y-92,10,drawing,rotation = 180)
    text_align("School",x-mid_trophy,y-80,10.5,drawing,rotation = 180)
    text_align("Trophy",x-mid_trophy,y-67.2,10.5,drawing,rotation = 180)
    text_align("awarded to", x-mid_trophy, y-44.5,7, drawing,rotation = 180)
    text_align(name.upper(),x-mid_trophy,y-34.5,4.5,drawing, style = 'STANDARD',rotation = 180)
    text_align(str(year), x-mid_trophy, y-24,6, drawing,rotation = 180)



drawing = dxf.drawing()
ref_points = (generate_ref_point(h1,h2,w))

add_school_trophy_top(ref_points[0], drawing, 'Tama Widhiwipati', 2017)
add_school_trophy_top(ref_points[1], drawing, 'Brendan Kwan', 2017)
add_school_trophy_top(ref_points[2], drawing, 'Isaiah Wibowo', 2017)
add_school_trophy_top(ref_points[3], drawing, 'Jason Wang', 2017)

add_school_trophy_bottom(ref_points[4], drawing, 'Archie Fox', 2017)
add_school_trophy_bottom(ref_points[5], drawing, 'Shovel Quazi', 2017)
add_school_trophy_bottom(ref_points[6], drawing, 'Mr Comben', 2017)
add_school_trophy_bottom(ref_points[7], drawing,  'Jackk Jiang', 2017)


add_school_trophy_upside_down(ref_points[9], drawing, 'A really very long name', 2017)
add_school_trophy_upright(ref_points[8], drawing, 'Monster Kid', 2017)

generate_template(h1,h2,w,drawing)
drawing.saveas('outputlongnametrophies.dxf')
print('done')
os.startfile('outputlongnametrophies.dxf')


