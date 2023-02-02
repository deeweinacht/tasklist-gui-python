import functions
import PySimpleGUI as sg
import os

functions.initialize_task_list()

# Set graphical style for the GUI
sg.theme('DarkGrey6')

# Create widgets using PySimpleGUI
task_prompt_label = sg.Text('Enter a new task:')
task_input_textbox = sg.InputText(tooltip='Enter new task', key='new_task')
task_enter_button = sg.Button('Add new')
tasks_listbox = sg.Listbox(values=functions.get_tasks(), key='tasks_list',
                           enable_events=True, size=(30, 15))
task_edit_button = sg.Button('Edit')
task_complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')

main_window = sg.Window('Simple Task List',
                        layout=[[task_prompt_label],
                                [task_input_textbox, task_enter_button],
                                [tasks_listbox, task_edit_button,
                                 task_complete_button],
                                [exit_button]],
                        font=('Helvetica', 12))

# Listen for events and value changes
while True:
    event, values = main_window.read()
    print(event)
    print(values)
    match event:
        case 'Add new':
            if values['new_task'] != '':
                tasks = functions.get_tasks()
                new_task = values['new_task']
                tasks.append(new_task + '\n')
                functions.save_tasks(tasks)
                main_window['tasks_list'].update(tasks)
            else:
                sg.popup('Please enter a task name!')
        case 'Complete':
            task_to_complete = values['tasks_list'][0]
            tasks = functions.get_tasks()
            tasks.remove(task_to_complete)
            functions.save_tasks(tasks)
            main_window['tasks_list'].update(tasks)
            main_window['new_task'].update('')
        case 'tasks_list':
            main_window['new_task'].update(
                value=values['tasks_list'][0].strip('\n'))
        case 'Edit':
            try:
                task_to_edit = values['tasks_list'][0]
                new_task = values['new_task']

                tasks = functions.get_tasks()
                task_index = tasks.index(task_to_edit)
                tasks[task_index] = new_task + '\n'
                functions.save_tasks(tasks)
                main_window['tasks_list'].update(tasks)
            except IndexError:
                sg.popup('Please select a task to edit!',
                         font=('Helvetica', 12))
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break

main_window.close()