def fb(i, number, fbdict):
    return str(fbdict[i % number][number])


def fbcalc(size, numbers, fbdict):
    a, b = numbers
    for i in range(size):
        print(''.join({fb(i, a, fbdict), fb(i, b, fbdict)}) or i)


if __name__ == '__main__':
    numbers = (3, 13)
    fbsize = 1000000
    nonfb = {numbers[0]: '', numbers[1]: ''}
    fbdict = [{numbers[0]: 'fizz', numbers[1]: 'buzz'}]
    for j in range(max(numbers)):
        fbdict.append(nonfb)
    fbcalc(fbsize, numbers, fbdict)
