def search4vowels_old():
    """Display the list of vowels found in an asked-for phrase"""
    vowels = set('aeiou')
    phrase = input("Provide a phrase to search for vowels:")
    found = vowels.intersection(set(phrase))

    print(sorted(found))
    return bool(found)


def search4vowels(phrase: str) -> set:
    """Return a set of vowels found in a given phrase"""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """Return a set of letters found in a given phrase"""
    return set(letters).intersection(set(phrase))
