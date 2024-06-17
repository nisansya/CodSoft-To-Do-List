def add_task(tasks_list):
    td=input("enter task you want to add:")
    tasks_list.append(td)
    print(f"task {td} has been successfully added")
def del_task(tasks_list):
    td=input("enter task you want to delete:")
    tasks_list.remove(td)
    print(f"task {td} has been successfully deleted")
def view_task(tasks_list):
    print("total tasks= ",tasks_list)
def update_task(tasks_list):
    up_task=input("enter task name you want to update:")
    new_task=input("enter new task:")
    for i in range(0,len(tasks_list)):
        if tasks_list[i]==up_task:
            tasks_list[i]=new_task
    print(f"updated task = {new_task}")
print("------walcome to task management app------")
nu_task=int(input("enter how many tasks you want to add:"))
tasks_list=[]
for i in range(1,nu_task+1):
    task=input(f"enter task {i}=")
    tasks_list.append(task)
print(f"today tasks are: {tasks_list}")
while(1):
    print("enter \n1 - add\n2 - update\n3 - delete\n4 - view\n5 - exit")
    choice=int(input())
    if choice==1:
        add_task(tasks_list)
    elif choice==2:
        update_task(tasks_list)
    elif choice==3:
        del_task(tasks_list)
    elif choice==4:
        view_task(tasks_list)
    elif choice==5:
        exit()
    else:
        print("you entered a wrong choice")
