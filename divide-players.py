class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        left = 0 
        right = len(skill)-1

        res = skill[left] * skill[right]
        total_skill = skill[left] + skill[right]
        left += 1
        right -= 1

        while left < right:
            if skill[left] + skill[right] != total_skill:
                return -1
            else:
                res += skill[left] * skill[right]
                left += 1
                right -= 1

        return res
