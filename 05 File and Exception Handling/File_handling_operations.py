with open("C:\\Users\\DAI.STUDENTSDC\\Desktop\\document.rtf",'r') as file:
    content = file.read()
   # print(content)
    global update_content
    update_content= content.replace("After", "Before")
    print(update_content)
    #file.write(update_content)
with open("C:\\Users\\DAI.STUDENTSDC\\Desktop\\document.rtf", 'w') as file:
    file.write(update_content)

