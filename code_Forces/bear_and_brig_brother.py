def main():
    x, y = input().split()
    x , y = int(x), int(y)
    years = 0
    while(x<=y):
        x *= 3
        y *= 2
        years += 1

    print(years)

main()