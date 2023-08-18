class Solution:
    def isValid(self, s: str) -> bool:
        stk = []

        for i in s:
            if i in "({[":
                stk.append(i)
                

            if i in ")}]":
                if len(stk) == 0:
                    return False

                elif len(stk) !=0: 
                    if (i == ")" and stk[-1] == "(") or (i == "}" and stk[-1] == "{") or (i == "]" and stk[-1] == "["):
                        stk.pop(-1)

                    else:
                        return False

        if len(stk) == 0:
            return True

        else:
            return False

        return 

