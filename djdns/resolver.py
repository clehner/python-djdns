class Resolver(object):
    '''
    Taxonomical class for objects that fulfill Resolver interface.
    '''

    def get(self, request):
        '''
        Takes request, returns array of pymads records.
        '''
        raise NotImplementedError('Resolver subclass must define get()')

class ResolverWrapper(Resolver):
    '''
    Wrap an object that already fulfills Resolver interface, but isn't
    a subclass of Resolver.
    '''

    def __init__(self, source):
        self.source = source

    def get(self, request):
        return self.source.get(request)
