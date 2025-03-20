import random
import string

passwords = []
for _ in range(5):
    password = ''.join(random.choices(string.ascii_lowercase, k=15))
    passwords.append(password)

replacement_dict = {}

for _ in range(5):
    letter = input("Enter a lowercase character: ")
    replacements = set()
    while len(replacements) < 3:
        replacement = input(f"Enter a replacement for '{letter}': ")
        replacements.add(replacement)  
    replacement_dict[letter] = list(replacements)  

categorized_passwords = {"strong": [], "weak": []}
for password in passwords:
    replaced_password = []
    replacements_count = 0
    for char in password:
        if char in replacement_dict:
            new_char = random.choice(replacement_dict[char])  
            replaced_password.append(new_char)
            replacements_count += 1
        else:
            replaced_password.append(char)
    
    
    if replacements_count > 4:
        categorized_passwords["strong"].append(''.join(replaced_password))
    else:
        categorized_passwords["weak"].append(''.join(replaced_password))


print("\nGenerated Passwords:\n")

print("STRONG PASSWORDS:")
for strong_password in categorized_passwords["strong"]:
    print(strong_password)

print("\nWEAK PASSWORDS:")
for weak_password in categorized_passwords["weak"]:
    print(weak_password)
