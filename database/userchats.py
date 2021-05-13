from . import DB


def add_chat(id: str):
    CCH = DB.get("ALLCHATS")
    if not CCH:
        DB.set("ALLCHATS", str(id))
        return
    for chat in CCH.split(" "):
        if id == chat:
            return
    ALL = CCH + " " + id
    DB.set("ALLCHATS", ALL)


def get_all_chats():
    CCH = DB.get("ALLCHATS")
    if not CCH:
        return []
    return CCH.split(" ")


def remove_chat(id):
    CCH = DB.get("ALLCHATS")
    if not CCH:
        return
    WA = ""
    for CHA in CCH.split(" "):
        if CHA != id:
            WA += f" {CHA}"
    DB.set("ALLCHATS", WA)
    return True
