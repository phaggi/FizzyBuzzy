def fb(i, number):
    return str(fbdict[i % number][number])

def fbcalc(size, numbers):
    a, b = numbers
    for i in range(size):
        print(''.join(set([fb(i, a)
        , fb(i, b)])) or i)


if __name__ == '__main__':
    numbers = (3, 13)
    fbsize = 1000
    nonfb = {numbers[0]: '', numbers[1]: ''}
    fbdict = [{numbers[0]: 'fizz', numbers[1]: 'buzz'}]
    for j in range(max(numbers)):
        fbdict.append(nonfb)
    fbcalc(fbsize, numbers)
