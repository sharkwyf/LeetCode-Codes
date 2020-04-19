__author__ = 'DELL'

import map
import random
import time


class Player:

    def __init__(self, name, balance, m):
        self.name = name
        self.balance = balance
        self.pos = 0
        self.again = False  # �����ظ�����
        self.finish = True  # �غ��Ƿ����
        self.map = m
        self.prison = 0  # ��Ҫ���̶��ٻغ�
        self.prison_card = False
        self.protect_card = False
        self.is_protected = False

    def trade(self):
        print("trade")

    def build(self):
        i = 0
        while i < len(self.map.map):
            own_all = True
            if self.map.map[i].type == 'l' and self.map.map[i].owner == self:
                while self.map.map[i].type == 'l':
                    if self.map.map[i].owner == self:
                        i += 1
                    else:
                        own_all = False
                        break
                if own_all:
                    k = i - 1
                    if self.map.map[k].fee <= 100:  # �ж��Ƿ��з���
                        print("build house")
                        temp = k
                        c = 0
                        while self.map.map[temp].type == 'l':
                            temp -= 1
                            c += 1
                        if self.balance > 500*c:  # Ǯ���췿��
                            while self.map.map[k].type == 'l':
                                self.map.map[k].fee *= 10
                                self.balance -= 500
                                print("build house at %s" % self.map.map[k].name)
                                k -= 1
                        else:
                            print("Not enough gold to build house")
                else:
                    while self.map.map[i].type == 'l':
                        i += 1

            else:
                if self.map.map[i].type != 'l':
                    i += 1
                else:
                    while self.map.map[i].type == 'l':
                        i += 1

    def evaluate_one(self, pos):
        prob = 1/6 - abs(7-pos+self.pos)/36
        if pos >= len(self.map.map):
            pos -= len(self.map.map)
        if self.map.map[pos].type == 'ch' and self.map.map[pos].owner == self:  # �Լ�����
            return -self.balance * self.map.map[pos].fee * prob
        if (self.map.map[pos].owner is not None) and self.map.map[pos].owner != self:
            if self.map.map[pos].type == 'l' or self.map.map[pos].type == 'st' or self.map.map[pos].type == 'ch':
                if self.map.map[pos].type == 'ch':  # ���˽���
                    return self.balance * self.map.map[pos].fee * prob
                else:  # ���˷��ӡ���վ
                    return self.map.map[pos].fee * prob
        return 0

    def evaluate(self):
        sum = 0  # ����ָ��
        for i in range(2, 13):
            sum += self.evaluate_one(self.pos+i)
        print("expected payment is %d" % sum)
        if sum > 200:  # ������ֵ
            return True
        else:
            return False

    def use_card(self):
        if (not self.prison) and self.protect_card:
            is_worth = self.evaluate()
            if is_worth:
                print("use protect card")
                self.is_protected = True
                self.protect_card = False

    def roll(self):
        r1 = random.randint(1, 6)
        r2 = random.randint(1, 6)
        self.again = False
        if r1 == r2:
            self.again = True
        print("%s gets %d and %d" % (self.name, r1, r2))
        if self.prison != 0:
            if r1 == r2:
                self.prison = 0
                print("lucky dog")
            else:
                print("still need %d turns" % self.prison)
                self.prison -= 1
                self.finish = True
                return
        self.pos += r1 + r2
        if self.pos >= len(self.map.map):
            self.pos -= len(self.map.map)
            self.balance += 200  # һȦ��200
            print("%s finishes one loop, add 200" % self.name)
        print("%s goes to block %d" % (self.name, self.pos))
        self.map.map[self.pos].exec(self)
        if self.again:
            print("Bao zi!")
            self.roll()

    def start(self):
        self.finish = False
        if self.prison != 0:  # ����ڷ���
            print("in prison")
            if not self.prison_card:  # û�г�����
                x = random.randint(0, 3)  # ģ������ж�����
                if x == 0:  # ��Ǯ����
                    self.balance -= 100
                    self.prison = 0
                    print("pay for freedom")
            else:
                print("use a prison card")
                self.prison_card = False
                self.prison = 0
        self.use_card()
        self.roll()
        self.trade()
        self.build()
        self.finish = True