from dxfwrite.const import CENTER
import dxfwrite
from dxfwrite import DXFEngine as dxf


drawing = dxf.drawing("trop.dxf")
drawing.add_layer('dxfwrite')
drawing.add_layer('LINES')
drawing.add(dxf.line((0, 0), (90,0), color=1, layer='LINES', thickness=0.00))
drawing.add(dxf.line((90, 0), (90,225), color=1, layer='LINES', thickness=0.00))
drawing.add(dxf.line((0, 0), (0,155), color=1, layer='LINES', thickness=0.00))
drawing.add(dxf.line((90, 225), (0,155), color=1, layer='LINES', thickness=0.00))


def text(s,x,y,h,d):
    text = dxf.mtext(s,(x,y), height=h,style="TIMES_ITALIC",mirror=dxfwrite.MIRROR_X,layer='TEXT')
    d.add(text)

text('Sydney Boys High School',85,125,5,drawing)
text('Student Award Scheme',87,115,6,drawing)
text("The",56,100,10,drawing)
text("School",67,90,10,drawing)
text("Trophy",67,77,10,drawing)
text("SHOVEL",56,38,4,drawing)
drawing.save()
