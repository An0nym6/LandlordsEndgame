#file  -- ending.py --
# -*- coding: UTF-8 -*-

# 依赖
import copy
from itertools import combinations

# 输入
playerA = []
playerB = []

# 对抗树
# [
#   [val, [cards], [next]]
#   ...
# ]
tree = [[0, [], []]]
root = 0
count = 0

# 映射
def getVal(cards):
    vals = { '3': 0, '4': 1, '5': 2, '6': 3, '7': 4, '8': 5, '9': 6, '10': 7, 'J': 8, 'Q': 9, 'K': 10, 'A': 11, '2': 12, 'Y': 13, 'Z': 14 }
    for i, card in enumerate(cards):
        cards[i] = vals[card]
def getCard(vals):
    cards = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', 'Y', 'Z']
    ans = []
    for val in vals:
        ans.append(cards[val])
    return ans

# 获得顺子
def getSeq(cards, length, size, num):
    ans = []
    seq = []
    if len(cards) >= length * num:
        for card in list(set(cards)):
            if ((len(seq) == 0 and card > size and card < 12 and cards.count(card) >= num) or
                (len(seq) != 0 and seq[-1] + 1 == card and card < 12 and cards.count(card) >= num)):
                seq = seq + [card] * num
            else:
                seq = [card]
            if len(seq) == length * num:
                pattern = -1
                if num == 1:
                    pattern = length + 2
                elif num == 2:
                    pattern = length + 12
                elif num == 3:
                    pattern = length + 21
                ans.append({ 'c': copy.deepcopy(seq), 'p': pattern, 's': seq[0] })
                seq = seq[num:]
    return ans

# 获得飞机带翅膀
def getPlane(cards, length, size):
    ans = []
    seq = []
    if len(cards) >= length * 4:
        for card in list(set(cards)):
            if ((len(seq) == 0 and card > size and card < 12 and cards.count(card) >= 3) or
                (len(seq) != 0 and seq[-1] + 1 == card and card < 12 and cards.count(card) >= 3)):
                seq = seq + [card] * 3
            else:
                seq = []
            if len(seq) == length * 3:
                cardBs = list(set(cards) - set(seq))
                for case in list(combinations(cardBs, length)):
                    newSeq = seq + list(case)
                    ans.append({ 'c': newSeq, 'p': length + 26, 's': seq[0] })
                seq = seq[3:]
    return ans

# 枚举可能的下一步
def getNextMove(cards, pattern, size):
    moves = []
    # 火箭
    if 13 in cards and 14 in cards:
        moves.append({ 'c': [13, 14], 'p': 0, 's': 100 })
    # 炸弹
    if pattern != 0:
        for card in set(cards):
            if cards.count(card) == 4 and (pattern != 1 or (pattern == 1 and card > size)):
                moves.append({ 'c': [card] * 4, 'p': 1, 's': card })
    # 单个牌
    if pattern == -1 or pattern == 2:
        for card in set(cards):
            if card > size:
                moves.append({ 'c': [card], 'p': 2, 's': card })
    # 对子牌
    if pattern == -1 or pattern == 3:
        for card in set(cards):
            if cards.count(card) >= 2 and card > size:
                moves.append({ 'c': [card] * 2, 'p': 3, 's': card })
    # 三张牌
    if pattern == -1 or pattern == 4:
        for card in set(cards):
            if cards.count(card) >= 3 and card > size:
                moves.append({ 'c': [card] * 3, 'p': 4, 's': card })
    # 三带一
    if pattern == -1 or pattern == 5:
        for card in set(cards):
            if cards.count(card) >= 3 and card > size:
                for cardB in set(cards):
                    if card != cardB:
                        moves.append({ 'c': [card] * 3 + [cardB], 'p': 5, 's': card })
    # 三带二
    if pattern == -1 or pattern == 6:
        for card in set(cards):
            if cards.count(card) >= 3 and card > size:
                for cardB in set(cards):
                    if card != cardB and cards.count(cardB) >= 2:
                        moves.append({ 'c': [card] * 3 + [cardB] * 2, 'p': 6, 's': card })
    # 单顺子
    if pattern == -1:
        for length in range(5, 13):
            moves = moves + getSeq(cards, length, -1, 1)
    if pattern >= 7 and pattern <= 12:
        moves = moves + getSeq(cards, pattern - 2, size, 1)
    # 双顺子
    if pattern == -1:
        for length in range(3, 11):
            moves = moves + getSeq(cards, length, -1, 2)
    if pattern >= 15 and pattern <= 22:
        moves = moves + getSeq(cards, pattern - 12, size, 2)
    # 三顺子
    if pattern == -1:
        for length in range(2, 7):
            moves = moves + getSeq(cards, length, -1, 3)
    if pattern >= 23 and pattern <= 27:
        moves = moves + getSeq(cards, pattern - 21, size, 3)
    # 飞机带翅膀
    if pattern == -1:
        for length in range(2, 7):
            moves = moves + getPlane(cards, length, -1)
    if pattern >= 28 and pattern <= 32:
        moves = moves + getPlane(cards, pattern - 26, size)
    # 四带两张单牌
    if pattern == -1 or pattern == 33:
        for card in set(cards):
            if cards.count(card) >= 4 and card > size:
                cardBs = list(set(cards) - set([card]))
                for case in list(combinations(cardBs, 2)):
                    moves.append({ 'c': [card] * 4 + list(case), 'p': 33, 's': card })
    # 四带两个对子
    if pattern == -1 or pattern == 34:
        for card in set(cards):
            if cards.count(card) >= 4 and card > size:
                cardBs = list(set(cards) - set([card]))
                for case in list(combinations(cardBs, 2)):
                    flag = True
                    for element in list(case):
                        if cards.count(element) < 2:
                            flag = False
                            break
                    if flag:
                        moves.append({ 'c': [card] * 4 + list(case) * 2, 'p': 34, 's': card })
    # 不出
    if pattern != -1:
        moves.append({ 'c': [], 'p': -1, 's': -1 })
    return moves

# 从 list 中删掉另一个 list
def removeElements(listA, listB):
    for element in listB:
        listA.remove(element)

# 对抗树
def searchTree(playerA, playerB, pattern, size, level, parent):
    global count
    global tree
    moves = getNextMove(playerA, pattern, size)
    for i, move in enumerate(moves):
        if level < 2:
            print '  ' * level * 2 + '正在尝试', i, '/', len(moves)
        newPlayerA = copy.deepcopy(playerA)
        removeElements(newPlayerA, move['c'])
        count += 1
        temp = count
        tree.append([0, move['c'], []])
        tree[parent][2].append(count)
        # print '  ' * level * 2 + 'D ->', move['c'], '|', newPlayerA
        if len(newPlayerA) == 0:
            tree[count][0] = 1
            return 1
        else:
            flag = 1
            moves_ = getNextMove(playerB, move['p'], move['s'])
            for j, move_ in enumerate(moves_):
                if level < 2:
                    print '  ' * (level * 2 + 1) + '正在尝试', j, '/', len(moves_)
                newPlayerB = copy.deepcopy(playerB)
                removeElements(newPlayerB, move_['c'])
                count += 1
                tree.append([0, move_['c'], []])
                tree[temp][2].append(count)
                # print '  ' * (level * 2 + 1) + 'N ->', move_['c'], '|', newPlayerB
                if len(newPlayerB) == 0 or searchTree(newPlayerA, newPlayerB, move_['p'], move_['s'], level + 1, count) == 0:
                    flag = 0
                    break
            if flag == 1:
                tree[temp][0] = 1
                return 1
            elif flag == 0 and level < 3:
                tree = tree[:temp]
                count = temp - 1
    return 0

# 主体
playerAStr = raw_input('请输入地主牌：')
playerBStr = raw_input('请输入农民牌：')
playerA = playerAStr.split()
playerB = playerBStr.split()

# 使用数值代替牌面
getVal(playerA)
getVal(playerB)

# 搜索对抗树
if searchTree(playerA, playerB, -1, -1, 0, root):
    print '完成！'
    flag = 1
    while flag:
        flag = 0
        for node in tree[root][2]:
            if tree[node][0] == 1:
                print '地主应出', getCard(tree[node][1])
                root = node
                moveStr = raw_input('请输入农民的出牌：')
                move = moveStr.split()
                getVal(move)
                for node_ in tree[root][2]:
                    if sorted(tree[node_][1]) == sorted(move):
                        root = node_
                        break
                flag = 1
                break
else:
    print '失败！'
