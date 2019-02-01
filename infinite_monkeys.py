from random import randint


def generate_new_string(length, alphabet):
    """Generates a new string of length length"""
    new_str = ''

    alpha_length = len(alphabet)
    for x in range(length):
        new_str = new_str + alphabet[randint(0, alpha_length - 1)]
    return new_str


def score_strings(target, new_str):
    """Compares two strings and returns if they are equal"""

    num_matches = 0
    ret_str = ''
    for x in range(len(target)):
        if target[x] == new_str[x]:
            num_matches = num_matches + 1
            ret_str = ret_str + new_str[x].upper()
        else:
            ret_str = ret_str + new_str[x]
    return num_matches / len(target_string), ret_str


target_string = 'methinks it is like a weasel'
#target_string = 'hello'
target_length = len(target_string)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z', ' ']


def main():
    """Main function"""

    count = 0
    score = 0
    max_score = 0
    best_str = ''
    while score < 1:
        new_str = generate_new_string(target_length, alphabet)
        score, new_str = score_strings(target_string, new_str)

        count = count + 1
        if count % 10000 == 0:
            print(str(count) + ': ' + str(max_score * 100) + '% - ' + best_str)
        if score > max_score:
            max_score = score
            best_str = new_str

    print(str(count) + ': ' + new_str)
    print('END')


main()
