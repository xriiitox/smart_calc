
response=['Welcome to smart calculator','My name is Calc',
          'Thanks for using me!','Sorry, this is beyond my ability']

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def mod(a,b):
    return a%b

def lcm(a,b):
    L=a if a>b else b
    while L<=a*b:
        if l%a == 0 and L%b==0:
            return L
        L += 1

def hcf(a, b):
    H=a if a<b else b
    while H>=1:
        if a%H==0 and b%H==0:
            return H
        H-=1
        
def extract_from_text(text):
    l=[]
    
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
        
    return l

def myname():
    print(response[1])
    
def end():
    print(response[2])
    input('press enter to exit')
    exit()

operations = {
    "ADD":add,
    "PLUS": add,
    "SUM": add,
    "ADDITION": add,
    "SUB": sub,
    "SUBTRACT": sub,
    "MINUS": sub,
    "DIFFERENCE": sub,
    "LCM": lcm,
    "HCF": hcf,
    "PRODUCT": mul,
    "MULTIPLY": mul,
    "MULTIPLICATION": mul,
    "DIVIDE": div,
    "DIVISION": div,
    "MODULO": mod,
    "MOD": mod,
    "REMAINDER": mod,
    "MODULUS": mod
}

commands = {
    'NAME': myname,
    'EXIT': end,
    'END': end,
    'CLOSE': end,
}

print(response[0])
print(response[1])

while True:
    text = input('enter your queries: ')
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l = extract_from_text(text)
                r = operations[word.upper()] (l[0], l[1])
                print(r)
            except:
                print("something went wrong, please enter again!")
            finally:
                break
        elif word.upper() in commands.keys():
            commands[word.upper()]()
            break
    else:
        print(response[3])