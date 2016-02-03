class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0

        # Write value iteration code here
        "*** YOUR CODE HERE ***"

        for i in range(iterations):
            temp = util.Counter()
            for state in mdp.getStates():
                Vs = []
                #print(state)
                actions = mdp.getPossibleActions(state)
                #print("actions", actions)
                for action in actions:
                    Vs.append(self.computeQValueFromValues(state, action))
                if Vs:
                    temp[state] = max(Vs)
            self.values = temp

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"

        totals = 0
        for _future_state, T in self.mdp.getTransitionStatesAndProbs(state, action):
            #print(state, action, _future_state, T)
            R = self.mdp.getReward(state, action, _future_state)
            if self.mdp.isTerminal(_future_state):
                return R
            else:
                sample = self.discount * self.values[_future_state] + R
                Qs = T * sample
                totals += Qs

        return totals


    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"

        directions = {
            'north': (0, 1),
            'south': (0, -1),
            'west': (-1, 0),
            'east': (1, 0)
        }

        actions = self.mdp.getPossibleActions(state)

        if actions:
            results = []
            for action in actions:
                if action == 'exit':
                    return action
                else:
                    results.append((
                        self.computeQValueFromValues(state, action), action)
                    )

            return max(results)[1]

        return None
