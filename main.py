# os 
import os 

# navigation 
print(os.getcwd())

os.chdir("dossier1")

print(os.getcwd())

# chemins absolus 

os.chdir("C:\\Users\\Louis\\Desktop\\python\\07 - système de fichiers\\dossier2")

print(os.getcwd())

os.chdir(r"C:\Users\Louis\Desktop\python\07 - système de fichiers")

print(os.getcwd())

# conditions

filepath = r"dossier2\demo.txt"

if os.path.exists(filepath):
    print("Ce chemin existe")
    if os.path.isfile(filepath):
        print("Il s'agit d'un fichier")

folder_path = "dossier2"

if os.path.isdir(folder_path):
    print("Il s'agit d'un dossier")

# combiner des chemins 

input_folder = os.path.join(os.getcwd(), r"input_dir\data")

# création
if not os.path.exists(input_folder):
    os.makedirs(input_folder)

# déplacement 
src = r"dossier2\demo.txt"
dest = "demo.txt"

try:
    os.replace(src, dest)
except FileNotFoundError:
    print("Ce chemin n'existe pas")

# renommage 
try:
    os.rename("demo.txt", "renamed_demo.txt")
except FileNotFoundError:
    print("Ce chemin n'existe pas")

# suppression 
try:
    os.rmdir("dossier3")
except FileNotFoundError:
    print("Ce chemin n'existe pas")

try:
    os.removedirs(r"dossier4\2024\janvier")
except FileNotFoundError:
    print("Ce chemin n'existe pas")

# variables d'environnement 
os.environ["HOME"] = r"user\home"

home_dir = os.path.join(os.getcwd(), os.environ.get("HOME"))

print(home_dir)

# informations sur les fichiers
print(os.stat("renamed_demo.txt"))

# méthodes utiles 
filepath = os.path.join(os.getcwd(), "renamed_demo.txt")
print(os.path.basename(filepath))
print(os.path.dirname(filepath))
print(os.path.split(filepath))
print(os.path.splitext(filepath))
print(os.path.abspath(__file__))

# lancer un fichier 
# os.startfile(filepath)

# boucles
for filepath in os.listdir():
    print(filepath)

os.chdir("courses")

# for f in os.listdir():
#     f_name, f_ext = os.path.splitext(f)
#     f_title, f_course, f_num = f_name.split("-")
#     new_name = f"{f_num}-{f_title}{f_ext}"
#     os.rename(f, new_name)

os.chdir(os.pardir)

for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print(dirpath)
    if dirnames:
        print(dirnames)
    if filenames:
        print(filenames)


src = os.path.join(os.getcwd(), "src")
images = []
image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.gif', '*.bmp', '*.tiff']

from fnmatch import fnmatch

for root, dirs, files in os.walk(src):
    for filename in files:
        for ext in image_extensions:
            if fnmatch(filename, ext):
                images.append(filename)

print(images)

# shutil 
import shutil 

os.chmod("log.txt", 0o444) # lecture seule 

# copies
try:
    shutil.copyfile("log.txt", "copies\\copy1.txt")
    shutil.copy("log.txt", "copies\\copy2.txt")
    shutil.copy2("log.txt", "copies\\copy3.txt")
except FileNotFoundError:
    print("ce chemin n'existe pas")
except PermissionError:
    print("Vous n'avez pas la permission")


print(os.stat(r"copies\copy1.txt").st_mode)
print(os.stat(r"copies\copy2.txt").st_mode)

print(os.stat("log.txt").st_mtime)
print(os.stat(r"copies\copy1.txt").st_mtime)
print(os.stat(r"copies\copy2.txt").st_mtime)
print(os.stat(r"copies\copy3.txt").st_mtime)

try:
    shutil.rmtree("folder")
except FileNotFoundError:
    print("ce chemin n'existe pas")

# glob
import glob 

jpg_paths = glob.glob("src/*.jpg")
print(jpg_paths)

jpg_paths = glob.glob("src/**/*.jpg", recursive=True)
print(jpg_paths)

# Pathlb 
from pathlib import Path 

print(Path.cwd())

filepath = Path("dossier1")
filepath = Path(r"C:\Users\Louis\Desktop\python\07 - système de fichiers")
filepath = Path.cwd() / "dossier1"
print(filepath)
filepath = Path(__file__).parent
print(filepath)

# conditions
if filepath.exists():
    print("ce chemin existe")

# boucles
for p in Path("courses").iterdir():
    print(p)

root_path = Path("src")

for path in root_path.glob("*"):
    print(path)

for path in root_path.rglob("*"):
    print(path)

for path in root_path.rglob("*.jpg"):
    print(path)

for path in root_path.rglob("*.jpeg", case_sensitive=False):
    print(path)

# match
logfile = Path("log.txt")
print(logfile.match("*.txt"))

# suppression 
filepath = Path(__file__).parent / "dossier1" / "demo.txt"
try:
    filepath.unlink()
except FileNotFoundError:
    print("ce chemin n'existe pas")

# création  de fichiers
filepath.touch()

# création de dossiers
Path("parent_dir/output_dir").mkdir(parents=True, exist_ok=True)

# écrire et lire des fichiers
filepath.write_text("hello")
print(filepath.read_text())

# renommage
p = Path("renamed_demo.txt")
p.rename("demo.txt")

# déplacement 
Path("demo.txt").replace("dossier2/demo.txt")

# informations sur les chemins
print(Path().cwd().stat().st_mtime)

# propriétés utiles
print(filepath.name)
print(filepath.stem)
print(filepath.suffix)
print(filepath.parent)

# évaluation 
print(Path(__file__) == Path.cwd() / "main.py")

# méthodes utiles
print(Path("dossier1"))
print(Path("dossier1").absolute())
print(Path("dossier1\..").absolute())
print(Path("dossier1\..").resolve())
print(Path("dossier1\..").resolve().as_posix())

# boucles
src = Path.cwd() / "src"

images = []

image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.gif']

for file_path in src.rglob("*"):
    if file_path.is_file(): 
        for ext in image_extensions:
            if file_path.match(ext):
                images.append(file_path.name)

print(images)