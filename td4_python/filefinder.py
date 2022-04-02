import os

def getfile(filename, extension="", directory="td4_python"):
    filepath = os.path.join(os.getcwd(), filename)
    if os.path.exists(filepath):
        return filepath
    for folder in os.listdir(os.getcwd()):        
        filepath = os.path.join(os.getcwd(), folder, filename)
        print(filepath)
        # td4_python is my runtime directory 
        # (change if u want that u file stay in a specific diretory)
        if filepath.split("\\")[-2] != directory:
            continue
        if os.path.exists(filepath):
            ext = filepath[filepath.rfind(".")+1:]
            print("extension : " + ext)
            if(ext !="py" or ext == extension):
                return filepath
            else:
                print("===> Don't touch python file")
    exit(
        f"\n==> File `{filename}` not found\n"
        "\n|| Les fichiers necessaire au fonctionnement du bot\n"
        "|| doivent être stocker sous le repertoire 'td4_python'"
    )
    