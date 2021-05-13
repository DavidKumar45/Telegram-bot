from . import DB


def caption_True(id):
    CA = DB.get("YESCAPTION")
    CN = DB.get("NOCAPTION")
    if not CN:
        ART = []
    else:
        ART = CN.split(" ")
    AMP = ""
    if id in ART:
        for pp in ART:
            if id != pp:
                AMP += " " + str(pp)
        DB.set("NOCAPTION", AMP)
    if not CA:
        DB.set("YESCAPTION", str(id))
        return True
    if str(id) in CA.split(" "):
        return True
    DB.set("YESCAPTION", CA + " " + str(id))
    return True


def caption_False(id):
    CA = DB.get("NOCAPTION")
    CN = DB.get("YESCAPTION")
    if CN and id in CN.split(" "):
        AM = CN.split(" ").remove(id)
        if not AM:
          DB.delete("YESCAPTION")
        else:
          DB.set("YESCAPTION", "".join(f" {mm}" for mm in AM))
    if not CA:
        DB.set("NOCAPTION", str(id))
        return True
    if str(id) in CA.split(" "):
        return True
    DB.set("NOCAPTION", CA + " " + str(id))
    return True


def check_settings(id):
    CA = DB.get("YESCAPTION")
    CN = DB.get("NOCAPTION")
    if not (CN or CA):
        return "None"
    if CA and id in CA.split(" "):
        return "True"
    if CN and id in CN.split(" "):
        return "False"
