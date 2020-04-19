import hrcalc
ir = []
with open("ir.log", "r") as f:
    for line in f:
        ir.append(int(line))

red = []
with open("red.log", "r") as f:
    for line in f:
        red.append(int(line))

for i in range(37):
    print(hrcalc.calc_hr_and_spo2(ir[25*i:25*i+100], red[25*i:25*i+100]))