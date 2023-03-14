# !/usr/bin/env python3

"""
Script to configure device, test reachability and save configuration
"""
from netmiko import ConnectHandler


def configureDevice(net_connect):
    print("Configuring inputs")
    ip = input("enter the IP and mask: ")
    interface = input("interface: ")
    description = input("description: ")
    config_commands = ['int ' + interface, 'ip address ' + ip, 'description ' + description]
    output = net_connect.send_config_set(config_commands)
    print(output)


def testRechability(net_connect):
    print("Test reachability")
    ip = input("enter the IP to test: ")
    output = net_connect.send_command("ping " + ip)
    print(output)


def save(net_connect):
    print("Save Configuration")
    output = net_connect.send_command("wr")
    print(output)
    print("Configuration saved")


def connect():
    print("Inputs for the ssh connection")
    ip = input("enter the IP of the router: ")
    user = input("username: ")
    passwd = input("password: ")
    device = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': user,
        'password': passwd,
        'secret': 'cisco123',
    }
    return ConnectHandler(**device)


def menu():
    try:
        net_connect = connect()
        print("ssh connection sucessfully")
    except:
        print("error in ssh connection")
        exit()

    option = 1
    while option != 0:
        print("""
    Select the following options:
        [1] Configure Device
        [2] Reachability
        [3] Save Configuration
        [0] Exit\n
    """)
        option = int(input("option: "))

        if option == 1:
            configureDevice(net_connect)
        elif option == 2:
            testRechability(net_connect)
        elif option == 3:
            save(net_connect)
        else:
            print("Bye!")
            option = 0


if __name__ == "__main__":
    menu()
