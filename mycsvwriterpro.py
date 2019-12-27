import csv

M_p = 1.67 * 10 ** (-27)  # Proton mass (kg)
k = 1.38 * 10 ** (-23)  # Boltzman Constant (Joule/K)
eV = 11600  # K

with open("WI_K0_SWE_74093.csv", "r") as SWE:
    SWE_reader = csv.reader(SWE)
    next(SWE_reader)
    time_SWE = []
    SW_Th = []  # km/s
    th_sw = []  # km/s
    Ion_Np = []  # #/cm^3
    Del_t = []  # ms
    V_x = []  # km/s
    V_y = []  # km/s
    V_z = []  # km/s
    V_tot = []  # km/s
    P_dyn = []  #
    T = []  # K
    i = 0
    v_x_sum = 0
    for line in SWE_reader:
        time = line[0]
        th_sw = float(line[1])
        n = float(line[2])
        x = float(line[4])
        y = float(line[5])
        z = float(line[6])
        time_SWE.append(time)
        Ion_Np.append(n)
        V_x.append(x)
        V_y.append(y)
        V_z.append(z)
        V_tot.append((x ** 2 + y ** 2 + z ** 2) ** (1 / 2))  # km/s
        v_x_sum += x
        v_x_sum += V_x[i]
        T.append(((th_sw ** 2) * M_p * (10 ** 6)) / (3 * k))  # unit (K)
        P_dyn.append( (n * 1000 * 1000)* M_p * (V_tot[i] * 1000 )**(2)  * 10**9)  # calculated to unit nPa
        i += 1

    meanV_tot_wind = sum(V_tot) / (len(V_x))
    print(meanV_tot_wind)

with open("WI_H0_MFI_113987.csv", "r") as MFI:
    MFI_reader = csv.reader(MFI)
    next(MFI_reader)
    B_x = []
    B_y = []
    B_z = []
    B_tot = []
    bxfake = []
    byfake = []
    bzfake = []

    for line in MFI_reader:
        bx = float(line[1])
        by = float(line[2])
        bz = float(line[3])

        bxfake.append(bx)
        byfake.append(by)
        bzfake.append(bz)

    for i in range(0, 184):
        bxmean = (bxfake[2 * i] + bxfake[2 * i + 1]) / 2
        bymean = (byfake[2 * i] + byfake[2 * i + 1]) / 2
        bzmean = (bzfake[2 * i] + bzfake[2 * i + 1]) / 2
        B_x.append(bxmean)
        B_y.append(bymean)
        B_z.append(bzmean)

    for i in range(0, len(B_y)):
        B_tot.append((B_y[i] ** 2 + B_x[i] ** 2 + B_z[i] ** 2) ** (1 / 2))

with open("THB_L2_FGM_138046.csv", "r") as FGM:
    FGM_reader = csv.reader(FGM)
    next(FGM_reader)
    L2B_tot = []  # nT
    L2B_x = []  # nT
    L2B_y = []  # nT
    L2B_z = []  # nT
    L2B_totfake = []  # nT
    L2B_xfake = []  # nT
    L2B_yfake = []  # nT
    L2B_zfake = []  # nT

    for line in FGM_reader:
        btot = float(line[1])
        bx = float(line[2])
        by = float(line[3])
        bz = float(line[4])
        L2B_totfake.append(btot)  # nT
        L2B_xfake.append(bx)
        L2B_yfake.append(by)
        L2B_zfake.append(bz)

    for i in range(0, 201):
        bxnew = 0
        bynew = 0
        bznew = 0
        btotnew = 0

        for j in range(0, 29):
            bxnew += L2B_xfake[i * 30 + j]
            bynew += L2B_yfake[i * 30 + j]
            bznew += L2B_zfake[i * 30 + j]
            btotnew += L2B_totfake[i * 30 + j]
        L2B_x.append(bxnew / 30)
        L2B_y.append(bynew / 30)
        L2B_z.append(bznew / 30)
        L2B_tot.append(btotnew / 30)

with open("THB_L2_MOM_150448.csv", "r") as MOM:
    MOM_reader = csv.reader(MOM)
    next(MOM_reader)
    Mom_ion = []  # /cc
    MomV_x = []  # km/s
    MomV_y = []
    MomV_z = []
    MomT_x = []  # eV
    MomT_y = []
    MomT_z = []
    MomT_tot = []
    MomV_tot = []
    Momv_x = []  # km/s
    Momv_y = []
    Momv_z = []
    Momt_x = []  # eV
    Momt_y = []
    Momt_z = []
    Mom_N = []
    Momt_tot = []
    L2_time = []
    Momv_tot = []

    for line in MOM_reader:
        time = line[0]
        n_ion = float(line[1])
        v_x = float(line[2])
        v_y = float(line[3])
        v_z = float(line[4])
        t_x = float(line[5])
        t_y = float(line[6])
        t_z = float(line[7])
        Mom_ion.append(n_ion)
        Momt_x.append(t_x)
        Momt_y.append(t_y)
        Momt_z.append(t_z)
        Momv_x.append(v_x)
        Momv_y.append(v_y)
        Momv_z.append(v_z)
        Momv_tot.append((v_x ** 2 + v_z ** 2 + v_y ** 2) ** (1 / 2))
        Momt_tot.append((t_x + t_z + t_y) / 3 * eV)
        L2_time.append(time)
    for i in range(0, 201):
        sumvx = 0
        sumvy = 0
        sumvz = 0
        sumn = 0
        sumtx = 0
        sumty = 0
        sumtz = 0

        for j in range(0, 29):
            sumvx += Momv_x[i * 30 + j]
            sumvy += Momv_y[i * 30 + j]
            sumvz += Momv_z[i * 30 + j]
            sumtx += Momt_x[i * 30 + j]
            sumty += Momt_y[i * 30 + j]
            sumtz += Momt_z[i * 30 + j]
            sumn += Mom_ion[i * 30 + j]

        MomV_x.append(sumvx / 30)
        MomV_y.append(sumvy / 30)
        MomV_z.append(sumvz / 30)
        MomT_x.append(sumtx / 30)
        MomT_y.append(sumtx / 30)
        MomT_z.append(sumtx / 30)
        Mom_N.append(sumn / 30)

    for i in range(0, len(MomT_x)):
        MomT_tot.append((MomT_x[i] ** 2 + MomT_y[i] ** 2 + MomT_z[i] ** 2) ** (1 / 2))
        MomV_tot.append((MomV_x[i] ** 2 + MomV_y[i] ** 2 + MomV_z[i] ** 2) ** (1 / 2))

print(len(B_x))
print(len(V_x))
print(len(Mom_N))
print(len(L2B_x))
with open("themisloc.txt", "r") as Location:
    Location_reader = Location.read().split("\n")
    themis = []
    sumthemis = 0

    for line in Location_reader:
        themis.append(float(line))
        sumthemis += float(line)

    meanthemis = sum(themis) / (len(themis))
    print(meanthemis)

with open("windloc.txt", "r") as Location:
    Location_reader = Location.read().split("\n")
    wind = []
    sumwind = 0

    for line in Location_reader:
        wind.append(float(line))
        sumwind += float(line)

    meanwind = sum(wind) / (len(wind))

with open("L1Dataraw.csv", "w") as L1:
    labels = ["Time", "IMF B_x", "IMF B_y", "IMF B_z", "IMF B_tot", "n", "T", "V_x", "V_y", "V_z", "V_tot", "P_dyn"]
    writer = csv.DictWriter(L1, fieldnames=labels)
    writer.writeheader()

    for j in range(0, len(B_x)):
        writer.writerow(
            {"Time": time_SWE[j], "IMF B_x": B_x[j], "IMF B_y": B_y[j], "IMF B_z": B_z[j], "IMF B_tot": B_tot[j],
             "n": Ion_Np[j], "T": T[j]
                , "V_x": V_x[j], "V_y": V_y[j], "V_z": V_z[j], "V_tot": V_tot[j], "P_dyn": P_dyn[j]})

with open("L2Dataraw.csv", "w") as L1:
    labels = ["Time", "IMF B_x", "IMF B_y", "IMF B_z", "IMF B_tot", "n", "T", "V_x", "V_y", "V_z", "V_tot"]
    writer = csv.DictWriter(L1, fieldnames=labels)
    writer.writeheader()

    for j in range(0, len(L2_time)):
        writer.writerow({"Time": L2_time[j], "IMF B_x": L2B_xfake[j], "IMF B_y": L2B_yfake[j], "IMF B_z": L2B_zfake[j],
                         "IMF B_tot": L2B_totfake[j], "n": Mom_ion[j], "T": Momt_tot[j]
                            , "V_x": Momv_x[j], "V_y": Momv_y[j], "V_z": Momv_z[j], "V_tot": Momv_tot[j]})

delta_t = (meanwind - meanthemis) / (meanV_tot_wind)
print("mean themis : ", meanthemis)
print("mean wind: ", meanwind)
print("mean vel: ", meanV_tot_wind)
print(delta_t)
print(range(0, len(themis)))
