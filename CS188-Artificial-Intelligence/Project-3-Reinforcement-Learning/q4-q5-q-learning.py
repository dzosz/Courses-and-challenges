class QLearningAgent(ReinforcementAgent):
    """
      Q-Learning Agent

      Functions you should fill in:
        - computeValueFromQValues
        - computeActionFromQValues
        - getQValue
        - getAction
        - update

      Instance variables you have access to
        - self.epsilon (exploration prob)
        - self.alpha (learning rate)
        - self.discount (discount rate)

      Functions you should use
        - self.getLegalActions(state)
          which returns legal actions for a state
    """
    def __init__(self, **args):
        "You can initialize Q-values here..."
        ReinforcementAgent.__init__(self, **args)

        "*** YOUR CODE HERE ***"

        #self.visited = set()
        self.states = util.Counter()


    def getQValue(self, state, action):
        """
          Returns Q(state,action)
          Should return 0.0 if we have never seen a state
          or the Q node value otherwise
        """
        "*** YOUR CODE HERE ***"

        return self.states[(state, action)]


    def computeValueFromQValues(self, state):
        """
          Returns max_action Q(state,action)
          where the max is over legal actions.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return a value of 0.0.
        """
        "*** YOUR CODE HERE ***"

        # Qs = 1-self.alpha
        actions = self.getLegalActions(state)
        if actions:
            best = float('-inf')
            for action in actions:
                val = self.getQValue(state, action)
                best = val if val > best else best
            return best
        return 0.0


    def computeActionFromQValues(self, state):
        """
          Compute the best action to take in a state.  Note that if there
          are no legal actions, which is the case at the terminal state,
          you should return None.
        """
        "*** YOUR CODE HERE ***"

        actions = self.getLegalActions(state)
        if actions:
            bestActions = []
            bestScore = float('-inf')
            for action in actions:
                QVal = self.getQValue(state, action)
                if QVal == bestScore:
                    bestActions.append(action)
                elif QVal > bestScore:
                    bestActions = [action]
                    bestScore = QVal
            return random.choice(bestActions)
        return None


    def getAction(self, state):
        """
          Compute the action to take in the current state.  With
          probability self.epsilon, we should take a random action and
          take the best policy action otherwise.  Note that if there are
          no legal actions, which is the case at the terminal state, you
          should choose None as the action.

          HINT: You might want to use util.flipCoin(prob)
          HINT: To pick randomly from a list, use random.choice(list)
        """
        # Pick Action
        legalActions = self.getLegalActions(state)
        action = None
        "*** YOUR CODE HERE ***"
        if legalActions:
            if util.flipCoin(self.epsilon):
                return random.choice(legalActions)
            return self.computeActionFromQValues(state)

        return action

    def update(self, state, action, nextState, reward):
        """
          The parent class calls this to observe a
          state = action => nextState and reward transition.
          You should do your Q-Value update here

          NOTE: You should never call this function,
          it will be called on your behalf
        """
        "*** YOUR CODE HERE ***"

        f_value = self.computeValueFromQValues(nextState)
        sample = reward + self.discount * f_value
        #sample = reward + self.discount * self.states[nextState]
        Vs = (1-self.alpha) * self.states[(state, action)] + self.alpha * sample
        self.states[(state, action)] = Vs

        return Vs
