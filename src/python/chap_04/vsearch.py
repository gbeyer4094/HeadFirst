def search4vowels():
    """Display the list of vowels found in an asked-for word/phrase"""
    vowels = set('aeiou')
    word = input("Provide a word to search for vowels:")
    found = vowels.intersection(set(word))

    print(sorted(found))
    return bool(found)


def search4vowelswithword(word):
    """Display the list of vowels found in a given word/phrase """
    vowels = set('aeiou')
    found = vowels.intersection(set(word))

    print(sorted(found))
    return bool(found)


def search4vowelsreturnset(word:str) -> set:
    """Return a set of vowels found in an asked-for word/phrase"""
    vowels = set('aeiou')
    word = input("Provide a word to search for vowels:")
    return vowels.intersection(set(word))

