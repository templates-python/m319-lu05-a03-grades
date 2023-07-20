def main():
    points = int(input('Give points [0-100]:\n'))
    if points < 0:
        print('impossible!')
    elif points <= 49:
        print('failed')
    elif points <= 59:
        print(1)
    elif points <= 69:
        print(2)
    elif points <= 79:
        print(2)
    elif points <= 89:
        print(4)
    elif points <= 100:
        print(5)
    elif points > 100:
        print('incredible!')


if __name__ == '__main__':
    main()
