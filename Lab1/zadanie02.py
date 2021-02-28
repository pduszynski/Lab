user = input("")
polish: str = "ąćęłńóśźż"
english: str = "acelnoszz"
translator = str.maketrans(polish, english)
print(user.translate(translator))
