message = "quick brown fox jumps over the lazy dog"
newSet= set(message)      # {'u', 'e', 's', 'a', 'Q', 'j', 'x', 'o', 'l', 'b', 'd', ' ', 'f', 'z', 'r', 'y', 'g', 'i', 'h', 't', 'w', 'p', 'c', 'v', 'n', 'k', 'm'}
print((sorted(newSet)))
newSet = sorted(newSet)   # [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
message1 = ""
for i in newSet:
  message1+=i
print(message1.strip())   # use to remove space