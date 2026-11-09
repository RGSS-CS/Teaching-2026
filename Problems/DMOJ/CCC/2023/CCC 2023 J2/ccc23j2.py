from sys import stdin
input = stdin.readline

pepperToHeat = {
    "Poblano" :	1500,
    "Mirasol" :	6000,
    "Serrano" :	15500,
    "Cayenne" :	40000,
    "Thai" : 75000,
    "Habanero" : 125000
}

totalHeat = 0
N = int(input())
for i in range(N):
    pepper = input().strip()

    totalHeat += pepperToHeat[pepper]

print(totalHeat)
