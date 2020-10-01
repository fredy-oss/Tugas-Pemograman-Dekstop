berat=float
O(input("masukkan berat badan:"))
tinggi=float(input("masukkan berat tinggi:"))
bmi = berat / (tinggi*tinggi)
if  bmi <18.5 :
    print("Berat badan kurang")
elif 18.5> bmi <22.9 :
    print("Berat badan normal")
elif 23> bmi <29.9 :
    print("Berat badan berlebih (kecenderungan obesitas)")
elif 30 :
    print("Obesitas")
    
    
    
