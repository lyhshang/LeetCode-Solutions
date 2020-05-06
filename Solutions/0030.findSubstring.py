from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(s) == 0 or len(words) == 0:
            return []
        word_len = len(words[0])
        all_words_len = len(words) * word_len
        s_len = len(s)
        res = []
        ws = {}
        for w in words:
            if ws.get(w) is None:
                ws[w] = 1
            else:
                ws[w] += 1
        for i in range(word_len):
            left, right = i, i + word_len
            counter = {}
            while right <= s_len:
                w = s[right - word_len:right]
                if ws.get(w) is None:
                    left = right
                    counter.clear()
                else:
                    counter[w] = 1 if counter.get(
                        w) is None else counter[w] + 1
                    if right - left == all_words_len:
                        if counter == ws:
                            res.append(left)
                        counter[s[left:left + word_len]] -= 1
                        left += word_len
                right += word_len
        return res


if __name__ == '__main__':
    print(
        Solution().findSubstring("barfoothefoobarman", ["foo", "bar"]), [0, 9],
        Solution().findSubstring(
            "wordgoodgoodgoodbestword", [
                "word", "good", "best", "word"]), [],
    )
