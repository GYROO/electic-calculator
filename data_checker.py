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

class pnominal_by_one_value_err(Exception):
    pass

class pnominal_value_err(Exception):
    pass

class cosu_value_err(Exception):
    pass

class tgu_value_err(Exception):
    pass

class ki_value_err(Exception):
    pass

class ki_x_pnominal_value_err(Exception):
    pass
class  ki_x_pnominal_x_tgu_value_err(Exception):
    pass

class count_x_pnominal_by_one_pow_value_err(Exception):
    pass

class pactive_value_err(Exception):
    pass

class qreactive_value_err(Exception):
    pass

class sfull_value_err(Exception):
    pass

class icurrent_value_err(Exception):
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
          'voltage': 380,
          'count': 6,
          'pnominal_by_one': 1,
          'pnominal': 1,
          'cosu': 1,
          'tgu': 1,
          'ki':1,
          'ki_x_pnominal': 1,
          'ki_x_pnominal_x_tgu': 1,
          'count_x_pnominal_by_one_pow': 2,
          'pactive': 10,
          'qreacive': 10,
          'sfull': 11,
          'icurrent': 15
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
    else:
        print("[ok]")

def pnominal_by_one_checker(inputs):
    print(f"обработка значения мощности на единицу нагрузки...")
    void_data_pharser(inputs['pnominal_by_one'])
    number_pharser(inputs['pnominal_by_one'])
    if inputs['pnominal_by_one'] <= 0:
        raise pnominal_by_one_value_err
    else:
        print("[ok]")

def pnominal_checker(inputs):
    print(f'обработка значения общей активной мощности')
    void_data_pharser(inputs['pnominal'])
    number_pharser(inputs['pnominal'])
    if inputs['pnominal'] <= 0:
        raise pnominal_value_err
    else:
        print("[ok]")

def cosu_checker(inputs):
    print(f"обработка значения cos(u)")
    void_data_pharser(inputs['cosu'])
    number_pharser(inputs['cosu'])
    if inputs['cosu'] <= 0:
        raise cosu_value_err
    elif  inputs['cosu'] > 1:
        raise cosu_value_err
    else:
        print("[ok]")

def tgu_checker(inputs):
    print(f"обработка значения tg(u)")
    void_data_pharser(inputs['tgu'])
    number_pharser(inputs['tgu'])
    if inputs['tgu'] <= 0:
        raise tgu_value_err
    else:
        print("[ok]")

def ki_checker(inputs):
    print(f"обработка значения ki (коэфф.  исп)...")
    void_data_pharser(inputs['ki'])
    number_pharser(inputs['ki'])
    if  inputs['ki'] <= 0:
        raise ki_value_err
    elif  inputs['ki'] >1:
        raise ki_value_err
    else:
        print("[ok]")

def ki_x_pnominal_checker(inputs):
    print(f"обработка значения Kи * Рном...")
    void_data_pharser(inputs['ki_x_pnominal'])
    number_pharser(inputs['ki_x_pnominal'])
    if inputs['ki_x_pnominal'] < 0:
        raise ki_x_pnominal_value_err
    elif inputs['ki_x_pnominal'] > inputs['pnominal'] :
        raise ki_x_pnominal_value_err
    else:
        print("[ok]")

def ki_x_pnominal_x_tgu_checker(inputs):
    print(f"обработка значения Kи * Рном. *tg(u) ..")
    void_data_pharser(inputs['ki_x_pnominal_x_tgu'])
    number_pharser(inputs['ki_x_pnominal_x_tgu'])
    if inputs['ki_x_pnominal_x_tgu'] <= 0:
        raise ki_x_pnominal_x_tgu_value_err
    else:
        print("[ok]")

def  count_x_pnominal_by_one_pow_checker(inputs):
    print(f"обработка значения n * рном(единиц)^2  ..")
    void_data_pharser(inputs['count_x_pnominal_by_one_pow'])
    number_pharser(inputs['count_x_pnominal_by_one_pow'])
    if inputs['count_x_pnominal_by_one_pow'] <= 0:
        raise count_x_pnominal_by_one_pow_value_err
    elif inputs['count_x_pnominal_by_one_pow'] < inputs['pnominal_by_one']:
        raise count_x_pnominal_by_one_pow_value_err
    else:
        print("[ok]")

def pactive_checker(inputs):
    print(f"обработка значения P(акт.)  ..")
    void_data_pharser(inputs['pactive'])
    number_pharser(inputs['pactive'])
    if inputs['pactive'] <= 0:
        raise pactive_value_err
    else:
        print("[ok]")

def qreactive_checker(inputs):
    print(f"обработка значения Q(реакт.)  ..")
    void_data_pharser(inputs['qreacive'])
    number_pharser(inputs['qreacive'])
    if inputs['qreacive'] <= 0:
        raise qreactive_value_err
    else:
        print("[ok]")

def sfull_checker(inputs):
    print(f"обработка значения S(полн.)  ..")
    void_data_pharser(inputs['sfull'])
    number_pharser(inputs['sfull'])
    if inputs['sfull'] <= 0:
        raise sfull_value_err
    else:
        print("[ok]")

def icurrent_checker(inputs):
    print(f"обработка значения I(ток)  ..")
    void_data_pharser(inputs['icurrent'])
    number_pharser(inputs['icurrent'])
    if inputs['icurrent'] <=0:
        raise icurrent_value_err
    else:
        print("[ok]")

def loadcl_full_check(inputs):
    print(f"сканирование всех значений нагрузки...")
    name_pharser(inputs)
    bool_checker(inputs)
    phase_checker(inputs)
    voltage_checker(inputs)
    count_checker(inputs)
    pnominal_by_one_checker(inputs)
    pnominal_checker(inputs)
    cosu_checker(inputs)
    tgu_checker(inputs)
    ki_checker(inputs)
    ki_x_pnominal_checker(inputs)
    ki_x_pnominal_x_tgu_checker(inputs)
    count_x_pnominal_by_one_pow_checker(inputs)
    pactive_checker(inputs)
    qreactive_checker(inputs)
    sfull_checker(inputs)
    icurrent_checker(inputs)
    print(f"---------------завершено успешно--------------")

loadcl_full_check(inputs)
