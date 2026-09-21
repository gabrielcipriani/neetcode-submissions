class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    s_counts = {}
    for letter in s:
        if letter in s_counts:
            s_counts[letter] += 1
        else:
            s_counts[letter] = 1

    t_counts = {}
    for letter in t:
        if letter in t_counts:
            t_counts[letter] += 1
        else:
            t_counts[letter] = 1
    
    if s_counts == t_counts:
        return True
    return False
                