from gym.envs.registration import register


register(id='Debug-v0',
         entry_point='kmgym.envs:Debug')

register(id='ImageState-v0',
         entry_point='kmgym.envs:ImageState')
