class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
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
                return min(points)
            else:
                return 99999

        values = []
        for action in gameState.getLegalActions(0):
            newState = gameState.generateSuccessor(0, action)
            value = myMin(newState, self.depth, 1)
            values.append((value, action))


        return max(values)[1]

