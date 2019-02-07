import gym
import numpy as np
from gym import spaces

class ImageState(gym.Env):

    def __init__(self):
        """Init should set up the environment, the observation and action spaces.
           It cannot take any arguments (only self)"""
        self.obs_shape = (64,64,50)
        self.observation_space = spaces.Box(low=-1, high=1, shape=self.obs_shape)
        self.action_space = spaces.Box(low=-1, high=1, shape=(1,))
        self.reset()


    def reset(self):
        """Reset should reset the environment, and return the new state"""
        self.nsteps = 0
        return np.random.randint(0,2,self.obs_shape)


    def step(self, action):
        """Step should take an action (integer or array of integers in discrete case,
           float (or array of floats) in continuous case.  It should return a tuple
             (s_t+1, reward, done_flag, information)
           s_t+1 : next state
           reward: float
           done_flag: boolean
           information: some other information that you want passed around.  I've never seen this used by anything
        """
        self.nsteps += 1
        return np.random.randint(0,2,self.obs_shape), 0.0, self.nsteps==100, None

