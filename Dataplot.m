% yyyy-MM-dd'T'HH:mm:ss.SSS'Z' time format


L2datatt = table2timetable(L1Dataraw)
figure(1)
L1plot = stackedplot(L2datatt)
L1plot.Color = [0 0 0]
grid on
