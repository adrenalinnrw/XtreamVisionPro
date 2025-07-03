from enigma import eServiceReference, eDVBDB
import json
import requests

class StreamManager:
    def __init__(self):
        self.bouquet_path = "/etc/enigma2/userbouquet.xtreamvision_pro.tv"
    
    def fetch_streams(self, url):
        try:
            response = requests.get(url, timeout=5)
            return json.loads(response.text)
        except Exception as e:
            print(f"[StreamManager] Error: {str(e)}")
            return []
