# Zadanie
# https://github.com/daftcode/python_levelup_2018/blob/master/zadania_rekrutacyjne/Zadanie_4/Zadanie_4_polecenie.md

import glob


def iterate_over_files(path):
    files = glob.glob(path)
    for file in files:
        yield file


def read_file(filename):
    with open(filename, 'r') as file:
        for n, _ in enumerate(file):
            pass

    n += 1
    arr = [[0] * n for _ in range(n)]

    with open(filename, 'r') as file:
        for i, line in enumerate(file):
            for j, number in enumerate(line.split()):
                arr[i][j] = int(number)
    print(arr)
    return arr


def find_max(arr):
    for i in range(len(arr)-2, -1, -1):
        for j in range(i+1):
            arr[i][j] += max(arr[i+1][j], arr[i+1][j+1])
    return arr[0][0]


def main():
    path = '' #path to directory
    for file in iterate_over_files(path):
        print(find_max(read_file(file)))


if __name__ == '__main__':
    main()



