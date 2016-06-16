# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import Vicsek as vicsek
import os


def scatter_plot(x_array, y_array, time, base_path=None):
    plt.cla()
    plt.clf()
    plt.title("TIME = {time}".format(time=time))
    plt.scatter(x_array, y_array)
    save_path = os.path.join(base_path, "vicsek-{time}.png".fomat(time=time))
    plt.savefig(save_path)
    # plt.show()


if __name__ == '__main__':
    update_number = 1

    objs = []

    x_pos_array = []
    y_pos_array = []

    for x_pos in np.arange(10):
        for y_pos in np.arange(10):
            obj = vicsek.SPP(x_pos, y_pos)
            objs.append(obj)
            x_pos_array.append(obj.pos_x)
            y_pos_array.append(obj.pos_y)

    scatter_plot(x_pos_array, y_pos_array, 0, base_path="/Users/himepro/Desktop/vicsek-png")

    x_pos_array = []
    y_pos_array = []

    after_obj = []
    for obj in objs:
        obj.update(objs)
        after_obj.append(obj)
        x_pos_array.append(obj.pos_x)
        y_pos_array.append(obj.pos_y)

    scatter_plot(x_pos_array, y_pos_array, 1, base_path="/Users/himepro/Desktop/vicsek-png")
