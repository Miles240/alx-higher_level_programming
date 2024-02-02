class Myclass:
    pass

def unpredict(obj):
    """Returns the id of an object

        Examples:
        >>> unpredict(Myclass())
            <__main__.Myclass object at 0x0000022C8B27A510>
        
        Args:
            obj: object
    """
    return obj

print(unpredict(Myclass()))