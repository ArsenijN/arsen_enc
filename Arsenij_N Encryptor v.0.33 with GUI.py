"""Треба зробити окремо .bat або .ps1 в котрому буде pip install pysimplegui

https://pip.pypa.io/en/stable/installation/

можна зробити автономний пакет pip щоб запустити всередині python, тобто, зробити встановлювальник

Або просто import залишити, я хз як воно буде себе вести на ноуті (вирішив)
Вирішити проблему з басе64
"""
import os
#try:
    
#except ValueError:
os.system('py -m pip install PySimpleGUI')
import PySimpleGUI as sg
#import PySimpleGUI as sg

#def makepasswords():
#    layout = [ [sg.Text('Введіть кількість паролей: '), sg.Input()] ]


# All the stuff inside your window.
#def main():


#def makepasswords():
#    layout = [ [sg.Text('Введіть кількість паролей: '), sg.Input()] ]
#    window = sg.Window('Arsenij_N Encryptor v.0.32 with GUI: make passwords')

#main




sg.theme('DarkAmber')   # Add a touch of color
import PySimpleGUI as sg

#def passwordmaker():
    
"""
def waiting():
    layout = [[sg.Text('Arsenij_N Encryptor v.0.32 with GUI')],
              [sg.Button("Створення паролів", key="makepasswords")]]
    window = sg.Window("Main Window", layout, size=(320, 240))
    while wait == 1:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        #if event == "makepasswords":
            #makepasswords()
            #break
        
    #window.close()

"""

def finish():
    layout = [[sg.Text('Файл було створено!')],
              [sg.Button("Дивитися файл", key='openfile')],
              [sg.Button("Exit", key="Exit")]]
    window = sg.Window("Arsenij_N Encryptor v.0.32 with GUI: ending", layout, size=(320, 240))
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            os.remove('.temp')
            break
        if event == "openfile":
            from pathlib import Path
            txt = Path('.temp').read_text()
            txt = '"' + txt + '"' #'@echo off, ' + '"' + txt + '"'
            os.system(txt)
            #break
        
    window.close()

def makepasswords():
    layout = [[sg.Text("Кількість паролей:")],
              [sg.Input('', enable_events=True, key='countpass')],
              [sg.Text('Довжина паролей:')],
              [sg.Input('', enable_events=True, key='lengthpass')],
              [sg.Button("Створити!", key='passwordmaker')],
              [sg.Button("Повернутися", key='return')]]#, justification='left')]]
    window = sg.Window("Arsenij_N Encryptor v.0.32 with GUI: making passwords", layout, size=(320, 240), modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'return':
            window.close()
            main()
        if event == 'passwordmaker':
            #if values['countpass'] not in ('0123456789'):
            #    sg.popup('Тільки числа!')
            #    window['countpass'].update(values['countpass'][:-1])
            #if values['lengthpass'] not in ('0123456789'):
            #    sg.popup('Тільки числа!')
            #    window['lengthpass'].update(values['lengthpass'][:-1])

            #if values['countpass'] in ('0123456789') and values['lengthpass'] in ('0123456789'):
            count = values['countpass']
            length = values['lengthpass']
            #wait = '1'
            #waiting
            os.system('"Arsenij_N Encryptor v.0.33 woGUI.py" -ne ' + count + ' ' + length)
            #wait = '0'
            window.close()
            finish()
            
        
    #window.close()

def base64_type():
    layout = [[sg.Text("Виберіть тип тексту:")],
              [sg.Button('Генерований', key='gentext')],
              [sg.Button('Власний', key='usertext')],
              #[sg.Input('', enable_events=True, key='lengthpass')],
              #[sg.Button("Створити!", key='passwordmaker')],
              [sg.Button("Повернутися", key='return')]]#, justification='left')]]
    window = sg.Window("Arsenij_N Encryptor v.0.32 with GUI: base64: type of encoding", layout, size=(320, 240), modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'return':
            window.close()
            main()
        if event == 'gentext':
            #if values['countpass'] not in ('0123456789'):
            #    sg.popup('Тільки числа!')
            #    window['countpass'].update(values['countpass'][:-1])
            #if values['lengthpass'] not in ('0123456789'):
            #    sg.popup('Тільки числа!')
            #    window['lengthpass'].update(values['lengthpass'][:-1])

            #if values['countpass'] in ('0123456789') and values['lengthpass'] in ('0123456789'):
            #count = values['countpass']
            #length = values['lengthpass']
            #wait = '1'
            #waiting
            #os.system('"Arsenij_N Encryptor v.0.33 woGUI.py" -ne ' + count + ' ' + length)
            #wait = '0'
            #window.close()
            #finish()
            base64_gen()
            window.close()

def base64_gen():
    layout = [[sg.Text("Кількість паролей:")],
              [sg.Input('', enable_events=True, key='countpass')],
              [sg.Text('Довжина паролей:')],
              [sg.Input('', enable_events=True, key='lengthpass')],
              [sg.Button("Створити!", key='passwordmaker')],
              [sg.Button("Повернутися", key='return')]]#, justification='left')]]
    window = sg.Window("Arsenij_N Encryptor v.0.32 with GUI: making base64 passwords", layout, size=(320, 240), modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'return':
            window.close()
            main()
        if event == 'passwordmaker':
            #if values['countpass'] not in ('0123456789'):
            #    sg.popup('Тільки числа!')
            #    window['countpass'].update(values['countpass'][:-1])
            #if values['lengthpass'] not in ('0123456789'):
            #    sg.popup('Тільки числа!')
            #    window['lengthpass'].update(values['lengthpass'][:-1])

            #if values['countpass'] in ('0123456789') and values['lengthpass'] in ('0123456789'):
            count = values['countpass']
            length = values['lengthpass']
            #wait = '1'
            #waiting
            os.system('"Arsenij_N Encryptor v.0.33 woGUI.py" -b64 ' + count + ' ' + length)
            #wait = '0'
            window.close()
            finish()
def main():
    layout = [[sg.Text('Arsenij_N Encryptor v.0.32 with GUI')],
              [sg.Text('Виберіть функцію:')],
              [sg.Button("Створення паролів", key="makepasswords")],
              [sg.Button('base64', key='b64')]]
    window = sg.Window("Arsenij_N Encryptor v.0.32 with GUI: home", layout, size=(320, 240))
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "makepasswords":
            makepasswords()
            break
        if event == 'b64':
            base64_type()
            break

    window.close()


if __name__ == "__main__":
    main()
