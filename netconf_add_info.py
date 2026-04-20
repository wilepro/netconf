from ncclient import manager

my_device = {
        "host": "192.168.1.111",
        "port": 830,
        "username": "john",
        "password": "Cisco123",
        "hostkey_verify": False
}

ntp_config = """
        <config>
                <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                        <ntp operation="replace">
                                <server xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ntp">
                                        <server-list>
                                                <ip-address>3.3.3.3</ip-address>
                                        </server-list>
                                </server>
                        </ntp>
                </native>
        </config>
        """


with manager.connect(**my_device) as connection:
    result = connection.edit_config(target="running", config=ntp_config)
    print(result)
