
def word_counter(input):
    word_list = input.split()
    print(f'Found {len(word_list)} total words')


def character_counter(input):
    new_dict = dict()
    new_set = set(input.lower())
    for i in new_set:
        word_count =  input.lower().count(i)
        new_dict.update({f'{i}': word_count})
    return new_dict



def dict_sort(input: dict):
    sorted_x = dict(sorted(input.items()\
                      , key=lambda kv: kv[1]\
                      , reverse=True
                    ))
    return sorted_x
