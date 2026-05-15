class Solution:
    def calPoints(self, operations: List[str]) -> int:
        new_list=[]
        for ops in operations:
            if ops=="C":
                new_list.pop()
            elif ops=="D":
                new_list.append(2*new_list[-1])
            elif ops=="+":
                new_list.append(new_list[-1]+new_list[-2])
            else:
                new_list.append(int(ops))
        return sum(new_list)
        