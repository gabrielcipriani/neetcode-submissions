class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_counts = {}
    for letter in s:
        s_counts[letter] = s_counts.get(letter, 0) + 1

    t_counts = {}
    for letter in t:
        t_counts[letter] = t_counts.get(letter, 0) + 1

    return s_counts == t_counts
                