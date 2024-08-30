class Solution
    def areSentencesSimilar(self, sentence1 List[str], sentence2 List[str], similarPairs List[List[str]]) - bool
        if len(sentence1) != len(sentence2) return False
        for i in range(len(sentence1))
            if len(sentence1[i]) != len(sentence2[i])
                if [sentence1[i], sentence2[i]] in similarPairs or [sentence2[i], sentence1[i]] in similarPairs continue
                else return False
        return True