# -*- coding: utf-8 -*-
import numpy as np

CONST_VELOCITY = 0
THRESHOLD_RADIUS = 10
TIMER = 0


class VicsekModel(object):
    pos_x = 0
    pos_y = 0
    idx = 0

    def __init__(self, idx, pos_x, pos_y):
        self.idx = idx
        self.pos_x = pos_x
        self.pos_y = pos_y

    def moving_theta(self, time, round_spps):
        """
        周囲のSPPたちが必要
        :param time:
        :param round_spps:
        :return:
        """
        self._averaged_angle(round_spps) + self._white_noise(time)

    def moving_radius(self, self_spp, updated_theta):
        """
        返り値はいまは、大きさで返すことにしました。
        :param self_spp:
        :param updated_theta:
        :return:
        """
        global CONST_VELOCITY
        _x = self_spp.pos_x + CONST_VELOCITY * (- np.sin(updated_theta))
        _y = self_spp.pos_y + CONST_VELOCITY * (np.cos(updated_theta))
        return np.sqrt(_x ** 2 + _y ** 2)

    def _white_noise(self, time):
        # Todo: あとで、ホワイトノイズは作ってね！
        return 0

    def _averaged_angle(self, round_spps):
        """
        ラジアンで返値
        Todo: THRESHOLD_RADIUSの範囲内にある粒子だけを足し合わせる
        """
        exp_sum = 0
        for single_spp in round_spps:
            exp_sum += np.exp(single_spp.theta * 1j)
        return np.arctan(exp_sum.imag / exp_sum.real)


class SPP(VicsekModel):
    # デカルト座標系で粒子を作る
    pos_x = 0
    pos_y = 0
    theta = 0
    radius = 0
    PARTICLE_TOTAL_NUMBER = 0

    def __init__(self, pos_x, pos_y):
        SPP.PARTICLE_TOTAL_NUMBER = SPP.PARTICLE_TOTAL_NUMBER + 1
        super(SPP, self).__init__(pos_x=pos_x, pos_y=pos_y, idx=self.PARTICLE_TOTAL_NUMBER)
        self._update_polar_axis()  # デカルト座標が決まっていれば、極表を更新

    def update(self, another_SPPs):
        global TIMER
        TIMER = TIMER + 1
        # THRESHOLD_RADIUS 内にある粒子を取得
        valid_spps = []
        for another_SPP in another_SPPs:
            if self._spp_distance(another_SPP) <= THRESHOLD_RADIUS:
                valid_spps.append(another_SPP)

        # THRESHOLD_RADIUS内にある粒子から位置を更新
        self.update_position(valid_spps)

        # 極座標の更新
        self._update_descarts_axis()

    def update_position(self, valid_round_spps):
        global TIMER
        self.theta = self.moving_theta(TIMER, valid_round_spps)
        self.radius = self.moving_radius(self, self.theta)

    def _spp_distance(self, another_SPP):
        x_diff = self.pos_x - another_SPP.pos_x
        y_diff = self.pos_y - another_SPP.pos_y
        kyori = x_diff ** 2 + y_diff ** 2
        return np.sqrt(kyori)

    def _update_polar_axis(self):
        self.theta = np.arctan(self.pos_y / self.pos_x)
        self.radius = np.sqrt(self.pos_x ** 2 + self.pos_y ** 2)

    def _update_descarts_axis(self):
        self.pos_x = self.radius * np.cos(self.theta)
        self.pos_y = self.radius * np.sin(self.theta)
