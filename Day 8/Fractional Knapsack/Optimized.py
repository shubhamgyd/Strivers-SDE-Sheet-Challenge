class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight




class Solution:
    def fractionalKnapsack(self, W, arr, n):
        arr.sort(key=lambda x: x.value / x.weight, reverse=True)
        curWeight = 0
        finalvalue = 0.0
        for i in range(n):
            if curWeight + arr[i].weight <= W:
                curWeight += arr[i].weight
                finalvalue += arr[i].value
            else:
                remain = W - curWeight
                finalvalue += arr[i].value / arr[i].weight * remain
                break
        return finalvalue




if __name__ == '__main__':
    n = 3
    W = 50
    arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
    obj = Solution()
    ans = obj.fractionalKnapsack(W, arr, n)
    print("The maximum value is", ans)