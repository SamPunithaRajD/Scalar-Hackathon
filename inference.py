from env.environment import KoNectEnv
from env.models import Action

def smart_agent(obs):
    assign = 1
    trains = 0
    resolve = 0

    if obs.demand_level == "high":
        trains = 2
        assign = 2

    if obs.pending_issues > 0:
        resolve = 2

    if obs.delays > 2:
        assign += 1

    return Action(
        assign_drivers=assign,
        add_trains=trains,
        resolve_issues=resolve
    )

def run():
    env = KoNectEnv()
    obs = env.reset()

    total_reward = 0

    for _ in range(10):
        action = smart_agent(obs)
        obs, reward, done, _ = env.step(action)
        total_reward += reward

        print(f"Step: {_}, State: {obs}, Reward: {reward}")

        if done:
            break

    print("Final Score:", total_reward)

if __name__ == "__main__":
    run()
