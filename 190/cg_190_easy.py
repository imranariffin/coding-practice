class Solution:
  m = {}

  # @param n, an integer
  # @return an integer
  def reverseBits(self, n):
    rev = ""
    b_str = bin(n)[2:]
    b_str = b_str.zfill(32)
    chunks = self.chunk(b_str)

    for chunk in chunks:
      if self.m.get(chunk) == None:
        self.m[chunk] = chunk[::-1]
      rev = self.m[chunk] + rev

    return int(rev, 2)

  def chunk(self, b_string):
    chunks = []
    i = 0
    len_b = len(b_string)

    while i < len_b:
      if (i + 4) < len_b:
        chunks += [b_string[i:i + 4]]
      else:
        chunks += [b_string[i:]]
      i += 4

    return chunks
