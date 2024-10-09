from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD

firmware_url = "https://raw.githubusercontent.com/4p51-herd/ota_test/"

ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "test_ota.py")

ota_updater.download_and_install_update_if_available()

# Added this new line
