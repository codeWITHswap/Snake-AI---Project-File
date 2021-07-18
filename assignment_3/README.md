# Windy Gridworld Solver
  
| Argument    | Description |
| ----------- | ----------- |
| -h, --help|show the help message and exit|
| -al, --algorithm|Choose an algorithm|
|--kings|Flag for enabling Kings move|
| -stc, --stochastic|Flag for enabling stochastic wind|
| -ep EPSILON, --epsilon EPSILON|epsilon to be used in greedy method|
|-gam GAMMA, --gamma GAMMA|discount factor|                        
|-lr ALPHA, --alpha ALPHA|learning rate|                      
|-rs RANDOMSEED, --randomSeed RANDOMSEED|random seed|                      
|--rows|ROWS|
|--columns|COLUMNS|
|-hz EPISODES, --episodes EPISODES|max number of episodes|                      
|-pl, --plot|Flag for plotting the generated graphs|
|-sp, --showpath|For showing the path taken by the policy|
|--title TITLE|title to be given to plotted graph|
|--savenum|SAVENUM|
  



#### The --algorithm can be used with four options: <br />
- Sarsa <br />
- Q_Learning <br />
- Expected_Sarsa <br />
- all - For doing all in one plot

The flag plot can be used to show the **generated plots**.<br />
The flag showpath can be used to show the path from the **inital state** to **final state**.<br />
The flag kings can be enabled for **Kings move** ; default is **standard move**.<br />

The default name of the output plot generated is output_default.png.<br />

After running the below script lines the output plots were saved in output_1.png, output_2.png,output_3.png, output_4.png

~~~
python3 WindyGridworld.py --algorithm Sarsa --title 'Baseline plot for Sarsa agent' --savenum 1  
~~~
~~~
python3 WindyGridworld.py --algorithm Sarsa --kings --title 'Sarsa agent with Kings move' --savenum 2 
~~~
~~~
python3 WindyGridworld.py --algorithm Sarsa --kings --stochastic --title 'Sarsa agent with Kings move and stochastic wind' --savenum 3 
~~~
~~~
python3 WindyGridworld.py --algorithm all --title 'Baseline plots for all the algorithms' --savenum 4 
~~~

---

# TASK 1

I have set the parameters as given in the book.
<br />
In all the cases, the default values of the parameters are 𝜀 = 0.1, 𝛼 = 0.5, and 𝛾 = 1.
<br /><br />
I have organized the code in the form of classes and the three agents are inheriting from that base class. 
<br />
Q is a NumPy 2d array of num_states * num_actions.
<br />
Num_states is rows * columns and num_actions is 4 for baseline, 8 with King’s Moves enabled.
<br />
The average for the Q is taken over the 20 seeds.
<br /><br />
I have made an update to the x and y. And the case where they go out of the grid can be handled by this formula: 
<br />
𝑥 = min(max(𝑥, 0) , 𝐶 − 1) 𝑦 = min(max(𝑦, 0) , 𝑅 − 1)
<br />
<br />
X can only change by the person’s move
<br />
Y can change both from wind and person’s move
<br />
<br />
A reward of -1 is given to all the intermediate states, except the terminal states.

---

# TASK 2

The plot obtained for Sarsa(0) is given below. The slopes increase with time-steps/episodes as it is a convex graph hence we can see the time steps per episode decrease as the episode number increases.

<img width="587" alt="1" src="https://user-images.githubusercontent.com/81500272/126053008-44bc3640-19bc-4ad8-a48e-e9ce5f5fe92a.png">

We can now predict how our algorithm performs after training it for 200 episodes!

**ALL THE GRIDS WHICH ARE SHOWN HAVE WIND IN THE DOWNWARD DIRECTION, DIRECTION OF INCREASING Y (WHICH IS OPPOSITE TO THE CASE DISCUSSED IN THE BOOK, WHERE THEY HAD TAKEN IT TO BE IN THE UPWARD DIRECTION)**

<img width="721" alt="1 1" src="https://user-images.githubusercontent.com/81500272/126053030-0edfffa5-aa17-4244-ba78-a196ec564778.png">

The start state is Blue and the end state is green **(this convention remains same in every grid)** . The wind values are the same as given in the example. The plot is obtained using the average statistic i.e averaging over action-value functions obtained over each random seeds!
Although for this grid we are correctly able to predict the optimal path from start to end(terminal) state, it may not always be the case, we may need to change the values of the number of episodes over which we need to update our action-value function! And the values of alpha and epsilon can also be changed to see which works better in different cases. If we visit any state again(i.e any state is visited earlier) then this implies we got stuck because from each state the actions of wind is determined and by choosing actions greedily we always take the same action from that state!

---

# TASK 3


There are now 8 actions instead of 4, as now we can move diagonally as well. Hence intuitively the length of the optimal path should decrease as we have more actions from any of the states. Comparing with above graphs the plot here now yield better results as we can see the slope value is high which indicates the time-steps per episode on episodes with high number is low with Kings-move.

<img width="740" alt="2" src="https://user-images.githubusercontent.com/81500272/126053039-d185b772-4cfe-4bcc-bf4d-5755655fbcd7.png">


The path obtained by acting greedily(always taking the action with max Q-value for that state):

<img width="719" alt="2 1" src="https://user-images.githubusercontent.com/81500272/126053046-a8d9725b-5421-4cd8-884f-45f0b836c409.png">

The length of the optimal path for the given values of wind is observed to be 7, which can be achieved in many ways.
And here with the above grid we can see that the length of path taken is 7. So we observe that we are indeed following the optimal path. Increasing the values of **numseeds** or **numepisodes** may change the path, but the length remains the same i.e., 7.

---

# TASK 4 : (Kings’ Move enabled + Stochastic)

The plot obtained for Stochastic Wind with King’s Moves enabled is:
Here due to the randomness of wind effect the model is learning quite slow. Due to this stocacity the avg time-step per episode at a large number of episodes is quite higher than compared to any of the above 2 graphs as the slope is very less at higher episodes!
<br /><br />
We can see the slope increasing with more number of episodes and hence the model learns faster at high episodes and thus our models predicts learns better with more number of episodes!


<img width="667" alt="3" src="https://user-images.githubusercontent.com/81500272/126053049-97b14342-a532-4199-892f-55a460172a85.png">

The path obtained by greedily following the policy is:

<img width="737" alt="3 1" src="https://user-images.githubusercontent.com/81500272/126053061-e901bb0d-786b-455b-91f3-7c72c6242677.png">

Here, as the value of the wind can be 𝑤 − 1, 𝑤, or 𝑤 + 1, if 𝑤 ≠ 0.
Due to the slow learning as can be seen in the graph we need to keep total episodes higher thus enabling the agent to learn better. Also, as there is stochasticity enabled we may get different paths for this grid on different runs!

# TASK 5

Comparison plot for Sarsa(0), Q-learning and Expected Sarsa is as shown!

<img width="683" alt="4" src="https://user-images.githubusercontent.com/81500272/126053062-911d77a3-363b-4281-89b7-643c95868f12.png">

Q-learning outperforms the rest 2 models followed by Expected-Sarsa and then Sarsa agent. Q-learning learns the fastest and has the highest value of slope at high episodes! Therefore the avg time-steps per episode would be least for Q-learning.
As Expected-Sarsa and Q-learning are almost the same model, only difference is expected-sarsa instead of the maximum over the next state–action pairs use the expected value, taking into account how likely each action is under the current policy.
Expected Sarsa is more complex computationally than Sarsa but, in return, it eliminates the variance due to the random selection of A<sub>t+1</sub>. Hence it is quite “expected” that expected-Sarsa will perform better than Sarsa and so is our observation from the above plot!

Also, the path obtained by greedily following the policy in Q-learning and Expected Sarsa is the optimal path.
Epsilon-greedy approach was used in Expected Sarsa, with 𝜀 = 0.1, i.e.,
<img width="796" alt="4 1" src="https://user-images.githubusercontent.com/81500272/126053063-a96fef22-8fc6-4939-985a-22a9a3b3f71a.png">

actions and 𝑎​ = argmax​ 𝑄(𝑠, 𝑎).
