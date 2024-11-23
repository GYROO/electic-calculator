class void_data_err(Exception):
    pass

class  value_not_bool_err(Exception):
    pass

class phase_value_err(Exception):
    pass

class value_not_number_err(Exception):
    pass
class voltage_value_err(Exception):
    pass
class value_not_integer(Exception):
    pass

class count_value_err(Exception):
    pass
def do_some(obj):
    pass

def is_number(input_obj):
    try:
        float(input_obj)
        return True
    except ValueError:
        return False

inputs = {'name': 'd',
          'is_conv_from_icurrent':  False,
          'is_conv_1ph':False,
          'is_conv_linear_1ph': False,
          'is_prior': False,
          'phase': 3,
          'voltage':380,
          'count': 6,

          }

def void_data(obj):
    test = str(obj)
    if len(test) == 0:
        return True
    elif test == None:
        return True
    else:
        return False

def void_data_pharser(obj):
      test = void_data(obj)
      if test == False:
          pass
      else:
          raise void_data_err


def number_pharser(obj):
    test = is_number(obj)
    if test  == True:
        pass
    else:
        raise value_not_number_err
def name_pharser(inputs):

    print(f'обработка имени...')
    void_data_pharser(inputs["name"])
    data_upd_step1= str(inputs['name'])
    data_upd_step2 = data_upd_step1.strip()
    inputs['name'] = data_upd_step2
    print(f'[ok]')

def bool_pharser(obj):
    print(f'обработка булевых значений...')
    void_data_pharser(obj)
    test = obj
    test = str(test)
    if test == "True":
        print('[ok]')
    elif test == "False":
        print('[ok]')
    else:
              raise value_not_bool_err

def bool_checker(inputs):
    bool_pharser(inputs['is_conv_from_icurrent'])
    bool_pharser(inputs['is_conv_1ph'])
    bool_pharser(inputs['is_conv_linear_1ph'])
    bool_pharser(inputs['is_prior'])


def phase_checker(inputs):
    print("проверка фазности...")
    void_data_pharser(inputs['phase'])
    number_pharser(inputs['phase'])
    test = int(inputs['phase'])
    if test == 0:
        print('[ok]')
    elif test ==1:
        print('[ok]')
    elif test ==2:
        print('[ok]')
    elif test ==3:
        print('[ok]')
    elif test == 4:
        print('[ok]')
    else:
        raise phase_value_err

def voltage_checker(inputs):
    print("обработка значений напряжения...")
    void_data_pharser(inputs['voltage'])
    number_pharser(inputs['voltage'])
    test = int (inputs['voltage'])
    if test <= 0:
        raise voltage_value_err
    else:
        print("[ok]")

def equals_integer(obj):
    test = obj
    test = int (obj)
    if test == obj:
        pass
    else:
        raise value_not_integer
def count_checker(inputs):
    print(f'обработка значения количества...')
    void_data_pharser(inputs['count'])
    number_pharser(inputs['count'])
    equals_integer(inputs['count'])
    if inputs['count'] <= 0:
        raise count_value_err





name_pharser(inputs)
bool_checker(inputs)
phase_checker(inputs)
voltage_checker(inputs)
count_checker(inputs)


