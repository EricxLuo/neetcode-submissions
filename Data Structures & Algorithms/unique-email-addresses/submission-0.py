class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        count = 0
        seen = {}
        
        for email in emails:
            skip = False
            domain = False
            address = ""
            for char in email:
                if char == "." and domain == False :
                    continue
                if char == "+":
                    skip = True
                    continue
                if char == "@":
                    domain = True
                    skip = False
                if skip != True:    
                    address += char
            seen[address] = 1 + seen.get(address, 0)
            
        return len(seen)

                


                
