[Source](https://www.youtube.com/watch?v=5NgNicANyqM)

**Agent**: entity that perceives its env and acts up on that environment
**state** : A configuration of the agent in its environment
**Initial state**: A state where agent start
**Actions (<sub>s </sub>)**: Choices that can be made in any given state. Actions returns the set of actions that can be executed in state (<sub>s </sub>)
**eg** : In solving puzzle we can only move the number. in one of directions (left, right, top, bottom). This is called actions that can be taken
![[Pasted image 20240208081557.png]]
**Transition model**:
A description of what state results from performing any applicable action in any state. Results(<sub>s,a</sub>) returns the state resulting from performing action `a` in state `s`
Visual example:
![[Pasted image 20240208082154.png]]
**State space**:
The set of all states reachable from the initial state by any sequence of actions
![[Pasted image 20240208082630.png]]
Above screen shot is usually represented as graph like below
![[Pasted image 20240208082715.png]]
**Goal test**:
Way to determine whether a given state is a goal state (end state)

**Path cost**:
Numerical cost associated with a given path
![[Pasted image 20240208083143.png]]
For few use cases path cost could be same, example puzzle, as we can only move one direction, there are no multiple routes to take and find path cost.

# Search Problems:
- Initial state
- actions
- transition model
- goal test
- path cost function
**Solution**:
A sequence of actions that leads from the initial state to a goal state
**Optimal solution**
A solution that has the lowest path cost among all solutions

### Node :
A data structure that keeps track of 
- A state
- A parent (Node that generated this node)
- An action (Action applied to parent to get node)
- A path cost (From initial state to node)

## Approach
- Start with a frontier that contains the initial state
	- Frontier: is going to represent all of the things that we could explore next that we haven't explored or visited
- Repeat:
	- If the frontier is empty, then so solution
	- other wise Remove a node from the frontier
	- If node contains goal state, return the solution
	- Expand node, add resulting nodes to the frontier.
	There is one issue with above approach, As we are not saving the node we visited , there are chance of going on infinite loop of visiting same node again and again
## Revised Approach
- Start with a frontier that contains the initial state.
- Start with an empty explored set
- Repeat:
	- If the frontier is empty, then no solution
	- Remove a node from the frontier.
	- If node contains goal state, return the solution
	- Add the node to explored set
	- Expand node, add resulting nodes to the frontier if they aren't already in the frontier or the explored set
**Uninformed search**
Search strategy that uses no problem specific knowledge

**Informed search**
Search strategy that uses problem specific knowledge to find solutions more efficiently

## **Greedy best-first search (gbfs)**
Search algorithm that expands the node that is closest to goal, as estimated by a heuristic function h(<sub>n</sub>)
**Heuristic Function**
A heuristic function (algorithm) or simply a heuristic is a shortcut to solving a problem when there are no exact solutions for it or the time to obtain the solution is too long.

![[Pasted image 20240209081814.png]]
![[Pasted image 20240209081954.png]]
![[Pasted image 20240209082201.png]]
Heuristic function also fails in certain conditions, like below
![[Pasted image 20240209082356.png]]
## A* search
Search algorithm that expands node withl owest value of g(n) + h(n)
g(n) = cost to reach node
h(n) = Estimated cost to goal
![[Pasted image 20240209083112.png]]
A* is optimal if
- h(n) is admissible (never overestimates the true cost)
- h(n) is consistent (for every node n and successor n with step cost c, h(n) <= h(n')+c)
### **Adversarial Search**
algorithms are similar to graph search except that we plan under the assumption that our opponent will maximize his own advantage.
eg: tic-tac-toe, chess

#### MinMax algo:
 - MAX(x) aims to maximize score
 - MIN(O) aims to minimize score
#### Game
- S<sub>o</sub> : initial state
- Player (s) : returns which player to move in state _s_
![[Pasted image 20240209092557.png]]
- Actions (s) : returns legal moves in state _s_
![[Pasted image 20240209092646.png]]
- Result (s, a) : returns state after action _a_ taken in state _s_
![[Pasted image 20240209092719.png]]
- Terminal (s) : checks if state _s_ is a terminal state
![[Pasted image 20240209092802.png]]
- Utility (s) : final numerical value for terminal state _s_
![[Pasted image 20240209092833.png]]
![[Pasted image 20240209093322.png]]
![[Pasted image 20240209093704.png]]
![[Pasted image 20240209094030.png]]
- Given a state _s_:
	- MAX picks a action _a_ in Actions(_s_) that produces highest value of Min-Value(Result(_s_,_a_))
	- MIN picks acton _a_ in Actions(_s_) that produces smallest value of MAX-Value (Result(_s_,_a_))
**Pseudo code for min-max**
- ##### MAX Function:
	function Max-Value(_state_):
		if Terminal(_state_):
			return Utility(_state_)
		_v_= - _♾️_
		for actions in Actions(_state_):
			_v_=Max(_v_, Min-Value(Result(_state_, _action_)))
			return _v_
- ##### Min Function:
	- function Min-Value(_state_):
		if Terminal(_state_):
			return Utility(_state_)
		_v_=  _♾️_
		for actions in Actions(_state_):
			_v_=Max(_v_, Max-Value(Result(_state_, _action_)))
			return _v_
Graphical view of the tic tac on steps of min , max.
this below graph shows if you are green(max) what would be the chances if red(min) takes one of the options available
![[Pasted image 20240209101655.png]]
Max function calculates all the possibilities that Min function has and takes the highest value from Min function 
![[Pasted image 20240209100328.png]]
##### Alpha-Beta Pruning
Optimising above search by not visiting the nodes below the min value

![[Pasted image 20240209100751.png]]
#### Depth-Limited Minimax
**Evaluation function**:
Function that estimates the expected utility of the game from a given state
**pseudo code for depth-limited** min max algo
**function** minimax(node, depth, maximizingPlayer) **is**
    **if** depth = 0 **or** node is a terminal node **then**
        **return** the heuristic value of node
    **if** maximizingPlayer **then**
        value := −∞
        **for each** child of node **do**
            value := max(value, minimax(child, depth − 1, FALSE))
        **return** value
    **else** _(* minimizing player *)_
        value := +∞
        **for each** child of node **do**
            value := min(value, minimax(child, depth − 1, TRUE))
        **return** value

`redit`
>You want to go as deep as possible in the time that you have. Conceptually, this means you'd want to use breadth-first search, but this may be very memory-intensive and makes it hard to implement minimax, so instead you could use [iterative deepening depth-first search](http://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search). When your time is up, return the action from the last depth that you fully analyzed. How deep you can search in a certain amount of time is of course related to the branching factor.
>
It's hard to say what depth you need to reach to get reasonable performance, because it depends on details of your game, your heuristic function and your opponent. If your heuristic function is perfect, you only need to look at the next layer. If it's always bad, you're screwed unless you can search to the end of the tree. Presumably it will get better as you get closer to the end of the tree, and I imagine that if you have a high branching factor, going a level deeper is more valuable than with a low branching factor, but it's difficult to say.

**Knowledge-based agents**
Agents that reason by operating on internal representations of knowledge
**Propositional logic**
Propositional symbols:
P,Q,R
**Entailment**
`⍺ |=ß`
In every model in which sentence ⍺ is true, sentence ß is also true
**Inference**
The process of deriving new sentences from old ones

P: It is a Tuesday
Q: It is raining
R: Harry will go for a run

**Model checking**
- To Determine if KB|=⍺ (kb = knowledge base)
	- Enumerate all possible models
	- If every model where KB is true, ⍺ is true, then KB entails ⍺
	- Otherwise, KB does not entail ⍺
![[Pasted image 20240315222337.png]]
### Inference Rules
**Modus Penens** Rule
![[Pasted image 20240316084751.png]]
![[Pasted image 20240316084820.png]]
**And Elimination** Rule
![[Pasted image 20240316085239.png]]
![[Pasted image 20240316085336.png]]
**Double Negation  Elimination** Rule
![[Pasted image 20240316085429.png]]
![[Pasted image 20240316085443.png]]
**Implication Elimination** Rule
![[Pasted image 20240316085622.png]]
**Biconditional Elimination**
![[Pasted image 20240316085755.png]]
![[Pasted image 20240316085819.png]]
**De Morgan's** Law
![[Pasted image 20240316085927.png]]
![[Pasted image 20240316090030.png]]
**Distributive Property**
![[Pasted image 20240316090148.png]]
Distributive property can also be defined as 
![[Pasted image 20240316090228.png]]

### Search Problems
- Initial state
- actions
- transition model
- goal test
- path cost funtion
#### Theorem Proving
- `initial state`: Starting knowledge base
- `actions`: inference rules
- `transition model`: new knowledge base after inference
- `goal test`: check statement we're trying to prove
- `path cost function`: number of steps in proof

![[Pasted image 20240316091326.png]]
![[Pasted image 20240316091359.png]]
**Complex Inference rules** 
![[Pasted image 20240316090940.png]]
![[Pasted image 20240316091018.png]]
Above inference rule can be generalised to any number of conditions
![[Pasted image 20240316091111.png]]
-----------------------------------------------------------------
![[Pasted image 20240316091158.png]]
![[Pasted image 20240316091221.png]]
Generalisation of above rule
![[Pasted image 20240316091257.png]]
**Conjunctive normal forms** (CNF)
__Conversion to CNF__
- Eliminate biconditionals
	- turn(⍺ <--> ß) in to (⍺ -> ß)⌃ (ß -> ⍺)
- Eliminate implications
	- turn (⍺ -> ß) into  ¬ ⍺ ⌄ ß
- Move  ¬ inwards using De Morgan's Laws
	- eg turn ¬(⍺ ⌃ ß) into ¬⍺ ⌄ ¬ß
- Use distributive law to distribute V where ever possible
![[Pasted image 20240316093304.png]]
 ### Inference by resolution
 The resolution inference rule takes two premises in the form of clauses (_A_ ∨ _x_) and (_B_ ∨ ¬x) and gives the clause (_A_ ∨ _B_) as a conclusion. The two premises are said to be resolved and the variable _x_ is said to be resolved away.
![[Pasted image 20240316094035.png]]
![[Pasted image 20240316094249.png]]
Proving something by contradicting is approach in computer science
**Resolution** from above step
![[Pasted image 20240316094621.png]]
`First order logic` is more effective than `propositional logic` explained above

### `First order logic`
![[Pasted image 20240316095207.png]]

![[Pasted image 20240316095148.png]]
![[Pasted image 20240316095331.png]]

#### Universal quantification
Some thing is going to be true for all values of variable
![[Pasted image 20240316095616.png]]

#### Existential Quantification
Some expression is going to be true for some value of a variable, atleast one value of the variable
![[Pasted image 20240316095821.png]]

![[Pasted image 20240316095919.png]]

# Uncertainty
**Unconditional Probability**
Degree of belief in a proposition in the absence of any other evidence

**Random variable**
A variable in probability theory with a domain of possible values it can take on
 
**Conditional Probability**
Degree of belief in a proposition given some evidence that has already been revealed
P(a|b) -> Probability of _a_ given _b_
P(route change | traffic changes)
P(a|b) = P(a ⌃  b)
	 .     --------
		P(b)
`P(a⌃b)`= `p(b)P(a|b)` or `p(a)p(b|a)`

**Probability Distribution**
The probability distribution gives the possibility of each outcome of a random experiment or event
`P(random variable = possible value of domain) = probability value`

```
P(Flight = on time) = 0.6
P(Flight = delayed) = 0.3
P(Flight = cancelled) = 0.1
```
or
`P(Flight)=<0.6,0.3,0.1>`

**Independence**
The knowledge that one event occurs does not affect the probability of the other event
eg: clouds and whether are dependent, rolling one dice does not effect another dice roll value, these are independent

`P(a⌃b)`=`p(a)p(b)`
![[Pasted image 20240317104648.png]]
this statement of 1/36 is not true, because when you roll a die , either it could be 6 or 4 but not both
![[Pasted image 20240317104501.png]]
Above screen shot, probability of  die having value 4 when a die has value of 6 is zero, hence above use case/event is not independent, though it looks independent

Conditional probability is the bridge that lets you talk about how multiple uncertain events are related. It lets you talk about how the probability of an event can vary under different conditions.

For example, consider the probability of winning a race, given the condition you didn't sleep the night before. You might expect this probability to be lower than the probability you'd win if you'd had a full night's sleep.
![[Pasted image 20240317105114.png]]
That is, the "probability of event A given event B" is not the same thing as the "probability of event B, given event A".
>The probability of clouds, given it is raining (100%) is **not** the same as the probability it is raining, given there are clouds.

## Bayes' Rule

Bayes' Rule tells you how to calculate a conditional probability with information you already have.

It is helpful to think in terms of two events – a hypothesis (which can be true or false) and evidence (which can be present or absent).
![[Pasted image 20240317105252.png]]
![[Pasted image 20240317105330.png]]
There are four parts:

- **Posterior probability** (updated probability after the evidence is considered)
- **Prior probability** (the probability before the evidence is considered)
- **Likelihood** (probability of the evidence, given the belief is true)
- **Marginal probability** (probability of the evidence, under any circumstance)
Bayes' Rule lets you calculate the **posterior (or "updated") probability**. This is a conditional probability. It is the probability of the hypothesis being true, if the evidence is present.
![[Pasted image 20240317105539.png]]
![[Pasted image 20240317111302.png]]
Using one conditional probability we can get the reverse of the conditional probability
![[Pasted image 20240317111537.png]]
![[Pasted image 20240317111607.png]]
**Joint Probability**
Let A and B be the two events, joint probability is the probability of event B occurring at the same time that event A occurs.
For any given day what is the probability of both cloudy and raining
![[Pasted image 20240317111945.png]]
**1. Find the probability that the number “4” will occur twice when 2 dices are rolled simultaneously.** 

**Solution.** Number of possible outcomes when dice is rolled = 6   
Let X be the event of number 4 occurring on the first die, whereas Y is the event of number 4 occurring on the second die. 
X = 1/6   
Y = 1/6   
P(X,Y) = 1/6x 1/6 = 1/36 

**2. What is the joint probability of drawing two red cards with the number 9?** 

**Solution.** Event ‘C’ - Probability of drawing a 9 = 2/52  = 0.0384
Event ‘D’ - Probability of drawing a card that is red = 26/52 = 0.5 
P(C,D) = 0.0384x0.5 = 0.0192 = 1.92 

**3. Express the probability that in a pack of cards, a card which is drawn is 4 and black.** 

**Solution.** Let ‘A’  be the probability that a card is 4   
Let ‘B’ be the probability that a card is black. 

P(A,B) = ? 
A = 4/52 = 0.076 
B = 2/52  = 0.038 
P(A,B) = 2.9

**Negation**
`p(¬a) = 1-P(a)`
**Inclusion-Exclusion** Principle
![[Pasted image 20240317112902.png]]
>n(A⋃B⋃C) = n(A) + n(B) + n(C) – n(A⋂B) – n(A⋂C) – n(B⋂C) + n(A⋂B⋂C)
#### **marginalisation**

Marginalisation is a method that requires summing over the possible values of one variable to determine the marginal contribution of another.
Suppose we’re interested in how the weather affects someone’s happiness in the United Kingdom (UK). We can write this mathematically as P(happiness|weather) i.e. what’s the probability of someone’s happiness level given the type of weather.

![[Pasted image 20240317114237.png]]
When you have joint distribution and when you want to calculate cloudy, consider another variable (rainy)
![[Pasted image 20240317114155.png]]
**Conditioning**
![[Pasted image 20240317114540.png]]
### Bayesian Network
Data structure that represents the dependencies among random variables
![[Pasted image 20240317115259.png]]

![[Pasted image 20240317115518.png]]
**Sampling**
![[Pasted image 20240317120634.png]]
**Markov Assumption**
The assumption that the current state depends on only a finite fixed number of previous states
**Hidden Markov Model**
A Markov model for a system with hidden states that generate some observed events
# Optimisation
**state-space landscape**
The state-space landscape is a graphical representation of the hill-climbing algorithm which is showing a graph between various states of algorithm and Objective function/Cost.
![[Pasted image 20240317211548.png]]
- Hill climbing algorithm is a local search algorithm which continuously moves in the direction of increasing elevation/value to find the peak of the mountain or best solution to the problem. It terminates when it reaches a peak value where no neighbor has a higher value.
- Hill climbing algorithm is a technique which is used for optimizing the mathematical problems. One of the widely discussed examples of Hill climbing algorithm is Traveling-salesman Problem in which we need to minimize the distance traveled by the salesman.

**Sudo code for hill climbing algorithm**
![[Pasted image 20240317212040.png]]
**Simulated Annealing**
- Early on , higher "Temperature": more likely to accept neighbours that are worse than current state
- Later on , lower "Temperature": less likely to accept neighbors that are worse than current state
![[Pasted image 20240317221654.png]]

**Linear Programming**
Minimize a cost function c1x1+c2x2+.... +cnxn

**Linear programming** is an [optimization](https://brilliant.org/wiki/optimization-problems/ "optimization") technique for a [system of linear constraints](https://brilliant.org/wiki/systems-of-inequalities/ "system of linear constraints") and a linear objective function. An **objective function** defines the quantity to be optimized, and the goal of linear programming is to find the values of the variables that maximize or minimize the objective function.

good resource : https://brilliant.org/wiki/linear-programming/

**Backtracking search**
![[Pasted image 20240318141245.png]]
**Arch consistency algo**
Good resource : https://cs.uwaterloo.ca/~a23gao/cs486686_s19/slides/lec05_csp_arc_consistency_backtracking_search_nosol.pdf

![[Pasted image 20240318142131.png]]
# Learning
## Supervised learning
Given a data set of input output pairs, learn a function to map inputs to outputs
### Classification
Supervised learning task of leaning a function mapping an input point to a discrete category
#### Nearest-neighbor classification
Algorithm that, given an input, choose the class of nearest data point to that input
#### K-Nearest-neighbor classification
 Algorithm that, given an input, chooses the most common class out of the k nearest data points to that input
 #### Perceptron Learning algorithm
 **Perceptron** is a linear supervised machine learning algorithm. It is used for binary classification.A perceptron takes _inputs_, modifies the inputs using certain _weights_, and then uses a _function_ to output the final result
 ![[Pasted image 20240318201353.png]]
 The output generated is based on the input values, �1,�2,...,��x1​,x2​,...,xm​. The output can only have two values (binary classification), usually `1` or `0`.

The summation function (represented by _Σ_ in the above diagram) multiplies the inputs with the weights and then adds them up. This can be represented using the following equation:

`x1​∗w1​+x2​∗w2​+…+wm​∗xm`

**Maximum margin separator**
Boundary that maximizes the distance between any of the data points

#### Regression
Supervised learning task of learning a function mapping an input point to a continuous value

**Loss Function**
Function that expresses how poorly our hypothesis performs

**Regularization**
Penalizing hypotheses that are more complex to favor simpler, more general hpotheses

**k-fold cross-validation**
splitting data into k sets, and experimenting k times, using each set as a test set once, and using remaining data as training set

### Reinforcement learning
Given a set of rewards or punishments, learn what actions to take in the future.

**A Markov decision process (MDP)** is defined as a stochastic decision-making process that uses a mathematical framework to model the decision-making of a dynamic system in scenarios where the results are either random or controlled by a decision maker, which makes sequential decisions over time. This article explains MDP with the help of some real-world examples.

**Function approximation**
Approximating Q(s,a), often by a function combining various features, rather than storing one value for every state-action pair
## Unsupervised learning
Given input data without any additional feedback, learn patterns
### Clustering
Organizing a set of objects into groups in such a way that similar objects tend to be in the same group
**Some clustering Applications**
- Genetic research
- image segmentation
-  market research
- medical imaging
- Social network analysis
#### k-means clustering
Algorithm for clustering data based on repeatedly assigning points to clusters and updating those clusters centers

## Learning
- Supervised learning
- Reinforcement learning
- Unsupervised Learning
# Neural Network
### Gradient Descent
Algorithm for minimising loss when training neural network
## Computer vision
**Pooling**
Reducing the size of an input by sampling from regions in the input

 
![[Screenshot 2024-03-21 at 7.31.59 PM.png]]
`Cnn-Convenutional neural network`
![[Pasted image 20250922081257.png]]

### Feed forward neural network
Feed forward neural networks are [artificial neural networks](https://www.turing.com/kb/importance-of-artificial-neural-networks-in-artificial-intelligence) in which nodes do not form loops. This type of neural network is also known as a multi-layer neural network as all information is only passed forward.

During data flow, input nodes receive data, which travel through hidden layers, and exit output nodes. No links exist in the network that could get used to by sending information back from the output node.

> There are many different types of neural networks


























