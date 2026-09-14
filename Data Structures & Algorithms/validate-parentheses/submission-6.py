class Solution:
    def isValid(self, s: str) -> bool:

        opp = "([{"
        close = ")}]"
        stack =[]
        weight = 0


        for i in range(len(s)):

            if s[i] in opp:

                stack.append(s[i])
                weight += 1

            elif len(stack)!=0:

                if s[i] == "]":
                    
                    if stack.pop() != "[":
                        return False
    
                    else:
                        weight -= 1

                elif s[i] == "}":
                    
                    if stack.pop() != "{":
                        return False
  
                    else:
                        weight -= 1

                elif s[i] == ")":
                    
                    if stack.pop() != "(":
                        return False

                    else:
                        weight -= 1

            else:

                return False

        if weight == 0:

            return True
        return False





        