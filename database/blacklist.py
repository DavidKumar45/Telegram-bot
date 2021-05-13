from . import DB


def add_blacklist(id):
    Bl = DB.get("BLACKLIST")
    if not Bl:
        DB.set("BLACKLIST", str(id))
        return True
    for pp in Bl.split(" "):
        if id == pp:
            return True
    AL = Bl + " " + str(id)
    DB.set("BLACKLIST", AL)


def check_blacklist(id):
    Bl = DB.get("BLACKLIST")
    if not Bl:
        return False
    for pl in Bl.split(" "):
        if id in pl:
            return True
    return False


def remove_blacklist(id):
    Bl = DB.get("BLACKLIST")
    if not Bl:
        return "Blacklisted User List is Empty !"
    WA = ""
    if id not in Bl.split(" "):
        return "User Was Not Blacklisted !"
    for op in Bl.split(" "):
        if not op == id:
            WA += " " + op
    DB.set("BLACKLIST", WA)
    return "Removed User from BLACKLIST"


def get_blacklisted():
    Bl = DB.get("BLACKLIST")
    if not Bl:
        return []
    return Bl.split(" ")
