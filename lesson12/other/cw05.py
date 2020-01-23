"""
Реализуйте вызовы функции greeting
с помощью оператора запаковки * и **.
"""

def greeting(msg, name=None, lang="en"):
    if not name:
        return msg
    elif lang == "ru":
        return f"{msg} {name}!"
    elif lang == "en":
        return f"{msg} {name}!"
    else:
        return f"Unknown language"

print(greeting(msg="Hello" ,name="me", lang="uk"))
greating_agrs1 = ("Привет", "вам", "ru")
print(*greating_agrs1)
print(greeting(**dict(msg="Привет", name="me", lang="en")))
print(greeting(**{"msg":"Hello everybody!"}))