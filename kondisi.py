# memberikan nilai pada variabel
nilai = 10

# kondisi lebih dari
if nilai > 9:
    print("nilai lebih dari 9")

# kondisi kurang dari
if nilai < 11:
    print("nilai kurang dari dari 11")

# kondisi sama dengan
if nilai == 10:
    print("nilai sama dengan 10")

print("=" * 20)  # tanda pemisah

# kondisi if else
if nilai > 20:
    print("nilai lebih dari 20")
else:
    print("nilai lebih kurang dari 20")

print("=" * 20)  # tanda pemisah

# kondisi elif
waktu = "siang"

if waktu == "pagi":
    print("saatnya makan pagi")
elif waktu == "siang":
    print("saatnya makan siang")
elif waktu == "malam":
    print("saatnya makan malam")