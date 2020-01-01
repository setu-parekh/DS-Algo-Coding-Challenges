'''
QUESTION -
----------
https://leetcode.com/problems/word-ladder/

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

APPROACH -
----------
    This will be solved using BFS. (See comments in the code for explanation)

TIME COMPLEXITY -
-----------------

'''

from collections import defaultdict


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        # Initializing dict to store words together with difference of only 1 alphabet.
        word_dict = defaultdict(list)
        # As length of all the words in the word list is same, we will find the length of begin word only.
        L = len(beginWord)

        # Iterating for each word in the word list:
        for w in wordList:
            # Iterating through each alphabet of the word
            for i in range(L):
                similar_word = w[:i] + '_' + w[i+1:] # This will give the bucket word with one blank space in between.
                word_dict[similar_word].append(w) # Finally, we will append the words having only 1 different alphabet together.

        # Performing BFS
        # Initializing a queue with begin word and its level as 1.
        q = [(beginWord, 1)]
        visited = set()
        visited.add(beginWord)

        # Iterating till queue is not empty
        while q:
            current_word, level = q.pop(0)

            for i in range(L):
                # Obtaining the skeleton word with one blank space for each popped word.
                intermediate_word = current_word[:i] + '_' + current_word[i+1:]
                # for each skeleton word, look into its similar word list
                for word in word_dict[intermediate_word]:
                    if not word in visited:
                        if word == endWord:
                            return level + 1

                        q.append((word, level+1))
                        visited.add(word)

        return 0

if __name__ == '__main__':
    s = Solution()
    begin = "hit"
    end = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print(s.ladderLength(begin, end, wordList))
