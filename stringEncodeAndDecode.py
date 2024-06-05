class Solution:

    def encode(self, strs: List[str]) -> str | None:
        if strs == []:
            return None

        encoded_str = "\0".join(strs)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        if s == None:
            return []

        decoded_str = s.split("\0")
        return decoded_str
