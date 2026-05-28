class Solution:
    def stringIndices(self, wordsContainer, wordsQuery):

        trie = {}
        END = "#"
        def better(a, b):

            if len(wordsContainer[b]) < len(wordsContainer[a]):
                return b

            if len(wordsContainer[b]) == len(wordsContainer[a]) and b < a:
                return b

            return a

        best = 0
        for i in range(len(wordsContainer)):
            best = better(best, i)

        trie[END] = best
        for i, word in enumerate(wordsContainer):

            node = trie
            node[END] = better(node[END], i)

            for ch in reversed(word):

                if ch not in node:
                    node[ch] = {}

                node = node[ch]

                if END not in node:
                    node[END] = i
                else:
                    node[END] = better(node[END], i)

        ans = []

        for q in wordsQuery:

            node = trie

            for ch in reversed(q):

                if ch not in node:
                    break

                node = node[ch]

            ans.append(node[END])

        return ans