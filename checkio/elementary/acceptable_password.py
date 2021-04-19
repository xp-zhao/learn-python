def is_acceptable_password(password: str) -> bool:
    # your code here
    return len(password) > 6


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') is False
    assert is_acceptable_password('muchlonger') is True
    assert is_acceptable_password('ashort') is False
