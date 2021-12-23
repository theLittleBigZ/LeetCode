class Solution:

    def buildAdjList(self):
        self.adjList = dict()
        for index in range(self.numCourses):
            self.adjList[index] = []
        for dest, src in self.preReq:
            self.adjList[src].append(dest)
                
    def findDependentCourses(self, sourceNode):
        if self.visited[sourceNode]:
            return True
        if self.checked[sourceNode]:
            return False
        self.visited[sourceNode] = True
        for neighNode in self.adjList.get(sourceNode, []):
            isCyclic = self.findDependentCourses(neighNode)
            if isCyclic: 
                return True
        self.visited[sourceNode] = False
        self.checked[sourceNode] = True
        self.orderedCourses.append(sourceNode)
        return False   
       
            
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        self.numCourses = numCourses
        self.preReq = prerequisites
        self.visited = [False] * numCourses
        self.checked = [False] * numCourses
        self.orderedCourses = []
        self.buildAdjList()
        
        for sourceNode in self.adjList.keys():
            if not self.visited[sourceNode]:
                isCyclic = self.findDependentCourses(sourceNode)
                if isCyclic: 
                    return []
                
        return self.orderedCourses[::-1]
