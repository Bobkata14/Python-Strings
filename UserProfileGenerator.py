#User Profile Generator
print("--User Profile--\n".center(25))

first_name = input("Enter your first name: ") #I decided to make more user friendly by doing it with input!
last_name = input("Enter your last name: ")
full_name = first_name + " " + last_name
country = "Bulgaria"
favorite_language = "Python"
nickname = full_name[:5]

print(f"Full name: {first_name} {last_name}")
print(f"Country: {country}")
print(f"Favorite language: {favorite_language}\n")

print(f"Name length: {len(full_name)}")
print(f"First letter: {full_name[0]}")
print(f"Last letter: {full_name[-1]}\n")

print(f"Uppercase name: {full_name.upper()}")
print(f"Lowercase name: {full_name.lower()}\n")
print(f"Title: {nickname}")

#Overall - 6.00