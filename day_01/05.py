def chessboard(n=8):
    for i in range(0, n):
        for j in range(0, n, 2):
            if not i % 2:
                print('#', end=' ')
            else:
                print(' ', end="#")
        print()


chessboard(5)
