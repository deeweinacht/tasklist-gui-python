import functions
import PySimpleGUI as sg

# Create widgets using PySimpleGUI
task_prompt_label = sg.Text('Enter a new task:')
task_input_textbox = sg.InputText(tooltip='Enter new task', key='new_task')
task_enter_button = sg.Button('Add new')
tasks_listbox = sg.Listbox(values=functions.get_tasks(), key='tasks_list',
                           enable_events=True, size=(30, 15))
task_edit_button = sg.Button('Edit')

main_window = sg.Window('Simple Task List',
                        layout=[[task_prompt_label],
                                [task_input_textbox, task_enter_button],
                                [tasks_listbox, task_edit_button]],
                        font=('Helvetica', 12))

while True:
    event, values = main_window.read()
    print(event)
    print(values)
    match event:
        case 'Add new':
            tasks = functions.get_tasks()
            new_task = values['new_task']
            tasks.append(new_task + '\n')
            functions.save_tasks(tasks)
            main_window['tasks_list'].update(tasks)
        case 'Edit':
            task_to_edit = values['tasks_list'][0]
            new_task = values['new_task']

            tasks = functions.get_tasks()
            task_index = tasks.index(task_to_edit)
            tasks[task_index] = new_task + '\n'
            functions.save_tasks(tasks)
            main_window['tasks_list'].update(tasks)
        case 'tasks_list':
            main_window['new_task'].update(
                value=values['tasks_list'][0].strip('\n'))
        case sg.WIN_CLOSED:
            break

main_window.close()




