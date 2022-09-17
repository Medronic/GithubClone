from time import sleep

import PySimpleGUI as sg
import requests

import modules as md


md.LoadSettings()

sg.theme("DarkPurple4")

DownloadFolder = md.GetDownloadPath()

main = [
    [sg.Text(f'{md.lngMainTab_lblUser}', key='lblUser'), sg.Input(key='github_user', size=(45, 1))],
    [sg.Text(f'{md.lngMainTab_lblDir}', key='lblDir'), sg.Input(default_text=f'{DownloadFolder}', key='download_path', size=(42, 1))],
    
    [sg.Button(f'{md.lngMainTab_BtnDownloadRepositories}', key='download_repositories', size=(20, 1))],

    [sg.Text(f'Status: '), sg.Text(f'{md.lngMainTab_StatusMsg1}', key='lblstatus')],
]

settings = [

    [sg.Text(f'{md.lngSettingsTab_lblTheme}', key='lblTheme'), sg.Drop(values=('Dark', 'Light'), default_value=f'{md.stgTheme}', key='stg_theme', readonly=True)],
    [sg.Text(f'{md.lngSettingsTab_lblLanguage}', key='lblLanguage'), sg.Drop(values=('english', 'portuguese'), default_value=f'{md.stgLang}', key='stg_language', readonly=True)],

    [sg.Text(f'{md.lngSettingsTab_lblDefaultDir}', key='lblDefaultDir'), sg.Input(default_text=f'{md.stgDownloadPath}', key='stg_downloadpath', size=(42, 1), tooltip='Please, add exactly Path!')],
    [sg.Button(f'{md.lngSettingsTab_btnSaveSettings}', key='btnSaveSettings',
               size=(18, 1), font='15px')]
               
]

about = [
    
    # [sg.Text(f'{md.AppName}', font='15px')],
    [sg.Text(f'{md.lngAboutTab_lblDescription} {md.AppDescription}', font='15px')],
    [sg.Text(f'{md.lngAboutTab_lblAuthor} {md.AppAuthor} - {md.AppAuthorNickname}', font='15px')],
    [sg.Text('-' * 80)],
    [sg.Text(f'{md.lngAboutTab_lblVersion} {md.AppVersion}', font='15px'), sg.Button(f'{md.lngAboutTab_BtnCheckUpdate}', key='check_update', size=(18, 1), font='15px')],
    [sg.Text(f'{md.lngAboutTab_lbl1}'), sg.Text('...', key='txtExtra', visible=True)]
]

layout = [
    [sg.TabGroup([[sg.Tab(f'{md.lngMainTab}', main), sg.Tab(
    f'{md.lngSettingsTab}', settings), sg.Tab(f'{md.lngAboutTab}', about)]])],
]

window = sg.Window(f"{md.AppName}", layout, size=(460, 250), icon="./static/img/icons/favicon.ico")

while True:
    event, values = window.read()

    if event == 'download_repositories':
        if values['github_user'] != '':
            if md.VerifyPath(values['download_path']) == True:
                md.DownloadRepositories(values['github_user'], values['download_path'])
                window['lblstatus'].update(f"{md.status}")
            else:
                sg.popup(f'{md.lngMainTab_StatusPath1}', title='Error')
        else:
            sg.popup("Provide a username", title="Error")

    if event == 'btnSaveSettings':
        md.stgTheme = values['stg_theme']
        md.stgLang = values['stg_language']
        md.stgDownloadPath = values['stg_downloadpath']

        md.SaveSettings(md.stgTheme, md.stgLang, md.stgDownloadPath)
        sg.popup(f'{md.lngSettingsTab_MsgSuccess}', title='Success')
        md.SaveLogs('Settings saved successfully\n')

    if event == 'check_update':
        md.checkUpdate()
        if md.needUpdate == True:
            msg = str(f'{md.lngAboutTab_lbl2}')
            window['txtExtra'].Update(value=f'{msg}')

            window['txtExtra'].Update(value=f'{md.updateMsg}')
        elif md.needUpdate == False:
            msg = str(f'{md.lngAboutTab_lbl3}')
            window['txtExtra'].Update(value=f'{msg}')
    
    if event == sg.WIN_CLOSED or event == 'Exit':
        break