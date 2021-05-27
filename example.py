
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
#!/usr/bin/env python
 
import textwrap
 
from six.moves.BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
 
 
class HelloRequestHandler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        if self.path != '/':
            self.send_error(404, "Object not found")
            return
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>Hello World</title>
            </head>
            <body>
                <h1>Hello, World!</h1>
                <p>... Here we are!</p>
            </body>
            </html>
        ''')
        self.wfile.write(response_text.encode('utf-8'))
 
 
server_address = ('', 8000)
httpd = HTTPServer(server_address, HelloRequestHandler)
httpd.serve_forever()