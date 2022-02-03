from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm


class Data:
    def __init__(self):
        self.x = []
        self.y = []
        self.z = []

    def upgrade(self, tmp):
        tmp = list(map(float, tmp))
        self.x.append(tmp[0])
        self.y.append(tmp[1])
        self.z.append(tmp[2])


def make_model(x, y, z, name):
    fig = plt.figure()
    ax = Axes3D(fig)
    surf = ax.plot_trisurf(x, y, z, cmap=cm.jet,
                           alpha=0.5, linewidth=0.1)
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.savefig(name + '.png')
    plt.close()


def read_data(name):
    data = Data()
    file = open(name)
    for line in file:
        tmp = line.split()
        data.upgrade(tmp)
    print(data)
    return data

data = read_data('test.cvs')
make_model(data.x, data.y, data.z, 'rez.png')
