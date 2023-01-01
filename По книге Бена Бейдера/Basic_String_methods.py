# start or end line

one_word = "Enterprise"
second_word = "     Production    "

print(one_word.endswith("se"))  # True
print(one_word.startswith("ent"))  # False (start with 'Ent')
print(one_word.find("r"))  # 4 (first search) if you don't search then return -1
print(one_word.find("ri"))  # 6
print(one_word.rfind("e"))  # 9 start search in right
print(one_word.replace("e", "a"))  # Entarprisa
print(one_word.replace("prise", " name"))  # Enterprise => Enter name
print(one_word * 2)  # EnterpriseEnterprise
print(len(one_word))  # 10
print(f"{one_word}-{second_word.strip().lower()}")  # Enterprise-production


# Mini task for replace words
some_text = input("Enter some text: ")  # Mike
change_dict = {"M": "1", "i": "2", "k": "3", "e": "4"}
for i in range(len(some_text)):
    if some_text[i] in change_dict.keys():
        some_text = some_text.replace(f"{some_text[i]}", f"{change_dict[some_text[i]]}")
print(some_text)  # 1234
