import winreg
import logging

# Log file & Config options
logging.basicConfig(filename='winreg.log', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s\n',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

machines = ['computer1', 'computer2', 'computer3']


def get_hkeyusers(machine):
    userkeys = []
    i = 0
    while True:
        try:
            hive = winreg.ConnectRegistry(r'\\{}'.format(machine), winreg.HKEY_USERS)
            userkeys.append(winreg.EnumKey(hive, i))
            i += 1
        except WindowsError as err:
            print(err)
            logging.error('{} | {} \n'.format(machine, err))
            break
    return userkeys


def searchvalue(machine, userkeys):
    for uniquekey in userkeys:
        hive = winreg.ConnectRegistry(r'\\{}'.format(machine), winreg.HKEY_USERS)
        print(uniquekey)
        try:
            with winreg.OpenKey(hive, '{}\Software\Microsoft'.format(uniquekey), 0, winreg.KEY_ALL_ACCESS) as key:
                existvalue = winreg.QueryValue(key, '')
                if existvalue != '':
                    with open("winreg_results.txt", "a") as f:
                        f.write('{}\{}\Software\Microsoft - Value = {} \n'.format(machine, uniquekey, existvalue))
                    print(existvalue)
        except WindowsError as err:
            print(err)
            logging.error('{}\{}\Software\Microsoft | {}'.format(machine, uniquekey, err))

def main(*args):
    for machine in args:
        userkeys = get_hkeyusers(machine)
        searchvalue(machine, userkeys)

main(*machines)


