class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # This is your main map that holds the grouped strings
        ans = {}

        for s in strs:
            # 1. Create the 'bucket' (frequency map) for the current string
            # We use 26 for the 26 lowercase English letters
            count = [0] * 26
            
            for char in s:
                # Map 'a' -> 0, 'b' -> 1, etc.
                index = ord(char) - ord('a')
                count[index] += 1
            
            # 2. Convert the bucket to a tuple so it can be a key
            # This 'key' represents the "place value" you mentioned
            key = tuple(count)
            
            # 3. If this 'place' doesn't exist, initialize it with a list
            if key not in ans:
                ans[key] = []
            
            # 4. Add the original string to its corresponding bucket
            ans[key].append(s)
            
        # 5. Return only the groups of strings
        return list(ans.values())