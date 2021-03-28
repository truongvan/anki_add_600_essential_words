from .oxford_dictionary import get_word


def dictionary_search(word_detail:dict) -> dict:
    word = word_detail.get("Word")
    part_of_speech = word_detail.get("Parts_of_speech")
    return get_word(word, part_of_speech)