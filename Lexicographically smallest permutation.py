class Solution(object):
    def lexGreaterPermutation(self, s, target):
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        used = []

        for i in range(len(s)):
            x = ord(target[i]) - ord('a')

            # Try to keep the prefix equal to target
            if cnt[x] > 0:
                cnt[x] -= 1
                used.append(x)
                continue

            # Cannot match target[i].
            # Try the smallest character greater than target[i].
            for c in range(x + 1, 26):
                if cnt[c] > 0:
                    ans = []

                    # Prefix that was equal to target
                    for v in used:
                        ans.append(chr(v + ord('a')))

                    # Make the string strictly greater
                    ans.append(chr(c + ord('a')))
                    cnt[c] -= 1

                    # Smallest possible suffix
                    for j in range(26):
                        ans.append(chr(j + ord('a')) * cnt[j])

                    return ''.join(ans)

            # No larger character here → backtrack
            break

        # Backtrack through the equal prefix
        for i in range(len(used) - 1, -1, -1):
            current = used[i]
            cnt[current] += 1

            x = ord(target[i]) - ord('a')

            # Find smallest character > target[i]
            for c in range(x + 1, 26):
                if cnt[c] > 0:
                    ans = []

                    # Prefix before i
                    for j in range(i):
                        ans.append(chr(used[j] + ord('a')))

                    # Make it greater
                    ans.append(chr(c + ord('a')))
                    cnt[c] -= 1

                    # Smallest possible suffix
                    for j in range(26):
                        ans.append(chr(j + ord('a')) * cnt[j])

                    return ''.join(ans)

        return 
    
        