import itertools
import progressbar

def generate_combinations(start_letter, letters, max_length):
    combinations = [''.join(comb) for comb in itertools.product(letters, repeat=max_length) if comb[0] == start_letter and len(comb) <= 20]
    return combinations

def save_combinations_to_file(combinations, filepath):
    total_combinations = len(combinations)
    bar = progressbar.ProgressBar(maxval=total_combinations)
    bar.start()
    with open(filepath, 'w') as file:
        try:
            for i, combination in enumerate(combinations):
                file.write(combination + ',')
                bar.update(i)
        finally:
            bar.finish()

start_letter = 'a'
letters = ' abcdefghijklmnopqrstuvwxyz'
max_length = 6
filepath = 'C:/Users/joche/OneDrive/Bureaublad/python/combinations.txt'

combinations = generate_combinations(start_letter, letters, max_length)
save_combinations_to_file(combinations, filepath)
