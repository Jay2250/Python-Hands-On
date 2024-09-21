dict1 = {0: 10, 1: 43, 2: 20, 3: 21}
print(min(dict1))  # Gives minimum from keys

#-----------------------------------------------------------

dict1 = {chr(i): chr(i+13) for i in range(ord('a'), ord('z')+1)}
print(dict1)

#-----------------------------------------------------------

# Create the dictionary
my_dict = {chr(i): chr(i + 13) for i in range(ord('a'), ord('z') + 1)}

# Print the dictionary
for key in my_dict:
    print(f"{key}: {my_dict[key]}")

#-----------------------------------------------------------

# print(ord('z'))
my_dict = {}
for i in range(ord('a'), ord('z') + 1):
    if i+13 <= 122:
        my_dict = {chr(i): chr(i + 13)}
print(my_dict)

#-----------------------------------------------------------

# message coding

my_dict = {
    'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r',
    'f': 's', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'w',
    'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b',
    'p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g',
    'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l',
    'z': 'm',
    'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R',
    'F': 'S', 'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W',
    'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A', 'O': 'B',
    'P': 'C', 'Q': 'D', 'R': 'E', 'S': 'F', 'T': 'G',
    'U': 'H', 'V': 'I', 'W': 'J', 'X': 'K', 'Y': 'L',
    'Z': 'M'
}
# print(my_dict)

message1 = "Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"

message2 = ""
for char in message1:
    if char in my_dict:
        message2 += my_dict[char]
    else:
        message2 += char

print(message2)

#-----------------------------------------------------------
message1 = '''Qrne Tx
KLM V pna’g funxr gur zrzbevrf bs hf. Rirel ynhtu, rirel dhvrg zbzrag, yvatref va zl urneg yvxr n ornhgvshy npur.
 Ybfvat lbh srryf yvxr ybfvat n cneg bs zlfrys, n ibvq gung abguvat pna svyy. V bsgra svaq zlfrys jvfuvat V pbhyq ghea
  onpx gvzr, gb ubyq lbh pybfr naq gryy lbh whfg ubj zhpu lbh zrna gb zr. Lbh jrer zl yvtug, naq jvgubhg lbh, rirelguvat
   srryf qvzzre. V erterg gur zbzragf V gbbx sbe tenagrq, gur gvzrf V qvqa’g nccerpvngr lbh rabhtu.

Lbh qrfreir nyy gur unccvarff va gur jbeyq, rira vs vg’f abg jvgu zr. Whfg xabj, lbh ner qrrcyl ybirq naq zvffrq.

Sberire va zl urneg,
[Lbhef WP]
'''
message2 = ""
for char in message1:
    if char in my_dict:
        message2 += my_dict[char]
    else:
        message2 += char

print(message2)

#-------------------------------------------------------------

dict1 = {'Arman': 'Blue', 'Lisa': 'Yellow', 'Vinod': 'Purple', 'Jenny': 'Pink'}
# total numbers of students in list
print(len(dict1))

# changing lisa's favourite colour
dict1['Lisa'] = 'Red'
print(dict1)

# remove jenny
# dict.pop('Jenny')
del dict1['Jenny']
print(dict1)

# Sort list using name
sorted_dict = dict(sorted(dict1.items()))
print(sorted_dict)
