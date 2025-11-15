def get_num_words(text):
   num_words = len(text.split())
   print(f"Found {num_words} total words")
   return num_words

def get_character_count(text):
    character_count = {}
    for char in text.lower():
        character_count[char] = character_count.get(char, 0) + 1
    return character_count


def dict_sort(character_count):
    alpha_list = []
    for char, count in character_count.items():
        if char.isalpha():
            alpha_list.append({"char":char, "num": count})
    sorted_alphas = sorted(alpha_list, key=lambda item: item["num"], reverse=True)
    return sorted_alphas