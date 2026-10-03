class Solution:
  def isValid(self, s: str) -> bool:

    pairs = {'(':')', '[':']', '{':'}'}

    if len(s) < 2 or s[0] not in pairs:
      return False

    stack = []
    for char in s:
      if char in pairs:
        stack.append(char)
      elif len(stack) != 0 and char == pairs[stack[-1]]:
        stack.pop()
      else:
        return False

    if len(stack) == 0:
      return True
    else:
      return False