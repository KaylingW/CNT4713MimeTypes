#Name: Kayling Wong
#PID: 5964595
#Source: https://gist.github.com/HaiyangXu/ec88cbdce3cdbac7b8d5
#Mimetypes found here: https://www.freeformatter.com/mime-types-list.html
import http.server
from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver

PORT = 8080

#Request Handler
Handler = http.server.SimpleHTTPRequestHandler

#Mimetypes
Handler.extensions_map = {
    '.manifest': 'text/cache-manifest',
    '.html': 'text/html',
    '.png': 'image/png',
    '.jpg': 'image/jpg',
    '.svg':	'image/svg+xml',
    '.css':	'text/css',
    '.js':	'application/x-javascript',
    '.mp4': 'video/mp4', #For MP4 conversion
    '.mp3': 'audio/mpeg', #For mp3 conversion
    '.aac': 'audio/x-aac', #For AAC conversion
    '': 'application/octet-stream',  # Default
}

#Server
httpd = socketserver.TCPServer(("", PORT), Handler)

#Print if server is running properly
print("serving at port", PORT)
httpd.serve_forever()
