import csv
import numpy as np

with open("AC_H0_SWE_95692.csv", "r") as SWEPAM:
    SWEPAM_reader = csv.reader(SWEPAM)
    next(SWEPAM_reader)
    Vx = []
    Vswe = []
    nswe = []
    Tswe = []
    time_swe = []

    for line in SWEPAM_reader:
        t = line[0]
        x = line[1]
        x = float(x)
        if abs(x) > 10 ** 10:
            continue
        nswe.append(x)
        time_swe.append(t)

        y = line[3]
        y = float(y)
        if abs(y) > 10 ** 10:
            continue
        Tswe.append(y)

        z1 = line[4]
        z2 = line[5]
        z3 = line[6]
        z1 = float(z1)
        z2 = float(z2)
        z3 = float(z3)
        z = np.sqrt((z1 ** 2) + (z2 ** 2) + (z3 ** 2))
        if z > 10 ** 10:
            continue
        Vswe.append(z)

        x = line[4]
        x = abs(float(x))
        if x > 6000:
            continue
        Vx.append(x)

    print(time_swe)
    print(time_swe[2])
    print(time_swe[10])

with open("AC_H0_MFI_95692.csv", "r") as MFI:
    MFI_reader = csv.reader(MFI)
    next(MFI_reader)

    Bmfi = []
    Bxmfi = []
    Bymfi = []
    Bzmfi = []
    fakeBmfi = []
    fakeBxmfi = []
    fakeBymfi = []
    fakeBzmfi = []
    for line in MFI_reader:

        x = line[1]
        x = float(x)
        if abs(x) > 10 ** 10:
            continue
        fakeBmfi.append(x)
        if len(fakeBmfi) == 4:
            data = np.mean(fakeBmfi)
            Bmfi.append(data)
            fakeBmfi = []

        x1 = line[2]
        x1 = float(x1)
        if abs(x1) > 10 ** 10:
            continue
        fakeBxmfi.append(x1)
        if len(fakeBxmfi) == 4:
            data = np.mean(fakeBxmfi)
            Bxmfi.append(data)
            fakeBxmfi = []

        y1 = line[3]
        y1 = float(y1)
        if abs(y1) > 10 ** 10:
            continue
        fakeBymfi.append(y1)
        if len(fakeBymfi) == 4:
            data = np.mean(fakeBymfi)
            Bymfi.append(data)
            fakeBymfi = []

        z1 = line[4]
        z1 = float(z1)
        if abs(z1) > 10 ** 10:
            continue
        fakeBzmfi.append(z1)
        if len(fakeBzmfi) == 4:
            data = np.mean(fakeBzmfi)
            Bzmfi.append(data)
            fakeBzmfi = []

with open("THC_L2_MOM_216777.csv", "r") as MOM:
    MOM_reader = csv.reader(MOM)
    next(MOM_reader)
    Vmom = []
    nmom = []
    Tmom = []
    fakenmom = []
    fakeVmom = []
    fakeTmom = []
    for line in MOM_reader:

        x = line[1]
        x = float(x)
        if abs(x) > 10 ** 10:
            continue
        fakenmom.append(x)
        if len(fakenmom) >= 20:
            data = np.mean(fakenmom)
            fakenmom = []
            nmom.append(data)

        z1 = line[5]
        z2 = line[6]
        z3 = line[7]
        z1 = float(z1)
        z2 = float(z2)
        z3 = float(z3)
        y = 11600 * np.sqrt((z1 ** 2) + (z2 ** 2) + (z3 ** 2))
        if abs(y) > 100000000000000000:
            continue
        fakeTmom.append(y)
        if len(fakeTmom) == 20:
            data = np.mean(fakeTmom)
            Tmom.append(data)
            fakeTmom = []

        z1 = line[2]
        z2 = line[3]
        z3 = line[4]
        z1 = float(z1)
        z2 = float(z2)
        z3 = float(z3)
        z = np.sqrt((z1 ** 2) + (z2 ** 2) + (z3 ** 2))
        if z > 10 ** 10:
            continue
        fakeVmom.append(z)
        if len(fakeVmom) == 20:
            data = np.mean(fakeVmom)
            Vmom.append(data)
            fakeVmom = []

with open("THC_L2_FGM_89446.csv", "r") as FGM:
    FGM_reader = csv.reader(FGM)
    next(FGM_reader)
    Bfgm = []
    Bx = []
    By = []
    Bz = []
    fakeBfgm = []
    fakeBx = []
    fakeBy = []
    fakeBz = []
    for line in FGM_reader:

        x = line[1]
        x = float(x)
        if abs(x) > 10 ** 10:
            continue
        fakeBfgm.append(x)
        if len(fakeBfgm) == 20:
            data = np.mean(fakeBfgm)
            Bfgm.append(data)
            fakeBfgm = []

        x1 = line[2]
        x1 = float(x1)
        if abs(x1) > 10 ** 10:
            continue
        fakeBx.append(x1)
        if len(fakeBx) == 20:
            data = np.mean(fakeBx)
            Bx.append(data)
            fakeBx = []

        y1 = line[3]
        y1 = float(y1)
        if abs(y1) > 10 ** 10:
            continue
        fakeBy.append(y1)
        if len(fakeBy) == 20:
            data = np.mean(fakeBy)
            By.append(data)
            fakeBy = []

        z1 = line[4]
        z1 = float(z1)
        if abs(z1) > 10 ** 10:
            continue
        fakeBz.append(z1)
        if len(fakeBz) == 20:
            data = np.mean(fakeBz)
            Bz.append(data)
            fakeBz = []

with open("new_data.csv", "w") as new_file:
    fieldnames = ['time', 'Vswe', "Tswe", "nswe", "BmagMFI", "BxMFI", "ByMFI",
                  "BzMFI", "Vmom", "Tmom", "nmom", "BmagFGM", "BxFGM", "ByFGM", "BzFGM"]

    writer = csv.DictWriter(new_file, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(len(Vswe)):
        writer.writerow({'time': time_swe[i], 'Vswe': Vswe[i], "Tswe": Tswe[i], "nswe": nswe[i], "BmagMFI": Bmfi[i],
                         "BxMFI": Bxmfi[i], "ByMFI": Bymfi[i], "BzMFI": Bzmfi[i], "Vmom": Vmom[i], "Tmom": Tmom[i],
                         "nmom": nmom[i], "BmagFGM": Bfgm[i], "BxFGM": Bx[i], "ByFGM": By[i], "BzFGM": Bz[i]})