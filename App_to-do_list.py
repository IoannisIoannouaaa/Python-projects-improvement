tasks = []
def add_task(tasks):
    while True:
        task = input('What is your task?').strip().title()
        if task:
            break
        print('Please enter a valid task!')
    tasks.append(task)
    
def view_tasks(tasks):
    if not tasks:
        print('No tasks in your list')
    else:
        print('\nYour tasks:')
        for index, task in enumerate(tasks, start = 1):
            print(f"{index}. {task}")
def remove_tasks(tasks):
    if not tasks:
        print('There are no tasks to remove')
        return
    index_str = input('Which task would you like to remove?(enter the number of the task)')
    if not index_str.isdigit():
        print('Please enter a number!')
    
    index_q = int(index_str)
    if index_q < 1 or index_q > len(tasks):
        print('Invalid task number!')
        return
    removed_task = tasks.pop(index_q - 1)
    print('Removed tasks:',removed_task )
            
                        
def main():
    while True:
        print('To-do list menu:')
        print('Option 1: Add a task')
        print('Option 2: View tasks')
        print('Option 3 : Exit')
        print('Option 4 : Remove a task')
        
        option = input('Pick 1 2 3 or 4').strip()
        
        if option == '1':
            add_task(tasks)
            
        elif option == '2':
            view_tasks(tasks)
                        
        elif option == '3':
            print('See you next time!')
            break
        
        elif option == '4':
            remove_tasks(tasks)
            
        else:
            print('Please enter a valid choice')
            
            
main()
        