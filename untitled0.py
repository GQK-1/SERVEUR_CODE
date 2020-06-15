# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 09:59:10 2020

@author: Administrator
"""
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
from IPython.display import IFrame

PORT = 8080

with TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

page = 'http://localhost:8000/welcome.html'

# crée un iframe qui effectue une requête vers le serveur
# que vous êtes censés avoir démarré
IFrame(page,1080,120)
