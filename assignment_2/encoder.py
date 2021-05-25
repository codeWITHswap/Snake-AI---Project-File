import numpy as np
import argparse

def encode(grid):
    rows, col = len(grid), len(grid[0])
    nS = 0
    # up = 0, left = 1, down = 2, right = 3
    nA = 4
    end = []
    state_mapping = {}

    for i in range(rows):
        for j in range(col):
            id = i * col + j
            if grid[i][j] != 1:
                state_mapping[id] = nS
                nS += 1
            if grid[i][j] == 2:
                start = nS - 1
            elif grid[i][j] == 3:
                end.append(nS - 1)

    print('numStates %d'% nS)
    print('numActions %d' % nA)
    print('start %d' % start)
    print('end %s' % " ".join([str(x) for x in end]))

    # dir N, W, S, E
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    for i in range(rows):
        for j in range(col):
            id = i * col + j

            if grid[i][j] == 3 or grid[i][j] == 1:
                continue
            else:
                curr_state = state_mapping[id]
                for action in range(4):
                    ni = i + dx[action]
                    nj = j + dy[action]

                    if ni >= 0 and ni < rows and nj >= 0 and nj < col:
                        t = 1
                        if grid[ni][nj] != 1:
                            next_state = state_mapping[ni * col + nj]
                            r = 100 * rows * col if grid[ni][nj] == 3 else -1
                        else:
                            next_state = curr_state
                            r = -100 * rows * col
                        print('transition %d %d %d %.1f %.1f' % (curr_state, action, next_state, r, t))

    print('mdptype episodic')
    print('discount 0.999')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Maze_encoder')
    parser.add_argument('--grid', default='data/maze/grid10.txt', help='path to the gridfile')
    args = parser.parse_args()

    grid = np.loadtxt(args.grid, dtype=int)
    encode(grid)