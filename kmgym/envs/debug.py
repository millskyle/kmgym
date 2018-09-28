import gym
import numpy as np


def dec2binarray(d, bits=8):
    s = str(bin(d)[2:]).zfill(bits)


class Debug(gym.env):

    def __init__(self):
        self._current_state_dec_internal = 0

    @property
    def current_state(self):
        return dec2binarray(self._current_state_dec_internal)

    def reset(self):
        self._current_state_dec_internal = 0


    def step(self, action):
        if action==0:
            self._current_state_dec_internal -= 1
        else action==1:
            self._current_state_dec_internal += 1

        if self._current_state_dec_internal < 0:
            self._current_state_dec_internal = 0

        if self._current_state_dec_internal > 2**8:
            self._current_state_dec_internal = 2**8

        return self.current_state, 0.0, False, {}








    def render(self):
        print(self.current_state)
