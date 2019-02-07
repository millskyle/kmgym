# kmgym
Kyle's Gym environments for debugging

`Debug`: A simple discrete observation and action space test that should be trivial for any RL agent to learn

`ImageState`: An environment with a fairly data-intensive observation space of shape (64,64,50). Useful for benchmarking memory demands of algorithms as each observation is about 1 MiB in size.  The states are random, and the actions do nothing.


