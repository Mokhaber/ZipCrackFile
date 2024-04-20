import zipfile

zip_file = "A.zip"  # Replace "example.zip" with the name of your zip file
password_file = "C://Users/test/Desktop/New folder/important-list.txt"

with open(password_file, 'r', encoding='utf-8') as file:
    password_list = [line.strip() for line in file]

for password in password_list:
    try:
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(pwd=bytes(password, 'utf-8'))
        print("Success! Password is:", password)
        break
    except Exception as e:
        print("Tried", password, "but failed.")
