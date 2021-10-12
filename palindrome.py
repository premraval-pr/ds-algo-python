
def is_palindrome(match_string):
    if len(match_string) == 0:
        return False
    match_string = match_string.lower()
    reversed_string = match_string[::-1]
    return match_string == reversed_string


def find_longest_palindrome(input_string):
    solution_word = ""
    solution_index = -1
    if len(input_string) == 0:
        print("The String can not be emtpy.")
        return

    for i in range(len(input_string)):
        for j in range(i, len(input_string)):
            check_string = input_string[i:j+1]

            if is_palindrome(check_string):
                if len(check_string) > len(solution_word):
                    solution_word = check_string
                    solution_index = i

    return [solution_word, solution_index, len(solution_word)]


print(find_longest_palindrome("Stackcatssothatyousteponnopets"))

print(find_longest_palindrome(""))

print(find_longest_palindrome("AnnaandAnna"))

print(find_longest_palindrome("A"))

print(find_longest_palindrome("Annaand*;Anna"))

print(find_longest_palindrome("Stack cats"))
