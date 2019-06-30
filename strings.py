from commons import word_list


def compare_equal(str1, str2, case_sensitive=True):
    result = True
    counter = 0
    try:
        #print(f'compare_equal {str1}, {str2} | {len(str1) - len(str2)} | {case_sensitive}')
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
    counter = 0
    off_count = 0
    len_str1 = len(str1)
    len_str2 = len(str2)
    if off_by_tolerance == 0:
        return compare_equal(str1, str2, False)
    elif abs(len_str1 - len_str2) > off_by_tolerance:
        return False
    else:
        while off_count <= off_by_tolerance:
            try:
                # case letters at counter are equal - keep going
                if str1[counter] == str2[counter]:
                    counter += 1
                else:  # case next letter at next counter of one of them are equal
                    for i in range(0, off_by_tolerance+1):
                        if str1[counter] == str2[counter + i]:
                            # print("if")
                            return compare_similar(str1[counter:], str2[counter+i:], off_by_tolerance - i)
                        elif str1[counter + i] == str2[counter]:
                            # print("elif 1")
                            return compare_similar(str1[counter + i:], str2[counter:], off_by_tolerance - i)
                        elif str1[counter + i] == str2[counter + i]:
                            # print("elif 2")
                            return compare_similar(str1[counter + i:], str2[counter + i:], off_by_tolerance - i)
                    off_count += 1
            except IndexError:
                # print("resolved by index error")
                return abs(len(str1) - len(str2)) <= off_by_tolerance

        if len(str1) >= len(str2):
            return compare_similar(str1[counter+1:], str2[counter:], off_by_tolerance - 1)
        else:
            return compare_similar(str1[counter:], str2[counter + 1:], off_by_tolerance - 1)


def find_similar(str, strict_equal=False):
    counter = 0
    found_equal = False
    similar_by_1 = []
    while True:
        try:
            # print(f'comparing {str1} and {word_list[counter]}')
            if compare_similar(str, word_list[counter], 1):
                similar_by_1.append(word_list[counter])
            counter += 1
        except IndexError as err:
            print('Done searching!')
            break

    return found_equal, similar_by_1
