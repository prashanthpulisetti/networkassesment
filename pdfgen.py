from WebKit.Page import Page
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

class hello(Page):
 def writeHTML(self):
  c = canvas.Canvas(None)
  c.drawString(9*cm, 27*cm, 'Hello, World!')
  r = c.getpdfdata()
  self.response().setHeader('Content-Type', 'application/pdf')
  self.response().setHeader('Content-Length', str(len(r)))
  self.response().setHeader('Content-Disposition', 'inline; filename="hello.pdf"')
  self.write(r)


