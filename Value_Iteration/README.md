# TASK 1

For **Value Iteration**, the transition probabilities and rewards are stored in a 3d NumPy matrix with dimension S * A * S.

## Value Iteration : 

We start the initial estimate value with a 1d NumPy array of zeros and dimension S. <br />
The update is made according to the following rule/pseudocode and the stopping condition taken : the norm of the difference between V<sub>t</sub> and V<sub>t+1</sub> less than 1e-10.

<img src="https://imgur.com/u7fb9OM.jpg" alt_text="Value Iteration Pseudocode" width="700">

---

# TASK 2

To model the given maze as MDP, at each state we have 4 possible actions ‘N’, ‘S’, ‘E’, ‘W’ and we can encode them as 0, 1, 2, 3 respectively. The transition probabilities can only be 0 or 1. As we want the length of the path to be shortest, we can give a negative reward for each step taken. So from one state where the agent can go to the next state with probability 1, I have kept -1 as the immediate reward. If the next state is the final state then I have kept a very large reward(of order 100 * rows * columns). If for any action there is a wall and it can’t go to that state then probability will be 0 and hence to accommodate the sum of probability to be 1, I made a self-loop with probability 1 and a very negative reward, so that it is not favored.
<br />
<br />
However, if we enumerate all the cells of the matrix as the state, then it would be quite slow due to a very large statespace and therefore what we can do is to just forget about the cell which has a wall at that location because they will not be ever reached in our path. This will reduce the number of states by a considerable amount.
<br />
<br />
Solving the above MDP will give us the policy and then we can follow that path to reach any of the end states.
<br />
<br />
I took Gamma to be 0.999 because if we take it to be 1 and suppose that we have a loop of 1 around a particular 0 cell, then while calculating the value function it will not converge. So we can take the value of gamma slightly off by 1.
