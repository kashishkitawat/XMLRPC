import xmlrpclib

"""
    system.listMethods()
    This returns all the methods that are registered in the server
    returns in a list data structure
"""

if __name__ == '__main__':
    server_url = 'http://localhost:5555'
    server = xmlrpclib.ServerProxy(server_url)
    methods = server.system.listMethods()
    for method in range(len(methods)-4):
        print("")
        print(methods[method])
        print(server.system.methodHelp(methods[method]))
        print("")
