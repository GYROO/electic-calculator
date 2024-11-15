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
                  ki=0.5,
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
test = Load()
test.print_attr()
test.calc_tgu()
test.calc_cosu()