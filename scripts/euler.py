import numpy as np
import matplotlib.pyplot as plt
def euler(t0, y0, t, h):
    derivada = lambda t,y: -20*y+7*np.e**(-0.05*t)
    X = [t0]
    Y = [y0]

    for i in range(int(t/h)):
        y = y0 + h*derivada(t0+i*h,y0)
        y0 = y
        X.append(t0+(i+1)*h)
        Y.append(y)

    return X, Y

graf = euler(0,5,0.1,0.01)
print(graf)

# plt.plot(graf[0],graf[1])
# plt.show()