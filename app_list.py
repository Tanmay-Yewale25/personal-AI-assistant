import os

def app_list():
    paths = [
    r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs",
    os.path.expandvars(
        r"%APPDATA%\Microsoft\Windows\Start Menu\Programs"
    )
    ]

    apps = []

    for path in paths:
        for root, _, files in os.walk(path):
            for file in files:
                if file.endswith(".lnk"):
                    apps.append(file[:-4])

    return apps
