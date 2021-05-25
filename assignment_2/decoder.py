import numpy as np
import argparse

def decode(grid, policy):
    rows, col = len(grid), len(grid[0])
    end = []
    nS = 0
    state_mapping = {}

    for i in range(rows):
        for j in range(col):
            id = i * col + j
            if grid[i][j] != 1:
                state_mapping[id] = nS
                nS += 1
            if grid[i][j] == 2:
                start = id
            elif grid[i][j] == 3:
                end.append(id)

    action_mapping = {0: "N", 1:"W", 2:"S", 3:"E"}
    delta = {'N': -col, 'W': -1, 'S': col, 'E':1}

    curr_state = start
    path = []

    while(curr_state not in end):
        action = action_mapping[policy[state_mapping[curr_state]]]
        path.append(action)
        curr_state += delta[action]

    return path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Maze decoder')
    parser.add_argument('--grid', default='data/maze/grid10.txt', help='path to the gridfile')
    parser.add_argument('--value_policy', default='value_and_policy_file', help='path to policy and value function file')
    args = parser.parse_args()

    grid = np.loadtxt(args.grid, dtype=int)

    with open(args.value_policy, 'r') as f:
        content = f.readlines()
        policy = np.array(list(map(lambda line: int(line.strip().split()[1]), content)))

    path = decode(grid, policy)
    print('%s' % " ".join([str(x) for x in path]))