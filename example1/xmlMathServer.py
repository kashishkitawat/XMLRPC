import SimpleXMLRPCServer

"""
    register_introspection_functions()
    This registers introspect functions. Which will allow to querry all the
    methods of the server.
    Introspect functions are:
    system.listMethods, system.methodHelp and system.methodSignature
    When a user querrys for the methods in the server,
    it uses obj.system.listMethods()

    register_multicall_functions()
    This allows multicall of functions. So that the client can call multiple
    functions together, instead of calling them serially

    register_instance(MathOperations())
    This registers the class and all the methods associated wih it
    We can also register individual functions if required
"""


class MathOperations:

    def add(self, x, y):
        """ Simple Math Addition function to add two numbers
        Returns:
        Sum of two numbers
        """
        return (x + y)

    def subtract(self, x, y):
        """ Simple Math Subtract function to subtract two numbers
        Returns:
        Difference of two numbers
        """
        return (x - y)

    def multiply(self, x, y):
        """ Simple Math Multiply function to multiply two numbers
        Returns:
        Multiplication of two numbers
        """
        return (x * y)

    def division(self, x, y):
        """ Simple Math division function to divide two numbers
        Returns:
        Quotient of two numbers
        """
        return (x * y)


if __name__ == '__main__':
    server = SimpleXMLRPCServer.SimpleXMLRPCServer(('localhost', 5555))
    server.register_introspection_functions()  # this registers introspect functions
    server.register_multicall_functions()  # this allows multicall of functions
    server.register_instance(MathOperations())  # this registers the class and all the methods associated wih it
    print("Server Listening on port 5555")
    server.serve_forever()  # this command will start the server
