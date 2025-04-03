def get_num_words(content):
        return len(content.split())


def count_characters(input_text):
        text = input_text.lower()
        character_count = {}
        for char in text:
                if char in character_count:
                        character_count[char] += 1
                else:
                        character_count[char] = 1
        return character_count

def sort_characters(big_dict):
        character_list = [{"character": char, "count": count} for char, count in big_dict.items()]
        character_list.sort(key=lambda x: x["count"], reverse=True)

        return character_list