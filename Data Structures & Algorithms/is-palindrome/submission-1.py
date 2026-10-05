class Solution:
  def isPalindrome(self, s: str) -> bool:
    new_s = ""
    for char in s:
      if char.isalnum() and char != " ":
        new_s += char.lower()
    
    if len(new_s)%2 == 1:
      prefix = new_s[:len(new_s)//2]
      suffix = new_s[len(new_s)//2+1:]
      return prefix == suffix[::-1]
    else:
      prefix = new_s[:len(new_s)//2]
      suffix = new_s[len(new_s)//2:]
      return prefix == suffix[::-1]