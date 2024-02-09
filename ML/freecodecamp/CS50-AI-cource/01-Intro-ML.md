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
Way to determine whether a given state is a goal state (end)

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
![[Pasted image 20240209081814.png]]
![[Pasted image 20240209081954.png]]
![[Pasted image 20240209082201.png]]
Heuristic function also fails in certain conditions, like below
![[Pasted image 20240209082356.png]]
## A* search
Search algorithm that expands nodd withlowest value of g(n) + h(n)
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
- Actions (s) : returns legal moves in state _s_
- Result (s, a) : returns state after action _a_ taken in state _s_
- Terminal (s) : checks if state _s_ is a terminal state
- Utility (s) : final numerical value for terminal state _s_
![[Pasted image 20240209092557.png]]
![[Pasted image 20240209092646.png]]
![[Pasted image 20240209092719.png]]
![[Pasted image 20240209092802.png]]
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


`time : 1hr51min`

