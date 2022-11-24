import gym
#env = gym.make('CartPole-v1',render_mode="rgb_array")
env = gym.make('CartPole-v0',render_mode="human")
observation = env.reset()
for _ in range(1000):
    env.render()
    action = env.action_space.sample()
    observation, reward, done, info,_score = env.step(action)
    if done:
        # break
        env.reset()
env.close()