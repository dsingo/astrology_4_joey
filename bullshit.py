def countSpacesBetweenTrues(acc, nextValue):
    if (acc["prevValue"] == True & nextValue == True):
        return acc
    elif (acc["prevValue"] == True & nextValue == False):
        return { "spaces": acc["spaces"] + [0], "prevValue": False}
    elif (acc["prevValue"] == False & nextValue == False):
        return {"spaces": acc["spaces"][:-1] + [acc["spaces"][-1] + 1], "prevValue": False}
    elif (acc["preValue"] == False & nextValue == True):
        return {"spaces": acc["spaces"], "prevValue": True}

countSpacesBetweenTrues({"spaces":[0], "prevValue":False}, False)