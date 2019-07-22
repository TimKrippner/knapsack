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


val = [
    4,
    11,
    21,
    22,
    26,
    28,
    29,
    31,
    36,
    36,
    39,
    40,
    50,
    54,
    54,
    55,
    55,
    55,
    56,
    66,
    74,
    78,
    108,
    113
]
wt = [
    427,
    885,
    1212,
    1578,
    1401,
    2193,
    2069,
    3016,
    2757,
    2065,
    3790,
    495,
    879,
    4283,
    3177,
    4357,
    5275,
    3231,
    3267,
    4845,
    5412,
    7568,
    7629,
    8089
] 
xW = input('Enter your available money: ')
W = int(xW)
n = len(val)
K = knapSack(W, wt, val, n)
ix = knapSackIndex(W, wt, val, n ,K)
print("Monthly payment reduction: ${}, by paying off loans: {}".format(K[-1][-1], str(ix)))
