def computeProjection(a):

    b=np.ones(np.size(a))

    projection= (np.dot(a,b)/(np.sum(a*2)))a

    return(projection)

