"""
Project 2: Basic Encryption & Decryption
Cyber Security Industrial Training Kit - DecodeLabs

Technique: Caesar Cipher
Goal: Encrypt user text, decrypt the encrypted text, and display both outputs.
"""


def encrypt_text(plain_text: str, shift: int) -> str:
    """Encrypt text using Caesar Cipher logic."""
    encrypted_text = ""

    for char in plain_text:
        if char.isupper():
            # Convert A-Z to 0-25, apply shift, wrap with % 26, then convert back
            encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            # Convert a-z to 0-25, apply shift, wrap with % 26, then convert back
            encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            # Keep spaces, numbers, and punctuation unchanged
            encrypted_text += char

    return encrypted_text


def decrypt_text(cipher_text: str, shift: int) -> str:
    """Decrypt text by reversing the Caesar Cipher shift."""
    return encrypt_text(cipher_text, -shift)


def get_shift_value() -> int:
    """Ask the user for a valid integer shift key."""
    while True:
        try:
            shift = int(input("Enter shift key (example: 3): "))
            return shift
        except ValueError:
            print("Invalid input. Please enter a number only.")


def main() -> None:
    print("=" * 50)
    print("Project 2: Basic Encryption & Decryption")
    print("Technique: Caesar Cipher")
    print("=" * 50)

    plain_text = input("Enter text to encrypt: ")
    shift = get_shift_value()

    encrypted = encrypt_text(plain_text, shift)
    decrypted = decrypt_text(encrypted, shift)

    print("\n--- Results ---")
    print(f"Original Text : {plain_text}")
    print(f"Shift Key     : {shift}")
    print(f"Encrypted Text: {encrypted}")
    print(f"Decrypted Text: {decrypted}")

    if decrypted == plain_text:
        print("\nValidation: Successful. Decryption returned the original text.")
    else:
        print("\nValidation: Failed. Decryption did not match the original text.")


if __name__ == "__main__":
    main()
