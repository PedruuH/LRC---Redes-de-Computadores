import sys,os
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class Servidor(BaseHTTPRequestHandler): 
    def do_GET(self):
        try:
            if self.path.endswith(".html"):                
                f = open(Diretorio + self.path)
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                return

            if (self.path.endswith(".jpeg") or self.path.endswith(".jpg")):
                self.send_response(200)
                self.send_header('Content-type','image/jpeg')
                image = os.stat(Diretorio + self.path)
                img_size = image.st_size
                self.send_header("Content-length", img_size)
                self.end_headers() 
                f = open(Diretorio + self.path, 'rb')
                self.wfile.write(f.read())
                f.close()
                return
            if self.path.endswith(".pdf"):
                self.send_response(200)
                self.send_header('Content-type', 'application/pdf')                
                self.end_headers()            
                with open(Diretorio + self.path,'rb') as file:
                    self.wfile.write(file.read())
                return

        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)
        

        
if __name__ == '__main__':
    Diretorio = os.path.realpath(os.path.dirname(__file__))+"/Server/"
    PORT = 8000
    HOST = '192.168.0.105'
    
    try:          
        server = HTTPServer((HOST,PORT), Servidor)
        print 'Server runing in: %s:%s' % (HOST,PORT)
        server.serve_forever()        

    except KeyboardInterrupt:
        print 'Closing Server'
        server.socket.close()
