class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []

        if len(strs) == 1 and strs[0] == "":
            return [[""]]
        else:
            word_dict = {}

            for word in strs:
                sorted_word = tuple(sorted(word))

                if sorted_word in word_dict:
                    word_dict[sorted_word].append(word)
                else:
                    word_dict[sorted_word] = [word]

            for value in word_dict.values():
                result.append(value)

            return result