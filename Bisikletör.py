import tkinter as tk
from openpyxl import load_workbook
import pandas as pd
import os

# Excel dosya adı
excel_file = "bisiklet_fiyatlari.xlsx"

# Eğer Excel dosyası yoksa hata ver, çünkü bu veri seti var olan bir dosya
if not os.path.exists(excel_file):
    raise FileNotFoundError(f"{excel_file} bulunamadı!")

# Tkinter pencere oluşturma
pencere = tk.Tk()
pencere.geometry("500x400+50+100")
pencere.title("Bisiklet Fiyatları")

def degistir():
    # Entry alanlarından veri al
    fiyat = fiyat_entry.get()
    ozellik1 = ozellik1_entry.get()
    ozellik2 = ozellik2_entry.get()

    if not fiyat or not ozellik1 or not ozellik2:
        # Eksik bilgi varsa kullanıcıya uyarı göster
        sonuc_label.config(text="Tüm alanları doldurun!", fg="red")
        return

    try:
        # Verilerin doğru formatta olup olmadığını kontrol et
        fiyat = float(fiyat)
        ozellik1 = float(ozellik1)
        ozellik2 = float(ozellik2)
    except ValueError:
        sonuc_label.config(text="Lütfen sayısal değerler girin!", fg="red")
        return

    # Excel dosyasını aç ve veri ekle
    wb = load_workbook(excel_file)
    ws = wb.active
    ws.append([fiyat, ozellik1, ozellik2])
    wb.save(excel_file)

    # Kullanıcıya başarı mesajı göster
    sonuc_label.config(text="Veri kaydedildi!", fg="green")

    # Entry alanlarını temizle
    fiyat_entry.delete(0, tk.END)
    ozellik1_entry.delete(0, tk.END)
    ozellik2_entry.delete(0, tk.END)

# Fiyat alanı
fiyat_label = tk.Label(pencere, text="Fiyat:", font="Courier 14 bold")
fiyat_label.place(x=10, y=20)

fiyat_entry = tk.Entry(pencere, width=30)
fiyat_entry.place(x=150, y=25)

# Özellik 1 alanı
ozellik1_label = tk.Label(pencere, text="Özellik 1:", font="Courier 14 bold")
ozellik1_label.place(x=10, y=70)

ozellik1_entry = tk.Entry(pencere, width=30)
ozellik1_entry.place(x=150, y=75)

# Özellik 2 alanı
ozellik2_label = tk.Label(pencere, text="Özellik 2:", font="Courier 14 bold")
ozellik2_label.place(x=10, y=120)

ozellik2_entry = tk.Entry(pencere, width=30)
ozellik2_entry.place(x=150, y=125)

# Kaydet butonu
dugme = tk.Button(pencere, text="Kaydet", command=degistir, font="Courier 14 bold")
dugme.place(x=200, y=180)

# Sonuç mesajı için label
sonuc_label = tk.Label(pencere, text="", font="Courier 12 italic")
sonuc_label.place(x=150, y=230)

pencere.mainloop()


#entry yanına tarih yazısı ekliyoruz 
sütun=tk.Label(text="tarih:",font="Courier 14 bold",justify="left")
sütun.place(x=0,y=18)


#entry yanına not yazısını veriyoruz
sütun2=tk.Label(text="not  :",font="Courier 14 bold",justify="left",)
sütun2.place(x=0,y=98)


#duğmeyi buton olarak tanımlayıp commandını degistir fonksiyonuna verip butonun üstündeki yazısını kaydet verip fontunu ayarlıyoruz
dugme=tk.Button(pencere,text="kaydet",command=degistir,font="Courier 14 bold")
#düğmeye konum veriyoruz
dugme.place(x=300,y=135)