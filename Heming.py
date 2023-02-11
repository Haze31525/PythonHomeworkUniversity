import itertools


def hamming_distance(a, b):
    return sum(el1 != el2 for el1, el2 in zip(a, b))


def main():
    k = int(input("Enter the value of k: "))
    s = input("Enter the bit string: ")
    n = len(s)
    answer = ''
    for i in range(n):
        for subset in itertools.combinations(range(n), i):
            new_s = [c for c in s]
            for j in subset:
                new_s[j] = '0' if s[j] == '1' else '1'
            if hamming_distance(s, ''.join(new_s)) == k:
                answer = ''.join(new_s) + ' ' +  answer
    print(answer)


if __name__ == "__main__":
    main()
