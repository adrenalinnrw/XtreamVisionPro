from Plugins.Plugin import PluginDescriptor
from Screens.Screen import Screen

class XtreamVision(Screen):
    skin = """
    <screen position="center,center" size="800,600">
        <widget name="title" position="50,50" size="700,50" font="Regular;28"/>
    </screen>
    """
    
    def __init__(self, session):
        Screen.__init__(self, session)
        self["title"] = Label("XtreamVision Pro")

def main(session, **kwargs):
    session.open(XtreamVision)

def Plugins(**kwargs):
    return PluginDescriptor(
        name="XtreamVision Pro",
        description="Premium IPTV Client",
        where=PluginDescriptor.WHERE_PLUGINMENU,
        fnc=main
    )
