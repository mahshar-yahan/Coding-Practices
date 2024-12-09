nums1 = [-1,0,0,3,3,3,0,0,0]
m = 6
nums2 = [1,2,2]
n = 3
j = 0
# nums = []
# for i in range(max(m.n)):
#     if nums1[i]==nums2[j]:
#         nums.append(nums1[i])
#         nums.append(nums2[j])
#         j+=1
#     elif nums1[i]<nums[j]:
#         nums.append(nums1[i])
#     else:
#         nums.append()

# nums = []
# nums = nums1+nums2
# nums.sort()
# while 0 in nums:
#     nums.remove(0)
# nums.sort()
# nums1.clear()
# for i in nums:
#     nums1.append(i)
for j in range(n):
    nums1[m+j] = nums2[j]
nums1.sort()


print(nums1)