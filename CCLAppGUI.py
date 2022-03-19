# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 11:59:51 2022

@author: John Ergen
"""
import PySimpleGUI as sg
import CustomizeCoverLetterApp as ccl

#global companyName

layout=[[sg.Text('Please input the company name')], 
        [sg.InputText()],
        [sg.Button('OK')]]

window = sg.Window('Custom Cover Letter App', layout)

while True:
    event, values = window.read()
    kwInput = values
    companyName = kwInput[0]
    if event == 'OK' or event == sg.WIN_CLOSED:
        ccl.ccl(companyName)
        break
    
window.close()
    
print(type(companyName))
print(companyName)


