import re
from collections import Counter
import sys
import unicodedata

def normalize_symbol(char):
    # Normalize the character to its canonical form
    normalized_char = unicodedata.normalize('NFKC', char)
    return normalized_char

def main():
    pattern = re.compile('[A-Za-zÁÉÍÓÚáéíóú ]+')
    punctuation = re.compile('[!.,;:?]+')
    non_alpha_freq = Counter()

    for line in sys.stdin:
        if pattern.search(line) and punctuation.search(line.rstrip()):
            # Output lines with both upper and lower case alphabetic characters to stdout
            sys.stdout.write(line)

            # Update non-alphabetic character frequency list
            non_alpha_chars = re.findall(r'[^A-Za-zÁÉÍÓÚáéíóú]', line)
            non_alpha_freq.update(non_alpha_chars)
            
            for char in non_alpha_chars:
                # Categorize the character
                category = unicodedata.category(char)
        
                # Normalize the character if it is a spacing symbol or formatting symbol
                if category.startswith('Zs') or category.startswith('Cf'):
                    normalized_char = normalize_symbol(char)

    for char, freq in non_alpha_freq.items():
        sys.stderr.write(f"{char}\t{freq}\n")

if __name__ == "__main__":
    main()
