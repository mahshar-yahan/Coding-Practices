nums = [1,3,5,6]
target = 7

low = 0
high = len(nums)-1
while(low<=high):
    mid = (high+low)//2
    if nums[mid] == target:
        print(mid)
        break
    elif nums[mid] > target:
        high = mid-1
    else:
        low = mid+1
print(high,low)
print(max(high,low))