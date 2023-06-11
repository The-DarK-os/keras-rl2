import time
import gym
import numpy as np


class Register():
    def __init__(self, env_name, sample_test):
        self.env_name = env_name
        self.render_mode = True

    def initialize(self):
        env = gym.make(self.env_name)
        if self.render_mode:
            env.reset()
            for _ in range(40):
                env.render(mode="human")
                action = env.action_space.sample()
                env.step(action)
            env.close()
        return env

    def __del__(self):
        return "deleted env"
