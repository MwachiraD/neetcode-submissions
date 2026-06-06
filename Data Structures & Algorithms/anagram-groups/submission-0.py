class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sub_list = {}

        for string in strs:
            key =tuple(sorted(string))
            if key not in sub_list:
                sub_list[key] = []
            
            sub_list[key].append(string)
        return list(sub_list.values())
            
        