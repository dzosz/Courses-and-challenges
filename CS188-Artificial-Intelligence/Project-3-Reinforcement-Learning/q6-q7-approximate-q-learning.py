class ApproximateQAgent(PacmanQAgent):
    """
       ApproximateQLearningAgent

       You should only have to overwrite getQValue
       and update.  All other QLearningAgent functions
       should work as is.
    """
    def __init__(self, extractor='IdentityExtractor', **args):
        self.featExtractor = util.lookup(extractor, globals())()
        PacmanQAgent.__init__(self, **args)
        self.weights = util.Counter()

    def getWeights(self):
        return self.weights

    def getQValue(self, state, action):
        """
          Should return Q(state,action) = w * featureVector
          where * is the dotProduct operator
        """
        "*** YOUR CODE HERE ***"

        Qs = 0
        for key, Fi in self.featExtractor.getFeatures(state, action).items():
            Qs += Fi * self.weights[key]

        return Qs

    def update(self, state, action, nextState, reward):
        """
           Should update your weights based on transition
        """
        "*** YOUR CODE HERE ***"

        Q_future_best = self.computeValueFromQValues(nextState)
        sample = reward + self.discount * Q_future_best
        difference = sample - self.getQValue(state, action)

        for key, val in self.featExtractor.getFeatures(state, action).items():
            self.weights[key] = self.weights[key] + \
                self.alpha * difference * val

    def final(self, state):
        "Called at the end of each game."
        # call the super-class final method
        PacmanQAgent.final(self, state)

        # did we finish training?
        if self.episodesSoFar == self.numTraining:
            # you might want to print your weights here for debugging
            "*** YOUR CODE HERE ***"
            pass
