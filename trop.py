from dxfwrite.const import CENTER
import dxfwrite
from dxfwrite import DXFEngine as dxf

__author__ = 'Shovel, Jack, and Archie @sydneyboyshigh.com? Copyright 2016'

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

def generate_template(h1,h2,w):
    drawing = dxf.drawing("template.dxf")
    drawing.add_layer('dxfwrite')
    drawing.add_layer('LINES')
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

def text(s,x,y,height,d):
    text = dxf.mtext(s,(x,y), height=height,style="TIMES_ITALIC",mirror=dxfwrite.MIRROR_X,layer='LINES')
    d.add(text)


def add_school_trophy(ref_point, drawing):
    """Adds a trophey to the drawing, where ref_points is the bottom left corner """
    # TODO FINISH THIS AND ALIGN THE STUFF BETTER!
    x = ref_point[0]
    y = ref_point[1]
    text('Sydney Boys High School',85+x,125+y,5,drawing)
    text('Student Award Scheme',87+x,115+y,6,drawing)
    text("The",56+x,100+y,10,drawing)
    text("School",67+x,90+y,10,drawing)
    text("Trophy",67+x,77+y,10,drawing)
    text("SHOVEL",56+x,38+y,4,drawing)
    drawing.save()



