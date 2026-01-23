issues=[]
invalid_chars = ['b','a','d','f']

issues.append(f'{", ".join(invalid_chars)} are not allowed in the password')

print(issues)