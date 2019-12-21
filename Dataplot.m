L1data = readtable("L1Data.csv")
L2data = readtable("L2Data.csv")
SWEdata = readtable("WI_K0_SWE_74093.csv")


L1datatt = table2timetable(L1data)
L2datatt = table2timetable(L2data)

figure(1)
L1plot = stackedplot(L1datatt)
grid on
figure(2)
L2plot = stackedplot(L2datatt)
grid on 


figure(3)
stackedplot(SWEdata)