import os, time
import pwinput

class BengkelDanny:
    def __init__ (self, Tanggal, Nama, Service, NoHP):
        self.Tanggal = Tanggal
        self.Nama = Nama
        self.Service = Service
        self.NoHP = NoHP
        self.next = None

class Bengkel1:
    def __init__ (self):
        self.head = None

    def PelangganBaru (self, baru):
        pel_baru = BengkelDanny(baru['Tanggal'], baru['Nama'], baru['Service'], baru['NoHP'])
        if self.head is None:
            self.head = pel_baru
        else:
            current_pel = self.head
            while current_pel.next is not None:
                current_pel = current_pel.next
            current_pel.next = pel_baru

    def HapusDataPel (self, Nama):
        current_pel = self.head
        previous_pel = None
        while current_pel is not None:
            if current_pel.Nama == Nama:
                if previous_pel is None:
                    self.head = previous_pel.next
                else:
                    previous_pel.next = current_pel.next
                return
            previous_pel = current_pel
            current_pel = current_pel.next

    def PrintDataPelanggan (self):
        current_pel = self.head
        print(" "*30, "Data Riwayat Pelanggan Bengkel Danny")
        print("-"*100)
        while current_pel is not None:
            print(f"Tanggal: {current_pel.Tanggal}, Nama Pelanggan: {current_pel.Nama}, Service: {current_pel.Service}, No HP: {current_pel.NoHP}")
            current_pel = current_pel.next
        print("Anda sudah berada di akhir data.")

print("-"*100)
print(" "*38, "BENGKEL MOTOR DANNY")
print("-"*100)
print("Silahkan login untuk melanjutkan melihat data riwayat pelanggan.")
time.sleep(1.5)
login = input("Nama: ")
pw = pwinput.pwinput("Kata Sandi: ")
time.sleep(1.5)
print("Anda berhasil login!")
print("-"*100)

# Data Program
DataPel = Bengkel1()

data1 = {'Tanggal': '03/01/2023', 'Nama': 'Kailan', 'Service': 'Ganti oli', 'NoHP': '082166784532'}
data2 = {'Tanggal': '12/05/2022', 'Nama': 'Johnny', 'Service': 'Servis rutin bulanan', 'NoHP': '082278670998'}
data3 = {'Tanggal': '25/02/2023', 'Nama': 'Sabila', 'Service': 'Tambal ban', 'NoHP': '089065782321'}
data4 = {'Tanggal': '19/01/2022', 'Nama': 'Radito', 'Service': 'Ganti lampu sen', 'NoHP': '087765348792'}

DataPel.PelangganBaru(data1)
DataPel.PelangganBaru(data2)
DataPel.PelangganBaru(data3)
DataPel.PelangganBaru(data4)

DataPel.PrintDataPelanggan()
# DataPel.HapusDataPel()
