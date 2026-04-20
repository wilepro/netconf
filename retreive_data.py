from ncclient import manager
from xml.dom import minidom

my_device = {
        "host": "192.168.1.111",
        "port": 830,
        "username": "john",
        "password": "Cisco123",
        "hostkey_verify": False
}

with manager.connect(**my_device) as connection:
    result = connection.get_config(source="running").xml
    print(minidom.parseString(result).toprettyxml())
