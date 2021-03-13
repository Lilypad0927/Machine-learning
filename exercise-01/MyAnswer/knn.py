import numpy as np

def knn(samples, k):
    # compute density estimation from samples with KNN
    # Input
    #  samples    : DxN matrix of data points
    #  k          : number of neighbors
    # Output
    #  estDensity : estimated density in the range of [-5, 5]

    #####Insert your code here for subtask 5b#####
    # Compute the number of the samples created
    N = len(samples)
    pos = np.arange(-5, 5.0, 0.1)  # a 100 dimensional vector
    Y = []
    for x in pos:
        distances = []
        sum = 0
        for xn in samples:
            distances.append(np.abs(x - xn))
        K_nearest_neighbours = sorted(distances)[:k]
        # P = K/NV
        Y.append(k / (2 * N * K_nearest_neighbours[-1]))
    #print(Y)
    estDensity = np.stack((pos, Y), axis=-1)
    return estDensity