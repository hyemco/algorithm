def power(n, m):
    if m == 0:
        return 1
    else:
        return n * power(n, m - 1)


for _ in range(10):
    tc = int(input())
    n, m = map(int, input().split())

    print(f'#{tc} {power(n, m)}')