# Task
# https://github.com/daftcode/python_levelup_2018/blob/master/zadania_rekrutacyjne/Zadanie_2/Zadanie_2_polecenie.md


def find_prime_number():
    primes = {}
    number = 2

    while True:
        if number not in primes:
            yield number
            primes[number*number] = [number]
        else:
            for p in primes[number]:
                primes.setdefault(p+number, []).append(p)
                primes.pop(number, None)
        number += 1


def sum_prime_numbers(n=1234567):
    sum = 0
    if n <= 0:
        return 0

    for i, number in enumerate(find_prime_number()):
        sum += number
        if i == n-1:
            break
    return sum


def main():
    print(sum_prime_numbers())


if __name__ == '__main__':
    main()