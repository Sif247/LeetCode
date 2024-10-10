class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = {}
        for i in magazine:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1

        for j in ransomNote:
            if j not in counter:
                return False
            elif counter[j] == 1:
                del counter[j]
            else:
                counter[j] -= 1
        return True




class Test:
    solution = Solution()
    ransomNote = "a"
    magazine = "b"
    ris = solution.canConstruct(ransomNote, magazine)
    print(ris)

    ransomNote2 = "aa"
    magazine2 = "ab"
    ris2 = solution.canConstruct(ransomNote2, magazine2)
    print(ris2)

    ransomNote3 = "aa"
    magazine3 = "aa"
    ris3 = solution.canConstruct(ransomNote3, magazine3)
    print(ris3)

