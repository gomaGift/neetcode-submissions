class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
       
        a, b = nums1, nums2
        if len(b) < len(a):
            a,b = b, a

        n = len(a)
        m = len(b)

        total = n + m

        half = total // 2
        l,r = 0, n - 1
        
        while True:
            i = (l+r) // 2
            j = half - (i + 1) - 1

            aLeft = a[i] if i >= 0 else -math.inf
            aRight = a[i + 1] if (i + 1) < n else math.inf

            bLeft = b[j] if j >= 0 else -math.inf
            bRight = b[j+1] if (j + 1) < m else math.inf

            if aLeft <= bRight and aRight >= bLeft:
                if total % 2:
                    return min(aRight, bRight) * 1.0

                return (min(aRight, bRight) + max(aLeft, bLeft)) / 2

            elif aLeft > bRight:
                r = i - 1
            else:
                l = i + 1  









        
        
        








        
        #  two pointers n(logn)
        #  median wants the middle elements, so processing half the elements + 1 guarantees the
        #  the median we do a merge sort

        n = len(nums1)
        m = len(nums2)
        i = j = 0
        median1 = median2 = 0

        for mid in range((n + m) // 2 + 1):
            median2 = median1
            if i < n and j < m:
              if nums1[i] < nums2[j]:
                median1 = nums1[i]
                i +=1
              else:
                median1 = nums2[j]
                j += 1

            elif i < n:
                median1 = nums1[i]
                i+=1
            elif j < m:
                median1 = nums2[j]
                j+=1

        if (n+ m) % 2:
            return float(median1)
        return(median1 + median2) / 2.0


        #  Brute force by sorting (nlogn)
        nums3 = sorted(nums1 + nums2)
        if len(nums3) % 2:
            return float(nums3[len(nums3) // 2])

        return (nums3[len(nums3)//2] + nums3[len(nums3) // 2 - 1]) / 2.0 
        

        