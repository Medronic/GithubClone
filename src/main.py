import PySimpleGUI as sg
import requests

import modules as md

md.LoadSettings()

sg.theme("DarkPurple4")

# print(ttv.getUserID("medronic"))

UserProfile = md.getUserProfile()

main = [
    [sg.Text(f'{md.lngLblUser}', key='lblUser'), sg.Input(key='github_user', size=(45, 1))],
    [sg.Text(f'{md.lngLblDir}', key='lblDir'), sg.Input(default_text=f'{UserProfile}', key='download_path', size=(42, 1))],
    
    [sg.Button(f'{md.lngBtnDownloadRepositories}', key='download_repositories', size=(20, 1))],

    [sg.Text('Status: '), sg.Text(f'{md.lngStatusMsg1}', key='lblstatus')],
]


settings = [

    [sg.Text(f'Tema', key='lblTheme'), sg.Drop(values=('Dark', 'Light'), default_value=f'{md.stgTheme}', key='stg_theme', readonly=True)],
    [sg.Text(f'Linguagem', key='lblLanguage'), sg.Drop(values=('english', 'portuguese'), default_value=f'{md.stgLang}', key='stg_language', readonly=True)],

    [sg.Text('Diretório Padrão:', key='lblDefaultDir'), sg.Input(default_text=f'{md.stgDownloadPath}', key='stg_downloadpath', size=(42, 1))],
    [sg.Button('Salvar Configurações', key='btnSaveSettings',
               size=(18, 1), font='15px')]
               
]

about = [
    [sg.Text(f'{md.AppName}', font='15px')],
    [sg.Text(f'Description: {md.AppDescription}', font='15px')],
    [sg.Text(f'Desenvolvido: {md.AppAuthor} - {md.AppAuthorNickname}', font='15px')],
    [sg.Text(f'Versão: {md.AppVersion}', font='15px')],
    [sg.Button('Verificar Atualizações', key='check_update', size=(18, 1), font='15px')]
]

layout = [
    [sg.TabGroup([[sg.Tab('Main', main), sg.Tab(
        'Configurações', settings), sg.Tab('Sobre', about)]])],
]

window = sg.Window(f"{md.AppName}", layout, size=(460, 200), icon="./static/img/icons/favicon.ico")

while True:
    event, values = window.read()

    if event == 'download_repositories':
        if values['github_user'] != '':
            md.DownloadRepositories(values['github_user'], values['download_path'])
            window['lblstatus'].update(f"{md.status}")
        else:
            sg.popup("Provide a username", title="Error")

    if event == 'btnSaveSettings':
        md.stgTheme = values['stg_theme']
        md.stgLang = values['stg_language']
        md.stgDownloadPath = values['stg_downloadpath']

        md.SaveSettings(md.stgTheme, md.stgLang, md.stgDownloadPath)
        md.SaveLogs('Settings saved successfully')
    if event == sg.WIN_CLOSED or event == 'Exit':
        break