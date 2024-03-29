def is_all_upper(text: str) -> bool:
    # your code here
    return text == text.upper()


if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') is True
    assert is_all_upper('all lower') is False
    assert is_all_upper('mixed UPPER and lower') is False
    assert is_all_upper('') is True
    assert is_all_upper('     ') is True
    assert is_all_upper('444') is True
    assert is_all_upper('55 55 5') is True
