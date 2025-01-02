#
# Verificar Permissão
#

import ctypes

if not ctypes.windll.shell32.IsUserAnAdmin():
    raise PermissionError("Este script precisa ser executado como administrador.")
    input()

#
# Importações
#

import time, os, requests, shutil, urllib3
from rich import print
from zipfile import ZipFile

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

print('Importações de terceiros carregada.')

#
# Visual
#

class ascii:

	logo = '''
	AUTOMATIZAR A INSTALAÇÃO DO:[red1]
        ╔╦╗┬┌┐┌┌─┐┌─┐┬─┐┌─┐┌─┐┌┬┐
        ║║║││││├┤ │  ├┬┘├─┤├┤  │ 
        ╩ ╩┴┘└┘└─┘└─┘┴└─┴ ┴└   ┴
        ╔╗ ┌─┐┌┬┐┬─┐┌─┐┌─┐┬┌─    
        ╠╩╗├┤  ││├┬┘│ ││  ├┴┐    
        ╚═╝└─┘─┴┘┴└─└─┘└─┘┴ ┴    [/red1]

    [red1](1)[/red1] Instalar o [u]MCLauncher[/u]
    [red1](2)[/red1] Remover a versão [u]Trial[/u] do Minecraft [yellow1](é recomendado abrir o programa via powershell)[/yellow1]
    [red1](3)[/red1] Sair
    '''

class visual:
    def center(texto):
        return texto.center(os.get_terminal_size().columns)

    def Logger(texto):
        print(time.strftime(f"[bold dark_orange3][%H:%M:%S]:[/bold dark_orange3] {texto}", time.localtime()))

#
# Funções do menu
#

def instalar_Launcher():
    if not os.path.isfile('MCLauncher.zip'):
        file = requests.get('https://github.com/MCMrARM/mc-w10-version-launcher/releases/download/0.4.0/MCLauncher.zip', verify = False)
        if file.status_code == requests.codes.OK:
            with open('MCLauncher.zip', 'wb') as MCLauncher:
                    MCLauncher.write(file.content)
            with ZipFile("MCLauncher.zip", 'r') as launcher:
                launcher.extractall("MCLauncher/")
            os.remove('MCLauncher.zip')
            visual.Logger('Instalado com sucesso!')

def cheat_trial():
	dll = r"C:\Windows\System32\Windows.ApplicationModel.Store.dll"

	if not os.path.exists('Windows.ApplicationModel.Store.dll'):
		dlltobypass = requests.get('https://github.com/makonhacolorida/mc-bedrock/raw/refs/heads/main/Windows.ApplicationModel.Store.dll', verify = False)
		if dlltobypass.status_code == requests.codes.OK:
			with open('Windows.ApplicationModel.Store.dll', 'wb') as DLL_PASS:
				DLL_PASS.write(dlltobypass.content)
			visual.Logger('DLL Instalada!')

	visual.Logger('Começando a injeção..')

	try:
		if os.path.exists(dll):
			if not os.path.isdir("backup"):
				os.mkdir("backup")

			shutil.move(dll, os.getcwd() + '\\backup\\Windows.ApplicationModel.Store.dll.original')

		# Copiar a nova DLL para o System32
		shutil.copy(r"Windows.ApplicationModel.Store.dll", dll)
		time.sleep(1)
		os.remove('Windows.ApplicationModel.Store.dll')
		visual.Logger(f"[bold red u]ByPass[/bold red u] Injetado com Sucesso!")

	except Exception as e:
	    visual.Logger(f"Ocorreu um erro: {e}")


#
# Menu
#

while True:
	os.system('cls')
	print(visual.center(ascii.logo))

	opcao = input('>>> ')

	if(opcao == '1'):
		instalar_Launcher()
		input('Aperte alguma tecla para continuar')

	if(opcao == '2'):
		cheat_trial()
		input('Aperte alguma tecla para continuar')

	if(opcao == '3'):
		print('Bye Bye')
		exit()

	time.sleep(0.2)

