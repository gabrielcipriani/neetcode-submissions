class Solution:
  def encode(self, strs: list[str]) -> str:
    parts = []
    for word in strs:
      parts.append(f"{str(len(word))}:{word}")

    return "".join(parts)

  def decode(self, s: str) -> list[str]:
    decoded = []
    i = 0
    start = 0

    while i < len(s):
      if s[i] == ":":
        split_size = int(s[start:i])
        word = s[i+1 : i+1+split_size]
        decoded.append(word)
        # put the pointer for 'start'  and i at end of word
        start = i+1+split_size
        i = i+1+split_size

      else:
        i += 1

    return decoded
