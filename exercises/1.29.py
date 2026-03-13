# import itertools


# def possibleCharacters(characters):
#         # Generate all permutations of the list of characters
#         permutations = itertools.permutations(characters)
        
#         # Convert each permutation from tuple to string and print it
#         for perm in permutations:
#                 print(''.join(perm))

characters = ['c', 'a', 't', 'd', 'o', 'g']

# result = possibleCharacters(characters)
# print(result)


def generate_permutations(s, chosen=""):
    if len(s) == 0:
        print(chosen)
    else:
        for i in range(len(s)):
            # Choose the character at index i
            char = s[i]
            # Explore with the chosen character removed from the string
            remaining = s[:i] + s[i+1:]
            generate_permutations(remaining, chosen + char)


# Initial characters to permute
characters = "catdog"

# Generate and print all permutations
generate_permutations(characters)
