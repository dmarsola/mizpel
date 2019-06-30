import strings as s
from commons import word_list
import datetime


def test_methods():
    s1, s2 = "ABCDE", "ABCDE"
    print(f'{"Pass" if s.compare_equal(s1, s2) else "Fail"} | {s1}, {s2}\n')

    # test different case sensitive
    s1, s2 = "ABCDE", "aBCDe"
    print(f'{"Pass" if not s.compare_equal(s1, s2) else "Fail"} | {s1}, {s2}\n')

    # test equal case insensitive
    s1, s2 = "ABCDE", "aBCDe"
    print(f'{"Pass" if s.compare_equal(s1, s2, False) else "Fail"} | {s1}, {s2}\n')

    # test different on last
    s1, s2 = "ABCDE", "ABCDF"
    print(f'{"Pass" if not s.compare_equal(s1, s2) else "Fail"} | {s1}, {s2}\n')

    # test different on first
    s1, s2 = "ABCDE", "FBCDE"
    print(f'{"Pass" if not s.compare_equal(s1, s2) else "Fail"} | {s1}, {s2}\n')

    # test different off by 1 (0 tolerance)
    s1, s2 = "ABCDE", "ABCDEF"
    print(f'{"Pass" if not s.compare_equal(s1, s2) else "Fail"} | {s1}, {s2}\n')

    # test different types
    s1, s2 = "12345", 12345
    print(f'{"Pass" if s.compare_equal(s1, s2) else "Fail"} | {s1}, {s2}\n')

    # test different types
    s1, s2 = "abcdef", ('a', 'b', 'c', 'd', 'e', 'f')
    print(f'{"Pass" if s.compare_equal(s1, s2) else "Fail"} | {s1}, {s2}\n')

    # test different types
    s1, s2 = "1abcdef1", ('a', 'b', 'c', 'd', 'e', 'f')
    print(f'{"Pass" if s.compare_similar(s1, s2, 2) else "Fail"} | {s1}, {s2}\n')

    # test equal off by 1 last (1 tolerance)
    s1, s2 = "abcdef", "ABCDEF"
    print(f'{"Pass" if s.compare_similar(s1, s2) else "Fail"} | {s1}, {s2}\n')

    # test equal off by 1 last (1 tolerance)
    s1, s2 = "abcdef", "ABCDEF"
    print(f'{"Pass" if s.compare_similar(s1, s2) else "Fail"} | {s1}, {s2}\n')

    # test equal off by 1 first leter (1 tolerance)
    s1, s2 = "abcdef", "FABCDEF"
    print(f'{"Pass" if s.compare_similar(s1, s2, 1) else "Fail"} | {s1}, {s2}\n')

    # test equal off by 1 first leter (1 tolerance)
    s1, s2 = "casa", "caça"
    print(f'{"Pass" if s.compare_similar(s1, s2, 1) else "Fail"} | {s1}, {s2}\n')

    s1, s2 = "aaa", "a"
    print(f'{"Pass" if s.compare_similar(s1, s2, 2) else "Fail"} | {s1}, {s2}\n')

    s1, s2 = "aaa", "a"
    print(f'{"Pass" if not s.compare_similar(s1, s2, 1) else "Fail"} | {s1}, {s2}\n')

    print("done!")


if __name__ == "__main__":
    test_methods()
    # print(word_list[10])
    print("Finding similar words to abductor...")
    start = datetime.datetime.now()
    print(s.find_similar("craize"))
    end = datetime.datetime.now()
    print(f'it took {end-start} milliseconds')

    # start = datetime.datetime.now()
    # print(s.find_similar("Bode", True))
    # end = datetime.datetime.now()
    # print(f'it took {end-start} milliseconds')

