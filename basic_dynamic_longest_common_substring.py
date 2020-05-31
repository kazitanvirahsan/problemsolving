# Two given strings to calculate longest common subsequence using dynamic programming

# algorithm
# inputs x & y
# for i =0 to len(x)-1 
#    for j =0 to - len(y)-1
#        if x[i] == y[j]
#           arr[i][j] = arr[i-1][j-1] + 1
#        else
#           arr[i][j] = max(arr[i-1][j],arr[i][j-1])

x = "ABABC"[::-1]
y = "BABCA"[::-1]

x_len = len(x) + 1
y_len = len(y) + 1

arr = [ [0 for i in range(y_len)] for j in range(x_len)]

for i in range(1,x_len):
    for j in range(1,y_len):
        if x[i-1] == y[j-1]:
            arr[i][j] = arr[i-1][j-1] + 1
        else:
            arr[i][j] = max(arr[i-1][j], arr[i][j-1])

# output = 4 
print('lcs=%d'% arr[len(x)][len(y)])

