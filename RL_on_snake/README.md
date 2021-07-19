The python file `agent.py` accepts the following command-line arguments:
* `--algorithm` followed by the algorithm to train the agent. The options include **Sarsa, Q-Learning, Expected-Sarsa, Dyna-Q, compare**. _Compare_ plots the relative performance of the algorithms.
* `--episodes` followed by the number of episodes to train the agent over.

Example Usage:

##### To train the agent using the Q-learning algorithm over 100 episodes
```bash
python3 agent.py --algorithm q-learning --episodes 100
```
![q-learning](https://user-images.githubusercontent.com/81500272/126119649-4af9f332-16a1-413f-9dee-6012a8fc7be6.png)

##### To train the agent using the Sarsa algorithm over 100 episodes
```bash
python3 agent.py --algorithm sarsa --episodes 100
```
![sarsa](https://user-images.githubusercontent.com/81500272/126119653-357a3e69-4f99-423c-b692-3a85803ca863.png)

##### To train the agent using the Expected-Sarsa algorithm over 100 episodes
```bash
python3 agent.py --algorithm expected-sarsa --episodes 100
```

![expected-sarsa](https://user-images.githubusercontent.com/81500272/126119659-bd8768b0-0f38-4727-82c8-088590646354.png)
##### To train the agent using the all the algorithms over 100 episodes and compare their individual performances
```bash
python3 agent.py --algorithm compare --episodes 100
```
![comparing_over_100_episodes](https://user-images.githubusercontent.com/81500272/126119662-13c127d4-30e1-4021-8582-40d23a27c3ab.png)

---
[Implementing RL on Snake](https://drive.google.com/file/d/1_8GMAZCWGbYJNiU24zqzT8msPWBN6618/view) <br />
[Training my RL agent on various algorithms over 100 episodes](https://drive.google.com/file/d/1ahQOfrDSjjAFMLAv7c6K8_2KDok4oSEG/view?usp=sharing)
