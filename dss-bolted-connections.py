#
#    Design of Steel Structures
#    Bolted Connections
#    
#    Author: Afaan Bilal
#    URL: https://afaanbilal.github.io
#    
#    (c) 2018 Afaan Bilal
#    Released under the MIT License
#

from __future__ import print_function

import math

# factor of safety (ultimate)
Y_M = 1.25

def vdsb(f_ub, d, N_n, N_s):
    '''
        Design shear strength of bolt.
    '''
    unthreaded_area = math.pi * (d ** 2) / 4
    threaded_area   = 0.78 * unthreaded_area
    return f_ub * (threaded_area * N_n + unthreaded_area * N_s) / (Y_M * math.sqrt(3))

def vdpb(f_ub, f_up, d, p, e, t):
    '''
        Design bearing strength of bolt.
    '''
    # hole dia
    d_0 = d + 2
    if d <= 14:
        d_0 = d + 1
    elif d >= 27:
        d_0 = d + 3
    k_b = min(e / (3 * d_0), p / (3 * d_0) - 0.25, f_ub / f_up, 1.0)
    return 2.5 * k_b * t * d * f_up / Y_M

def tdb(f_up, d):
    '''
        Design tensile strength of bolt.
    '''
    threaded_area   = 0.78 * math.pi * (d ** 2) / 4
    return 0.9 * f_up * threaded_area / Y_M

print("")
print("Design of Steel Structures")
print("Bolted Connections")
print("(c) Afaan Bilal\n")

factored_load= float(input("Enter factored load (kN): "))
d            = int(input("Enter bolt diameter (mm): "))
bolt_grade   = str(input("Enter bolt grade (eg: 4.6): "))
t            = int(input("Enter aggregate minimum plate thickness (mm): "))
f_up         = int(input("Enter plate ultimate strength (N/mm2): "))
N_n          = int(input("Enter number of shear planes (threaded): "))
N_s          = int(input("Enter number of shear planes (non-threaded): "))
e            = int(input("Enter edge distance (e) (mm): "))
p            = int(input("Enter pitch (p) (mm): "))

f_ub = int(bolt_grade.split('.')[0]) * 100
f_yb = float(f_ub * float('0.' + bolt_grade.split('.')[1]))

design_shear = vdsb(f_ub, d, N_n, N_s) / 1000
design_bearing = vdpb(f_ub, f_up, d, p, e, t) / 1000
design_tension = tdb(f_up, d) / 1000

bolt_value = min(design_shear, design_bearing, design_tension)

print("----------------------------------------")
print("fub = %d N/mm2" % f_ub)
print("fyb = %.3f N/mm2" % f_yb)
print("----------------------------------------")
print("Shear strength of bolt  :     %.3f kN" % design_shear)
print("Bearing strength of bolt:     %.3f kN" % design_bearing)
print("Tensile strength of plate:    %.3f kN" % design_tension)
print("----------------------------------------")
print("Bolt value:                   %.3f kN" % bolt_value)

number_of_bolts = math.ceil(factored_load / bolt_value)

print("Number of bolts required:     %d" % number_of_bolts)

print("\n")
print("__________________________________________________")
print("|                        |                       |")
for i in range(number_of_bolts):
    print("|                        |                       |")
    print("|                   ()   |                       |")
    print("|                        |                       |")
print("|________________________|_______________________|")
