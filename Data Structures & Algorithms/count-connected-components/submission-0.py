class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parent = [i for i in range(n)]
        rank = [1] * n

        def find (node): #for updating the current root parent node
            cur = node
            while cur != parent[cur]: #[0,1,2,3,4] [0,0,2,3,4] if [1] doesnt = the rootParen 0
                parent[cur] = parent[parent[cur]] # unnecessary, for optimization
                cur = parent[cur]
            return cur

        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)

            if parent1 == parent2:
                return 0
            
            if rank[parent2] > rank[parent1]:
                parent[parent1] = parent2
                rank[parent2]+=rank[parent1]
            else:
                parent[parent2] = parent1
                rank[parent1]+=rank[parent2]
            return 1


        res = n
        for node1, node2 in edges:
            
            res-= union(node1,node2)    
        return res