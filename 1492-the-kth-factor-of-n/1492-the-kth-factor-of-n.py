class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        revfac = []
        i = 1
        while i*i <= n:
            if n%i == 0:
                factors.append(i)
                if n//i != i:
                    revfac.append(n//i)
            i+=1
        new = revfac[::-1]
        sorted_lis = factors + new
        if len(sorted_lis) >= k:
            return sorted_lis[k-1]
        else:
            return -1    
