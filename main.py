# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import Vicsek as vicsek
import os


def scatter_plot(x_array, y_array, time, base_path=None):
    plt.cla()
    plt.clf()
    plt.title("No: {time}".format(time=time))
    plt.scatter(x_array, y_array)
    save_path = os.path.join(base_path, "vicsek-{time}.png".format(time=time))
    plt.savefig(save_path)
    print("No. {time}を出力しました。".format(time=time))
    # plt.show()


if __name__ == '__main__':
    # パラメータの設定
    x_time_y = [20, 20]
    x_pos_array = []
    y_pos_array = []
    vicsek.CONST_VELOCITY = 0.0001
    vicsek.THRESHOLD_RADIUS = 2
    time_coeff = 100

    # ----------------------------------------
    objs = []
    for x_pos in np.arange(x_time_y[0]):
        for y_pos in np.arange(x_time_y[1]):
            obj = vicsek.SPP(x_pos + 0.01, y_pos + 0.01)
            objs.append(obj)
            x_pos_array.append(obj.pos_x)
            y_pos_array.append(obj.pos_y)

    scatter_plot(x_pos_array, y_pos_array, 0, base_path="/Users/himepro/Desktop/vicsek-png")

    for time in range(1, 10):
        x_pos_array = []
        y_pos_array = []
        after_obj = []
        for obj in objs:
            obj.update(objs, time=time / time_coeff)
            after_obj.append(obj)
            x_pos_array.append(obj.pos_x)
            y_pos_array.append(obj.pos_y)
        scatter_plot(x_pos_array, y_pos_array, time=time, base_path="/Users/himepro/Desktop/vicsek-png")
        objs = after_obj
