import timeit
from typing import Callable


def boyer_moore_search(text, pattern):
    def build_shift_table(pattern):
        table = {}
        length = len(pattern)
        for index, char in enumerate(pattern[:-1]):
            table[char] = length - index - 1
        table.setdefault(pattern[-1], length)
        return table

    shift_table = build_shift_table(pattern)
    i = 0

    while i <= len(text) - len(pattern):
        j = len(pattern) - 1

        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j < 0:
            return i
        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))
    return -1


def kmp_search(main_string, pattern):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        return lps

    M = len(pattern)
    N = len(main_string)

    lps = compute_lps(pattern)
    i = 0
    j = 0

    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == M:
            return i - j

    return -1



def rabin_karp_search(main_string, substring):
    def polynomial_hash(s, base=256, modulus=101):
        n = len(s)
        hash_value = 0
        for i, char in enumerate(s):
            power_of_base = pow(base, n - i - 1) % modulus
            hash_value = (hash_value + ord(char) * power_of_base) % modulus
        return hash_value

    substring_length = len(substring)
    main_string_length = len(main_string)

    base = 256
    modulus = 101

    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)

    h_multiplier = base ** (substring_length - 1) % modulus

    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i:i + substring_length] == substring:
                return i

        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus

    return -1


def read_file(filename):
    with open(filename, 'r', encoding='utf8') as f:
        return f.read()


def benchmark(func: Callable, text_: str, pattern_: str):
    setup_code = f"from __main__ import {func.__name__}"
    stmt = f"{func.__name__}(text, pattern)"
    return timeit.timeit(stmt=stmt, setup=setup_code, globals={'text': text_, 'pattern': pattern_}, number=10)


if __name__ == "__main__":
    article1 = read_file("стаття 1.txt")
    article2 = read_file("стаття 2.txt")

    real_pattern = "Висновки. "
    fake_pattern = "мама мила раму"

    results = []
    for pattern in (real_pattern, fake_pattern):
        time = benchmark(boyer_moore_search, article1, pattern)
        results.append((boyer_moore_search.__name__, pattern, "стаття 1", time))
        time = benchmark(boyer_moore_search, article2, pattern)
        results.append((boyer_moore_search.__name__, pattern, "стаття 2", time))

        time = benchmark(kmp_search, article1, pattern)
        results.append((kmp_search.__name__, pattern, "стаття 1", time))
        time = benchmark(kmp_search, article2, pattern)
        results.append((kmp_search.__name__, pattern, "стаття 2", time))


        time = benchmark(rabin_karp_search, article1, pattern)
        results.append((rabin_karp_search.__name__, pattern, "стаття 1", time))
        time = benchmark(rabin_karp_search, article2, pattern)
        results.append((rabin_karp_search.__name__, pattern, "стаття 2", time))

    title = f"{'Алгоритм':<30} | {'Підрядок':<30} | {'Стаття:':<20} | {'Час виконання, сек'}"
    print(title)
    print("-" * len(title))
    for result in results:
        print(f"{result[0]:<30} | {result[1]:<30} | {result[2]} | {result[3]}")
