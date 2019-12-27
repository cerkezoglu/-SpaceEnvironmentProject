% yyyy-MM-dd'T'HH:mm:ss.SSS'Z' time format
degreeSymbol = char(176);


L2datatt = table2timetable(L2Datarawtable2);
figure(1)
newYlabels = {'B_x(nT)','B_y(nT)', 'B_z(nT)','B_tot(nT)','n(#/cc)',['T (' degreeSymbol 'K)'],'V_x(km/s)','V_y(km/s)','V_z(km/s)','V_tot(km/s)'};
L2plot = stackedplot(L2datatt,'Title','THEMIS-B-DATA','DisplayLabels',newYlabels);
L2plot.Color = [0 0 0];
grid on


L1datatt = table2timetable(L1Datarawtable2);
newYlabels = {'B_x(nT)','B_y(nT)', 'B_z(nT)','B_tot(nT)','n(#/cc)',['T (' degreeSymbol 'K)'],'V_x(km/s)','V_y(km/s)','V_z(km/s)','V_tot(km/s)','P_dyn(nPa)'};
figure(2)
L1plot = stackedplot(L1datatt,'Title','WIND-DATA','DisplayLabels',newYlabels);
L1plot.Color = [0 0 0];
grid on


Pdyn = table2array(TotalTable2(8:32,12));
Rmp = table2array(TotalTable2(8:32,24));
Rbs = table2array(TotalTable2(8:32,25));
long = table2array(TotalTable2(8:32,26));

figure(3)

subplot(1,2,1)
mpplot = plot(Pdyn,Rmp,'o')
mpplot.Color = [0 0 1]
xlabel('Pdyn(nPa)')
ylabel('Rmp(Re)')
title('Rmp to Pdyn')
hold on
line1 =plot(Pdyn,Rmp)
line1.Color = [1 0 0]
grid on

subplot(1,2,2)

bsplot = plot(Pdyn,Rbs,'o')
bsplot.Color = [0 1 1]
xlabel('Pdyn(nPa)')
ylabel('Rbs(Re)')
title('Rbs to Pdyn')
hold on 

line2 =plot(Pdyn,Rbs)
line2.Color = [1 0 0]
grid on


figure(4)

plot()