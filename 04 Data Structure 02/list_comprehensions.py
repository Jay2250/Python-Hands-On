#dictionary comprehension
messageList = input("Enter the message : ").split(" ")
print(messageList)
messageDict = {i: len(i) for i in messageList}

print(messageDict)