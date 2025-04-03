age = input("Type your age: ")

def categorize_by_age(age):
    if 0 <= age <= 9:
        return "Child"
    elif 9 < age <= 18:
        return "Adolescent"
    elif 18 < age <= 65:
        return "Adult"
    elif 65 < age <= 150:
        return "Elderly"
    else:
        return f"Invalid age: {age}"
    
print(categorize_by_age(int(age)))