class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"

        def myMax(newState, depth, A, B):
            """
            A - alfa - maximum
            B - beta - minimum
            """
            if newState.isWin() or newState.isLose() or depth < 1:
                return self.evaluationFunction(newState)

            points = []
            for action in newState.getLegalActions(0):
                postState = newState.generateSuccessor(0, action)
                newval = myMin(postState, depth, 1, A, B)
                points.append(newval)
                if max(points) > B:
                    return max(points)

                A = max(max(points), A)

            if points:
                return max(points)
            else:
                return -99999


        def myMin(newState, depth, gid, A, B):
            if newState.isWin() or newState.isLose():
                return self.evaluationFunction(newState)

            points = []
            for ghostAction in newState.getLegalActions(gid):
                ghostState = newState.generateSuccessor(gid, ghostAction)
                if gid + 1 == newState.getNumAgents():
                    newval = myMax(ghostState, depth-1, A, B)
                else:
                    newval = myMin(ghostState, depth, gid+1, A, B)
                points.append(newval)
                if min(points) < A:
                    # print('Cutting', A)
                    return min(points)

                B = min(B, min(points))

            if points:
                return min(points)
            else:
                return 99999


        values = []
        A, B = -99999, 99999
        for action in gameState.getLegalActions(0):
            newState = gameState.generateSuccessor(0, action)
            value = myMin(newState, self.depth, 1, A, B)
            values.append((value, action))

            if max(values)[0] > B:
                return max(values)[1]

            A = max(max(values)[0], A)

        return max(values)[1]
