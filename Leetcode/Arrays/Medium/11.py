height = [1,1]
L = 0
R = len(height)-1
output = 0
while R>=L:
    w = R-L
    h = min(height[L],height[R])
    temp = w*h
    if temp>= output:
        output = temp
    if height[L]>=height[R]:
        R-=1
    elif height[L]<height[R]:
        L+=1
# for i in range(len(height)):
#     for j in range(i+1,len(height)):
#         w = j-i
#         h = min(height[i],height[j])
#         temp_output = w*h
#         # print("width = ", w, "* height ", h ," = ",temp_output)
#         if temp_output > output:
#             output = temp_output

print(output)