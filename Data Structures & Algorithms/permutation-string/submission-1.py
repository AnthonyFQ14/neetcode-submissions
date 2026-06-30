class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m1 = {}
        m2 = {}
        l = 0

        for i in range(len(s1)):
            m1[s1[i]] = 1 + m1.get(s1[i], 0)

        # print(m1)

        for r in range(len(s2)):

            if s2[r] not in m1:
                l += 1
            else:
                m2[s2[r]] = 1 + m2.get(s2[r], 0)
           
            if m1 == m2:
                return True
        print(m1, m2)
        return False