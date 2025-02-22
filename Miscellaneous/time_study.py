# Output random time to study speaking time skill

from random import randint


def main():
    while True:
        s = input(f'{randint(0, 11):2}:{randint(0, 11) * 5:02}')
        if s != '':
            break


if __name__ == '__main__':
    main()
