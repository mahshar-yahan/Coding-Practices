k1 = "qwertyuiop"
k2 = "asdfghjkl"
k3 = "zxcvbnm"
words = ["Hello","Alaska","Dad","Peace"]
res=[]
# First Approch
# keyboard = ["qwertyuiop", "asdfghjkl","zxcvbnm"]
# for i in words:
#     n = i.lower()
#     n =''.join(set(n))
#     for w in keyboard:
#         r = ''.join([char for char in w if char not in n])
#         if len(r)==(len(w)-len(n)):
#             res.append(i)
#             break
#         r = ""
#     n=""

# Second Approch
for i in words:
    if len(set(k1+i.lower()))==len(k1) or len(set(k2+i.lower()))==len(k2) or len(set(k3+i.lower()))==len(k3):
        res.append(i)
print(res)
