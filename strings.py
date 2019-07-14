from commons import word_list


def compare_equal(str1, str2, case_sensitive=True):
    result = True
    counter = 0
    try:
        # print(f'compare_equal {str1}, {str2} | {len(str1) - len(str2)} | {case_sensitive}')
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
                except IndexError as err:
                    # Found equal by index error meaning that they are the same until the last letter.
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
    # print(f'{str1}, {str2}')
    str1 = str1.lower()
    str2 = str2.lower()
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
                    # print(f'if equal {str1[counter]} {str2[counter]}')
                    counter += 1
                else:  # case next letter at next counter of one of them are equal
                    for i in range(1, off_by_tolerance+1):
                        off_count += 1
                        # print(f'{str1[counter]} {str2[counter]} i:{i} off_count:{off_count}')
                        if str1[counter + i] == str2[counter + i]:
                            return compare_similar(str1[counter + i:], str2[counter + i:], off_by_tolerance - i)
                        else:
                            try:
                                if str1[counter] == str2[counter + i]:
                                    return compare_similar(str1[counter:], str2[counter + i:], off_by_tolerance - i)
                            except IndexError:
                                return compare_similar(str1[counter+i:], str2[counter:], off_by_tolerance - i)
                            try:
                                if str1[counter + i] == str2[counter]:
                                    return compare_similar(str1[counter + i:], str2[counter:], off_by_tolerance - i)
                            except IndexError:
                                return compare_similar(str1[counter:], str2[counter+i:], off_by_tolerance - i)
            except IndexError:
                # print(f'resolved by index error: {len(str1)} {len(str2)} {off_by_tolerance}, {off_count}')
                # have to add the off_count index so that it does not go over
                # print("index error: ", str1, str2, off_count, counter)
                if abs(len(str1)-len(str2)) + off_count <= off_by_tolerance:
                    return True
                elif len(str1)-len(str2) > 0:

                    if str1[counter + 1] == str2[counter]:
                        return abs(len(str1) - len(str2)) <= off_by_tolerance
                elif len(str2)-len(str1) > 0:
                    if str1[counter] == str2[counter + 1]:
                        return abs(len(str1) - len(str2)) <= off_by_tolerance
                # catch all
                return abs(len(str1) - len(str2)) + off_count + 1 <= off_by_tolerance

        if len(str1) > len(str2):
            # print(f'len str1 > len str2 - {str1}, {str2}')
            return compare_similar(str1[counter+1:], str2[counter:], off_by_tolerance - 1)
        else:
            # print(f'len str1 < len str2 - {str1}, {str2}')
            return compare_similar(str1[counter:], str2[counter + 1:], off_by_tolerance - 1)


def find_similar(str1, strict_equal=False):
    counter = 0
    found_equal = False
    similar_by_1 = []
    for word in word_list:
        counter += 1
        # print(f'comparing {str1} and {word_list[counter]}')
        if compare_similar(str1, word, 1):
            similar_by_1.append(word)
            if compare_equal(str1, word, strict_equal):
                found_equal = True
    print(f'Done! Total number of words searched: {counter}')
    return found_equal, similar_by_1
