import os


def format_size(size_in_bytes):
    """Convertit une taille en octets en Mo avec deux décimales."""
    size_in_mb = size_in_bytes / (1024 * 1024)  # Conversion en Mo
    return f"{size_in_mb:.2f} Mo"


def print_tree(directory, prefix="", ignore_list=None):
    """
    Affiche l'arborescence d'un dossier avec la taille des fichiers.

    Args:
        directory (str): Chemin du dossier à explorer.
        prefix (str): Préfixe pour l'affichage (indentation).
        ignore_list (list): Liste des fichiers ou dossiers à ignorer.
    """
    if ignore_list is None:
        ignore_list = []  # Par défaut, aucune exclusion

    try:
        # Liste tous les éléments dans le dossier courant
        elements = os.listdir(directory)
    except PermissionError:
        print(prefix + "└── [Permission Denied]")
        return

    for i, element in enumerate(elements):
        # Chemin complet de l'élément
        full_path = os.path.join(directory, element)

        # Vérifie si l'élément est dans la liste d'exclusion
        if element in ignore_list:
            continue  # Ignore cet élément et passe au suivant

        # Vérifie si c'est un dossier ou un fichier
        if os.path.isdir(full_path):
            # C'est un dossier, on l'affiche et on explore son contenu
            print(prefix + "├── " + element)
            if i == len(elements) - 1:
                print_tree(full_path, prefix + "    ", ignore_list)
            else:
                print_tree(full_path, prefix + "│   ", ignore_list)
        else:
            # C'est un fichier, on affiche son nom et sa taille
            try:
                size = os.path.getsize(full_path)  # Taille du fichier en octets
                formatted_size = format_size(size)
                print(prefix + f"└── {element} ({formatted_size})")
            except OSError:
                print(prefix + f"└── {element} (Taille inconnue)")


if __name__ == "__main__":
    # Remplacez ce chemin par le dossier que vous souhaitez explorer
    root_directory = "."

    # Liste des fichiers ou dossiers à ignorer
    ignore_list = [
        ".git",  # Ignorer le dossier .git
        "__pycache__",  # Ignorer les dossiers __pycache__
        ".DS_Store",  # Ignorer les fichiers .DS_Store (macOS)
        "node_modules",  # Ignorer le dossier node_modules
        ".idea",  # Ignorer les dossiers .idea (PyCharm)
        "myenv",
        "model_ML",
    ]

    print(f"Arborescence du dossier {root_directory}:")
    print_tree(root_directory, ignore_list=ignore_list)
