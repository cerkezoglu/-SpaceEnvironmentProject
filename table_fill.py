import csv
import numpy as np

M_p = 1.67 * 10 ** (-27)  # Proton mass (kg)
k = 1.38 * 10 ** (-23)  # Boltzman Constant (Joule/K)
eV = 11600  # K

with open("L2Dataraw.csv", "r") as l2:
    L2_reader = csv.reader(l2)
    next(L2_reader)
    L2B_x = []
    L2B_y = []
    L2B_z = []
    L2B_tot = []
    L2T = []
    L2N = []
    L2V_x = []
    L2V_y = []
    L2V_z = []
    L2V_tot = []
    Bx_sw = []
    By_sw = []
    Bz_sw = []
    Btot_sw = []
    T_sw = []
    N_sw = []
    Vx_sw = []
    Vy_sw = []
    Vz_sw = []
    Vtot_sw = []

    Bx_mp = []
    By_mp = []
    Bz_mp = []
    Btot_mp = []
    T_mp = []
    N_mp = []
    Vx_mp = []
    Vy_mp = []
    Vz_mp = []
    Vtot_mp = []

    Bx_bs = []
    By_bs = []
    Bz_bs = []
    Btot_bs = []
    T_bs = []
    N_bs = []
    Vx_bs = []
    Vy_bs = []
    Vz_bs = []
    Vtot_bs = []

    for line in L2_reader:
        bx = float(line[1])
        by = float(line[2])
        bz = float(line[3])
        btot = float(line[4])
        n = float(line[5])
        t = float(line[6])
        vx = float(line[7])
        vy = float(line[8])
        vz = float(line[9])
        vtot = float(line[10])
        L2B_x.append(bx)
        L2B_y.append(by)
        L2B_z.append(bz)
        L2B_tot.append(btot)
        L2T.append(t)
        L2N.append(n)
        L2V_x.append(vx)
        L2V_y.append(vy)
        L2V_z.append(vz)
        L2V_tot.append(vtot)

    for i in range(2121):
        Bx_mp.append(L2B_x[i])
        By_mp.append(L2B_y[i])
        Bz_mp.append(L2B_z[i])
        Btot_mp.append(L2B_tot[i])
        N_mp.append(L2N[i])
        T_mp.append(L2T[i])
        Vx_mp.append(L2V_x[i])
        Vy_mp.append(L2V_y[i])
        Vz_mp.append(L2V_z[i])
        Vtot_mp.append(L2V_tot[i])
    for i in range(2122, 4072):
        Bx_bs.append(L2B_x[i])
        By_bs.append(L2B_y[i])
        Bz_bs.append(L2B_z[i])
        Btot_bs.append(L2B_tot[i])
        N_bs.append(L2N[i])
        T_bs.append(L2T[i])
        Vx_bs.append(L2V_x[i])
        Vy_bs.append(L2V_y[i])
        Vz_bs.append(L2V_z[i])
        Vtot_bs.append(L2V_tot[i])
    for i in range(4073, 6059):
        Bx_sw.append(L2B_x[i])
        By_sw.append(L2B_y[i])
        Bz_sw.append(L2B_z[i])
        Btot_sw.append(L2B_tot[i])
        N_sw.append(L2N[i])
        T_sw.append(L2T[i])
        Vx_sw.append(L2V_x[i])
        Vy_sw.append(L2V_y[i])
        Vz_sw.append(L2V_z[i])
        Vtot_sw.append(L2V_tot[i])

# Solar wind table data
Btot_min_sw = min(Btot_sw)
Btot_max_sw = max(Btot_sw)
Btot_mean_sw = sum(Btot_sw) / (len(Btot_sw) + 1)

Bx_min_sw = min(Bx_sw)
Bx_max_sw = max(Bx_sw)
Bx_mean_sw = sum(Bx_sw) / (len(Bx_sw) + 1)

By_min_sw = min(By_sw)
By_max_sw = max(By_sw)
By_mean_sw = sum(By_sw) / (len(By_sw) + 1)

Bz_min_sw = min(Bz_sw)
Bz_max_sw = max(Bz_sw)
Bz_mean_sw = sum(Bz_sw) / (len(Bz_sw) + 1)

N_min_sw = min(N_sw)
N_max_sw = max(N_sw)
N_mean_sw = sum(N_sw) / (len(N_sw) + 1)

T_min_sw = min(T_sw)
T_max_sw = max(T_sw)
T_mean_sw = sum(T_sw) / (len(T_sw) + 1)

Vx_min_sw = min(Vx_sw)
Vx_max_sw = max(Vx_sw)
Vx_mean_sw = sum(Vx_sw) / (len(Vx_sw) + 1)

Vy_min_sw = min(Vy_sw)
Vy_max_sw = max(Vy_sw)
Vy_mean_sw = sum(Vy_sw) / (len(Vy_sw) + 1)

Vz_min_sw = min(Vz_sw)
Vz_max_sw = max(Vz_sw)
Vz_mean_sw = sum(Vz_sw) / (len(Vz_sw) + 1)

Vtot_min_sw = min(Vtot_sw)
Vtot_max_sw = max(Vtot_sw)
Vtot_mean_sw = sum(Vtot_sw) / (len(Vtot_sw) + 1)

# Magnetosphere table data

Btot_min_mp = min(Btot_mp)
Btot_max_mp = max(Btot_mp)
Btot_mean_mp = sum(Btot_mp) / (len(Btot_mp) + 1)

Bx_min_mp = min(Bx_mp)
Bx_max_mp = max(Bx_mp)
Bx_mean_mp = sum(Bx_mp) / (len(Bx_mp) + 1)

By_min_mp = min(By_mp)
By_max_mp = max(By_mp)
By_mean_mp = sum(By_mp) / (len(By_mp) + 1)

Bz_min_mp = min(Bz_mp)
Bz_max_mp = max(Bz_mp)
Bz_mean_mp = sum(Bz_mp) / (len(Bz_mp) + 1)

N_min_mp = min(N_mp)
N_max_mp = max(N_mp)
N_mean_mp = sum(N_mp) / (len(N_mp) + 1)

T_min_mp = min(T_mp)
T_max_mp = max(T_mp)
T_mean_mp = sum(T_mp) / (len(T_mp) + 1)

Vx_min_mp = min(Vx_mp)
Vx_max_mp = max(Vx_mp)
Vx_mean_mp = sum(Vx_mp) / (len(Vx_mp) + 1)

Vy_min_mp = min(Vy_mp)
Vy_max_mp = max(Vy_mp)
Vy_mean_mp = sum(Vy_mp) / (len(Vy_mp) + 1)

Vz_min_mp = min(Vz_mp)
Vz_max_mp = max(Vz_mp)
Vz_mean_mp = sum(Vz_mp) / (len(Vz_mp) + 1)

Vtot_min_mp = min(Vtot_mp)
Vtot_max_mp = max(Vtot_mp)
Vtot_mean_mp = sum(Vtot_mp) / (len(Vtot_mp) + 1)

# Magnetosteath table data
Btot_min_bs = min(Btot_bs)
Btot_max_bs = max(Btot_bs)
Btot_mean_bs = sum(Btot_bs) / (len(Btot_bs) + 1)

Bx_min_bs = min(Bx_bs)
Bx_max_bs = max(Bx_bs)
Bx_mean_bs = sum(Bx_bs) / (len(Bx_bs) + 1)

By_min_bs = min(By_bs)
By_max_bs = max(By_bs)
By_mean_bs = sum(By_bs) / (len(By_bs) + 1)

Bz_min_bs = min(Bz_bs)
Bz_max_bs = max(Bz_bs)
Bz_mean_bs = sum(Bz_bs) / (len(Bz_bs) + 1)

N_min_bs = min(N_bs)
N_max_bs = max(N_bs)
N_mean_bs = sum(N_bs) / (len(N_bs) + 1)

T_min_bs = min(T_bs)
T_max_bs = max(T_bs)
T_mean_bs = sum(T_bs) / (len(T_bs) + 1)

Vx_min_bs = min(Vx_bs)
Vx_max_bs = max(Vx_bs)
Vx_mean_bs = sum(Vx_bs) / (len(Vx_bs) + 1)

Vy_min_bs = min(Vy_bs)
Vy_max_bs = max(Vy_bs)
Vy_mean_bs = sum(Vy_bs) / (len(Vy_bs) + 1)

Vz_min_bs = min(Vz_bs)
Vz_max_bs = max(Vz_bs)
Vz_mean_bs = sum(Vz_bs) / (len(Vz_bs) + 1)

Vtot_min_bs = min(Vtot_bs)
Vtot_max_bs = max(Vtot_bs)
Vtot_mean_bs = sum(Vtot_bs) / (len(Vtot_bs) + 1)

Btot = [Btot_min_sw, Btot_max_sw, Btot_mean_sw, Btot_min_bs, Btot_max_bs, Btot_mean_bs, Btot_min_mp, Btot_max_mp,
        Btot_mean_mp]
N = [N_min_sw, N_max_sw, N_mean_sw, N_min_bs, N_max_bs, N_mean_bs, N_min_mp, N_max_mp, N_mean_mp]
T = [T_min_sw, T_max_sw, T_mean_sw, T_min_bs, T_max_bs, T_mean_bs, T_min_mp, T_max_mp, T_mean_mp]
Vtot = [Vtot_min_sw, Vtot_max_sw, Vtot_mean_sw, Vtot_min_bs, Vtot_max_bs, Vtot_mean_bs, Vtot_min_mp, Vtot_max_mp,
        Vtot_mean_mp]
Vx = [Vx_min_sw, Vx_max_sw, Vx_mean_sw, Vx_min_bs, Vx_max_bs, Vx_mean_bs, Vx_min_mp, Vx_max_mp, Vx_mean_mp]
Vy = [Vy_min_sw, Vy_max_sw, Vy_mean_sw, Vy_min_bs, Vy_max_sw, Vy_mean_bs, Vy_min_mp, Vy_max_mp, Vy_mean_mp]
Vz = [Vz_min_sw, Vz_max_sw, Vz_mean_sw, Vz_min_bs, Vz_max_bs, Vz_mean_bs, Vz_min_mp, Vz_max_mp, Vz_mean_mp]

with open("L2table1.txt", "w") as L2data:
    L2data.write("B_tot")
    for i in Btot:
        L2data.write("," + str(i))
    L2data.write("\n")

    L2data.write("N")
    for i in N:
        L2data.write("," + str(i))
    L2data.write("\n")

    L2data.write("T")
    for i in T:
        L2data.write("," + str(i))
    L2data.write("\n")

    L2data.write("V_tot")
    for i in Vtot:
        L2data.write("," + str(i))
    L2data.write("\n")

    L2data.write("V_x")
    for i in Vx:
        L2data.write("," + str(i))
    L2data.write("\n")

    L2data.write("V_y")
    for i in Vy:
        L2data.write("," + str(i))
    L2data.write("\n")

    L2data.write("V_z")
    for i in Vz:
        L2data.write("," + str(i))
    L2data.write("\n")

with open("L1Datarawtable1.csv", "r") as l1:
    L1_reader = csv.reader(l1)
    next(L1_reader)
    L1B_x = []
    L1B_y = []
    L1B_z = []
    L1B_tot = []
    L1T = []
    L1N = []
    L1V_x = []
    L1V_y = []
    L1V_z = []
    L1V_tot = []

    for line in L1_reader:
        bx = float(line[1])
        by = float(line[2])
        bz = float(line[3])
        btot = float(line[4])
        n = float(line[5])
        t = float(line[6])
        vx = float(line[7])
        vy = float(line[8])
        vz = float(line[9])
        vtot = float(line[10])
        L1B_x.append(bx)
        L1B_y.append(by)
        L1B_z.append(bz)
        L1B_tot.append(btot)
        L1T.append(t)
        L1N.append(n)
        L1V_x.append(vx)
        L1V_y.append(vy)
        L1V_z.append(vz)
        L1V_tot.append(vtot)

    L1B_tot_min_sw = min(L1B_tot[0:22])
    L1B_tot_max_sw = max(L1B_tot[0:22])
    L1B_tot_mean_sw = sum(L1B_tot[0:22]) / 22

    L1B_tot_min_msh = min(L1B_tot[22:81])
    L1B_tot_max_msh = max(L1B_tot[22:81])
    L1B_tot_mean_msh = sum(L1B_tot[22:81]) / 59

    L1B_tot_min_msp = min(L1B_tot[81:184])
    L1B_tot_max_msp = max(L1B_tot[81:184])
    L1B_tot_mean_msp = sum(L1B_tot[81:184]) / 103

    firstline = [L1B_tot_min_sw, L1B_tot_max_sw, L1B_tot_mean_sw, L1B_tot_min_msh, L1B_tot_max_msh, L1B_tot_mean_msh,
                 L1B_tot_min_msp, L1B_tot_max_msp, L1B_tot_mean_msp]

    L1N_min_sw = min(L1N[0:22])
    L1N_max_sw = max(L1N[0:22])
    L1N_mean_sw = sum(L1N[0:22]) / 22

    L1N_min_msh = min(L1N[22:81])
    L1N_max_msh = max(L1N[22:81])
    L1N_mean_msh = sum(L1N[22:81]) / 59

    L1N_min_msp = min(L1N[81:184])
    L1N_max_msp = max(L1N[81:184])
    L1N_mean_msp = sum(L1N[81:184]) / 103

    secondline = [L1N_min_sw, L1N_max_sw, L1N_mean_sw, L1N_min_msh, L1N_max_msh, L1N_mean_msh, L1N_min_msp, L1N_max_msp,
                  L1N_mean_msp]

    L1T_min_sw = min(L1T[0:22])
    L1T_max_sw = max(L1T[0:22])
    L1T_mean_sw = sum(L1T[0:22]) / 22

    L1T_min_msh = min(L1T[22:81])
    L1T_max_msh = max(L1T[22:81])
    L1T_mean_msh = sum(L1T[22:81]) / 59

    L1T_min_msp = min(L1T[81:184])
    L1T_max_msp = max(L1T[81:184])
    L1T_mean_msp = sum(L1T[81:184]) / 103

    thirdline = [L1T_min_sw, L1T_max_sw, L1T_mean_sw, L1T_min_msh, L1T_max_msh, L1T_mean_msh, L1T_min_msp, L1T_max_msp,
                 L1T_mean_msp]

    L1Vtot_min_sw = min(L1V_tot[0:22])
    L1Vtot_max_sw = max(L1V_tot[0:22])
    L1Vtot_mean_sw = sum(L1V_tot[0:22]) / 22

    L1Vtot_min_msh = min(L1V_tot[22:81])
    L1Vtot_max_msh = max(L1V_tot[22:81])
    L1Vtot_mean_msh = sum(L1V_tot[22:81]) / 59

    L1Vtot_min_msp = min(L1V_tot[81:184])
    L1Vtot_max_msp = max(L1V_tot[81:184])
    L1Vtot_mean_msp = sum(L1V_tot[81:184]) / 103

    fourthline = [L1Vtot_min_sw, L1Vtot_max_sw, L1Vtot_mean_sw, L1Vtot_min_msh, L1Vtot_max_msh, L1Vtot_mean_msh,
                  L1Vtot_min_msp, L1Vtot_max_msp, L1Vtot_mean_msp]

    with open("L1table1.csv", "w") as L1data:

        L1data.write("B_tot")
        for i in firstline:
            L1data.write("," + str(i))
        L1data.write("\n")

        L1data.write("N")
        for i in secondline:
            L1data.write("," + str(i))
        L1data.write("\n")

        L1data.write("T")
        for i in thirdline:
            L1data.write("," + str(i))
        L1data.write("\n")

        L1data.write("V_tot")
        for i in fourthline:
            L1data.write("," + str(i))
        L1data.write("\n")

    with open("L1Datarawtable1.csv", "r") as l1:
        L1_reader = csv.reader(l1)
        next(L1_reader)
        L1B_x = []
        L1B_y = []
        L1B_z = []
        L1B_tot = []
        L1T = []
        L1N = []
        L1V_x = []
        L1V_y = []
        L1V_z = []
        L1V_tot = []
        L1P_dyn = []
        l1bx = []
        l1by = []
        l1bz = []
        l1btot = []
        l1n = []
        l1t = []
        l1vx = []
        l1vy = []
        l1vz = []
        l1vtot = []
        l1pdyn = []
        l1time = []
        j = 1
        sumbx = 0
        sumby = 0
        sumbz = 0
        sumbtot = 0
        sumn = 0
        sumt = 0
        sumvx = 0
        sumvy = 0
        sumvz = 0
        sumvtot = 0
        sump = 0
        for line in L1_reader:
            time = line[0]
            bx = float(line[1])
            by = float(line[2])
            bz = float(line[3])
            btot = float(line[4])
            n = float(line[5])
            t = float(line[6])
            vx = float(line[7])
            vy = float(line[8])
            vz = float(line[9])
            vtot = float(line[10])
            pdyn = float(line[11])

            L1_time = time
            L1B_x.append(bx)
            L1B_y.append(by)
            L1B_z.append(bz)
            L1B_tot.append(btot)
            L1T.append(t)
            L1N.append(n)
            L1V_x.append(vx)
            L1V_y.append(vy)
            L1V_z.append(vz)
            L1V_tot.append(vtot)
            L1P_dyn.append(pdyn)
            print(L1_time)

            if j <= 3:
                sumbx += bx
                sumby += by
                sumbz += bz
                sumbtot += btot
                sumn += n
                sumt += t
                sumvx += vx
                sumvy += vy
                sumvz += vz
                sumvtot += vtot
                sump += pdyn
                if j ==3:
                    l1time.append(time)
                    l1bx.append(sumbx/3)
                    l1by.append(sumby/3)
                    l1bz.append(sumbz/3)
                    l1btot.append(sumbtot/3)
                    l1n.append(sumn/3)
                    l1t.append(sumt/3)
                    l1vx.append(sumvx/3)
                    l1vy.append(sumvy/3)
                    l1vz.append(sumvz/3)
                    l1vtot.append(sumvtot/3)
                    l1pdyn.append(sump/3)

                    sumbx = 0
                    sumby = 0
                    sumbz = 0
                    sumbtot = 0
                    sumn = 0
                    sumt = 0
                    sumvx = 0
                    sumvy = 0
                    sumvz = 0
                    sumvtot = 0
                    sump = 0
                    j = 0
                j +=1


B_0 = 0.3 * 10 ** (-4)  # Tesla or MKS
M_p = 1.67 * 10 ** (-27)  # Proton mass (kg)
k = 1.38 * 10 ** (-23)  # Boltzman Constant (Joule/K)
eV = 11600  # K
nu_0 = 4 * np.pi * 10 ** (-7)  # MKS Henry/m
l1Rmp = []
l1Rbs = []
l1long = []
gama = 5 / 3

for i in range(len(l1t)):
    rmp = ((B_0 ** 2) / (nu_0 * l1n[i] * M_p * l1vtot[i] ** 2 * 10 ** (12))) ** (1 / 6)
    l1Rmp.append(rmp)

    d = rmp * 1.1 * (gama - 1) / (gama + 1)

    l1Rbs.append(d + rmp)

    long = np.arccos(1 / ((rmp) ** (1 / 2))) * 180 / np.pi  # radian

    l1long.append(long)

l1long_min = min(l1long)
l1long_max = max(l1long)
l1long_avg = sum(l1long) / len(l1long)

rmp_min = min(l1Rmp)
rmp_max = max(l1Rmp)
rmp_av = sum(l1Rmp) / len(l1Rmp)

rbs_min = min(l1Rbs)
rbs_max = max(l1Rbs)
rbs_av = sum(l1Rbs) / len(l1Rbs)


with open("L2Datarawtable1.csv","r") as L2d2 :

    L2d2_reader = csv.reader(L2d2)
    next(L2d2_reader)

    L2B_tot = []  # nT
    L2B_x = []  # nT
    L2B_y = []  # nT
    L2B_z = []  # nT
    L2V_x = []
    L2V_y = []
    L2V_z = []
    L2V_tot = []
    L2time_fake = []
    L2time = []
    L2v_xfake = []
    L2v_yfake = []
    L2v_zfake = []
    L2_tfake = []
    L2_nfake = []
    L2B_totfake = []  # nT
    L2B_xfake = []  # nT
    L2B_yfake = []  # nT
    L2B_zfake = []  # nT
    L2T =[]
    L2N =[]
    # Time,IMF B_x,IMF B_y,IMF B_z,IMF B_tot,n,T,V_x,V_y,V_z,V_tot
    i =1
    sbx = 0
    sby = 0
    sbz = 0
    sbtot = 0
    sn = 0
    st = 0
    svx = 0
    svy = 0
    svz = 0
    svtot = 0

    for line in L2d2_reader:
        ti = line[0]
        bx = float(line[1])
        by = float(line[2])
        bz = float(line[3])
        btot = float(line[4])
        nn  = float(line[5])
        tt = float(line[6])
        vxx = float(line[7])
        vyy = float(line[8])
        vzz = float(line[9])
        vtoot = float(line[10])



        if i <= 100:
            sbx += bx
            sby += by
            sbz += bz
            sbtot += btot
            sn += nn
            st += tt
            svx += vxx
            svy += vyy
            svz += vzz
            svtot += vtoot

            if i == 100:
                L2B_x.append(sbx/100)
                L2B_y.append(sby/100)
                L2B_z.append(sbz/100)
                L2B_tot.append(sbtot/100)
                L2N.append(sn/100)
                L2T.append(st/100)
                L2V_x.append(svx/100)
                L2V_y.append(svy/100)
                L2V_z.append(svz/100)
                L2V_tot.append(svtot/100)
                L2time.append(ti)

                sbx = 0
                sby = 0
                sbz = 0
                sbtot = 0
                sn = 0
                st = 0
                svx = 0
                svy = 0
                svz = 0
                svtot = 0

                i = 1
        i += 1

print(len(L2T))
with open("TotalTable2.csv", "w") as Taa:
    labels = ["L1time", "L1bx", "L1by", "L1bz", "L1btot", "L1n", "L1T", "L1V_x", "L1V_y", "L1V_z", "L1V_tot", "L1P_dyn", "L2time", "L2bx","L2by","L2bz","L2btot","L2n","L2T","L2V_x", "L2V_y", "L2V_z", "L2V_tot","Rmp","Rbs","Long"]
    writer = csv.DictWriter(Taa, fieldnames=labels)
    writer.writeheader()

    for j in range(len(L2time)):
        writer.writerow({"L1time": L2time[j][11:16], "L1bx": l1bx[j], "L1by": l1by[j], "L1bz" : l1bz[j], "L1btot" : l1btot[j], "L1n" : l1n[j], "L1T": l1t[j], "L1V_x" : l1vx[j], "L1V_y" : l1vy[j], "L1V_z" : l1vz[j], "L1V_tot": l1vtot[j] , "L1P_dyn" : l1pdyn[j], "L2time" : L2time[-j][11:16], "L2bx" : L2B_x[j],"L2by" : L2B_y[j],"L2bz": L2B_z[j],"L2btot" : L2B_tot[j],"L2n" : L2N[j]   ,"L2T": L2T[j],"L2V_x": L2V_x[j], "L2V_y": L2V_y[j], "L2V_z": L2V_z[j], "L2V_tot": L2V_tot[j],"Rmp": l1Rmp[j],"Rbs": l1Rbs[j],"Long" : l1long[j]})




