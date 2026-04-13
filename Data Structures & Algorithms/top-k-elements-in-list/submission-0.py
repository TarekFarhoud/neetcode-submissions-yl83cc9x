class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # --- PART 1: Frequency Map ---
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1 # Start at 1 if new
            else:
                count[num] += 1 # Increment if exists

        # --- PART 2: Extraction ---
        result = [] # Fixed: used [] so we can use .append()
        
        # We only need to find the "max" k times
        while k > 0: # Using a while loop is cleaner for 'k' logic
            
            # FIXED: Find the key with the highest VALUE (frequency)
            # Without key=count.get, it just finds the biggest number
            winner = max(count, key=count.get) 
            
            result.append(winner)
            
            # FIXED: Remove the winner from the dictionary 
            # Otherwise, max() will just pick the same one next time!
            del count[winner] 
            
            k -= 1 # Decrement k (No k-- in Python!)

        return result