def hollow_triangle(height):
    triangle = []
    for i in range(1, height + 1):
        line = '_' * (height - i)
        if i == 1 or i == height:
            line += '#' * (2 * i - 1)
        else:
            line += '#' + '_' * (2 * i - 3) + '#'
        line += '_' * (height - i)
        triangle.append(line)
    return triangle


if __name__ == "__main__":
    triangle6 = hollow_triangle(6)
    for line in triangle6:
        print(line)
    print("---- Final Height")
    triangle9 = hollow_triangle(9)
    for line in triangle9:
        print(line)
    print("---- Final Height")
