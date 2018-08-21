import glob

# Zadanie
# https://github.com/daftcode/python_levelup_2018/blob/master/zadania_rekrutacyjne/Zadanie_1/Zadanie_1_polecenie.md
# tested on .txt files

def iterate_over_files(path):
    files = glob.glob(path)
    for file in files:
        yield file


def read_file(filename, dict, count):
    with open(filename, 'r') as file:
        while True:
            char = file.read(1)
            if not char:
                break
            if char.lower() in dict:
                dict[char.lower()] += 1
            else:
                dict[char.lower()] = 1
                count += 1


def summary(dict):
    result = ''
    for key, value in sorted(dict.items()):
        result += f'{key}{value}'
    return result


def main():
    path = '' #path to directory
    dict = {}
    count = 0
    for f in iterate_over_files(path):
        read_file(f, dict, count)
    print(summary(dict))


if __name__ == '__main__':
    main()
