from stats import word_counter, character_counter, dict_sort
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def print_report(input: dict, path):
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {path}...')
    print('----------- Word Count ----------')
    word_counter(get_book_text(path))
    print('--------- Character Count -------')
    for key, value in input.items():
        if key.isalpha():
            print(f'{key}: {value}')
    print('============= END ===============')



if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    else:
        script, first = sys.argv
        z = get_book_text(first)
        x = character_counter(z)
        y = dict_sort(x)
        print_report(y, first)

