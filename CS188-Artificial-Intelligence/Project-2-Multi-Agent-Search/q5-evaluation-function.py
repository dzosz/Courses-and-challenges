def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION:
                LOSE WIN / -99999 99999
                var1: x2 manhattan distance between pacman and closest
                      x2 summed distance between dots (BFS)
                var2: +100 eat big dot
                var3: +X time scared left for each ghost
                var4: +2 for each food eaten

                extra: to avoid blocking pacman in some locations it's manhattan distance is given
                       -2 points, if the closest dot is behind the wall (true distance function)

    """

    cgs = currentGameState
    foodLeft = cgs.getFood().asList()

    if cgs.isWin():
        return 99999
    elif cgs.isLose():
        return -99999

    total = 0

    mypos = cgs.getPacmanPosition()

    for gid in range(1, cgs.getNumAgents()):
        state = cgs.getGhostState(1)
        total += state.scaredTimer

    total -= cgs.getNumFood() * 2
    total -= len(cgs.getCapsules()) * 100

    def true_distance(p1, p2):
        M = manhattanDistance(p1, p2)
        x1, x2 = sorted([p1[0], p2[0]])
        y1, y2 = sorted([p1[1], p2[1]])
        if x1 == x2:
            if cgs.hasWall(x1, y1+1):
                return M+2
        if y1 == y2:
            if cgs.hasWall(x1+1, y1):
                return M+2
        return M


    while foodLeft:
        closest = min(foodLeft, key=lambda x: true_distance(mypos, x))
        dist = true_distance(mypos, closest)
        total -= dist *  cgs.getNumFood()
        foodLeft.remove(closest)
        mypos = closest

    return total

# Abbreviation
better = betterEvaluationFunction
