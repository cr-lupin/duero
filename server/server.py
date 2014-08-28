#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep
from urlparse import urlparse, parse_qs

PORT_NUMBER = 8080

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	counter = 1000;
	#Handler for the GET requests	
	def do_GET(self):
		try:			
			params = parse_qs(urlparse(self.path).query)
			if urlparse(self.path).params == 'nevezes':
				print 'path %s' % self.path	
				print 'parameter: %s' % urlparse(self.path).params
				print 'query (value): (%s)' % params['task'][0]
				mimetype='text/html'
				
				responsetext = ''
				#if params['task'][0] == 'aggya_rajtszamot':
				myHandler.counter += 1
				responsetext = str(myHandler.counter)
				#Open the static file requested and send it
				self.send_response(200)
				self.send_header('Content-type',mimetype)
				self.end_headers()
				self.wfile.write('<body><h1>%s</h1> %s </body>' % (responsetext, self.path) )
			else:
				self.send_error(404,'File Not Found: %s' % self.path)
			return


		except IOError:
			self.send_error(404,'File Not Found: %s' % self.path)

try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()
	