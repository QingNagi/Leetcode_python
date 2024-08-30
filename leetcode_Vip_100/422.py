class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        max_len = max(len(word) for word in words)
        words = [word + (max_len - len(word))* "#" for word in words]
        tempt = zip(*words)
        words_ = ["".join(item) for item in tempt]
        return words_ == words