def knapSack(W, wt, val, n):
    K = [[0 for x in range(W+1)] for x in range(n+1)] 
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    return K

def knapSackIndex(W, wt, val, n, K):
    res = K[-1][-1]
    ix = []
    w = W
    ix = []
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == K[i - 1][w]:
            continue
        else:
            ix.append(i-1)
            res = res - val[i - 1]
            w = w -  wt[i - 1]
    return ix

import csv

minWt = int(input('Enter your minimum available money: '))
maxWt = int(input('Enter your maximum available money: '))

W = minWt

wt = []
val = []

with open('loans.csv', 'r') as csv_file:
    lines = csv_file.readlines()

for line in lines:
    line = line.rstrip('\n')
    data = line.split(',')
    wt.append(int(data[0]))
    val.append(int(data[1]))

while W < maxWt:
	n = len(val)
	K = knapSack(W, wt, val, n)
	ix = knapSackIndex(W, wt, val, n ,K)
	print("With a spending of ${} has a monthly payment reduction of ${}, by paying off loans: {}".format(W, K[-1][-1], str(ix)))
	W = W + 100
