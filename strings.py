def compare_equal(str1, str2, case_sensitive=True):
    result = True
    counter = 0
    try:
        # print(f'{str1}, {str2} | {len(str1) - len(str2)}')
        if not len(str1) - len(str2) == 0:
            result = False
        else:
            if not case_sensitive:
                str1 = str1.upper()
                str2 = str2.upper()
            while True:
                try:
                    if not str1[counter] == str2[counter]:
                        result = False
                        break
                except IndexError:
                    break
                else:
                    counter += 1
    except TypeError:
        # print(f'type error found, retrying | {str(str1)}, {str(str2)}')
        result = compare_equal(str(str1), str(str2), case_sensitive)

    return result


def compare_similar(str1, str2, off_by_tolerance=0):
    result = True
    str1 = str1.upper()
    str2 = str2.upper()
    if off_by_tolerance == 0:
        result = compare_equal(str1, str2)
    else:
        len_str1 = len(str1)
        len_str2 = len(str2)
        is_off_by = abs(len_str1 - len_str2)
        counter_1 = 0
        counter_2 = 0
        # if not len_str1 + off_by == len_str2 or  not len_str1 + off_by == len_str2
        if is_off_by > off_by_tolerance:
            result = False
        else:
            result = True
            found_off_by = 0
            while True:
                try:
                    # case letters at counter are equal
                    if not str1[counter_1] == str2[counter_2] and off_by_tolerance > found_off_by:
                        result = False
                        break
                    else:
                        found_off_by += 1
                    # case letters at next counter are equal

                    # case letter at counter 1 is equal next counter 2

                    # case letter at counter 2 is equal next counter 1
                except IndexError:
                    break
                else:
                    counter_1 += 1

    return result, counter_1


if __name__ == "__main__":
    s1 = "ABCDE"

    # test equals
    s2 = "ABCDE"
    print(f'{"Pass" if compare_equal(s1, s2) else "Fail"} | {s1}, {s2}')

    # test different case sensitive
    s2 = "aBCDe"
    print(f'{"Pass" if not compare_equal(s1, s2) else "Fail"} | {s1}, {s2}')

    # test equal case insensitive
    s2 = "aBCDe"
    print(f'{"Pass" if compare_equal(s1, s2, False) else "Fail"} | {s1}, {s2}')

    # test different on last
    s2 = "ABCDF"
    print(f'{"Pass" if not compare_equal(s1, s2) else "Fail"} | {s1}, {s2}')

    # test different on first
    s2 = "FBCDE"
    print(f'{"Pass" if not compare_equal(s1, s2) else "Fail"} | {s1}, {s2}')

    # test different off by 1 (0 tolerance)
    s2 = "ABCDEF"
    print(f'{"Pass" if not compare_equal(s1, s2) else "Fail"} | {s1}, {s2}')

    s1 = "12345"
    # test different types
    s2 = 12345
    print(f'{"Pass" if compare_equal(s1, s2) else "Fail"} | {s1}, {s2}')

    s1 = "abcdef"
    # test different types
    s2 = ('a', 'b', 'c', 'd', 'e', 'f')
    print(f'{"Pass" if compare_equal(s1, s2) else "Fail"} | {s1}, {s2}')

    # test equal off by 1 last (1 tolerance)
    s2 = "ABCDEF"
    print(f'{"Pass" if compare_similar(s1, s2) else "Fail"} | {s1}, {s2}')

    # test equal off by 1 first leter (1 tolerance)
    s2 = "FABCDE"
    print(f'{"Pass" if compare_similar(s1, s2) else "Fail"} | {s1}, {s2}')

