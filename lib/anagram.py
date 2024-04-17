# your code goes here!

class Anagram:
    def __init__(self, word):
        self._word = word

    def match(self, anagrams):
        anagram_array = []
        for word in anagrams:
            if [letter for letter in sorted(self._word)] == [letter for letter in sorted(word)]:
                anagram_array.append(word)
        return anagram_array