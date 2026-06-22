class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        
        a,b = nums1, nums2

        if len(b) < len(a):
            a,b = b,a

        res = set()

        for num in a:
            if num in res:
                continue
            
            l,r = 0, len(b) - 1
            while l <= r:
                mid = (l+r) //2
                if b[mid] == num:
                    res.add(num)
                    break
                if b[mid]>num:
                    r = mid - 1
                else:
                    l= mid + 1

        return list(res)

            