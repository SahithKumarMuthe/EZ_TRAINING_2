def generate_magic_square(n):
    if n % 2 == 0:
        raise ValueError("Only odd-sized magic squares are supported")
    magic_square = [[0] * n for _ in range(n)]
    row, col = 0, n // 2
    num = 1
    while num <= n * n:
        magic_square[row][col] = num
        num += 1
        new_row, new_col = (row - 1) % n, (col + 1) % n
        if magic_square[new_row][new_col] != 0:
            row = (row + 1) % n
        else:
            row, col = new_row, new_col
    return magic_square
def print_magic_square(magic_square):
    for row in magic_square:
        for num in row:
            print(num, end="\t")
        print()
if __name__ == "__main__":
    n = int(input("Enter the size of the magic square (odd number): "))
    if n % 2 == 0:
        print("Only odd-sized magic squares are supported")
    else:
        magic_square = generate_magic_square(n)
        print("Magic Square of size", n, "x", n, "is:")
        print_magic_square(magic_square)
