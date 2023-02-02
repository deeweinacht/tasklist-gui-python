import PySimpleGUI

import functions
import PySimpleGUI as sg


task_prompt_label = sg.Text('Enter a new task:')
task_input_textbox = sg.InputText(tooltip='Enter new task')
task_enter_button = sg.Button('Enter')

main_window = sg.Window('Simple Task List', layout=[[task_prompt_label], [task_input_textbox, task_enter_button]])
main_window.read()
main_window.close()




