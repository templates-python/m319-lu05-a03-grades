def main():
    points = int(input('Give points [0-100]:\n'))
    if points < 0:
        print('impossible!')
    elif points <= 49:
        print(f'Grade: 1')
    elif points <= 59:
        print(f'Grade: 2')
    elif points <= 69:
        print(f'Grade: 3')
    elif points <= 79:
        print(f'Grade: 4')
    elif points <= 89:
        print(f'Grade: 5')
    elif points <= 100:
        print(f'Grade: 6')
    elif points > 100:
        print('incredible!')


if __name__ == '__main__':
    main()
