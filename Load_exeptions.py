import load_cl

message_1 = ' --> cannot calculate correctly'
message_2 = 'unable to set :'

class wrong_input(Exception):
    pass
##ddjkf

def is_number(input_obj):
    try:
        float(input_obj)
        return True
    except ValueError:
        return False

def verify_input(input_obj):

    if is_number(input_obj) == True:
        
        if int(input_obj) <=0:
            raise wrong_input
            
    elif input_obj == 'quit':
        
        exit()
        
    return input_obj        
    
inputs = {"name": "none"};

def input_name ():
    print ("enter a name of load, or type \'quit\' to end:")
    name = (input( )).strip()
    try:
        verify_input(name)
    except wrong_input:
        print (f"{message_2}{name}{message_1}")
        input_name()
    inputs["name"]  = name
    return inputs
    
input_name()     
print (inputs["name"])
