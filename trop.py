from dxfwrite.const import CENTER
import dxfwrite
from dxfwrite import DXFEngine as dxf
# drawing.add(dxf.line((0, 0), (0,0), color=1, layer='LINES', thickness=0.01))

drawing = dxf.drawing("trop.dxf")
drawing.add_layer('dxfwrite')
drawing.add_layer('LINES')
text = dxf.mtext('Line1\nLine2', (0,0), height=0.7,mirror=dxfwrite.MIRROR_X)
text.layer = 'TEXT'
text.color = 7
drawing.add(text)
drawing.save()
