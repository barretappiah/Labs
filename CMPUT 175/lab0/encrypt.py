ENCRYPTION_SOURCE = r"7elL2GJVkrv0dQ%Eb?N6uw*#t!@hYAop&O^a3FWCyKUT4PR5zBjDH8XgZnf9qMm1cSIsi$x "



def secure_pass(user_password):
    valid_chars = ENCRYPTION_SOURCE
    special_chars = "!@#$%^&*?"
    issues = []
 
    # Ensure conditions

    if not len(user_password) > 7:
        issues.append('Password should be at least 8 characters')
    if ' ' in user_password:
        issues.append('Password cannot have spaces')
    if not any(c.isupper() for c in user_password):
        issues.append('Missing an uppercase letter in the password')
    if not any(c.islower() for c in user_password):
        issues.append('Missing a lowercase letter in the password')
    if not any(c in special_chars for c in user_password):
        issues.append('Missing a special character in the password')
    if not any(c.isdigit() for c in user_password):
        issues.append('Missing a digit in the password')
    if any(c not in valid_chars for c in user_password):
        invalid_chars = []

        for c in user_password:
            if c not in valid_chars and c not in invalid_chars:
                invalid_chars.append(c)
        issues.append(f'{", ".join(invalid_chars)} are not allowed in the password')

    # If condititions not met, display faults to user

    if len(issues) > 0:
        INDENT = ' ' * 8
        print('\nIssues: ')

        for fault in issues:
            print(INDENT + fault)
        print('\nPlease enter a strong valid password')

        return True
    return False


def main():
    repeat = True
    encryption_key = input('Enter the Encryption key: ')
    
    while repeat:
        user_website = input('\nEnter website: ').lower().rstrip()
        
        repeat_password = True
        while repeat_password:
            user_password = input('Enter password: ')
            repeat_password = secure_pass(user_password)


main()