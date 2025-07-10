from datetime import datetime
from pprint import pprint
from typing import List, Tuple

import pytest


@pytest.fixture(scope="session")
def global_resource():
    # Setup global resource
    resource = "test_resource"
    yield resource
    # Cleanup code here


@pytest.fixture(scope="function")
def temp_resource():
    # Setup temporary resource
    resource = {"data": "temp"}
    yield resource
    # Cleanup code here

class Node:
    def __init__(self, i):
        self.data = i
        self.next = None


# https://www.codewars.com/kata/52a89c2ea8ddc5547a000863/train/python
def loop_size(node):
    head = slow = fast = node

    is_init = True
    while is_init or slow != fast:  # Converging on the start of loop
        slow = slow.next
        fast = fast.next.next
        is_init = False

#     is_init = True
#     dangling_count = 0
#     while is_init or head != slow:  # Starting from head -> start of loop
#         dangling_count += 1
#         head = head.next
#         is_init = False

    is_init = True
    loop_count = 0
    while is_init or slow != fast:  # Starting from start of loop -> self
        loop_count += 1
        fast = fast.next
        is_init = False
    return loop_count


def primeFactors(n):
    prm, pwr, p = 2, 0, []
    while n > 1:
        while n % prm == 0: n, pwr = n / prm, pwr + 1
        if pwr > 0: p.append([prm,pwr])
        prm, pwr = prm + 1, 0

    pprint(p)
    return ''.join('(%d' %q[0] + ('**%d' %q[1]) * (q[1] > 1) + ')' for q in p)


def prime_factors_2(n):
    def list_prime(until_no):
        is_prime = lambda un: all(un % i != 0 for i in range(2, int(un ** .5) + 1))
        return list(filter(is_prime, list(range(2, until_no + 1))))

    reduced_n = n
    ans = ''
    for p in list_prime(int(n ** 0.5)):

        cntr = 0
        while reduced_n % p == 0:
            cntr += 1
            reduced_n /= p
        if cntr > 1:
            ans += f'({p}**{cntr})'
        elif cntr == 1:
            ans += f'({p})'

    if reduced_n > 1:
        ans += f'({int(reduced_n)})'
    return ans


class RomanNumerals:
    translate = {  # python dict remembers insertion order
        'M': 1000, 'CM': 900,
        'D': 500, 'CD': 400,
        'C': 100, 'XC': 90,
        'L': 50, 'XL': 40,
        'X': 10, 'IX': 9,
        'V': 5, 'IV': 4,
        'I': 1}
    rev_translate = {y: x for x, y in translate.items()}

    @staticmethod
    def to_roman(val: int) -> str:
        ans = ''
        remain_no = val
        for no, rom in RomanNumerals.rev_translate.items():
            mul = remain_no // no
            ans += rom * mul
            if mul != 0:
                remain_no -= no * mul
        return ans

    @staticmethod
    def from_roman(roman_num: str) -> int:
        ans = 0
        remain_str = roman_num
        while len(remain_str) > 0:
            len_char_found = 2 if remain_str[:2] in RomanNumerals.translate else 1
            ans += RomanNumerals.translate[remain_str[:len_char_found]]
            remain_str = remain_str[len_char_found:]
        return ans


ZEROES_CACHE = {}

# O(n * log n)
def zeros(n):

    if n in ZEROES_CACHE:
        return ZEROES_CACHE[n]

    tens = 0
    twos = 0
    fives = 0
    no_a = [1]
    while no_a[0] < n + 1:
        str_no, no = str(no_a), no_a[0]
        no_a[0] += 1

        s_tens, s_fives, s_twos = 0, 0, 0
        if '0' in str_no:
            rev_str_no = str_no[::-1]

            for s in rev_str_no:
                if s == '0':
                    s_tens += 1
                else:
                    break

        rem_no = no / (10 ** s_tens)
        mul = 5
        while rem_no % mul == 0:
            rem_no /= mul
            s_fives += 1

        mul = 2
        while rem_no % mul == 0:
            rem_no /= mul
            s_twos += 1

        tens += s_tens
        twos += s_twos
        fives += s_fives

    ZEROES_CACHE[n] = tens + min(twos, fives)
    return ZEROES_CACHE[n]


# O(log n) <<- ChatGPT suggested this, apparently this is a mathematical formulae
class CountZeroes:

    @staticmethod
    def zeros(n):
        count = 0
        i = 5

        while n // i:
            count += n // i
            i *= 5

        return count


def score(dice):
    counted_dice = dict(Counter(dice))  # {1: 5, 2: 1}

    scoring_rules = sorted([
        {"face_value": 1, "face_value_count": 3, "score": 1000, "rank": 1},
        {"face_value": 6, "face_value_count": 3, "score": 600, "rank": 2},
        {"face_value": 5, "face_value_count": 3, "score": 500, "rank": 3},
        {"face_value": 4, "face_value_count": 3, "score": 400, "rank": 4},
        {"face_value": 3, "face_value_count": 3, "score": 300, "rank": 5},
        {"face_value": 2, "face_value_count": 3, "score": 200, "rank": 6},
        {"face_value": 1, "face_value_count": 1, "score": 100, "rank": 7},
        {"face_value": 5, "face_value_count": 1, "score": 50, "rank": 8}
    ], key=lambda x: x["rank"])

    total_score = 0

    for rule in scoring_rules:
        face_value, face_value_count = rule["face_value"], rule["face_value_count"]
        can_recheck_times = len(dice) // face_value_count

        for _ in range(can_recheck_times):
            if face_value in counted_dice and counted_dice[face_value] >= face_value_count:
                total_score += rule["score"]
                counted_dice[face_value] -= face_value_count
            if face_value in counted_dice and counted_dice[face_value] == 0:
                counted_dice.pop(face_value, None)

    return total_score


def old_main():
    if __name__ == "__main__":
        text = "The"
        text = text.lower()

        print()
        print('Scoore')
        print(score([1, 1, 1, 1, 1, 1]))
        print('Scoore')
        nodes = [Node(i + 1) for i in range(3904)]
        for node, next_node in zip(nodes, nodes[1:]):
            node.next = next_node
        nodes[49].next = nodes[21]
        print(loop_size(nodes[0]), ': is 29?')

        print(primeFactors(4860))
        print(sum([1, 60516, 4, 15129, 9, 6724, 36, 1681]))

        start = datetime.now()
        print(f'0: \t\t\t{CountZeroes.zeros(0)}')
        print(f'6: \t\t\t{CountZeroes.zeros(6)}')
        print(f'30: \t\t\t{CountZeroes.zeros(30)}')
        print(f'100: \t\t\t{CountZeroes.zeros(100)}')
        print(f'1000: \t\t\t{CountZeroes.zeros(1000)}')
        print(f'100000: \t\t\t{CountZeroes.zeros(100000)}')
        end1 = datetime.now()
        print()
        print(end1 - start)
        print()
        print(f'1000000000: \t\t\t{CountZeroes.zeros(1000000000)}')
        end2 = datetime.now()
        print()
        print(end2 - end1)
        print()


def shiftLinkedList(head, k):
    ihead, tmp = head, head
    length = 1
    while tmp.next is not None:
        length += 1
        tmp = tmp.next
    tmp.next = head

    # -: left | +: right
    head_should_be_at = k % length
    if head_should_be_at != 0:
        left_covering = head_should_be_at
        while left_covering != 0:
            tmp = tmp.next
            left_covering -= 1

        ihead = tmp.next
        tmp.next = None

    return ihead


def hasZeroSumSubarray(nums: List[int]) -> bool:
    print(nums)
    for i in range(2, len(nums)):
        pprev, prev, me = nums[i-2], nums[i-1], nums[i]
        print(pprev, prev, me, ' | ', pprev + prev + me)
        if pprev + prev + me == 0:
            return True
    return False


def findPair(nums: List[int], target: int) -> Tuple[int]:
    holder = nums[:]
    mapper = set(holder)

    ans = []
    for i in nums:
        if target - i in mapper:
            ans.append([i, target - i])
    return ans


def modify_array(arr):
    """
    :type arr: List[int]
    :rtype: List[int]
    """
    larr = len(arr)
    a = arr
    if larr < 2:
        return arr

    min_turn = True
    for i in range(0, larr):
        ai = a[i]
        mmin, mmax = i, i

        for j in range(i + 1, larr):
            aj = a[j]
            if aj < a[mmin]:
                mmin = j
            elif a[mmax] < aj:
                mmax = j

        if ai != a[mmin] and min_turn:
            a[i], a[mmin] = a[mmin], a[i]
        elif ai != a[mmax] and not min_turn:
            a[i], a[mmax] = a[mmax], a[i]
        min_turn = not min_turn
    return arr

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    if len(strs) < 2:
        return strs

    alfa = {chr(c): no for no, c in enumerate(range(ord('a'), ord('z') + 1), 1)}
    print(alfa)

    cntr = {}
    for word in strs:
        w_cntr = Counter(word)
        sot_word = ''.join([c * w_cntr[c] for c in alfa if c in w_cntr])
        print(sot_word)
        cntr[sot_word] = cntr.get(sot_word, [])
        cntr[sot_word].append(word)

    return cntr


from collections import defaultdict, Counter
from heapq import heappop, nlargest


def topKFrequent(nums: List[int], k: int) -> List[int]:
    cntr = dict(Counter(nums))
    heapp = nlargest(k, list([-1 * c for c in cntr.values()]))

    rev_cntr = {}
    for no, cnt in cntr.items():
        rev_cntr[cnt] = rev_cntr.get(cnt, set([]))
        rev_cntr[cnt].add(no)

    ans = []
    while len(ans) < k or len(heapp) != 0:
        k_no = -1 * heappop(heapp)
        if k_no in rev_cntr:
            ans.extend(rev_cntr[k_no])
            rev_cntr.pop(k_no)

    return ans[:k]

def productExceptSelf(nums: List[int]) -> List[int]:

    l_num = len(nums)
    # right [48, 24, 6, 1]
    # left [1, 1, 2, 8]

    left_2me, right_2me = [], []
    l_mul, r_mul = 1, 1
    for i in range(l_num):
        l = i
        l_mul *= nums[l - 1] if l != 0 else 1
        left_2me.append(l_mul)
    for i in range(l_num - 1, -1, -1):
        r = i
        r_mul *= nums[r + 1] if r != l_num - 1 else 1
        right_2me.append(r_mul)

    right_2me = right_2me[::-1]
    print('', '\n', nums, '\n', left_2me, '\n', right_2me)

    ans = []
    for i in range(l_num):
        ans.append(left_2me[i] * right_2me[i])
    return ans

board=[
    ["1","2",".",".","3",".",".",".","."],
    ["4",".",".","5",".",".",".",".","."],
    [".","9","8",".",".",".",".",".","3"],
    ["5",".",".",".","6",".",".",".","4"],
    [".",".",".","8",".","3",".",".","5"],
    ["7",".",".",".","2",".",".",".","6"],
    [".",".",".",".",".",".","2",".","."],
    [".",".",".","4","1","9",".",".","8"],
    [".",".",".",".","8",".",".","7","9"]
]


def isValidSudoku(board: List[List[str]]) -> bool:
    to_set = lambda x: [set() for _ in range(x)]
    rows, cols, sq = to_set(9), to_set(9), to_set(9)
    for rno, row in enumerate(board):
        for cno, val_cell in enumerate(row):
            sq_no = (rno // 3) * 3 + (cno // 3)
            print(rno, cno, sq_no, ' | ', val_cell)
            if val_cell in rows[rno] or val_cell in cols[cno] or val_cell in sq[sq_no]:
                print('-'*100)
                print(rows[rno], cols[cno], sq[sq_no])
                return False

            if val_cell != '.':
                rows[rno].add(val_cell)
                cols[cno].add(val_cell)
                sq[sq_no].add(val_cell)
    return True

def longestConsecutive(nums: List[int]) -> int:
    snum = sorted(nums)
    lnum = len(snum)

    print(snum)
    i = 0
    prev, prev_len, me_len = None, 0, 0
    while i < lnum:
        if i == 0:
            prev = snum[i]
            me_len = 1
            i += 1
            continue
        if prev == snum[i]:
            pass
        elif prev + 1 == snum[i]:
            me_len += 1
        else:
            print(i, me_len, prev_len, ' | ', prev)
            prev_len = max(me_len, prev_len)
            me_len = 1
        prev = snum[i]
        i += 1
    return max(prev_len, me_len)

def longest_consecutive_2(nums: List[int]) -> int:
    mp = defaultdict(int)
    res = 0

    for num in nums:
        if not mp[num]:
            print('-'*100, res, num)
            print(mp)
            mp[num] = mp[num - 1] + mp[num + 1] + 1
            print(mp, num - mp[num - 1])
            mp[num - mp[num - 1]] = mp[num]
            print(mp, num - mp[num + 1])
            mp[num + mp[num + 1]] = mp[num]
            print(mp)
            res = max(res, mp[num])
            print('-'*100, res)
    return res


class Solution:

    def idx_pair(self, char):
        idx = 0 if char.islower() else 1
        case_letter = 'a' if char.islower() else 'A'
        return idx, ord(char) - ord(case_letter)

    def cnt_em(self, s):
        ss2 = [[0] * 26]
        ss2.append([0] * 26)
        for c in s:
            idx, idx2d = self.idx_pair(c)
            ss2[idx][idx2d] += 1
        return ss2

    def display(self, arr, str, str2):
        sstr = []
        for idx, row in enumerate(arr):
            for idx2d, value in enumerate(row):
                char = chr(ord('a') + idx2d)
                char = char if idx==0 else char.upper()
                if value < 0:
                    print(f'Error value {value}: {str}: {char}')
                elif value > 0:
                    sstr.append(char)
        print(str2, ''.join(sorted(sstr)), '|-|', str)

    def minWindow(self, s: str, t: str) -> str:
        lens, lent = len(s), len(t)
        if lent > lens:
            return ""
        elif s==t:
            return t

        t_cnt = self.cnt_em(t)
        s_cnt = self.cnt_em('')

        two21d = lambda twod: twod[0] + twod[1]
        equate = lambda spr, chld: {True} == set([spr[idx] == cnt for idx, cnt in enumerate(chld) if cnt > 0])
        # equate = lambda spr, chld:  iequate(spr, chld)

        srt_sub = ''
        l, wnd = 0, lent
        while l + wnd < lens:
            r = l + 1
            rem_idx, rem_idx2d = self.idx_pair(s[l])
            s_cnt[rem_idx][rem_idx2d] += 1

            os_cnt = [c[:] for c in s_cnt]
            while r < lens:
                add_idx, add_idx2d = self.idx_pair(s[r])
                os_cnt[add_idx][add_idx2d] += 1

                fnd = s[l:r+1]
                if equate(two21d(os_cnt), two21d(t_cnt)):
                    if (not srt_sub) or len(fnd) < len(srt_sub):
                        srt_sub = fnd
                r+=1
            s_cnt[rem_idx][rem_idx2d] -= 1
            l += 1
        # 1,4
        return srt_sub


from typing import List


def shift_zeros_to_the_end(nums: List[int]) -> None:
    # Write your code here

    lnum = len(nums)
    cnt = 0
    l, r = 0, lnum - 1
    while l < lnum:
        if nums[l] == 0:
            cnt += 1

    l, r = 0, min(1, lnum - 1)
    while l < lnum and r < lnum:
        if nums[r] == 0:
            r += 1
            continue
        if nums[l] == 0:
            nums[l] = nums[r]
            r += 1
        l += 1

    l = lnum - 1
    while l >= lnum - cnt:
        nums[l] = 0
        l -= 1


def compute_hcf(x, y):
   while y:
       x, y = y, x % y
   return x


# This function computes LCM
def compute_lcm(x, y):
    lcm = (x*y)//compute_hcf(x,y)
    return lcm


def trap(height: list[int]) -> int:
    if not height:
      return 0

    ans = 0
    l = 0
    r = len(height) - 1
    maxL = height[l]
    maxR = height[r]

    while l < r:
      x = 0
      if maxL < maxR:
        ans+= maxL - height[l]
        l += 1
        maxL = max(maxL, height[l])
      else:
        ans+= maxR - height[r]
        r -= 1
        maxR = max(maxR, height[r])
    return ans

if __name__ == "__main__":
    print(trap([4, 2, 0, 3, 2, 5, 1, 2]))
    # k = 14
    # nodes = [Node(i) for i in range(1, 39)]
    # nodes = nodes[-k:] + nodes[:-k]
    # for node, next_node in zip(nodes, nodes[1:]):
    #     node.next = next_node
    #
    # print(nodes[0].data, nodes[0].next.data, '...', nodes[-1].data, '|', len(nodes), f'({k})')
    # new_n = shiftLinkedList(nodes[0], k)
    # print(new_n.data, new_n.next.data, '...', f'({k})')
    #
    # print("asZeroSumSubarray")
    # print(hasZeroSumSubarray([6, 1, -4, -3, 1, 7]))
    # print("asZeroSumSubarray")
    # print(modify_array([13, 7, 8, 3, 2, 10, 15, -1]))
    # print(groupAnagrams(strs=["act","pots","tops","cat","stop","hat"]))
    # print(topKFrequent([1,2,2,3,3,3], 2))
    # print(productExceptSelf([1,2,4,6]))
    # print(productExceptSelf([-1,0,1,2,3]))
    # print(isValidSudoku(board))
    # print(([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))
    # print(longest_consecutive_2([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))
    # s = Solution()
    # print('--->', s.minWindow(s="abc", t="bc"), '--->')
    # print(shift_zeros_to_the_end([0, 1, 0, 3, 2]))
