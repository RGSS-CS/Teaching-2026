from collections import defaultdict
from sys import stdin
input = stdin.readline

T,N = map(int, input().split()) # get T and N

for _ in range(T): # get the T lines of input
    line = input()

    freq = defaultdict(int)
    for i in range(N):
        freq[line[i]] += 1 # get freq of every letter

    lastHeavy = freq[line[0]] > 1 
    for i in range(1,N):
        if freq[line[i]] > 1: # consecutive heavy
            if lastHeavy:
                print('F')
                break
            lastHeavy = freq[line[i]] > 1 # update polarity 
        else:
            if not lastHeavy: # consecutive light
                print('F')
                break
            lastHeavy = freq[line[i]] > 1 # update polarity
    else:
        print('T')
    
