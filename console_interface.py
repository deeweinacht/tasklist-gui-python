"""
This program allows the user to create a list of tasks with the ability to add, remove, edit, and view tasks
"""

import functions

print('Welcome to your personal task list!')

while True:
    user_entry = input('\n================\nMake a selection, using a number:\n1. Show List\n2. Add Task\n3. Edit Task'
                       '\n4. Complete Task\n5. Quit\n================\nSelection:')
    choice_dict = {'1': 'Show', '2': 'Add', '3': 'Edit', '4': 'Complete', '5': 'Exit'}
    try:
        user_entry = choice_dict[user_entry]
    except KeyError:
        print('You have entered an invalid value. Please enter a number.')
        continue

    match user_entry:
        case 'Show':
            tasks = functions.get_tasks()
            functions.display_tasks(tasks)

        case 'Add':
            new_task = input("\nEnter a new to-do item:")
            tasks = functions.get_tasks()
            tasks.append(new_task + '\n')

            functions.save_tasks(tasks)
            print(f'{new_task} added to your task list!')

        case 'Edit':
            tasks = functions.get_tasks()
            functions.display_tasks(tasks)

            task_num = int(input('Enter the number of the task that you wish to edit:'))
            task_num -= 1
            tasks[task_num] = input(f'Replace task {task_num + 1} with what task?') + '\n'

            functions.save_tasks(tasks)
            print(f'Task number {task_num + 1} has been edited!')

        case 'Complete':
            tasks = functions.get_tasks()

            for i, task in enumerate(tasks):
                task = task.strip('\n')
                print(f'{i + 1}. {task}')

            try:
                task_num = int(input('Enter the number of the task that you have completed:'))
                task_num -= 1
                removed_task = tasks.pop(task_num).strip('\n')
            except IndexError:
                print('You have entered an invalid value, please try again')
                continue

            functions.save_tasks(tasks)
            print(f'{removed_task} complete, good job! It has been removed from your task list.')

        case 'Exit':
            break

        case _:
            print('Please enter a valid number!')
