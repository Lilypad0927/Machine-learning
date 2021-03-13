import numpy as np

pos = np.arange(-5, 5.0, 0.1)
print(pos)

def kde(samples, h):
    # compute density estimation from samples with KDE
    # Input
    #  samples    : DxN matrix of data points
    #  h          : (half) window size/radius of kernel
    # Output
    #  estDensity : estimated density in the range of [-5,5]

    #####Insert your code here for subtask 5a#####
    # Compute the number of samples created
    N = len(samples)
    pos = np.arange(-5, 5.0, 0.1)
    print(pos)
    #Probability density estimate (part4-page17)

    #up = np.sum(np.exp(-(pos[np.newaxis, :] - samples[:, np.newaxis]) ** 2 / (2 * h ** 2)), axis=0)
    #down = N * np.sqrt(2 * np.pi) * h
    #res =
    #estDensity = np.stack((pos, res), axis=1)

    return estDensity
