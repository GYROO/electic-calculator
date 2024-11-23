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
    def __init__ (self,
                  name='null',
                  is_conv_from_icurrent=False,
                  is_conv_1ph=False,
                  is_conv_linear_1ph=False,
                  is_prior=False,
                  phase=1,
                  voltage=380,
                  count=3,
                  pnominal_by_one=10,
                  pnominal=1,
                  cosu=0.95,
                  tgu=1,
                  ki=1,
                  ki_x_pnominal=1,
                  ki_x_pnominal_x_tgu=1,
                  count_x_pnominal_by_one_pow=1,
                  pactive=1,
                  qreacive=1,
                  sfull=1,
                  icurrent =56.97536,):

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

    def print_attr(Load):
            print (f"-------------------------{Load.__class__.__name__}--------------------------------\n[01] name: {Load.name};\n[02] is converted from current (bool): {Load.is_conv_from_icurrent};\n[03] is converted from one phase (bool): {Load.is_conv_1ph};\n[04] is converted from linear one phase (bool): {Load.is_conv_linear_1ph};\n[05] is prior (bool): {Load.is_prior};\n[06] current phase (1=L1, 2=L2, 3=L3, 4=L1,L2,L3): {Load.phase};\n[07] voltage of load: {Load.voltage}V;\n[08] count: {Load.count};\n[09] P nominal of one: {Load.pnominal_by_one}kW;\n[10] P nominal of count: {Load.pnominal}kw;\n[11] use coefficient Ki: {Load.ki};\n[12] cos(u): {Load.cosu};\n[13] tan(u): {Load.tgu};\n[14] ki * P nominal of count: {Load.ki_x_pnominal};\n[15] ki * P nominal of count * tan(u): {Load.ki_x_pnominal_x_tgu}; \n[16] count * (P nominal of one)^2 :{Load.count_x_pnominal_by_one_pow},\n[17] P active: {Load.pactive}kW;\n[18] Q reactive: {Load.qreactive}kVAr(s);\n[19] S full: {Load.sfull}kVA; \n[20] I nominal: {Load.icurrent}A;" )

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

        action = lambda : accuracy( Load.sfull / (math.sqrt(3) * (Load.voltage* 0.001 )))

        Load.icurrent=action()

        print(f"Рассчитана токовая нагрузка для {Load.name}  I(расч), А = {Load.icurrent}")


    def calc_power_method(Load):
       print(f' ---Запуск процедуры вычилсений от мощности для {Load.name}---')
       Load.calc_tgu()
       Load.calc_Pnominal()
       Load.calc_ki_x_Pnominal()
       Load.calc_ki_x_Pnominal_tgu()
       Load.calc_count_x_Pnominal_pow()
       Load.calc_Pactive()
       Load.calc_Qreactive()
       Load.calc_Sfull()
       Load.calc_I()
       print(f"[ok]: расчет завершен----------------------------------")

















            
test = Load()
test.print_attr()
test.calc_power_method()
test.print_attr()
