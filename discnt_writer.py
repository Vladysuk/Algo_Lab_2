import random

if __name__ == '__main__':
    file = open('discnt.in', 'w', newline="")
    for i in range(random.randint(1, 1000)):
        file.write('%d ' % random.randint(0, 10 ** 9))
    file.write('\n%d' % random.randint(0, 100))
    file.close()
