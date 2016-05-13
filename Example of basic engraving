from dxfwrite.const import CENTER
import dxfwrite
from dxfwrite import DXFEngine as dxf

namedrawing = input("Enter a name for the output file: ")
if not namedrawing:
    namedrawing = "doc1.dxf"
namedrawing += ".dxf"
drawing = dxf.drawing(namedrawing)

def main(basex, basey, text):
    drawing.add_layer("dxfwrite")
    drawing.add_layer("LINES")
    drawing.add(dxf.line((basex, basey), (basex + 500, basey), color = 1, layer = "LINES", thickness = 0.01))
    drawing.add(dxf.line((basex + 500, basey), (basex + 500, basey + 100), color = 1, layer = "LINES", thickness = 0.01))
    drawing.add(dxf.line((basex + 500, basey + 100), (basex, basey + 100), color = 1, layer = "LINES", thickness = 0.01))
    drawing.add(dxf.line((basex, basey + 100), (basex, basey), color = 1, layer = "LINES", thickness = 0.01))
    drawing.add_layer("TEXTLAYER")
    drawing.add(dxf.mtext(text, insert = (basex+250, basey+10), height = 50, color = 250, width = 0.01, valign = dxfwrite.BOTTOM, halign = dxfwrite.CENTER))
    drawing.save()

names = input("Enter the names you want engraved seperated by a commer: ").split(",")

for name in names:
    main(0, 150 * names.index(name), name.lstrip())

print("Drawing %s created." % (namedrawing))
