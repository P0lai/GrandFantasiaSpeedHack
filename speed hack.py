from pymem import *
from pymem.process import *
from os import system 

system("cls||clear")
system("title SPEED HACK")

try:
    mem = Pymem("GrandFantasia.exe")
except:
    print("\033[1;91m[*]The process 'GrandFantasia.exe' not found.\n")
    system("pause")
    exit()

module = module_from_name(mem.process_handle, "GrandFantasia.exe").lpBaseOfDll
offsets = [0xD0, 0x0, 0x0, 0x40, 0x10, 0x8, 0x80]

def getPointerAddr(base, offsets):
    addr = mem.read_int(base)

    for offset in offsets:
        if offset != offsets[-1]:
            addr = mem.read_int(addr + offset)
    
    addr = addr + offsets[-1]

    return addr

def main():
    while True:
        print("\033[1;96m" + """
        [*] GRAND FANTASIA SPEED HACK - 04/06/2022
                    by: Polai\n""")

        try:
            speed_value = float((input("\033[1;97m" + "Value: ")))

            if speed_value > 100 or speed_value < 1:
                system("cls||clear")
                print("\n" + "\033[1;91m" + "[-] The minimum speed value is 1 and maximum 100.")
                main()
        except:
            system("cls||clear")
            print("\n" + "\033[1;91m" + "[-] Only numbers.")    
            main()
        mem.write_float(getPointerAddr(module + 0x0096B6CC, offsets), speed_value)

        system("cls||clear")

        print("\n" + "\033[1;92m" + "[+] Injected.\n")
main()