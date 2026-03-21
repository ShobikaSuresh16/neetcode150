# Valid Anagram

## Generic learnings

- If order does not matter, think in terms of **frequency/count**, not position.
- Avoid `sort()` when possible because sorting usually makes time complexity `O(n log n)`, while hashmap counting can do it in `O(n)`.
- If counting in a hashmap, think: **“first time seen => start from 0”**.
- Strings are immutable in Python, so use `sorted(s)` and not `s.sort()`.

## One-line memory

Anagram = same characters with same frequency; order does not matter.

## My brute-force thinking

- First compare lengths. If lengths differ, return `False`.
- If lengths match, sort both strings.
- Compare character by character.
- If all match, return `True`.

## Why brute force is not best

- Sorting adds extra cost.
- I do not really care about order here, only character counts.

## Better technique learned

- Use two hashmaps to count frequency of each character.
- If both frequency maps are equal, the strings are anagrams.

## Important thinking shift

- Instead of making both strings look the same by sorting,
- directly check whether both contain the same characters the same number of times.

## Edge case to remember

When writing:
`count[ch] = 1 + count.get(ch, 0)`

the idea is:

- if `ch` is already present, increment its count
- if `ch` is not present yet, start from `0`

Without default `0`, first occurrence would fail.

## Loop note

- `while i < n` with `i = 0` runs from `0` to `n-1`
- `for i in range(n)` also runs from `0` to `n-1`
- `for i in range(1, n)` runs from `1` to `n-1`

## Case sensitivity note

Not needed in this problem because input contains only lowercase English letters.

If mixed case were allowed, convert both strings to lowercase first:
`s = s.lower()`
`t = t.lower()`

## Complexity

### Sorting approach

- Time: `O(n log n)`
- Space: `O(n)`

### Hashmap approach

- Time: `O(n + m)`
- Space: `O(1)` in this problem because only 26 lowercase letters are possible

## Mistakes / traps to remember

- Do not use `.sort()` on strings
- Do not use `ord()` unnecessarily
- For frequency counting, always think about first occurrence

## Brute-force code:

class Solution:
def isAnagram(self, s: str, t: str) -> bool:
if len(s) != len(t):
return False

        s = sorted(s)
        t = sorted(t)

        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True

## Optimized code - Hash Map

class Solution:
def isAnagram(self, s: str, t: str) -> bool:
if len(s) != len(t):
return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT
