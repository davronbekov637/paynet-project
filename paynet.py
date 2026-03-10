paynet_tarixi = {}
sotilgan_nomer = []
k_ketliklar = ["0000", "1111", "2222", "3333", "4444",
               "5555", "6666", "7777", "8888", "9999"]
xazna = 0
nomer_xazna = 0
menyu = """
	Paynetimizga xush kelibsiz!

	1) Paynetdan foydalanish
	2) Nomer sotib olish   
	3) Paynet tarixini korish
	4) Paynet xaznasini korish
	5) Sotilgan nomerlar
	0) Chiqish
"""
operatorlar = ["99", "98", "97", "95", "94", "93", "91",
               "90", "88", "77", "55", "50", "33", "20"]

while True:
    print(menyu)
    menyu_tanlash = int(input("\tMenyulardan birini tanlang: "))

    if menyu_tanlash == 1:
        while True:
            nomer = input("\n\tNomeringizni kiriting: ")
            if len(nomer) == 13 and nomer[0:4:] == "+998" and nomer[4:6:] in operatorlar:
                pul = int(input("\tQancha pul tashlamoqchisiz: "))
                if pul > 1200:
                    uslug = pul // 100
                    pul -= uslug
                    xazna += uslug
                    paynet_tarixi.update({nomer: pul})
                    print(f"\n\t{pul} so'm tushdi, 1% uslug {uslug} so'm ushlandi!")
                    break
                else:
                    print("\n\tPaynet uchun bu pul yetarli emas!")
            else:
                print("\n\tNomer xato kiritildi!")
    elif menyu_tanlash == 2:
        while True:
            nomer_t = input("\n\tQanday nomer sotib olmoqchisiz: ")
            if len(nomer_t) == 13 and nomer_t[0:4:] == "+998" and nomer_t[4:6:] in operatorlar:
                if nomer_t not in sotilgan_nomer:
                    if nomer_t[6:10:] in k_ketliklar or nomer_t[9:13:] in k_ketliklar:
                        print(f"""
    {nomer_t} bu raqam mavjud, narxi 450.000 so'm!

    1) Sotib olish
    0) Ortga qaytish
                        """)
                        sotib_olish = int(input("\tRaqamni sotib olmoqchimisiz: "))

                        if sotib_olish == 1:
                            sotilgan_nomer.append(nomer_t)
                            nomer_xazna += 450000
                            print("\n\tNomer sotib olindi")
                            break
                        else:
                            print("\n\tAsosiy menyu")
                            break
                    else:
                        print(f"""
    {nomer_t} bu raqam mavjud, narxi 100.000 so'm!

    1) Sotib olish
    0) Ortga qaytish
                                            """)
                        sotib_olish = int(input("\tRaqamni sotib olmoqchimisiz: "))

                        if sotib_olish == 1:
                            sotilgan_nomer.append(nomer_t)
                            nomer_xazna += 100000
                            print("\n\tNomer sotib olindi")
                            break
                        else:
                            print("\n\tAsosiy menyu")
                            break
                else:
                    print("\n\tBu raqam sotilgan!")
            else:
                print("\n\tRaqam xato kiritildi!")
    elif menyu_tanlash == 3:
        print("\n\tPaynet tarixi\n\t"
              f"{paynet_tarixi}")
    elif menyu_tanlash == 4:
        print(f"""
    Paynetdagi tushum xaznasi: {xazna} so'm
    Sotilgan nomerlar xaznasi: {nomer_xazna} so'm
        """)
    elif menyu_tanlash == 5:
        print(f"""
    Sotilgan nomerlar ro'yxati

    {sotilgan_nomer}
""")
    elif menyu_tanlash == 0:
        print("\n\tTashrifingiz uchun rahmat!")
        break
    else:
        print("Bunday menyu yo'q!")






