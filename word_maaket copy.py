import itertools
import progressbar

def generate_combinations(letters, length):
    return itertools.product(letters, repeat=length)

def save_combinations_to_file(combinations, filepath):
    # Create two independent iterators
    combinations, count_iterator = itertools.tee(combinations, 2)

    # Count the total combinations
    total_combinations = sum(1 for _ in count_iterator)

    bar = progressbar.ProgressBar(maxval=total_combinations)
    bar.start()

    with open(filepath, 'w') as file:
        try:
            for i, combination in enumerate(combinations):
                file.write(''.join(combination) + '\n')
                bar.update(i)
        finally:
            bar.finish()

letters = 'abcdefghijklmnopqrstuvwxyz'
length = 4
filepath = 'C:/Users/joche/OneDrive/Bureaublad/python/combinations.txt'

combinations = generate_combinations(letters, length)
save_combinations_to_file(combinations, filepath)
