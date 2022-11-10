import sys
from subprocess import call
import json
import os
import datetime
import zipfile
from time import sleep

import requests

# DEFINES

LOAD_SETTINGS = "Loading settings..."
LOAD_SETTINGS_SUCCESS = "Settings loaded successfully!"
LOAD_SETTINGS_ERROR = "Error loading settings!"

SAVE_SETTINGS = "Saving settings..."
SAVE_SETTINGS_SUCCESS = "Settings saved successfully!"
SAVE_SETTINGS_ERROR = "Error saving settings!"

url_base = 'https://api.github.com/'

# Função para Salvar arquivos de Log

def SaveLogs(p1):
    with open('logs.txt', 'a', encoding='utf-8') as outfile:
        date = datetime.datetime.now()
        outfile.write(f"{date} - {p1}")

# Função para salvar as configurações

def SaveSettings(p1 = None, p2 = None, p3 = None, p4 = None, p5 = None, p6 = None):
    data = {}
    data['Settings'] = {'Application': {'Name': AppName, 'Description': AppDescription, 'Author': AppAuthor, 'AuthorNickname': AppAuthorNickname, 'Version': AppVersion}, 'UI': {'Theme': p1, 'Language': p2, 'DownloadPath': p3}}
    with open('settings.json', 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile)

# Função para Ler as Configurações do Arquivo JSON

def LoadSettings():
    SaveLogs(f"Loading settings...\n")

    msgLog = None

    if os.path.isfile('settings.json'):
        arquivo_json = open('settings.json', 'r', encoding='utf-8')
        data = json.loads(arquivo_json.read())

        # Variáveis Globais da Aplicação
        
        global AppName
        global AppDescription
        global AppAuthor
        global AppAuthorNickname
        global AppVersion

        global stgTheme
        global stgLang
        global stgDownloadPath

        # Configurações da Aplicação

        AppName = data['Settings']['Application']['Name']
        AppDescription = data['Settings']['Application']['Description']
        AppAuthor = data['Settings']['Application']['Author']
        AppAuthorNickname = data['Settings']['Application']['AuthorNickname']
        AppVersion = data['Settings']['Application']['Version']

        stgTheme = data['Settings']['UI']['Theme']
        stgLang = data['Settings']['UI']['Language']
        stgDownloadPath = data['Settings']['UI']['DownloadPath']

        SaveLogs(f"Settings loaded successfully!\n")
    else:
        SaveLogs("Settings file not found! Creating default settings file...\n")
        
    SaveLogs(f"Loading Languages...\n")

    if os.path.isfile('languages.json'):
        arquivo_json = open('languages.json', 'r', encoding='utf-8')
        data = json.loads(arquivo_json.read())

        global lngMainTab
        global lngSettingsTab
        global lngAboutTab

        lngMainTab = data[f'{stgLang}'][0]['TabGroup']['Main']
        lngSettingsTab = data[f'{stgLang}'][0]['TabGroup']['Settings']
        lngAboutTab = data[f'{stgLang}'][0]['TabGroup']['About']

        ##############################################################################
        
        global lngMainTab_lblUser
        global lngMainTab_checkUser
        global lngMainTab_lblDir
        global lngMainTab_BtnDownloadRepositories

        global lngMainTab_StatusMsg1
        global lngMainTab_StatusMsg2
        global lngMainTab_StatusMsg3
        global lngMainTab_StatusMsg4
        global lngMainTab_StatusMsg5
        global lngMainTab_StatusMsg6
        global lngMainTab_StatusMsg7
        global lngMainTab_StatusPath1

        lngMainTab_lblUser = data[f'{stgLang}'][0]['MainTab']['lblUser']
        lngMainTab_checkUser = data[f'{stgLang}'][0]['MainTab']['checkUser']
        lngMainTab_lblDir = data[f'{stgLang}'][0]['MainTab']['lblDir']
        lngMainTab_BtnDownloadRepositories = data[f'{stgLang}'][0]['MainTab']['btnDownloadRepositories']
        lngMainTab_StatusMsg1 = data[f'{stgLang}'][0]['MainTab']['lblStatusMsg1']
        lngMainTab_StatusMsg2 = data[f'{stgLang}'][0]['MainTab']['lblStatusMsg2']
        lngMainTab_StatusMsg3 = data[f'{stgLang}'][0]['MainTab']['lblStatusMsg3']
        lngMainTab_StatusMsg4 = data[f'{stgLang}'][0]['MainTab']['lblStatusMsg4']
        lngMainTab_StatusMsg5 = data[f'{stgLang}'][0]['MainTab']['lblStatusMsg5']
        lngMainTab_StatusMsg6 = data[f'{stgLang}'][0]['MainTab']['lblStatusMsg6']
        lngMainTab_StatusMsg7 = data[f'{stgLang}'][0]['MainTab']['lblStatusMsg7']
        lngMainTab_StatusPath1 = data[f'{stgLang}'][0]['MainTab']['lblStatusPath1']

        ##############################################################################

        global lngSettingsTab_lblTheme
        global lngSettingsTab_lblLanguage
        global lngSettingsTab_lblDefaultDir
        global lngSettingsTab_btnSaveSettings

        lngSettingsTab_lblTheme = data[f'{stgLang}'][0]['SettingsTab']['lblTheme']
        lngSettingsTab_lblLanguage = data[f'{stgLang}'][0]['SettingsTab']['lblLanguage']
        lngSettingsTab_lblDefaultDir = data[f'{stgLang}'][0]['SettingsTab']['lblDefaultDir']

        global lngSettingsTab_btnSaveSettings
        global lngSettingsTab_MsgSuccess
        global lngSettingsTab_MsgError

        lngSettingsTab_btnSaveSettings = data[f'{stgLang}'][0]['SettingsTab']['SaveSettings']['btnSaveSettings']
        lngSettingsTab_MsgSuccess = data[f'{stgLang}'][0]['SettingsTab']['SaveSettings']['MsgSuccess']
        lngSettingsTab_MsgError = data[f'{stgLang}'][0]['SettingsTab']['SaveSettings']['MsgError']

        ##############################################################################

        global lngAboutTab_lblDescription
        global lngAboutTab_lblVersion
        global lngAboutTab_lblAuthor

        lngAboutTab_lblDescription = data[f'{stgLang}'][0]['AboutTab']['lblDescription']
        lngAboutTab_lblVersion = data[f'{stgLang}'][0]['AboutTab']['lblVersion']
        lngAboutTab_lblAuthor = data[f'{stgLang}'][0]['AboutTab']['lblAuthor']

        ##############################################################################

        global lngAboutTab_BtnCheckUpdate
        global lngAboutTab_lbl1
        global lngAboutTab_lbl2
        global lngAboutTab_lbl3
        global lngAboutTab_lbl4
        global lngAboutTab_lbl5
        global lngAboutTab_lbl6
        global lngAboutTab_lbl7
        global lngAboutTab_lbl8

        lngAboutTab_BtnCheckUpdate = data[f'{stgLang}'][0]['AboutTab']['FuncUpdate']['btnCheckUpdate']
        lngAboutTab_lbl1 = data[f'{stgLang}'][0]['AboutTab']['FuncUpdate']['lbl1']
        lngAboutTab_lbl2 = data[f'{stgLang}'][0]['AboutTab']['FuncUpdate']['lbl2']
        lngAboutTab_lbl3 = data[f'{stgLang}'][0]['AboutTab']['FuncUpdate']['lbl3']
        lngAboutTab_lbl4 = data[f'{stgLang}'][0]['AboutTab']['FuncUpdate']['lbl4']
        lngAboutTab_lbl5 = data[f'{stgLang}'][0]['AboutTab']['FuncUpdate']['lbl5']
        lngAboutTab_lbl6 = data[f'{stgLang}'][0]['AboutTab']['FuncUpdate']['lbl6']
        lngAboutTab_lbl7 = data[f'{stgLang}'][0]['AboutTab']['FuncUpdate']['lbl7']
        lngAboutTab_lbl8 = data[f'{stgLang}'][0]['AboutTab']['FuncUpdate']['lbl8']

        msgLog = f"Language Settings successfully loaded!\n"
        SaveLogs(msgLog)
    else:
        SaveLogs(f"Language file settings not found! Creating default language file...\n")

# Função para checkar se existe uma nova versão

def checkUpdate():
    global serverVersion
    global needUpdate
    url = 'https://pastebin.com/raw/sstKjksV'
    r = requests.get(url)
    serverVersion = float(r.text)

    SaveLogs('Checking for updates...\n')
    
    # print(serverVersion)
    # if sSilenceMode in ['yes']:
    #     print(1)
    # else:
    #     print(2)
    if AppVersion != serverVersion:
        SaveLogs('New version found!\n')
        needUpdate = True
        
        update()
    else:
        SaveLogs('No new version found!\n')
        needUpdate = False

    # print('Debug', type(clientVersion), type(serverVersion))

# Função para baixar a atualização. 

def update():
    global folder
    global file_name
    global updateMsg

    updateMsg = ''
    folder = f'GC_GUIv{serverVersion}'
    file_name = f'GC_GUIv{serverVersion}.zip'

    url = f'https://leavepriv8.com/Softwares/GC_GUI/{file_name}'
    r = requests.get(url, allow_redirects=True)
    
    open(f'{file_name}', 'wb').write(r.content)

    updateMsg = f'{lngAboutTab_lbl5}'
    SaveLogs(f'{updateMsg}\n')

    with zipfile.ZipFile(f'{file_name}','r') as zip_ref:
        zip_ref.extractall(f'{folder}')
        
        sleep(2)
        updateMsg = f'{lngAboutTab_lbl7}' + folder
        SaveLogs(f'{updateMsg}\n')

# Função para pegar a pasta de Downloads do usuário

def GetDownloadPath():
    if os.name == 'posix':
        return os.path.expanduser('~/Downloads')
    elif os.name == 'nt':
        return os.path.join(os.environ['USERPROFILE'], 'Downloads')
    else:
        return os.getcwd()

# Função para verificar se o diretório existe

def VerifyPath(path):
    if os.path.isdir(path):
        return True
    else:
        return False

# Função para baixar os repositórios
def DownloadRepositories(user, path, isUser):
    
    if isUser == True:
        # print("É um usuário")
        url = url_base + 'users/{0}/repos'.format(user)
        SubDownload(url, path)
    elif isUser == False:
        # print("É uma organização")
        url = url_base + 'orgs/{0}/repos'.format(user)
        SubDownload(url, path)

def SubDownload(url, path):
    error = False
    global status

    status = f"No errors for now!"

    try:
        r = requests.get(url, timeout=10)

    except requests.Timeout as e:
        status = f'{lngMainTab_StatusMsg3}'
        SaveLogs(status)
        return status
        error = True
    except requests.ConnectionError as e:
        status = f'{lngMainTab_StatusMsg4}'
        SaveLogs(status)
        return status
        error = True
    except socket.error as e:
        status = f'{lngMainTab_StatusMsg5}'
        SaveLogs(status)
        return status
        error = True
    except exception as e:
        status = e.message
        SaveLogs(e.message)
        return status
        error = True

    if (error == True):
        status = f'{lngMainTab_StatusMsg6}'
        SaveLogs(e.message)
        return status
        # exit(1)

    if (r.status_code == 404):
        status = f'{lngMainTab_StatusMsg7}'
        return status
        # exit(1)

    json_data = r.text

    data = json.loads(json_data)

    os.chdir(path)

    status = 'Downloading repositories...'
    SaveLogs(status)

    for i in range(0, len(data)):
        print('Cloning %i / %i' % (i+1, len(data)))
        print('Cloning repository: %s' % data[i]['name'])

        call(['git', 'clone', data[i]['clone_url']])
        status = 'All repositories cloned successfully!'