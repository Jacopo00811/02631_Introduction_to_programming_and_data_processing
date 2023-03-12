def gravitationalPull(x):
    R = 6371000
    G0 = 9.82
    if R <= x :
        g = G0*((R**2)/(x**2))
    elif R > x and x >= 0 :
        g = G0*(x/R)
        
    return g



