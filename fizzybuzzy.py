def fb(i, number_, fb_dict_):
    return str(fb_dict_[i % number_][number_])


def fb_calc(size, _numbers, _fb_dict):
    a, b = _numbers
    for i in range(size):
        print(''.join({fb(i, a, _fb_dict), fb(i, b, _fb_dict)}) or i)


if __name__ == '__main__':
    numbers = (3, 13)
    fb_size = 1000000
    non_fb = {numbers[0]: '', numbers[1]: ''}
    fb_dict = [{numbers[0]: 'fizz', numbers[1]: 'buzz'}]
    for j in range(max(numbers)):
        fb_dict.append(non_fb)
    fb_calc(fb_size, numbers, fb_dict)
