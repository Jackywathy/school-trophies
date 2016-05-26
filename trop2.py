from dxfwrite.const import CENTER
import dxfwrite
from dxfwrite import DXFEngine as dxf
import os
__author__ = 'Shovel, Jack, and Archie @sydneyboyshigh.com?'

h1=155.5 ################
h2= 225 ################
w = 90.4 #################
black = None # TODO choose the right colour



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

def text_align(text, x_align,y_align,height, d ,style= "TIMES_ITALIC"):
    """Creates text with the middle aligned to x_al. and y_al."""
    text = dxf.text(text, height = height,mirror=dxfwrite.MIRROR_X,halign=CENTER, alignpoint = (x_align,y_align), style = style, layer='LINES')
    d.add(text)

def add_school_trophy(ref_point, drawing, name, year):
    """Adds a trophey to the drawing, where ref_points is the bottom left corner """
    # TODO FINISH THIS AND ALIGN THE STUFF BETTER!
    x,y = ref_point
    text('Sydney Boys High School',85+x,125+y,5,drawing)
    text('Student Award Scheme',87+x,115+y,6,drawing)
    text("The",55+x,100+y,9,drawing)
    text("School",67+x,90+y,10.5,drawing)
    text("Trophy",67+x,77+y,10.5,drawing)
    text_align("awarded to", 45+x, 44.5+y,7, drawing)
    text_align("SHOVEL",45+x,34.5+y,4.5,drawing, style = 'STANDARD')
    text_align(str(year), 45+x, 24+y,6, drawing)
    drawing.save()

drawing = dxf.drawing()
add_school_trophy((generate_ref_point(h1,h2,w)[-2]), drawing, 'asdf', 100)
generate_template(h1,h2,w,drawing)
drawing.saveas('outfromnewtropheylongname.dxf')
print('done')
os.startfile('outfromnewtropheylongname.dxf')


