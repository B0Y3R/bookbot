def get_word_count(words):
    return len(words.split())

def get_letter_count(words):
    letter_count_dict = {}

    for word in words:
        for letter in word:
            new_letter = letter.lower()
            if new_letter in letter_count_dict:
                letter_count_dict[new_letter] += 1
            else:
                letter_count_dict[new_letter] = 1

    return letter_count_dict

def sort_on(dict):
    return dict['count']

def sort_letter_dicts(letter_dict):
    new_list = []
    for i in letter_dict:
        new_dict = {}
        new_dict['letter'] = i
        new_dict['count'] = letter_dict[i]

        new_list.append(new_dict)

    return sorted(new_list,reverse=True, key=sort_on)
       
    

