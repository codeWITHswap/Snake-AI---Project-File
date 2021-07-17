import argparse
import matplotlib.pyplot as plt
import numpy as np

class Agent:
    def __init__(self, args):
        self.args = args
        self.src = (0, 3)
        self.dest = (7, 3)

        self.rows = args.rows
        self.columns = args.columns

        if args.kings:
            self.nA = 8
            self.dx = [-1, -1, 0, 1, 1, 1, 0, -1]
            self.dy = [0, 1, 1, 1, 0, -1, -1, -1]
        else:
            self.nA = 4
            self.dx = [-1, 0, 1, 0]
            self.dy = [0, 1, 0, -1]

        self.wind_power = [0 , 0 , 0 , 1 , 1, 1 , 2 , 2, 1, 0]
        self.nS = self.rows * self.columns
        self.Q = np.zeros((self.nS, self.nA))
        self.nseeds = 20

    def convert(self, state):
        x, y = state
        return x + y * self.columns

    # returns next state
    def next_state(self, state, action):
        x, y = state

        if self.wind_power[x] > 0:
            y += self.wind_power[x] + np.random.randint(-1, 2) * args.stochastic

        x += self.dx[action]
        y += self.dy[action]

        x = max(0, x)
        y = max(0, y)

        x = min(x, self.columns - 1)
        y = min(y, self.rows - 1)

        return (x, y)

    def next_action(self, state):
        stateN = self.convert(state)

        if np.random.rand() < self.args.epsilon:
            A = np.random.randint(0, self.nA)
        else:
            action_value =self.Q[stateN, :]
            A = np.argmax(action_value)

        return A

    def train(self):
        Q_avg = np.zeros((self.nS, self.nA))
        time_steps = np.zeros(self.args.episodes)

        for seed in range(self.nseeds):
            self.Q = np.zeros((self.nS, self.nA))
            time = 0

            for episode in range(self.args.episodes):
                np.random.seed(seed)
                S = self.src
                A = self.next_action(S)

                while True:
                    if S == self.dest:
                        break
                    R = -1
                    S_dash = self.next_state(S, A)
                    A_dash = self.next_action(S_dash)
                    self.Q[self.convert(S)][A] += self.args.alpha*(R + self.args.gamma * self.update(self.convert(S_dash), A_dash) - self.Q[self.convert(S)][A])
                    S = S_dash
                    A = A_dash
                    time += 1
                time_steps[episode] += time
            Q_avg += self.Q

        time_steps = time_steps / self.nseeds
        Q_avg /= self.nseeds
        return Q_avg , time_steps

    def update(self, S_dash, A_dash):
        raise Exception('Must be implemented by child class')

class Sarsa(Agent):
    def update(self, S_dash, A_dash):
        return self.Q[S_dash][A_dash]

class Expected_Sarsa(Agent):
    def update(self, S_dash, A_dash):
        Pi = np.zeros(self.nA) + self.args.epsilon / self.nA
        Pi[np.argmax(self.Q[S_dash])] += (1 - self.args.epsilon)
        return np.sum(self.Q[S_dash] * Pi)

class Q_Learning(Agent):
    def update(self, S_dash, A_dash):
        return np.max(self.Q[S_dash])

name_to_agent = {
    'Sarsa' : Sarsa,
    'Expected_Sarsa' : Expected_Sarsa,
    'Q_Learning' : Q_Learning
}

def showpath(Q, args):
    grid = np.zeros((args.rows, args.columns))
    agent = Agent(args)
    S = agent.src

    path=[[],[]]

    while True:
        y, x = S
        path[0].append(y)
        path[1].append(x)

        if S == agent.src:
            grid[x, y] = 1
        elif S == agent.dest:
            grid[x, y] = 2
            break
        else:
            grid[x, y] = 3

        A = np.argmax(Q[agent.convert(S),:])

        S_dash = agent.next_state(S, A)
        nY, nX = S_dash

        if args.stochastic == 0 and grid[nX, nY] != 0:
            print(f"Stuck in state ({nX},{nY})")
            grid[agent.dest[0], agent.dest[1]]=2
            path[0].append(nY)
            path[1].append(nX)
            break

        S = S_dash

    fig = plt.figure()
    ax = plt.gca()
    ax.imshow(grid)

    xr = np.arange(args.columns + 1)
    yr = np.arange(args.rows + 1)
    plt.plot(path[0],path[1],color=(1, 0, 0))
    ax.set_xticks(xr - 0.5)
    ax.set_yticks(yr - 0.5)
    ax.set_xticklabels(xr)
    ax.set_yticklabels(yr)
    ax.grid(True, color = 'w', linewidth = 1.5)

    ax.set_title("%s, %s%s Greedily" % (args.algorithm, 'stochasticly, ' if args.stochastic else '', 'with Kings move,' if args.kings else 'with standard move,'))
    fig.savefig("path.png")

    plt.close(fig)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Windy Gridworld solver')
    parser.add_argument('-al', '--algorithm', default='Sarsa', choices=["Sarsa", "Q_Learning", "Expected_Sarsa", "all"])
    parser.add_argument('--kings', action='store_true', help='Flag for enabling Kings move')
    parser.add_argument('-stc', '--stochastic', action='store_true', help='Flag for enabling stochastic wind')
    parser.add_argument('-ep', '--epsilon', type=float, default=0.1, help='epsilon to be used in greedy method')
    parser.add_argument('-gam', '--gamma', type=float, default=1, help ='discount factor')
    parser.add_argument('-lr', '--alpha', type=float, default=0.5, help='learning rate')
    parser.add_argument('-rs', '--randomSeed', type=int, default=42, help='random seed')
    parser.add_argument('--rows', type=int, default=7)
    parser.add_argument('--columns', type=int, default=10)
    parser.add_argument('-hz', '--episodes', type=int, default=200, help='max number of episodes')
    parser.add_argument('-pl', '--plot', action='store_true', help='Flag for plotting the generated graphs')
    parser.add_argument('-sp', '--showpath', action='store_true', help='For showing the path taken by the policy')
    parser.add_argument('--title', default='', help='title to be given to plotted graph')
    parser.add_argument('--savenum', default='default')

    args = parser.parse_args()

    fig = plt.figure(figsize=(6,6))

    if args.algorithm != 'all':
        agent = name_to_agent[args.algorithm](args)
        Q, time_steps = agent.train()

        plt.plot(time_steps, range(args.episodes), label=args.algorithm)

        plt.legend()
        plt.grid(True)
        if args.title == '':
            args.title = '%s %s %s' % (args.algorithm, 'Kings move' if args.kings else 'standard move', 'stochastically' if args.stochastic else '')

        plt.title(args.title)

        plt.xlabel('Time Steps')
        plt.ylabel('Episodes')

        if args.plot:
            plt.show()
        else:
            plt.savefig(f'output_{args.savenum}')

        if args.showpath:
            showpath(Q, args)

    else:
        for algo in name_to_agent:
            agent = name_to_agent[algo](args)
            Q, time_steps = agent.train()

            plt.plot(time_steps, range(args.episodes), label=algo)

        plt.legend()
        plt.grid(True)

        plt.xlabel('Time Steps')
        plt.ylabel('Episodes')

        if args.title == '':
            args.title = 'Baseline plots for all algorithms'

        plt.title(args.title)

        if args.plot:
            plt.show()
        else:
            plt.savefig(f'output_{args.savenum}')
