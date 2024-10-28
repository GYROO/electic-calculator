import math

class Load:
    def __init__ (self, 
                  load_name ='null',
                  load_is_conv_from_icurrent = False,
                  load_is_conv_1ph = False,
                  load_is_conv_linear_1ph = False,
                  load_is_prior = False,
                  load_phase = 1,
                  load_voltage =380,
                  load_count = 3,
                  load_pnominal_by_one = 10,
                  load_pnominal = 1,
                  load_cosu = 0.8,
                  load_tgu = 1,
                  load_ki = 0.5,
                  load_ki_x_pnominal = 1,
                  load_ki_x_pnominal_x_tgu = 1,
                  load_count_x_pnominal_by_one_pow = 1,
                  load_pactive = 1,
                  load_qreacive = 1,
                  load_sfull = 1,
                  load_icurrent = 56.97536,):

                      self.name = load_name;
                      self.is_conv_from_icurrent = load_is_conv_from_icurrent;
                      self.is_conv_1ph = load_is_conv_1ph;
                      self.is_conv_linear_1ph = load_is_conv_linear_1ph;
                      self.is_prior = load_is_prior;
                      self.phase = load_phase;
                      self.voltage = load_voltage;
                      self.count = load_count;
                      self.pnominal_by_one = load_pnominal_by_one;
                      self.pnominal = load_pnominal;
                      self.ki = load_ki;
                      self.cosu = load_cosu;
                      self.tgu = load_tgu;
                      self.ki_x_pnominal = load_ki_x_pnominal;
                      self.ki_x_pnominal_x_tgu = load_ki_x_pnominal_x_tgu;
                      self.count_x_pnominal_by_one_pow = load_count_x_pnominal_by_one_pow;
                      self.pactive = load_pactive;
                      self.qreactive = load_qreacive;
                      self.sfull = load_sfull;
                      self.icurrent = load_icurrent

def print_load_attr(Load):
        print (f"-------------------------{Load.__class__.__name__}--------------------------------\n[01] name: {Load.name};\n[02] is converted from current (bool): {Load.is_conv_from_icurrent};\n[03] is converted from one phase (bool): {Load.is_conv_1ph};\n[04] is converted from linear one phase (bool): {Load.is_conv_linear_1ph};\n[05] is prior (bool): {Load.is_prior};\n[06] current phase (1=L1, 2=L2, 3=L3, 4=L1,L2,L3): {Load.phase};\n[07] voltage of load: {Load.voltage}V;\n[08] count: {Load.count};\n[09] P nominal of one: {Load.pnominal_by_one}kW;\n[10] P nominal of count: {Load.pnominal}kw;\n[11] use coefficient Ki: {Load.ki};\n[12] cos(u): {Load.cosu};\n[13] tan(u): {Load.tgu};\n[14] ki * P nominal of count: {Load.ki_x_pnominal};\n[15] ki * P nominal of count * tan(u): {Load.ki_x_pnominal_x_tgu}; \n[16] count * (P nominal of one)^2 :{Load.count_x_pnominal_by_one_pow},\n[17] P active: {Load.pactive}kW;\n[18] Q reactive: {Load.qreactive}kVAr(s);\n[19] S full: {Load.sfull}kVA; \n[20] I nominal: {Load.icurrent}A;" )


def accuracy(attr):
        return round(attr, 2)

def calc_tgu(Load):
        print (f"calculating tan(u)...")

        if Load.cosu == 0:
            print ('incorrect cosu = 0, cannot calculate correctly')
        Load.tgu = accuracy ( math.tan(math.acos(Load.cosu)) )
        print (f"[ok] tan(u): {Load.tgu}")

def calc_pnominal (Load):
        print (f"calculating P nominal of count...")

        if Load.pnominal_by_one == 0:
            print ('incorrect P nominal = 0, cannot calculate correctly')
            
        elif Load.count == 0:
            print ('incorrect count = 0, cannot calculate correctly')
        Load.pnominal = accuracy (Load.pnominal_by_one * Load.count)
        
        print (f"[ok] P nominal of count: {Load.pnominal}kW")
        
def calc_ki_x_pnominal(Load):
        print (f"calculating ki * P nominal of count...")
        
        if Load.ki == 0:
            print ('incorrect ki = 0, cannot calculate correctly')
        elif Load.ki >1:
            print ('incorrect ki > 1, cannot calculate correctly')
        Load.ki_x_pnominal = accuracy (Load.pnominal * Load.ki)
        
        print (f"[ok] ki * P nominal of count: {Load.ki_x_pnominal}kW")
            
def calc_ki_x_pnominal_x_tgu(Load):
        print (f"calculating ki * P nominal of count * tan(u) ...")
        
        if Load.ki == 0:
            print ('incorrect ki = 0, cannot calculate correctly')
            
        elif Load.ki >1:
            print ('incorrect ki > 1, cannot calculate correctly')
            
        elif Load.pnominal == 0:
            print('incorrect Pnominal = 0, cannot calculate correctly')
            
        elif Load.tgu >=1:
            print ('incorrect tgu >=1, cannot calculate correcly, check cosu')
            
        Load.ki_x_pnominal_x_tgu = accuracy(Load.ki_x_pnominal * Load.tgu)
        
        print (f"[ok] ki * P nominal of count * tan(u): {Load.ki_x_pnominal_x_tgu}kW")
        
                
        
def calc_count_x_pnominal_by_one_pow(Load):
        print (f"calculating count * (P nominal of one)^2 ...") 
    
        if Load.count ==0:
            print ('incorrect count of loads, cannot calculate correctly')
            
        elif Load.pnominal == 0:
            print ('incorrect Pnominal = 0, cannot calculate correctly')
            
        temp = math.pow(Load.pnominal_by_one,2)
        Load.count_x_pnominal_by_one_pow = accuracy (Load.count * temp)
        
        print (f"[ok] count * (P nominal of one)^2: {Load.count_x_pnominal_by_one_pow}kW")
        
        
            
def calc_pactive(Load):
        print(f"calculating P active...")
        
        Load.pactive = accuracy (Load.pnominal)
        
        print (f"[ok] P active: {Load.pactive}kW")
        
def calc_qreactive(Load):
        print(f"calculating Q reactive...")
        
        Load.qreactive = accuracy(Load.pnominal * Load.tgu)
        
        print(f"[ok], Q reacive: {Load.qreactive}kWAr(s)")
        
def calc_sfull(Load):
         print("calculating S full...") 
         if Load.pactive == 0:
             print ('note: P active = 0, verify P nom')
             
         elif Load.qreactive == 0:
             print ('load has no reactive power, Q reactive =0')
         temp1 = math.pow(Load.pactive,2)
         temp2 = math.pow(Load.qreactive,2)
         temp3 = temp1+temp2
         
         Load.sfull = accuracy (math.sqrt(temp3))
         
         print(f"[ok], S full: {Load.sfull} kVA")
            
         
def calc_icurrent(Load):
        print(f"calculating current...")
        if Load.sfull <=0:
            print ('incorrect S full <=0')
            
        elif Load.voltage <=0:
            print ('incorrect load voltage <=0, exeption divizion by zero')
            
        elif Load.voltage <=1:
            print ('verify volage of load, must be in volts (V), not kilovolts(kV)')
            
        if Load.phase == 4:
           print(f"gained three-phase parameter: {Load.phase}")
            
           temp4 = math.sqrt(3)
           temp5 = Load.voltage  * temp4 * 0.001
           Load.icurrent = accuracy (Load.sfull / temp5 )
           
           print(f"[ok], tree-phase current: {Load.icurrent}A")
        elif  Load.phase == 3 or Load.phase == 2 or Load.phase == 1:
              print (f"gained parameter for calculating I (current) for one-phase load: {Load.phase}")
              temp10 =(Load.voltage *0.001)
              Load.icurrent = accuracy (Load.sfull / temp10)
              print (f"I(current) of load at phase {Load.phase}, is {Load.icurrent}A)")
              
           
def calc_sfull_from_icurrent(Load):
        print ("calculaing from current, S full...")
        
        temp6 = math.sqrt(3)
        temp7 = Load.voltage * temp6 * 0.001
        
        Load.sfull = accuracy (Load.icurrent * temp7)
        
        print(f"[ok], S full from current: {Load.sfull}")
        
            
def calc_pactive_from_icurrent(Load):
        print(f"calculaing P active from current...")
        
        Load.pactive = accuracy (Load.sfull * Load.cosu)
        
        print (f"[ok], P active from current: {Load.pactive} kW")
        
def calc_qreactive_from_icurrent(Load):
        print (f"calculaing Q reactive from current...")
        
        print (f"regenerating tan(u) from cos(u)...")
        Load.tgu = accuracy ( math.tan(math.acos(Load.cosu)) )
        
        print(f"[ok], regenerated tan(u): {Load.tgu}")
        
        Load.qreactive = accuracy (Load.pactive * Load.tgu);
        
        print (f"[ok], Q reacive: {Load.qreactive} kVAr(s)")
        
def calc_pnominal_by_one_from_icurrent(Load):
        print(f"calculaing P nominal of one from current...")
     
        Load.pnominal_by_one = accuracy (Load.pactive / Load.count)
        
        print(f"[ok], P nominal of one: {Load.pnominal_by_one}kW")
           
def calc_from_power(Load):  
        print(f"sequence from power launched...") 
        
        calc_tgu(Load)
        calc_pnominal(Load)
        calc_ki_x_pnominal(Load)
        calc_ki_x_pnominal_x_tgu(Load)
        calc_count_x_pnominal_by_one_pow(Load)
        calc_pactive(Load)
        calc_qreactive(Load)
        calc_sfull(Load)
        calc_icurrent(Load)
        
        print (f"done sequence from power...")
            
def calc_from_icurrent(Load):
        print(f"launching sequence from current...")
       
        calc_sfull_from_icurrent(Load)
        calc_pactive_from_icurrent(Load)
        calc_qreactive_from_icurrent(Load)
        calc_tgu(Load)
        calc_pnominal_by_one_from_icurrent(Load)
        calc_pnominal(Load)
        calc_ki_x_pnominal(Load)
        calc_ki_x_pnominal_x_tgu(Load)
        calc_count_x_pnominal_by_one_pow(Load)
        
        print(f"done sequence from current...")
    
def calc(Load):
        print (f"-------main calculate funcion call---------------------------")
        
        if Load.is_conv_from_icurrent == True:
                print(f"gained parameter calculaing from current: {Load.is_conv_from_icurrent}")
            
                Load.name = Load.name + '[conv from current]'
                calc_from_icurrent(Load)
            
        elif Load.is_conv_1ph == False and Load.is_conv_linear_1ph == False:
                print(f"no parameters for one-phase status...")
                calc_from_power(Load)    
           
        elif Load.is_conv_1ph == True:
                print(f"gained parameter convertion from one-phase: {Load.is_conv_1ph} ")
            
                Load.name = Load.name + ' [1ph(conv)]'
                print(f"current one-phase P nominal is: {Load.pnominal_by_one}kW")
                Load.pnominal_by_one = accuracy (3 * Load.pnominal_by_one)
                print(f"converting one-phase to three-phase load, P nominal*3 : {Load.pnominal_by_one} kW")
                calc_from_power(Load)
           
        elif Load.is_conv_linear_1ph == True:
                print(f"gained parameter converion from linear one-phase: {Load.is_conv_linear_1ph}")
            
                Load.name = Load.name + ' [Linear 1ph(conv)]'
                print(f" current one-phase linear P nominal is:{Load.pnominal_by_one}kW")
                Load.pnominal_by_one = accuracy (math.sqrt(3) * Load.pnominal_by_one)
                print(f"convering one-phase to-three phase load, P nominal * sqrt(3) {Load.pnominal_by_one}kW")
                calc_from_power(Load)

        print_load_attr(Load)
                

load1 = Load ('test')

calc(load1)







         
