from math import floor
from sys import stdin
input = stdin.readline

while True:
    C = int(input())
    if C == 0: break

    lo = floor(C**0.5)
    while C % lo != 0:
        lo -= 1
    print(f"Minimum perimeter is {lo*2+C//lo*2} with dimensions {lo} x {C//lo}")
