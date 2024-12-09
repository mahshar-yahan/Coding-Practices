height = [1,1]

output = 0
for i in range(len(height)):
    for j in range(i+1,len(height)):
        w = j-i
        h = min(height[i],height[j])
        temp_output = w*h
        # print("width = ", w, "* height ", h ," = ",temp_output)
        if temp_output > output:
            output = temp_output

print(output)