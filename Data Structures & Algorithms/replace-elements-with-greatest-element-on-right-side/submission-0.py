class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest_ele=-1
        for i in range(len(arr)-1,-1,-1):
            original =arr[i]
            arr[i]=greatest_ele
            greatest_ele=max(greatest_ele,original)
        return arr
        