from Screens.Screen import Screen
from Components.ActionMap import ActionMap
from Components.MenuList import MenuList

class MainScreen(Screen):
    def __init__(self, session):
        Screen.__init__(self, session)
        self["actions"] = ActionMap(["OkCancelActions"], {
            "ok": self.onOk,
            "cancel": self.close
        })
        self["menu"] = MenuList([
            ("Canlı Yayınlar", "live"),
            ("VOD", "vod"),
            ("Ayarlar", "settings")
        ])
    
    def onOk(self):
        selected = self["menu"].getCurrent()[1]
        print(f"Selected: {selected}")
