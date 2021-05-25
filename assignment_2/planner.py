import argparse
import numpy as np
# import time

class MDP:
    def __init__(self, path):
        with open(path, 'r') as f:
            content = f.readlines()
            content = [tuple(line.strip().split()) for line in content]
            is_first = True
            for line in content:
                if line[0] == 'numStates':
                    self.nS = int(content[0][1])
                elif line[0] == 'numActions':
                    self.nA = int(content[1][1])
                elif line[0] == 'start':
                    self.start = int(content[2][1])
                elif line[0] == 'end':
                    self.end = list(map(int, content[3][1:]))
                elif line[0] == 'transition':
                    if is_first:
                        self.T = np.zeros((self.nS, self.nA, self.nS))
                        self.R = np.zeros((self.nS, self.nA, self.nS))
                        is_first = False
                    _, s1, ac, s2, r, p = line
                    s1, ac, s2 = int(s1), int(ac), int(s2)
                    r, p = float(r), float(p)
                    self.R[s1][ac][s2] = r
                    self.T[s1][ac][s2] = p
                elif line[0] == 'mdptype':
                    self.mtype = content[-2][1]
                elif line[0] == 'discount':
                    self.gamma = float(content[-1][1])
                else:
                    raise Exception('first word of the line does not seem to be of valid type')

        self.V = np.zeros(self.nS)

    def getQ(self, V):
        return np.sum(self.T * (self.R + self. gamma * V.reshape(1, 1, self.nS)), axis=2)

    def solve_belleman(self, policy):
        T, R = [], []
        for state in range(self.nS):
            R.append(self.R[state][policy[state]].reshape((1, self.nS)))
            T.append(self.T[state][policy[state]].reshape((1, self.nS)))

        T = np.concatenate(T, axis=0)
        R = np.concatenate(R, axis=0)

        b = (R * T).sum(axis=1)
        A = np.identity(self.nS) - T * self.gamma
        V = np.linalg.pinv(A) @ b
        return V


class ValueIteration(MDP):
    def solve(self):
        while True:
            Q = self.getQ(self.V)
            newV = np.max(Q, axis=1)
            if np.linalg.norm(newV - self.V) < 1e-10:
                break
            self.V = newV.copy()
        self.policy = np.argmax(Q, axis=1)
        return self.policy, self.V

# I might later come back to this point and write down the code for hpi and lp hence I have created the following dictionary

name_to_class = {
    'vi' : ValueIteration
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='MDP Planning Algorithms')
    parser.add_argument('--mdp', default='data/mdp/episodic-mdp-2-2.txt')
    parser.add_argument('-al', '--algorithm', default='vi')

    args = parser.parse_args()

    mdp = name_to_class[args.algorithm](args.mdp)
    optimal_policy, optimal_value = mdp.solve()
    for value, pi in zip(optimal_value, optimal_policy):
        print("%.6f %d" % (value, pi))