def word_count(text):
    word_list = text.split()
    return len(word_list)

def character_count(text):
    character_dict = {}
    for c in text:
        lower_c = c.lower()
        if lower_c in character_dict:
            character_dict[lower_c] += 1
        else:
            character_dict[lower_c] = 1
    return character_dict

def sort_on(dict):
    return dict["count"]

def sorted_characters(character_dict):
    character_count_list = []
    for key in character_dict:
        character_count_list.append({"char": key, "count": character_dict[key]})
    character_count_list.sort(reverse=True, key=sort_on)
    return character_count_list