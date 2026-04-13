class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # Format: <length> + "#" + <string>
            # Example: "lint", "code" -> "4#lint4#code"
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        
        while i < len(s):
            j = i
            # Find the delimiter to know where the length ends
            while s[j] != "#":
                j += 1
            
            # Get the length of the next string
            length = int(s[i:j])
            
            # Extract the string based on the length
            # Start at j+1 (after '#'), end at j + 1 + length
            res.append(s[j + 1 : j + 1 + length])
            
            # Move index to the start of the next length-prefix
            i = j + 1 + length
            
        return res