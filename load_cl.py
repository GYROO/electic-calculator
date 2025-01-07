import math



class value_over_one(Exception):
    pass
class value_lower_zero(Exception):
    pass

message1 = "вычислен"
message2 = "[ok]: "
message3 = "[ ! ] : "
def accuracy(attr):
    return round(attr, 4)

class Load:

    # creates a default obj heap (list) for class Load

    main_heap = []



    def __init__ (self,
                  name='null',
                  is_conv_from_icurrent=True,
                  is_conv_1ph=False,
                  is_conv_linear_1ph=False,
                  is_prior=False,
                  phase=2,
                  voltage=220,
                  count=1,
                  pnominal_by_one=10,
                  pnominal=1,
                  cosu=0.85,
                  tgu=1,
                  ki=0.85,
                  ki_x_pnominal=1,
                  ki_x_pnominal_x_tgu=1,
                  count_x_pnominal_by_one_pow=1,
                  pactive=1,
                  qreacive=1,
                  sfull=1,
                  icurrent =56.97536,
                  icurrent_peak =1,):

                      self.name = name;
                      self.is_conv_from_icurrent = is_conv_from_icurrent;
                      self.is_conv_1ph = is_conv_1ph;
                      self.is_conv_linear_1ph = is_conv_linear_1ph;
                      self.is_prior = is_prior;
                      self.phase = phase;
                      self.voltage = voltage;
                      self.count = count;
                      self.pnominal_by_one = pnominal_by_one;
                      self.pnominal = pnominal;
                      self.ki = ki;
                      self.cosu = cosu;
                      self.tgu = tgu;
                      self.ki_x_pnominal = ki_x_pnominal;
                      self.ki_x_pnominal_x_tgu = ki_x_pnominal_x_tgu;
                      self.count_x_pnominal_by_one_pow = count_x_pnominal_by_one_pow;
                      self.pactive = pactive;
                      self.qreactive = qreacive;
                      self.sfull = sfull;
                      self.icurrent = icurrent
                      self.icurrent_peak = icurrent_peak

                      #add to Load obj heap (list)

                      Load.main_heap.append(self)

    def print_attr(Load):
            print (f"-------------------------{Load.__class__.__name__}--------------------------------\n[01] name: {Load.name};\n[02] is converted from current (bool): {Load.is_conv_from_icurrent};\n[03] is converted from one phase (bool): {Load.is_conv_1ph};\n[04] is converted from linear one phase (bool): {Load.is_conv_linear_1ph};\n[05] is prior (bool): {Load.is_prior};\n[06] current phase (1=L1, 2=L2, 3=L3, 4=L1,L2,L3): {Load.phase};\n[07] voltage of load: {Load.voltage}V;\n[08] count: {Load.count};\n[09] P nominal of one: {Load.pnominal_by_one}kW;\n[10] P nominal of count: {Load.pnominal}kw;\n[11] use coefficient Ki: {Load.ki};\n[12] cos(u): {Load.cosu};\n[13] tan(u): {Load.tgu};\n[14] ki * P nominal of count: {Load.ki_x_pnominal};\n[15] ki * P nominal of count * tan(u): {Load.ki_x_pnominal_x_tgu}; \n[16] count * (P nominal of one)^2 :{Load.count_x_pnominal_by_one_pow},\n[17] P active: {Load.pactive}kW;\n[18] Q reactive: {Load.qreactive}kVAr(s);\n[19] S full: {Load.sfull}kVA; \n[20] I nominal: {Load.icurrent}A;\n[21] I peak: {Load.icurrent_peak}A" )

    def type_pharser(Load):

        if Load.is_conv_linear_1ph == True:
            print(f"приведение линейного однофазного потрибителя {Load.name} к трехфазной мощности: \nувеличение мощности на кор. из трех")
            Load.name = (Load.name+" (лин. 1ф прив. к 3ф)")
            action = lambda: accuracy(Load.pnominal_by_one * math.sqrt(3))
            Load.pnominal_by_one = action()
        elif Load.phase == 1 and Load.is_conv_1ph == False:
            print(f"приведение  наиболее загруженной фазы  А(L1) к трефазному потребителю ")
            action1 = lambda: accuracy(Load.pnominal_by_one * 3)
            Load.name = (Load.name+ "(1ф к 3ф экв)")
            Load.pnominal_by_one  = action1()
        elif Load.phase == 2 and Load.is_conv_1ph == False:
            print(f"приведение  наиболее загруженной фазы  В(L2) к трефазному потребителю ")
            action2 = lambda: accuracy(Load.pnominal_by_one * 3)
            Load.name = (Load.name + "(1ф к 3ф экв)")
            Load.pnominal_by_one = action2()
        elif Load.phase == 3 and Load.is_conv_1ph == False:
            print(f"приведение  наиболее загруженной фазы  C(L3) к трефазному потребителю ")
            action3 = lambda: accuracy(Load.pnominal_by_one * 3)
            Load.name = (Load.name + "(1ф к 3ф экв)")
            Load.pnominal_by_one = action3()
        else:
            pass







    def calc_tgu(Load):
        print("вызов вычисления tg(u)...")
        try:
            if Load.cosu > 1:
                raise value_over_one
            elif Load.cosu < 0:
                raise value_lower_zero
            else:
                action = lambda: accuracy(math.tan(math.acos(Load.cosu)))
                Load.tgu =action()
                print(f"{message1} tg(u) ={Load.tgu} | при cos(u) ={Load.cosu}")
        except value_over_one:
            print(f"{message3} задан cos(u) >1: {Load.cosu}")
        except value_lower_zero:
            print(f"{message3} задан cos(u) <0: {Load.cosu}")

    def calc_cosu(Load):
        print(f"вызов вычисления сos(u)...")
        try:
            if Load.tgu <0:
                 raise value_lower_zero
            else:
                action = lambda: accuracy(math.cos(math.atan(Load.tgu)))
                Load.cosu = action()
                print(f"{message1} cos(u) ={Load.cosu} | при tg(u) = {Load.tgu}")

        except value_lower_zero:
            print(f"задан tg(u)<0: {Load.tgu}")

    def calc_Pnominal (Load):
        print(f"Вызов вычисления Pном(общ.)...")

        try:

            if Load.count <= 0:

                raise value_lower_zero

            elif Load.pnominal_by_one <=0:

                raise value_lower_zero


            else:

                action = lambda: accuracy(Load.count * Load.pnominal_by_one)

                Load.pnominal = action()

                print(f"Расчитан Pном(общ.) ={Load.pnominal} кВт | при  кол-ве {Load.count} и мощности единицы {Load.pnominal_by_one} кВт")

        except value_lower_zero:

            print(f"{message3} получены некорректные данные: {Load.count} или {Load.pnominal} (кВт)--> расчет некорректен")


    def calc_ki_x_Pnominal(Load):

        print(f"Вызов расчета Ki *P(ном)...")

        try:

            if Load.ki >1:

                raise value_over_one

            elif Load.ki < 0:

                raise value_lower_zero

            elif Load.pnominal <0:

                raise value_lower_zero

            else:

                action = lambda: accuracy(Load.ki * Load.pnominal)

                Load.ki_x_pnominal  = action()

                print(f"Вычислен Ki*Pном ={Load.ki_x_pnominal} кВт | при  Ki ={Load.ki} и Pном= {Load.pnominal}")

        except  (value_lower_zero, value_over_one):

            print(f"{message3}  Кi должен быть в рамках 0<Ki <=1 и P(ном) >0, задан Ki={Load.ki}  и P(ном) = {Load.pnominal} кВт ")


    def calc_ki_x_Pnominal_tgu(Load):
         print(f"Вызван расчет Ki * P(ном) * tg(u)...")

         action = lambda: accuracy(Load.ki_x_pnominal * Load.tgu)

         Load.ki_x_pnominal_x_tgu = action()

         print(f"Выполнен расчет Ki * P(ном) * tg(u)= {Load.ki_x_pnominal_x_tgu} кВт | при  Ki * P(ном) ={Load.ki_x_pnominal}кВт и tg(u) ={Load.tgu}")


    def calc_count_x_Pnominal_pow(Load):

        print(f"Вызван расчет n * P(ном) ^2...")

        action = lambda : accuracy(Load.count * math.pow( Load.pnominal_by_one, 2 ))

        Load.count_x_pnominal_by_one_pow = action()

        print(f"Вычислен n * P(ном) ^2 = {Load.count_x_pnominal_by_one_pow} кВт")

    def  calc_Pactive(Load):
        print(f"Вызван расчет активной мощности  {Load.name} P (акт.)... ")

        action = lambda : accuracy (Load.ki*Load.pnominal)

        Load.pactive = action()

        print(f"Вычислена активная мощность для {Load.name} P(акт.) = {Load.pactive} кВт")

    def calc_Qreactive(Load):
        print(f"Вызван расчет рефктивной мощности {Load.name } Q кВАр")

        action = lambda : accuracy(Load.ki_x_pnominal * Load.tgu)

        Load.qreactive = action()

        print(f'Вычислена реактивная мощность для {Load.name} Q кВар = {Load.qreactive}')

    def calc_Sfull(Load):
        print(f"Вызов расчета полной мощности для {Load.name} S. кВА...")

        action = lambda: accuracy(math.sqrt(math.pow(Load.pactive,2)+ math.pow(Load.qreactive,2)))

        Load.sfull = action()

        print(f"Вычислена полная мощность для {Load.name} S кВА = {Load.sfull}")

    def calc_I(Load):
        print(f"Вызван Расчет токовой нагрузки I, А для {Load.name}....")
        if Load.phase == 4:
            print(f"{Load.name} - на линейном напряжении")
            action1 = lambda: accuracy( Load.sfull / (math.sqrt(3) * (Load.voltage* 0.001 )))
            Load.icurrent = action1()
        else:
            print(f"{Load.name} - на фазном напряжении, фаза: {Load.phase}")
            action2 = lambda: accuracy(Load.sfull / (Load.voltage * 0.001))
            Load.icurrent = action2()



        print(f"Рассчитана токовая нагрузка для {Load.name}  I(расч), А = {Load.icurrent}")

    def calc_Ipeak(Load):
        if Load.ki  <= 0:
            pass
        else:
            action = lambda : Load.icurrent / Load.ki
            Load.icurrent_peak = action()

    def calc_power_method(Load):
       print(f' ---Запуск процедуры вычилсений от мощности для {Load.name}---')
       #Load.type_pharser()
       Load.calc_tgu()
       Load.calc_Pnominal()
       Load.calc_ki_x_Pnominal()
       Load.calc_ki_x_Pnominal_tgu()
       Load.calc_count_x_Pnominal_pow()
       Load.calc_Pactive()
       Load.calc_Qreactive()
       Load.calc_Sfull()
       Load.calc_I()
       Load.calc_Ipeak()
       print(f"[ok]: расчет завершен----------------------------------")

    def calc_S_from_current(Load):
        print(f"вызов метода расчета S от тока")
        if Load.is_conv_from_icurrent == True:
            print("[ok] параметр расчета от така получен")
            if Load.phase == 4:
                action4 = lambda : (Load.voltage * 0.001) * math.sqrt(3)
                temp4 = action4()
                Load.sfull = (Load.icurrent * temp4)
            elif Load.phase == 1:
                action1 = lambda : (Load.voltage * 0.001)
                temp1 = action1()
                Load.sfull = (Load.icurrent* temp1)
            elif Load.phase == 2:
                action2 = lambda: (Load.voltage * 0.001)
                temp2 = action2()
                Load.sfull = (Load.icurrent * temp2)
            elif Load.phase == 3:
                action3 = lambda: (Load.voltage * 0.001)
                temp3 = action3()
                Load.sfull = (Load.icurrent * temp3)
            else:
                print(f"ошибка значения фазы : {Load.phase} ")

        else:
            print(f"Вызов не имеет требуемого параметра")
            pass

    def сalc_pactive_from_current(Load):
           print(f"Расчет активной мощности отталкиваясь от коэффициентов нагрузки")
           action = lambda : accuracy(Load.sfull * Load.cosu)
           Load.pactive = action()
           print(f"общая активная мощность P акт ={Load.pactive}")

    def calc_qreactive_from_current(Load):
        print(f"Расчет реактивной мощности отталкиваясь от коэффициентов нагрузки")
        action = lambda: accuracy(Load.pactive * Load.tgu)
        Load.qreactive = action()
        print(f"общая активная мощность P акт ={Load.qreactive}")

    def calc_pnominal_from_current(Load):
        print(f"Расчет активной номинальной мощности отталкиваясь от коэффициента использования")
        if Load.ki > 0:
            action = lambda: accuracy(Load.pactive / Load.ki)
            Load.pnominal = action()
            print(f"общая активная мощность без учета коэфф исп. P ном ={Load.pnominal}")
        else:
            pass

    def  calc_pnominal_by_one_from_current(Load):
        print(f"Расчет активной единичной мощности отталкиваясь от числа потребителей")
        if Load.count > 0:
            action  = lambda: accuracy(Load.pnominal / Load.count)
            Load.pnominal_by_one = action()
            print(f"активная мощность eдиницы ={Load.pnominal_by_one}")
        else:
            pass



    def calc_current_method(Load):
           Load.calc_tgu()
           Load.calc_S_from_current()
           Load.сalc_pactive_from_current()
           Load.calc_qreactive_from_current()
           Load.calc_pnominal_from_current()
           Load.calc_pnominal_by_one_from_current()
           Load.calc_count_x_Pnominal_pow()
           Load.is_conv_from_icurrent = True



    def sort_by_phase(Load):
        print('Вызов сортировки потребителей и распределения по фазам')

        L1  = [loads for loads in Load.main_heap if Load.phase == 1]

        L2 =  [loads for loads in Load.main_heap if Load.phase == 2]

        L3 =  [loads for loads in Load.main_heap if Load.phase == 3]

        L123 =  [loads for loads in Load.main_heap if Load.phase == 4]

        L1max_i = sum(Load.icurrent for Load in L1)

        L2max_i = sum(Load.icurrent for Load in L2)

        L3max_i = sum(Load.icurrent for Load in L3)

        L123max_i =  sum(Load.icurrent for Load in L123)

        load_sorted = [L1, L2, L3, L123]

        load_phase_max = [L1max_i, L2max_i, L3max_i, L123max_i]

        group = load_sorted

        return load_sorted, load_phase_max


def find_peak_phase(iter_obj):

        temp = iter_obj [1]
        temp1 = [temp [0] , temp [1], temp [2]]
        maximum = max([val for val in temp1])

        minimum = min([val for val in temp1])
        diff = maximum - minimum

        if minimum  == 0:
            if       maximum == temp1 [0]:
                percent = 'L1'
            elif    maximum == temp1 [1]:
                percent = 'L2'
            elif    maximum == temp1[2]:
                percent = 'L3'

        else:
            percent = (diff / minimum)* 100

        if maximum == 0:
            return 4, None
        elif maximum == temp1 [0]:
            return 1, percent
        elif maximum == temp1 [1]:
            return 2, percent
        elif maximum == temp1 [2]:
            return 3, percent


def phase_accumulate(load_sorted, set):
    if set == 1:
       phase = load_sorted[0] [0]
       phasemax =  load_sorted[1] [0]
       name = 'L1'
    elif set == 2:
        phase =load_sorted[0] [1]
        phasemax = load_sorted[1][1]
        name = 'L2'
    elif set == 3:
        phase = load_sorted[0][2]
        phasemax = load_sorted[1][2]
        name = 'L3'
    if phasemax ==0:
        return None


    accumulate_pnominal_phase =  sum(Load.pnominal for Load in phase)
    accumulate_ki_x_pnominal_phase = sum(Load.ki_x_pnominal for Load in phase)
    accumulate_ki_x_pnominal_tgu_phase = sum(Load.ki_x_pnominal_x_tgu for Load in phase)
    accumulate_count_x_pnominal_by_one_pow_phase = accuracy(math.pow(accumulate_pnominal_phase, 2))
    temp = accuracy(math.pow(accumulate_ki_x_pnominal_tgu_phase, 2) + math.pow(accumulate_ki_x_pnominal_phase, 2))
    accumulate_S_full_phase = accuracy(math.sqrt(temp))

    if accumulate_S_full_phase <= 0:
        pass
    else:
        accumulate_cosu_phase = accuracy(accumulate_ki_x_pnominal_phase / accumulate_S_full_phase)

    if accumulate_pnominal_phase == 0:
        accumulate_ki_phase = 0
    else:
        accumulate_ki_phase = accuracy((accumulate_ki_x_pnominal_phase/ accumulate_pnominal_phase))

    accumulate_tgu_phase  =accuracy (math.tan(math.acos(accumulate_cosu_phase)))

    if phasemax <=0:
        pass
    else:
        accumulate_voltage_phase = int(accuracy(accumulate_S_full_phase / phasemax) * 1000)

    if accumulate_ki_phase <= 0:
        pass
    else:
        accumulate_I_peak_phase = phasemax / accumulate_ki_phase

    ph_par_set =\
        {'name': name,
        'is_conv_1ph': False,
        'is_conv_linear_1ph': False,
        'is_prior': False,
        'phase':set,
        'voltage':accumulate_voltage_phase,
        'count': 1,
        'pnominal_by_one': accumulate_pnominal_phase,
        'pnominal': accumulate_pnominal_phase,
        'cosu': accumulate_cosu_phase,
        'tgu': accumulate_tgu_phase,
        'ki': accumulate_ki_phase,
        'ki_x_pnominal': accumulate_ki_x_pnominal_phase,
        'ki_x_pnominal_x_tgu': accumulate_ki_x_pnominal_tgu_phase,
        'count_x_pnominal_by_one_pow':accumulate_count_x_pnominal_by_one_pow_phase,
        'pactive': accumulate_ki_x_pnominal_phase,
        'qreacive': accumulate_ki_x_pnominal_tgu_phase,
        'sfull':accumulate_S_full_phase,
        'icurrent': phasemax,
        'icurrent_peak':  accumulate_I_peak_phase, }

    return ph_par_set

def phaseobj_creator(ph_par_set):
    ph_par_set ['name'] =\
        Load ( ph_par_set ['name'],
#
        )



test = Load()
test2 = Load()
test.print_attr()
test2.calc_power_method()
test.calc_power_method()
test.print_attr()
test.calc_current_method()
test.print_attr()
sorted_heap = test.sort_by_phase()
print(sorted_heap[0] [0])
peak_phase = find_peak_phase(sorted_heap)
print(peak_phase)
phase_one =phase_accumulate(sorted_heap,2)
print(phase_one)


