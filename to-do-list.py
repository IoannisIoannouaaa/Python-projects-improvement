task_list = []
def get_task():
    while True:
        task = input('What is your task?')
        if task:
            return task
        else:
            print('Please enter a valid task!')
            
            
def main():
    to_do =  int(input('How many tasks do you have?'))
    for i in range(to_do):
        task = get_task
        task_list.append(i)
    for index,  tasks in enumerate(task_list, start = 1):
        print(index, task)
        
main()
    







    
    

