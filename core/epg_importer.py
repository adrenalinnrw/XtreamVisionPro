from enigma import eEPGCache
from Tools.Directories import fileExists

class EPGImporter:
    def __init__(self):
        self.epgcache = eEPGCache.getInstance()
    
    def import_epg(self, xml_path):
        if fileExists(xml_path):
            self.epgcache.importEvents(xml_path)
