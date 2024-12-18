# initialisation
name = 'Paul'
name = str("Paul")

print(name)

# multiline string 
multiline = """
    <h1>Titre</h1>
    <h2>Sous-titre</h2>
"""

print(multiline)

# casting 
decade = 1980
decade = str(decade)

# concatenation
sentence = "J'aime la musique des années " + decade 
print(sentence)

# escaping 
sentence = 'J\'aime coder en : \n \t python \n \t javascript'
print(sentence)

# slicing 
website = "https://google.com"
protocol = website[0:4]
protocol = website[:4]
print(protocol)
url = website[8:]
print(url)
tld = website[-4:]
print(tld)
sld = website[8:-4]
print(sld)
crazy_url = website[0:18:2]
print(crazy_url)
reversed_url = website[::-1]
print(reversed_url)

# formatting
name1 = "Paul"
name2 = "Tom"

print("%s est l'ami de %s" % (name1, name2))
print("{} est l'ami de {}".format(name1, name2))
print("{1} est l'ami de {0}".format(name1, name2))
print("{name1} est l'ami de {name2}".format(name1=name2, name2=name1))
print(f"{name1} est l'ami de {name2}")

person = {"name": "Zoé", "age" : 28}
print(f"Son nom est {person["name"]}, et elle a {person["age"]}")
print(f"Son nom est {person["name"].upper()}, et elle a {2 * 10}")

pi = 3.1415927
bigNumber = 1000000000
print(f"Le nombre pi vaut {pi:.3f}")
print(f"Le nombre formaté correctement {bigNumber:,}")
print(f"Le nombre formaté correctement {bigNumber:,.2f}")
print(f"Le nombre en binaire {bigNumber:b}")
print(f"Le nombre en notation scientifique {bigNumber:E}")

for i in range(1, 11):
    sentence = "Valeur : {:03}".format(i)
    print(sentence)

for num in range(1,11):
    print(f"\n {num} divisé par 4.3 vaut {num / 4.3:.2%}")

from datetime import datetime 
import locale 

locale.setlocale(locale.LC_TIME, "fr_FR")

birthday = datetime(1988, 2, 12)
sentence = f"Mon anniversaire tombe le {birthday:%d %B %Y}"
sentence = f"Le {birthday:%d %B %Y} tombe le {birthday:%A} qui était le {birthday:%j} jour de l'année"
print(sentence)

today_date = datetime.now()
print(today_date)
print(today_date.strftime("%d_%B_%Y"))

print(dir(str))
help(str.lower)

message = "SALut ToUt LE MonDE"
message = message.lower()
print(message)
print(message.upper())
print(message.swapcase())
print(message.title())
print(message.capitalize())

# print(message.index("z"))
print(message.find("z"))
print(message.rfind("l"))

text = "text"
print(text.isalpha())
print(text.islower())
price = "99"
print(price.isdigit())
password = "pass123"
print(password.isalnum())
print("    ".isspace())
title = "Le Premier Chapitre"
print(title.istitle())
text = "Salut, Pythön!"
print(text.isascii())
print(message.startswith("salut"))
print(message.endswith("monde"))

print(message.replace("salut", "hello"))
message = "     salut tout le monde"
print(message)
print(message.strip())
file = "image.png"
print(file.removesuffix(".png"))
print(file.strip(".png"))
print(file[:-4])
print(website.removeprefix("https://"))

text = "Hello, World! こんにちは世界!"
encoded_text = text.encode("utf-8")
print(encoded_text)

text = "text"
print(text*3)
print(text.zfill(6))

list = ["Le", "Premier", "Chapitre"]
slug = ("-").join(list)
sentence = (" ").join(list)
print(slug)
print(sentence)
results = "42;49;38;20"
print(results.split(";"))
text = "a+b=c"
print(text.partition("="))
text = "Un message sur \n plusieurs \n lignes \n.."
print(text.splitlines())
print(text.splitlines(keepends=True))

import glob 

filepaths = glob.glob("*.txt")

tag = "h1"

for file in filepaths:
    if file.startswith("2024"):
        date_string = file.removesuffix(".txt")
        year, month, day = date_string.split("_")
        dict = {"year" : year, "month" : month, "day" : day}
        date = datetime.strptime(date_string, "%Y_%m_%d")
        text = "Le " + date.strftime("%d %B %Y")
        html = f"<{tag}>{text}</{tag}>"
        print(html)