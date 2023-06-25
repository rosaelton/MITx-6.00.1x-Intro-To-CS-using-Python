import math

def polysum(n, s):
    """
    Returns the sum of the area and the square of the perimeter of a polygon
    described by n and s.
        
        Parameters: 
            n (int): number of sides of the polygon. 
            s (int): length of the sides of the polygon. 
        
        Returns: round(area + squared_perimeter, 4) (float)
    """

    area = (0.25 * n * s ** 2)/math.tan(math.pi / n)
    squared_perimeter = (n * s) ** 2
    return round(area + squared_perimeter, 4)
