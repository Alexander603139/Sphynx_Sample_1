def hello(name):
    """Print hello addressed to *name*.
    
    Args:
      name (str): Name to address.
    """
    print('hello', name)

class Foo:

    """Foo class."""

    def bye(self, name):
        """Print bye addressed to *name*.

        Args:
          name (str): Name to address.
        """
        print('bye', name)

if __name__ == '__main__':
    hello('world')
    Foo().bye('python')