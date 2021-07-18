# Snake AI
This repository contains the code for my WnCC Summer of Code - 2021 Project under Shubham Lohiya

In this project, we are building a snake game from scratch, and will be implementing basic Reinforcement Learning techniques to help the snake master the game and get really high scores.
___

## Game Demo 
[Link to the Gameplay](https://drive.google.com/file/d/1AwzIKlioTHutlSaIQ4TMpIIDqLMYU6VE/view?usp=sharing)
___

## Assignment 1 - Solving Maze using Value Iteration
In this assignment, we had to implement a maze solver using Value Iteration.<br/>
[Link to Assignment 1](https://www.cse.iitb.ac.in/~shivaram/teaching/old/cs747-a2020/pa-2/programming-assignment-2.html)
___
## Assignment 2 - Sutton & Barto's Windy Gridworld using Model-free control
In this assignment, we solve the Windy Gridworld problem using different Model-free approaches - SARSA(0), Q-Learning, Expected-SARSA. Q-Learning and Expected-SARSA had similar performances.<br/>
[Sutton & Barto](https://www.andrew.cmu.edu/course/10-703/textbook/BartoSutton.pdf)  
[Link to the Assignment 2](https://www.cse.iitb.ac.in/~shivaram/teaching/old/cs747-a2020/pa-2/programming-assignment-3.html)
___

## Simple Tabular RL Agent
I have added a simple Tabular RL agent to play the Snake Game. The game has an extremely large state space representation and we must use a reduced representation to make the task feasible.
### State Space
My representation uses 7 bits of information to describe the current state of the snake:
* 4 bits of information to define the relative position of the fruit with respect to the head of the snake
* 3 bits of information for obstacles in front of the head and to the immediate right and left of the head

### Action Space
The snake has 3 possible actions:
* Do nothing: The snake continues to move in the same direction
* Turn right: The snake turns right to change its direction
* Turn left: The snake turns left to change its direction

### Reward Scheme
I have used a fairly simple reward scheme that can be optimized to improve the performance of the agent:
* Reward of +1 if the snake moves closer to the fruit
* Reward of -1 if the snake moves away from the fruit
* Reward of +10 for eating the fruit
* Reward of -100 for crashing  

### Hyperparameters
The starting learning rate and &epsilon; parameter for the &epsilon;-greedy policy were kept at 0.5 and 0.01. Upon training, the behaviour of the agent was very noisy without decaying these hyperparameters. With annealing, the performance had become more consistent. The agent has achieved a maximum score of 53. 

[Implementing RL on Snake](https://drive.google.com/file/d/1_8GMAZCWGbYJNiU24zqzT8msPWBN6618/view) <br />
[Training my RL agent on various algorithms over 100 episodes](https://drive.google.com/file/d/1ahQOfrDSjjAFMLAv7c6K8_2KDok4oSEG/view?usp=sharing)
___

## Resources
[Learning Resources](https://www.notion.so/SOC-Snake-AI-Project-471ff57983a24f749ca0ec08df8c9472 "Learning Resources")
___
