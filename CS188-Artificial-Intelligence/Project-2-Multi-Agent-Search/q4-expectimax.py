class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"

        def myMax(newState, depth):
            if newState.isWin() or newState.isLose() or depth < 1:
                return self.evaluationFunction(newState)

            points = []
            for action in newState.getLegalActions(0):
                postState = newState.generateSuccessor(0, action)
                newval = myMin(postState, depth, 1)
                points.append(newval)

            if points:
                return max(points)
            else:
                return -99999


        def myMin(newState, depth, gid):
            if newState.isWin() or newState.isLose():
                return self.evaluationFunction(newState)

            points = []
            for ghostAction in newState.getLegalActions(gid):
                ghostState = newState.generateSuccessor(gid, ghostAction)

                if gid + 1 == newState.getNumAgents():
                    newval = myMax(ghostState, depth-1)
                else:
                    newval = myMin(ghostState, depth, gid+1)
                points.append(newval)

            if points:
                return float(sum(points))/float(len(points))
            else:
                return 99999

        values = []
        for action in gameState.getLegalActions(0):
            newState = gameState.generateSuccessor(0, action)
            value = myMin(newState, self.depth, 1)
            values.append((value, action))

        # print(values)
        return max(values)[1]
