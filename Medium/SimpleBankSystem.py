from typing import List
'''
Problem: Simple Bank System
Number: 58
Difficulty: Medium
Time Complexity: O(1)
Space Complexity: O(n)
URL: https://leetcode.com/problems/simple-bank-system
Topics: Design, Array, Hash Table
'''
class Bank:

    def __init__(self, balance: List[int]):
        self.__acounts_dict = dict()
        for i in range(len(balance)):
            self.__acounts_dict[i+1] = balance[i]

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 in self.__acounts_dict and account2 in self.__acounts_dict:
            if self.__acounts_dict[account1] >= money:
                self.__acounts_dict[account1] -= money
                self.__acounts_dict[account2] += money
                return True
            return False
        return False

    def deposit(self, account: int, money: int) -> bool:
        if account in self.__acounts_dict:
            self.__acounts_dict[account] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if account in self.__acounts_dict and self.__acounts_dict[account] >= money:
            self.__acounts_dict[account] -= money
            return True
        return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)