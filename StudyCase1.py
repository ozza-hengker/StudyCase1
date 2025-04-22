import keyboard
import threading
import time

class PerangkatRumah:
    def __init__(self, nama, tombol):
        self.nama = nama
        self.tombol = tombol
        self.status = False
        keyboard.on_press_key(self.tombol, self.saklar)

    def saklar(self, e):
        self.status = not self.status
        if self.status:
            print(f"{self.nama} dinyalakan loh ya.")
        else:
            print(f"{self.nama} dimatikan loh ya.")

class SistemRumahPintar:
    def __init__(self):
        self.lampu = PerangkatRumah("Lampu Otomatis", 'l')
        self.kipas = PerangkatRumah("Kipas Otomatis", 'k')
        self.sensor_suhu = PerangkatRumah("Sensor Suhu", 't')

    def pantau_rumah(self):
        print("=== Kontrol Rumah Pintar ===")
        print("Tekan 'l' untuk menyalakan/mematikan Lampu")
        print("Tekan 'k' untuk menyalakan/mematikan Kipas")
        print("Tekan 't' untuk menyalakan/mematikan Sensor Suhu")
        print("Aktifkan semua untuk melihat status rumah...\n")

        # Thread untuk memantau status rumah
        status_thread = threading.Thread(target=self.tampilkan_status_rumah)
        status_thread.start()
        status_thread.join()

    def tampilkan_status_rumah(self):
        while True:
            if self.lampu.status and self.kipas.status and self.sensor_suhu.status:
                print(">>> Semua perangkat aktif. Rumah dalam kondisi optimal. <<<\n")
                time.sleep(2)
            time.sleep(0.2)

if __name__ == "__main__":
    sistem = SistemRumahPintar()
    sistem.pantau_rumah()
