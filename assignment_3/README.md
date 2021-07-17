usage: WindyGridworld.py [-h] [-al {Sarsa,Q_Learning,Expected_Sarsa,all}]
                         [--kings] [-stc] [-ep EPSILON] [-gam GAMMA]
                         [-lr ALPHA] [-rs RANDOMSEED] [--rows ROWS]
                         [--columns COLUMNS] [-hz EPISODES] [-pl] [-sp]
                         [--title TITLE] [--savenum SAVENUM]

Windy Gridworld solver

optional arguments:
  -h, --help            show this help message and exit
  -al {Sarsa,Q_Learning,Expected_Sarsa,all}, --algorithm {Sarsa,Q_Learning,Expected_Sarsa,all}
  --kings               Flag for enabling Kings move
  -stc, --stochastic    Flag for enabling stochastic wind
  -ep EPSILON, --epsilon EPSILON
                        epsilon to be used in greedy method
  -gam GAMMA, --gamma GAMMA
                        discount factor
  -lr ALPHA, --alpha ALPHA
                        learning rate
  -rs RANDOMSEED, --randomSeed RANDOMSEED
                        random seed
  --rows ROWS
  --columns COLUMNS
  -hz EPISODES, --episodes EPISODES
                        max number of episodes
  -pl, --plot           Flag for plotting the generated graphs
  -sp, --showpath       For showing the path taken by the policy
  --title TITLE         title to be given to plotted graph
  --savenum SAVENUM

#############################

The various options available are described above,

The --algorith can be used with four options:
    1. Sarsa
    2. Q_Learning
    3. Expected_Sarsa
    4. all - For doing all in one plot

The flag plot can be used to show the generated plots
The flag showpath can be used to show the path from the inital state to final state
The flag kings can be enabled for Kings move ; default is standard move

The default name of the output plot generated is output_default.png

python3 WindyGridworld.py --algorithm Sarsa --title 'Baseline plot for Sarsa agent' --savenum 1
python3 WindyGridworld.py --algorithm Sarsa --kings --title 'Sarsa agent with Kings move' --savenum 2
python3 WindyGridworld.py --algorithm Sarsa --kings --stochastic --title 'Sarsa agent with Kings move and stochastic wind' --savenum 3
python3 WindyGridworld.py --algorithm all --title 'Baseline plots for all the algorithms' --savenum 4

After running the script the output plots are saved in output_1.png, output_2.png,output_3.png, output_4.png
