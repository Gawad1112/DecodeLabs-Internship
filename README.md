# DecodeLabs Cyber Security Internship Tasks

This repository contains my completed tasks for the DecodeLabs Cyber Security Internship.

## Intern Information

**Name:** Mohamed Abdelgawad Omar  
**Track:** Cyber Security  
**Internship:** DecodeLabs Industrial Training  
**Batch:** 2026  

---

# Task 1: Password Strength Checker

## Overview

Task 1 is a Python GUI application that checks the strength of a password entered by the user.

The application analyzes the password based on length, character variety, common weak passwords, repeated characters, sequential patterns, and entropy.

It gives the user a strength rating and useful feedback to improve password security.

---

## Features

- Simple graphical user interface using Tkinter
- Password input field
- Show/hide password option
- Real-time password strength checking
- Strength meter progress bar
- Strength levels:
  - Very Weak
  - Weak
  - Moderate
  - Strong
  - Very Strong
- Feedback section with improvement tips
- Checks for:
  - Password length
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
  - Common weak passwords
  - Sequential patterns such as `123` or `abc`
  - Repeated characters such as `aaa` or `111`
  - Entropy/unpredictability score

---

## Tools and Technologies Used

- Python
- Tkinter
- Regular Expressions
- Math module

---

## How Task 1 Works

1. The user enters a password.
2. The program checks the password automatically.
3. A score from 0 to 100 is calculated.
4. The GUI displays the strength level.
5. The feedback box shows what is good and what needs improvement.

---

## How to Run Task 1

Make sure Python is installed on your device.

Run the following command:

```bash
python password_strength_checker.py
```

If your file has a different name, use:

```bash
python your_file_name.py
```

---

## Example

### Input

```text
Password123!
```

### Output

```text
Password Strength: Strong
Feedback:
- Contains uppercase letters
- Contains lowercase letters
- Contains numbers
- Contains special characters
- Good password length
```

---

# Task 2: Basic Encryption and Decryption

## Overview

Task 2 is a Python program that performs basic encryption and decryption using the Caesar Cipher technique.

The goal of this task is to understand the basic concept of data confidentiality by converting normal readable text into encrypted text, then reversing the process to get the original message again.

---

## Encryption Technique Used

The project uses the **Caesar Cipher**.

Caesar Cipher is a simple encryption method where each letter in the text is shifted by a fixed number of positions in the alphabet.

For example, with a shift key of 3:

```text
A → D
B → E
C → F
```

So the word:

```text
HELLO
```

becomes:

```text
KHOOR
```

---

## Features

- Takes text input from the user
- Takes shift key input from the user
- Encrypts the original text
- Decrypts the encrypted text
- Displays:
  - Original text
  - Encrypted text
  - Decrypted text
- Handles uppercase letters
- Handles lowercase letters
- Keeps spaces unchanged
- Keeps numbers unchanged
- Keeps symbols and punctuation unchanged
- Validates that decryption returns the original message

---

## Tools and Technologies Used

- Python
- Caesar Cipher logic
- Conditional statements
- Loops
- String manipulation

---

## How Task 2 Works

1. The user enters a message.
2. The user enters a shift key.
3. The program shifts each alphabetic character based on the key.
4. The encrypted text is displayed.
5. The program decrypts the encrypted text using the reverse shift.
6. The decrypted text is displayed to prove that the original message can be recovered.

---

## How to Run Task 2

Make sure Python is installed on your device.

Run the following command:

```bash
python task2_caesar_cipher_project.py
```

---

## Example

### Input

```text
Enter text: Hello World
Enter shift key: 3
```

### Output

```text
Original Text: Hello World
Encrypted Text: Khoor Zruog
Decrypted Text: Hello World
Validation: Decryption successful
```

---

# Project Learning Outcomes

By completing these tasks, I practiced important cybersecurity and programming concepts, including:

- Password security basics
- How weak passwords can be detected
- Password complexity analysis
- Data confidentiality
- Basic encryption and decryption
- Caesar Cipher logic
- Reversible encryption techniques
- Python GUI development
- Logic building and problem solving

---

# Cybersecurity Importance

## Why Password Strength Checking Matters

Weak passwords are one of the most common causes of account compromise.

A password strength checker helps users create stronger passwords by warning them about weak patterns, short length, and missing character types.

## Why Encryption and Decryption Matter

Encryption protects sensitive data by converting it into unreadable text.

Decryption allows authorized users to convert the encrypted text back into its original form.

These two tasks help build the foundation for understanding real-world cybersecurity concepts such as authentication, confidentiality, and secure communication.

---

# Repository Structure

```text
DecodeLabs-CyberSecurity-Tasks/
│
├── password_strength_checker.py
├── task2_caesar_cipher_project.py
└── README.md
```

---

# Conclusion

This repository contains two completed cybersecurity internship tasks.

Task 1 focuses on password strength checking and secure password practices.

Task 2 focuses on basic encryption and decryption using Caesar Cipher.

Both tasks helped me improve my Python programming skills and understand important cybersecurity concepts in a practical way.
