import numpy as np

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
    pos = np.arange(-5, 5.0, 0.1)  # a 100 dimensional vector
    Y = []
    # Probability density estimate (using the formula from part4-page17)
    for x in pos:
        sum = 0
        for xn in samples:
            expPart = np.exp(-(pow(x - xn, 2) / (2 * pow(h, 2))))
            sum += expPart / (np.sqrt(2 * np.pi) * h)
        sum = sum / N
        Y.append(sum)
    estDensity = np.stack((pos, Y), axis=-1)
    #print(pos)
    #print(Y)
    #print(estDensity)
    return estDensity
