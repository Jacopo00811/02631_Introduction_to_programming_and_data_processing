def bacteriaGrowth(n0, alpha, K, N):
    tN = 0

    while n0 < N:
        n0 = (1 + alpha*(1 - n0/K))*n0
        tN += 1
        
    return tN
print(bacteriaGrowth(100.0, 0.4, 1000.0, 500.0))