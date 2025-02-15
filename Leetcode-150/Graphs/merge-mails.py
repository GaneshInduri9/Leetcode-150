"""
    Given a list of accounts where each element accounts[i] is a list of strings,
    where the first element accounts[i][0] is a name, and the rest of the elements 
    are emails representing emails of the account.Now, we would like to merge these
    accounts. Two accounts definitely belong to the same person if there is some 
    common email to both accounts. Note that even if two accounts have the same name,
    they may belong to different people as people could have the same name. A person 
    can have any number of accounts initially, but all of their accounts definitely 
    have the same name.After merging the accounts, return the accounts in the following
    format: the first element of each account is the name, and the rest of the 
    elements are emails in sorted order. The accounts themselves can be returned in any order.
"""

from typing import List


class DisJointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)
        self.emptyEdges = 0

    def findUParent(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUParent(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        ul_pu = self.findUParent(u)
        ul_pv = self.findUParent(v)

        if ul_pu == ul_pv:
            self.emptyEdges += 1
            return

        if self.rank[ul_pv] < self.rank[ul_pu]:
            self.parent[ul_pv] = ul_pu

        elif self.rank[ul_pu] < self.rank[ul_pv]:
            self.parent[ul_pu] = ul_pv

        else:
            self.parent[ul_pu] = ul_pv
            self.rank[ul_pv] += 1


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """
            Intial config create a map of mail to node and then if we see
            a mail again we union this nodes as they are same user mails
            and then once that is done we can set marge the nodes by
            iterating over the map and then find it's ultimate parent

        Args:
            accounts (List[List[str]]): _description_

        Returns:
            List[List[str]]: _description_
        """
        n = len(accounts)
        D = DisJointSet(n)
        mapMailToNode = {}

        # {j1@.com : 1, j2@.com: 2.......}
        for i in range(n):
            for j in range(1, len(accounts[i])):
                mail = accounts[i][j]
                if mail in mapMailToNode:
                    D.union(i, mapMailToNode[mail])
                else:
                    mapMailToNode[mail] = i
        # [[j1@.com, j2@.com], [k1@.com, k2@.com:], [], [].....]
        mergeNodes = [[] for i in range(n)]
        for mail, node in mapMailToNode.items():
            ul_p = D.findUParent(node)
            mergeNodes[ul_p].append(mail)

        # [["john", j1@.com, j2@.com]]]
        res = []
        for i in range(n):
            if len(mergeNodes[i]) == 0:
                continue

            mergeNodes[i].sort()
            temp = []
            temp.append(accounts[i][0])
            temp.extend(mergeNodes[i])
            res.append(temp)
        return res


def test():

    sol = Solution()
    accounts = [
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ]
    print(sol.accountsMerge(accounts))


if __name__ == "__main__":
    test()
