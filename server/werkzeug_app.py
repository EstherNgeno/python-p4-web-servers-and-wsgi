#!/usr/bin/env python3
from werkzeug.wrappers import Request, Response 

@Request.application

def application(request):
    print(f"This web server is running at {request.remote_addr}") #this code is the sole function in our script Request.application method, which tells it to run any code inside of the function in the browser at the location we specify with our development server.
    return Response ("A WSGI generated this response!")


if __name__ == "__main__":
    from werkzeug.serving import run_simple
    run_simple(
        hostname = "localhost",      #The run_simple() method runs a server for a one-page application without complications
        port = 5555,                 #run_simple() requires three arguments: a hostname (generally localhost, as it is typically used for local development), a port, and an application
        application = application
    )