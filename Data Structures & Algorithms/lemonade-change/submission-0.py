class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        register = {5: 0, 10: 0}

        if bills[0] != 5:
            return False

        for i in range(len(bills)):
            if bills[i] == 5:
                register[5] += 1
            elif bills[i] == 10:
                register[10] += 1
                if register[5] < 1:
                    return False
                else:
                    register[5] -= 1
            elif bills[i] == 20:
                if register[5] >= 1 and register[10] >= 1:
                    register[5] -= 1
                    register[10] -= 1
                elif register[5] >= 3:
                    register[5] -= 3
                else:
                    return False
                        
        return True