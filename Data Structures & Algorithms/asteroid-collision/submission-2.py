class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
     
        stack = []
        
        for ast in asteroids:
            valid= True
            while stack and ast < 0 and stack[-1] > 0 and valid == True:
                
                if abs(stack[-1]) > abs(ast):
                    valid = False
                elif abs(stack[-1]) < abs(ast):
                    stack.pop()
                    valid = True
                else:
                    stack.pop()
                    valid = False
            if valid:
                stack.append(ast)
            
        return stack