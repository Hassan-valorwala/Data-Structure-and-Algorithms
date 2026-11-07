class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        add = 0
        while(n>0):
            x = n%10
            product *= x
            add += x
            n = n//10
        return product - add       

