from dxfwrite.const import CENTER
import dxfwrite
from dxfwrite import DXFEngine as dxf


offset_left = 0


drawing = dxf.drawing("trop.dxf")
drawing.add_layer('dxfwrite')
drawing.add_layer('LINES')


def create_outline(drawing, x = 0,y = 0):
    """Creates the outline to the shapes, given x and y offsets"""
    drawing.add(dxf.line((0 + x, 0 + y), (90 + x, 0 + y), color=1, layer='LINES', thickness=0.00))
    drawing.add(dxf.line((90 + x, 0 + y), (90 + x, 225 + y) , color=1, layer='LINES', thickness=0.00))
    drawing.add(dxf.line((0 + x, 0 + y), (0 + x,155 + y), color=1, layer='LINES', thickness=0.00))
    drawing.add(dxf.line((90 + x, 225 + y), (0 + x,155 + y), color=1, layer='LINES', thickness=0.00))


def create_text(text,x,y,height,drawing, style="TIMES_ITALIC"):
    """Create a line in the given drawing"""
    text_var = dxf.mtext(text,(x,y), height=height, style=style, mirror=dxfwrite.MIRROR_X, halign = dxfwrite.CENTER, valgin = dxfwrite.TOP, layer='TEXT')
    drawing.add(text_var)

def create_name(text, x, y, height, drawing, style = "STANDARD"):
    """Creates the name, by THE MAGIC OF SCALING!! SO long names are a little smaller"""
    line_height = 100 # the length of the line
    length_letter = (line_height)//len(text)
    # then do something?


create_outline(drawing)
create_text('Sydney Boys High School',45,125,5,drawing)
create_text('Student Award Scheme',45,115,6,drawing)
create_text("The",45,100,10,drawing)
create_text("School",45,90,10,drawing)
create_text("Trophy",45,77,10,drawing)
#TODO PUT IN THE RIGHT DIMENSIONS FOR THE awarded to!
create_text("awarded to", 45, 48, 5, drawing)
create_text("Shovel, Jack, Archie",45,38,5.5,drawing,style = "STANDARD")
drawing.save()
