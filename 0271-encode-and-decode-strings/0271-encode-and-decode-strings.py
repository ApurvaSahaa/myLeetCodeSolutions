class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        #we assume that only upto 256 ascii characters are going to be present
        #so we can take the 257th ascii character as a separator
        sep = chr(257)
        return sep.join(strs) 

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        sep = chr(257)
        return s.split(sep)


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))