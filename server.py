
# code reduced from https://wiki.python.org/moin/BaseHttpServer

import time
import BaseHTTPServer
#import Json
# example of a python class
 
class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
  def do_GET(s):

    """Respond to a GET request."""
    s.send_response(200)
    s.send_header("Content-type", "text/html")
    s.end_headers()
    s.wfile.write("<html><head><title>My first python program!</title></head>")
    s.wfile.write("<body><p>This is a test.</p>")
    s.wfile.write("<p>Hello World!</p>")
    s.wfile.write("<p>You accessed path: %s</p>" % s.path)
    split1 = s.path.split('/', 1)
    split2 = split1[1].split('+', 1)
    x = int(split2[0]) + int(split2[1])
    s.wfile.write(x)
    s.wfile.write("</body></html>")

  def do_POST(self):
    self.send_response(200)
    self.send_header("Content-type", "text/html")
    self.end_headers()
    self.wfile.write("<html><head><title>My first python program!</title></head>")
    self.wfile.write("<p>It should push the event</p>")
    self.wfile.write("</body></html>")
    
#httpd = BaseHTTPServer.HTTPServer(("localhost", 8000), MyHandler)
#httpd = BaseHTTPServer.HTTPServer(("172.31.16.91", 8000), MyHandler)
httpd = BaseHTTPServer.HTTPServer(("52.25.5.196", 8000), MyHandler)
httpd.serve_forever()