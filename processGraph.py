# Benjamin Chappell

fileToProcess = "2dsurface.txt"
fileToReturn = "2dsurfacep.txt"

def main(f, w):
    pFile = open(f, "r")
    adjList = pFile.readlines()
    vertexCount = int(adjList.pop(0))

    wFile = open(w, "w")
    for i in range(0, len(adjList)):
        adjList[i] = adjList[i].split()
        for j in range(0, len(adjList[i])):
            adjList[i][j] = int(adjList[i][j])

        del adjList[i][0]

    print (adjList)

    adjMatrix = [[0 for i in range(0, vertexCount)] for i in range(0, vertexCount)]
    
    for i in range(0, len(adjList)):
        #print (i)
        for j in range(0, len(adjList[i])):
            adjMatrix[i][adjList[i][j]] = 1

    for i in adjMatrix:
        for j in i:
            wFile.write(str(j) + " ")
        wFile.write("\n")

if __name__ == "__main__":
    main(fileToProcess, fileToReturn)