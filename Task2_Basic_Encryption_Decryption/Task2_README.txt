Project 2: Basic Encryption & Decryption
Cyber Security Internship - DecodeLabs

Objective:
Implement a simple encryption and decryption technique using the Caesar Cipher.

Implemented Requirements:
1. Encrypt user text using Caesar Cipher logic.
2. Decrypt the encrypted text using the reverse shift.
3. Display the original text, shift key, encrypted text, and decrypted text.
4. Handle uppercase letters, lowercase letters, spaces, numbers, and punctuation.
5. Validate that the decrypted output matches the original input.

How to Run:
1. Make sure Python is installed.
2. Open terminal or command prompt in the project folder.
3. Run:
   python task2_caesar_cipher_project.py

Example Test:
Input text: Hello Cyber Security 2026!
Shift key: 3
Encrypted output: Khoor Fbehu Vhfxulwb 2026!
Decrypted output: Hello Cyber Security 2026!

Explanation:
The Caesar Cipher shifts each alphabetic character by a fixed number called the shift key.
For encryption, the formula is:
E(x) = (x + n) % 26
For decryption, the reverse formula is:
D(x) = (x - n) % 26

Where:
x = character position in the alphabet
n = shift key
% 26 = wraps the result inside the 26 English letters

Spaces, numbers, and punctuation are not changed because they are edge cases that should remain readable and unchanged.
