from dxfwrite.const import CENTER
import dxfwrite
from dxfwrite import DXFEngine as dxf


offset_left = 0


drawing = dxf.drawing("trop.dxf")
drawing.add_layer('dxfwrite')
drawing.add_layer('LINES')


def 
drawing.add(dxf.line((0, 0), (90,0), color=1, layer='LINES', thickness=0.00))
drawing.add(dxf.line((90, 0), (90,225), color=1, layer='LINES', thickness=0.00))
drawing.add(dxf.line((0, 0), (0,155), color=1, layer='LINES', thickness=0.00))
drawing.add(dxf.line((90, 225), (0,155), color=1, layer='LINES', thickness=0.00))


def create_line(text,x,y,height,drawing, style="TIMES_ITALIC"):
    """Create a line in the given drawing"""
    text_var = dxf.mtext(text,(x,y), height=height,style=style,mirror=dxfwrite.MIRROR_X,layer='TEXT')
    drawing.add(text_var)

text('Sydney Boys High School',85,125,5,drawing)
text('Student Award Scheme',87,115,6,drawing)
text("The",56,100,10,drawing)
text("School",67,90,10,drawing)
text("Trophy",67,77,10,drawing)
text("SHOVEL",56,38,4,drawing)
drawing.save()
