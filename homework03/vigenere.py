def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ""
    firstLowerLetterCode = ord('a')
    firstUpperLetterCode = ord('A')
    alphLen = 26

    n = len(plaintext)
    textCodes = [ord(plaintext[i]) for i in range(n)]

    m = len(keyword)
    keyCodes = [ord(keyword[i]) for i in range(m)]
    for i in range(m):
        if keyword[i].isupper():
            keyCodes[i] -= firstUpperLetterCode
        else:
            keyCodes[i] -= firstLowerLetterCode

    for i in range(n):
        if plaintext[i].isalpha():
            if plaintext[i].isupper():
                textCodes[i] = (textCodes[i] - firstUpperLetterCode + keyCodes[i % m]) % alphLen + firstUpperLetterCode
            else:
                textCodes[i] = (textCodes[i] - firstLowerLetterCode + keyCodes[i % m]) % alphLen + firstLowerLetterCode

    for i in range(n):
        ciphertext += chr(textCodes[i])
    return ciphertext

def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    plaintext = ""
    firstLowerLetterCode = ord('a')
    firstUpperLetterCode = ord('A')
    alphLen = 26

    n = len(ciphertext)
    textCodes = [ord(ciphertext[i]) for i in range(n)]

    m = len(keyword)
    keyCodes = [ord(keyword[i]) for i in range(m)]
    for i in range(m):
        if keyword[i].isupper():
            keyCodes[i] -= firstUpperLetterCode
        else:
            keyCodes[i] -= firstLowerLetterCode

    for i in range(n):
        if ciphertext[i].isalpha():
            if ciphertext[i].isupper():
                textCodes[i] = (textCodes[i] - firstUpperLetterCode - keyCodes[i % m] + alphLen) % alphLen + firstUpperLetterCode
            else:
                textCodes[i] = (textCodes[i] - firstLowerLetterCode - keyCodes[i % m] + alphLen) % alphLen + firstLowerLetterCode

    for i in range(n):
        plaintext += chr(textCodes[i])

    return plaintext

if __name__ == "__main__":
    print(decrypt_vigenere("PYTHON", "A"))
    print(decrypt_vigenere("python", "A"))
    print(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"))
    print(encrypt_vigenere("PYTHON", "A"))
    print(encrypt_vigenere("python", "a"))
    print(encrypt_vigenere("ATTACKATDAWN", "LEMON"))