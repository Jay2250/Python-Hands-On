# To-Do list
my_todoList = []
choice = 1
while choice == 1:
 x = int(input("Enter Choice What Do You Want To Perform? \n1. Add Task to the List \n2. Remove Task from the List \n3. View the List "))
 if x == 1:
    addTask = str(input("Input the task to be added "))
    my_todoList.append(addTask)
    print("Task added successfully \nNew Updated List is ")
    print(my_todoList)
 elif x == 2 :
    removeTask = str(input("Input the task to be removed "))
    my_todoList.remove(removeTask)
    print("Task deleted successfully \nNew Updated List is ")
    print(my_todoList)
 elif x == 3:
    print(my_todoList)
 else:
  print("Enter Valid choice...")
 choice = int(input("Want to continue \n1. Yes    2.Exit"))