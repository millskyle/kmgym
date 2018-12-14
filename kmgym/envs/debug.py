import gym
import numpy as np
from gym import spaces


def dec2binarray(d, bits=8):
    s = str(bin(d)[2:]).zfill(bits)
    s = np.array([int(i) for i in s])
    return s


class Debug(gym.Env):

    def __init__(self):
        """Init should set up the environment, the observation and action spaces.
           It cannot take any arguments (only self)"""
        self.nbits = 5
        self.observation_space = spaces.Discrete(self.nbits)
        self.action_space = spaces.Discrete(2)
        self.observation_space.shape=[self.nbits,]
        self.reset()



    @property
    def current_state(self):
        return dec2binarray(self._current_state_dec_internal, bits=self.nbits)


    def reset(self):
        """Reset should reset the environment, and return the new state"""
        self._current_state_dec_internal = np.random.randint(0,self.nbits)
        self._nsteps = 0
        return self.current_state


    def step(self, action):
        """Step should take an action (integer or array of integers in discrete case,
           float (or array of floats) in continuous case.  It should return a tuple
             (s_t+1, reward, done_flag, information)
           s_t+1 : next state
           reward: float
           done_flag: boolean
           information: some other information that you want passed around.  I've never seen this used by anything
        """
        self._nsteps += 1
        if action==0:
            self._current_state_dec_internal -= 1
        elif action==1:
            self._current_state_dec_internal += 1
        else:
            print("ERROR: invalid action.  Must be 1 or 0.")


        if self._current_state_dec_internal < 0:
           self._current_state_dec_internal = 0
           done=True
           r=-1.
        else:
           done=False

        if self._current_state_dec_internal >= 2**self.nbits:
           self._current_state_dec_internal = 2**self.nbits-1
           done=True
           r=-1.
        else:
           done=False

        if self._current_state_dec_internal == 2**self.nbits/2:
            r = 1.0
        else:
            r = 0.0

        if self._nsteps > 200:
            done = True

        self.render()
        return (self.current_state, r, done, {})

    def render(self):
        print(self._current_state_dec_internal)
