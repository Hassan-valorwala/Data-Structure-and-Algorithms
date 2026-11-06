class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        s = num
        while(num > 0):
            l = num%10
            if(s%l == 0):
                count += 1
            num = num//10
            
        return count   
