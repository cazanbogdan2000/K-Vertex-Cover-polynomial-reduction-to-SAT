# keep in mind that the number of variables (literals) must be C^k^n, where:
# k is dimension of our vertex cover, and n is the number of vertices of our initial graph

def createGraph(graph, nrArcs):
    for i in range(nrArcs):
        arc = input().split(" ")
        row = int(arc[0])
        col = int(arc[1])
        graphMatrix[row - 1][col - 1] , graphMatrix[col - 1][row - 1] = 1, 1
    
def createVariables(n, k):
    result = []
    for i in range(n * k):
        result.append(i + 1)
    return result

def atMostOne(variables, k):
    length = len(variables)
    result = []
    for i in range(k):
        clause = []
        for j in range(i, length, k):
            clause.append(str(variables[j]))
        clause = "V".join(clause)
        clause  = "(" + clause + ")"
        result.append(clause)
        for j in range(i, length, k):
            for p in range(j + k, length, k):
                clause = "(~" + str(j + 1) + "V~" + str(p + 1) + ")"
                result.append(clause)
    return result

def atLeastOne(graph, k):
    result = []
    nrVertices = len(graph)
    for i in range(nrVertices):
        for j in range(i + 1, nrVertices):
            clause = []
            if graph[i][j] == 1:
                for p in range(0, k):
                    clause.append(str((i + 1) * k - p))
                    clause.append(str((j + 1) * k - p))
                result.append("(" + "V".join(clause) + ")")
    return result

if __name__ == "__main__":
    k = int(input())
    nrVertices = int(input())
    nrArcs = int(input())
    graphMatrix = [([0] * nrVertices) for i in range(nrVertices)]
    
    createGraph(graphMatrix, nrArcs)
    
    variables = createVariables(nrVertices, k)
    cnfSAT1 = atMostOne(variables, k)
    cnfSAT1 = "^".join(cnfSAT1)
    cnfSAT2 = atLeastOne(graphMatrix, k)
    cnfSAT2 = "^".join(cnfSAT2)
    
    cnfSAT = cnfSAT1 + "^" + cnfSAT2
    
    print(cnfSAT)