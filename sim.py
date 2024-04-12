# sim env
import numpy as np
import math

# for the NMOS
w_n1 = 10e-6
l_n1 = 1e-6
# SPICE Param KP (units A/V^2)
kp = 90e-6

v_g = 1
v_s = 0
v_gs = v_g - v_s
v_t = 0.5

i_d =1/2* kp * (w_n1/l_n1) * pow((v_gs - v_t),2) 

print(type(i_d))
print(i_d)

g_m = (2 * i_d) / v_gs
g_m = kp * (w_n1/l_n1) * (v_gs-v_t)


#say I want V_d to rest at 2V...
#I need to know the resistance of the PMOS, its R_ds (I think)

class MOSFET:
    def __init__(self, Vgs=0, Vds=0, Vth=0, kp=0, W=0, L=0):
        self.Vgs = Vgs  # Gate-to-Source Voltage
        self.Vds = Vds  # Drain-to-Source Voltage
        self.Vth = Vth  # Threshold Voltage
        self.kp = kp      # Transconductance Parameter
        self.W = W      # Width of the MOSFET
        self.L = L      # Length of the MOSFET

    def set_dimensions(self, W, L):
        self.W = W
        self.L = L

    def set_parameters(self, Vth, kp):
        self.Vth = Vth
        self.kp = kp

    def set_voltages(self, Vgs, Vds):
        self.Vgs = Vgs
        self.Vds = Vds

    def drain_current(self):
        if self.Vgs < self.Vth:
            return 0
        elif self.Vds < (self.Vgs - self.Vth):
            return 0
        else:
            i_d =1/2 * self.kp * (self.W/self.L) * pow((self.Vgs - self.Vth),2)
            return i_d

# Example usage:
n1 = MOSFET(Vth=v_t, kp=kp, W=w_n1, L=l_n1)
n1_v_gs = 1.0
n1_v_ds = 2.0
n1.set_voltages(v_gs, n1_v_ds)
print(type(n1.drain_current()))
print(n1.drain_current())

print(math.isclose(i_d,n1.drain_current(),rel_tol=1e-8))