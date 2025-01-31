file = open("test.txt")

# lecture

content = file.read()
print(content)

print("##################")

file.seek(0)
content = file.read(15)
print(content)

print("##################")

file.seek(27)
content = file.read()
print(content)

print("##################")
file.seek(0)
for line in file:
    print(line.rstrip())


print("##################")
file.seek(0)
lines = file.readlines()
print(lines)

file.close()

# écriture 
file = open("demo.txt", "w")
file.write("Voici le contenu du fichier \n")
file.close()

file = open("demo.txt", "w")
file.write("remplacer l'ancien contenu \n")
file.close()


# ajout 
file = open("demo.txt", "a")
file.write("Le nouveau contenu du fichier \n")
lines = ["voici un ajout d'une ligne \n", "une autre ligne \n"]
file.writelines(lines)
file.close()

# création 
import os 
if not os.path.exists("essai.txt"):
    file = open("essai.txt", "x")
    file.close()

# gestion des ressources
try:
    f = open("test.txt")
    print(f.read())
except:
    print("une erreur est survenue")
else:
    f.close()

try:
    f = open("test.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("Ce fichier n'existe pas")
except PermissionError:
    print("Vous n'avez pas les permissions")
except IOError:
    print("erreur sur une opération input / output")
except Exception as e: 
    print(e)
else: 
    print(content)
finally:
    if "f" in locals() and f:
        f.close()

    
# context manager 
with open("demo.txt") as f:
    content = f.read()
    print(content)

with open("demo.txt", "r") as f: 
    f.seek(27)
    content = f.read(15)
    print(content)
    print("position du curseur :", f.tell())

with open("demo.txt", "a") as f: 
    f.write("""encore une ligne
et une autre ligne""")

# copie 
with open("test.txt", "r") as test_file:
    with open("copy.txt", "w") as copy_file:
        for line in test_file:
            copy_file.write(line)


# fusion
from pathlib import Path 
dir = Path("data")
merged = ""
for index, filepath in enumerate(dir.iterdir()):
    with open(filepath, "r") as file:
        content = file.readlines()
        if index == 0 :
            merged += content[0].replace("AMOUNT", "UNITS")
        new_content = content[1:]
        merged += "".join(new_content) + "\n"

with open("merged.txt", "w") as file:
    file.write(merged)

# download 
import urllib.request 

url = "https://www.python.org/static/community_logos/python-logo.png"

# response = urllib.request.urlopen(url)
# with open("image.png", "wb") as f:
#     f.write(response.read())

# response.close()

# with urllib.request.urlopen(url) as res:
    # with open("image.png", "wb") as f:
    #     f.write(res.read())

# urllib.request.urlretrieve(url, "image.png")

import requests 
response = requests.get(url)
with open("image.png", "wb") as f:
        f.write(response.content)

# upload 
# url = "https://file.io"
# with open("image.png", "rb") as f:
#     response = requests.post(url, files={"file" : f })
#     print(response.json())

# copie image
with open("image.png", "rb") as image_file:
    with open("copy.png", "wb") as copy_file:
        chunk_size = 4096 
        image_chunk =  image_file.read(chunk_size)
        while len(image_chunk) > 0 :
            copy_file.write(image_chunk)
            image_chunk = image_file.read(chunk_size)

# archives
import shutil 
shutil.make_archive("archive", "zip", "data")
shutil.unpack_archive("archive.zip", "files")

import zipfile 
images_zip = zipfile.ZipFile("images.zip", "w", compression=zipfile.ZIP_DEFLATED)
images_zip.write("image.png")
images_zip.write("copy.png")
images_zip.close()

with zipfile.ZipFile("images.zip", "r") as f:
    print(f.namelist())
    f.extractall("images")