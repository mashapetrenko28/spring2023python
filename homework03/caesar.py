import typing as tp
def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    ciphertext = ""
    firstLowerLetterCode = ord('a')
    firstUpperLetterCode = ord('A')
    alphLen = 26
    n = len(plaintext)
    codes = [ord(plaintext[i]) for i in range(n)]
    for i in range(n):
        if plaintext[i].isalpha():
            if plaintext[i].isupper():
                codes[i] = (codes[i] - firstUpperLetterCode + shift) % alphLen + firstUpperLetterCode
            else:
                codes[i] = (codes[i] - firstLowerLetterCode + shift) % alphLen + firstLowerLetterCode
    for i in range(n):
        ciphertext += chr(codes[i])

    # for i in range(n):
    #     if plaintext[i].isupper():
    #         ciphertext += (plaintext[i] - firstUpperLetterCode + shift) + firstUpperLetterCode
    #     else:
    #         ciphertext += (plaintext[i] - firstLowerLetterCode + shift) % alphLen + firstLowerLetterCode

    return ciphertext

def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    plaintext = ""
    firstLowerLetterCode = ord('a')
    firstUpperLetterCode = ord('A')
    alphLen = 26
    n = len(ciphertext)
    codes = [ord(ciphertext[i]) for i in range(n)]
    for i in range(n):
        if ciphertext[i].isalpha():
            if ciphertext[i].isupper():
                codes[i] = (codes[i] - firstUpperLetterCode - shift + alphLen) % alphLen + firstUpperLetterCode
            else:
                codes[i] = (codes[i] - firstLowerLetterCode - shift + alphLen) % alphLen + firstLowerLetterCode
    for i in range(n):
        plaintext += chr(codes[i])
    return plaintext

def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift