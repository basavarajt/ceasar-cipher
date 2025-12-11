def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = -shift

    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(
        alphabet + alphabet.upper(),
        shifted_alphabet + shifted_alphabet.upper()
    )

    return text.translate(translation_table)


def encrypt(text, shift):
    return caesar(text, shift)


def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)



print("=== Caesar Cipher ===")

mode = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().lower()

text = input("Enter the text: ")

shift = int(input("Enter shift value (1–25): "))

if mode == 'e':
    result = encrypt(text, shift)
    print("\nEncrypted text:", result)

elif mode == 'd':
    result = decrypt(text, shift)
    print("\nDecrypted text:", result)

else:
    print("Invalid option! Choose E or D.")
