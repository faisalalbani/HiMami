# view.py
import customtkinter as ctk
from tkinter import Tk, messagebox, Label, OptionMenu, StringVar, Text
from PIL import Image, ImageTk, ImageOps
import tkinter as tk
from tkinter import font, END

def check_fonts():
        root = tk.Tk()
        available_fonts = font.families()
        print(available_fonts)
        root.destroy()

class LoginView:
    def __init__(self, controller):
        self.controller = controller
        self.root = Tk()
        self.root.title("KUMAR:)")

        custom_font = ("Lucida Fax", 70)  

        # Set fullscreen mode
        self.fullscreen = True
        self.root.attributes('-fullscreen', self.fullscreen)

        custom_font = ("Lucida Fax", 70)

        # Bind the Escape key to exit fullscreen mode
        self.root.bind("<Escape>", self.end_fullscreen)

        self.root.configure(bg='#3b3b3b')

        self.image_path = r"C:/Users/VICTUS/Downloads/login.jpg"  # Ganti dengan path ke gambar Anda

        # Initial image setup
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        image = Image.open(self.image_path)
        image = ImageOps.fit(image, (screen_width, screen_height), method=Image.Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(image)

        self.image_label = Label(self.root, image=self.photo)
        self.image_label.image = self.photo  # Menyimpan referensi gambar agar tidak dihapus oleh garbage collector
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Ensure the image resizes when the window size changes
        self.root.bind("<Configure>", lambda event: self.resize_image())

        self.daftar_akun = ctk.CTkLabel(self.root, text='Sign In', text_color="#FFFFFF", font=custom_font)
        self.daftar_akun.place(x=1000, y=110)

        self.email_label = ctk.CTkLabel(self.root, text='Email', text_color="#FFFFFF", font=("Arial", 15))
        self.email_label.place(x=1000, y=200)

        self.nama_entry = ctk.CTkEntry(self.root, width=200)
        self.nama_entry.place(x=1000, y=230)

        self.password_label = ctk.CTkLabel(self.root, text='Password', text_color="#FFFFFF", font=("Arial", 15))
        self.password_label.place(x=1000, y=270)

        self.pass_entry = ctk.CTkEntry(self.root, width=200, show='*')
        self.pass_entry.place(x=1000, y=300)

        self.login_btn = ctk.CTkButton(self.root, text='Login', bg_color="black", fg_color='#212121', command=self.controller.log_btn)
        self.login_btn.place(x=1025, y=360)

        self.regist_btn = ctk.CTkButton(self.root, text='Registration', bg_color='black', fg_color='#212121', command=self.controller.guest_btn)
        self.regist_btn.place(x=1025, y=400)

    def end_fullscreen(self, event=None):
        self.root.quit()

    def resize_image(self):
        screen_width = self.root.winfo_width()
        screen_height = self.root.winfo_height()
        image = Image.open(self.image_path)
        image = ImageOps.fit(image, (screen_width, screen_height), method=Image.Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=self.photo)
        self.image_label.image = self.photo

    def show(self):
        self.root.mainloop()

    def show_message(self, title, message, error=False):
        if error:
            messagebox.showerror(title, message)
        else:
            messagebox.showinfo(title, message)

class RegisterView:
    def __init__(self, controller):
        self.controller = controller
        self.root = Tk()
        self.root.title("KUMAR:)")
        self.fullscreen = True
        self.root.attributes('-fullscreen', self.fullscreen)

        custom_font = ("Lucida Fax", 70)

        self.root.bind("<Escape>", self.end_fullscreen)
        self.root.configure(bg='#3b3b3b')
        self.image_path = r"C:/Users/VICTUS/Downloads/registration.jpg"

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        image = Image.open(self.image_path)
        image = ImageOps.fit(image, (screen_width, screen_height), method=Image.Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(image)

        self.image_label = Label(self.root, image=self.photo)
        self.image_label.image = self.photo  
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.root.bind("<Configure>", lambda event: self.resize_image())

        self.daftar_akun = ctk.CTkLabel(self.root, text='Register', text_color="#FFFFFF", font=custom_font)
        self.daftar_akun.place(x=80, y=110)

        self.nama_label = ctk.CTkLabel(self.root, text='Nama', text_color="#FFFFFF", font=("Arial", 15))
        self.nama_label.place(x=80, y=200)

        self.nama_entry = ctk.CTkEntry(self.root, width=200)
        self.nama_entry.place(x=80, y=230)

        self.email_label = ctk.CTkLabel(self.root, text='Email', text_color="#FFFFFF", font=("Arial", 15))
        self.email_label.place(x=80, y=260)

        self.email_entry = ctk.CTkEntry(self.root, width=200)
        self.email_entry.place(x=80, y=290)

        self.password_label = ctk.CTkLabel(self.root, text='Password', text_color="#FFFFFF", font=("Arial", 15))
        self.password_label.place(x=80, y=320)

        self.pass_entry = ctk.CTkEntry(self.root, width=200, show='*')
        self.pass_entry.place(x=80, y=350)

        self.regist_btn = ctk.CTkButton(self.root, text='Register', bg_color="black", fg_color='#212121', command=self.controller.register_user)
        self.regist_btn.place(x=110, y=400)

        self.back_btn = ctk.CTkButton(self.root, text='Back to Menu', bg_color='black', fg_color='#212121', command=self.controller.bck_btn)
        self.back_btn.place(x=110, y=440)

    def end_fullscreen(self, event=None):
        self.root.quit()

    def resize_image(self):
        screen_width = self.root.winfo_width()
        screen_height = self.root.winfo_height()
        image = Image.open(self.image_path)
        image = ImageOps.fit(image, (screen_width, screen_height), method=Image.Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=self.photo)
        self.image_label.image = self.photo

    def show(self):
        self.root.mainloop()

    def show_message(self, title, message, error=False):
        if error:
            messagebox.showerror(title, message)
        else:
            messagebox.showinfo(title, message)

class MenuView:
    def __init__(self, controller):
        self.controller = controller
        self.root = Tk()
        self.root.title("SideBar Menu")
        self.root.attributes('-fullscreen', True)
        self.fullscreen = True

        custom_font = ("Lucida Fax", 50)

        # Bind the Escape key to end fullscreen mode
        self.root.bind("<Escape>", self.controller.end_fullscreen)
        
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Menghitung lebar untuk side frame sebagai 25% dari lebar layar
        side_frame_width = int(screen_width * 0.21)

        # Membuat side_frame dengan lebar yang ditentukan
        self.side_frame = ctk.CTkFrame(self.root, width=side_frame_width, height=screen_height, corner_radius=0, fg_color='#212121')
        self.side_frame.pack(side="left", fill="y")

        self.main_frame = ctk.CTkFrame(self.root, corner_radius=0, fg_color='#3b3b3b')
        self.main_frame.pack(side="right", fill="both", expand=True)

        self.image_path = r"C:\Users\VICTUS\Downloads\home main .png"  # Ganti dengan path ke gambar Anda
        image = Image.open(self.image_path)
        image = ImageOps.fit(image, (700, 320), method=Image.Resampling.LANCZOS)  # Sesuaikan ukuran gambar jika perlu
        photo = ImageTk.PhotoImage(image)

        self.image_label = Label(self.main_frame, image=photo, borderwidth=0)
        self.image_label.image = photo  # Menyimpan referensi gambar agar tidak dihapus oleh garbage collector
        self.image_label.place(x=150, y=180)

        self.search_entry = ctk.CTkEntry(self.main_frame, width=550, height=50, fg_color='#D9D9D9')
        self.search_entry.place(x=230, y=80)
        # self.search_entry.bind("<Return>", self.controller.search_action)

        menu = ctk.CTkLabel(self.side_frame, text='Menu', text_color="#483D8B", font=custom_font)
        menu.place(x=75, y=70)

        umkm_fav = ctk.CTkLabel(self.main_frame, text='Toko sedang Diskon', text_color="#FFFFFF", font=custom_font)
        umkm_fav.place(x=180, y=500)

        self.image_path = r"C:\Users\VICTUS\Downloads\home main .png"  # Ganti dengan path ke gambar Anda
        image = Image.open(self.image_path)
        image = ImageOps.fit(image, (700, 320), method=Image.Resampling.LANCZOS)  # Sesuaikan ukuran gambar jika perlu
        photo = ImageTk.PhotoImage(image)

        self.image_label = Label(self.main_frame, image=photo, borderwidth=0)
        self.image_label.image = photo  # Menyimpan referensi gambar agar tidak dihapus oleh garbage collector
        self.image_label.place(x=150, y=180)

        self.create_side_menu()
        self.create_main_menu()

    def create_side_menu(self):
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\halaman utama.png", "Halaman Utama", 20, 170, self.controller.halutama_action)
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\news.png", "Berita", 20, 270, self.controller.berita_action)
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\+ umkm.png", "Daftar UKM", 20, 370, self.controller.daftar_ukm)
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\profil.png", "Profil", 20, 470, self.controller.profil_action)

    def create_main_menu(self):
        self.create_label_with_image2(self.main_frame, r"C:\Users\VICTUS\Downloads\fnb.png", 875, 190, self.controller.fnb)
        self.create_label_with_image2(self.main_frame, r"C:\Users\VICTUS\Downloads\toko.png", 875, 270, self.controller.toko)
        self.create_label_with_image2(self.main_frame, r"C:\Users\VICTUS\Downloads\jasa.png", 875, 350, self.controller.jasa)
        self.create_label_with_image2(self.main_frame, r"C:\Users\VICTUS\Downloads\baju.png", 875, 430, self.controller.fashion)
        self.create_label_with_image4(self.main_frame, r"C:\Users\VICTUS\Downloads\search.png", 730, 83)

        self.create_label_with_image3(self.main_frame, r"C:\Users\VICTUS\Downloads\sale.png", 180, 580)
        self.create_label_with_image3(self.main_frame, r"C:\Users\VICTUS\Downloads\sale.png", 450, 580)
        self.create_label_with_image3(self.main_frame, r"C:\Users\VICTUS\Downloads\sale.png", 720, 580)

    def create_label_with_image(self, frame, image_path, text, x, y, action):
        image = Image.open(image_path)
        image = ImageOps.fit(image, (80, 80), method=Image.Resampling.LANCZOS)  # Sesuaikan ukuran gambar
        photo = ImageTk.PhotoImage(image)

        label = Label(frame, text=text, image=photo, compound="left", font=("Arial", 15), fg="#FFFFFF", bg="#212121", cursor="hand2")
        label.image = photo  # Menyimpan referensi gambar agar tidak dihapus oleh garbage collector
        label.place(x=x, y=y)
        label.bind("<Button-1>", action)

    def create_label_with_image2(self, frame, image_path, x, y, action):
        image = Image.open(image_path)
        image = ImageOps.fit(image, (60, 60), method=Image.Resampling.LANCZOS)  # Sesuaikan ukuran gambar
        photo = ImageTk.PhotoImage(image)

        label = Label(frame, image=photo, compound="left", font=("Arial", 15), fg="#FFFFFF", bg="#212121", cursor="hand2")
        label.image = photo  # Menyimpan referensi gambar agar tidak dihapus oleh garbage collector
        label.place(x=x, y=y)
        label.bind("<Button-1>", action)

    def create_label_with_image3(self, frame, image_path, x, y):
        image = Image.open(image_path)
        image = ImageOps.fit(image, (250, 250), method=Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        label = Label(frame, image=photo, bd=0)
        label.image = photo  # Menyimpan referensi gambar
        label.place(x=x, y=y)

    def create_label_with_image4(self, frame, image_path, x, y):
        image = Image.open(image_path)
        image = ImageOps.fit(image, (40, 40), method=Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        label = Label(frame, image=photo, bd=0)
        label.image = photo  # Menyimpan referensi gambar
        label.place(x=x, y=y)
        label.bind("<Button-1>")

    def display_user_info(self):
        if self.user:
            user_info = f"Nama: {self.user['nama']}\nEmail: {self.user['email']}"
            user_info_label = ctk.CTkLabel(self.side_frame, text=user_info, text_color="#FFFFFF", font=("Arial", 15))
            user_info_label.place(x=20, y=550)  # Adjust the position as needed

class NewsView:
    def __init__(self, controller):
        self.controller = controller
        self.root = Tk()
        self.root.title("SideBar Menu")
        self.root.attributes('-fullscreen', True)
        self.fullscreen = True

        custom_font = ("Lucida Fax", 50)

        # Bind the Escape key to end fullscreen mode
        self.root.bind("<Escape>", self.controller.end_fullscreen)
        
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Menghitung lebar untuk side frame sebagai 25% dari lebar layar
        side_frame_width = int(screen_width * 0.21)

        # Membuat side_frame dengan lebar yang ditentukan
        self.side_frame = ctk.CTkFrame(self.root, width=side_frame_width, height=screen_height, corner_radius=0, fg_color='#212121')
        self.side_frame.pack(side="left", fill="y")

        self.main_frame = ctk.CTkFrame(self.root, corner_radius=0, fg_color='#3b3b3b')
        self.main_frame.pack(side="right", fill="both", expand=True)

        menu = ctk.CTkLabel(self.side_frame, text='Menu', text_color="#483D8B", font=custom_font)
        menu.place(x=75, y=70)

        news = ctk.CTkLabel(self.main_frame, text='NEWS', text_color="#FFFFFF", font=custom_font)
        news.place(x=125, y=80)

    def create_side_menu(self):
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\halaman utama.png", "Halaman Utama", 20, 170, self.controller.halutama_action)
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\news.png", "Berita", 20, 270, self.controller.berita_action)
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\+ umkm.png", "Daftar UKM", 20, 370, self.controller.daftar_ukm)
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\profil.png", "Profil", 20, 470, self.controller.profil_action)

    def create_main_menu(self):
        self.create_label_with_image2(self.main_frame, r"C:\Users\VICTUS\Downloads\headline berita.png", 125, 150)
        self.create_label_with_image2(self.main_frame, r"C:\Users\VICTUS\Downloads\headline berita.png", 125, 300)
        self.create_label_with_image2(self.main_frame, r"C:\Users\VICTUS\Downloads\headline berita.png", 125, 450)
        self.create_label_with_image3(self.main_frame, r"C:\Users\VICTUS\Downloads\seemore.png", 1000, 130, self.controller.detail)
        self.create_label_with_image3(self.main_frame, r"C:\Users\VICTUS\Downloads\seemore.png", 1000, 290, self.controller.detail)
        self.create_label_with_image3(self.main_frame, r"C:\Users\VICTUS\Downloads\seemore.png", 1000, 440, self.controller.detail)

        Headinga = ctk.CTkLabel(self.main_frame, text='Heading Line', text_color="#FFFFFF", font=("Arial", 40))
        Headinga.place(x=775, y=210)

        headingb = ctk.CTkLabel(self.main_frame, text='Heading Line', text_color="#FFFFFF", font=("Arial", 40))
        headingb.place(x=775, y=360)

        Headingc = ctk.CTkLabel(self.main_frame, text='Heading Line', text_color="#FFFFFF", font=("Arial", 40))
        Headingc.place(x=775, y=510)

    def show(self):
        self.root.mainloop()

    def create_label_with_image(self, frame, image_path, text, x, y, action):
        image = Image.open(image_path)
        image = ImageOps.fit(image, (80, 80), method=Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        label = Label(frame, text=text, image=photo, compound="left", font=("Arial", 15), fg="#FFFFFF", bg="#212121", cursor="hand2")
        label.image = photo
        label.place(x=x, y=y)
        label.bind("<Button-1>", action)

    def create_label_with_image2(self, frame, image_path, x, y):
        image = Image.open(image_path)
        image = ImageOps.fit(image, (600, 200), method=Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        label = Label(frame, image=photo, borderwidth=0)
        label.image = photo
        label.place(x=x, y=y)

    def create_label_with_image3(self, frame, image_path, x, y, action):
        image = Image.open(image_path)
        image = ImageOps.fit(image, (200, 200), method=Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        label = Label(frame, image=photo, bd=0)
        label.image = photo  # Menyimpan referensi gambar
        label.place(x=x, y=y)
        label.bind("<Button-1>", action)

class DetailNewsView:
    def __init__(self, controller):
        self.controller = controller
        self.root = Tk()
        self.root.title("SideBar Menu")
        self.root.attributes('-fullscreen', True)
        self.fullscreen = True

        # Bind the Escape key to end fullscreen mode
        self.root.bind("<Escape>", self.controller.end_fullscreen)
        
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Menghitung lebar untuk side frame sebagai 25% dari lebar layar
        side_frame_width = int(screen_width * 0.21)

        # Membuat side_frame dengan lebar yang ditentukan
        self.side_frame = ctk.CTkFrame(self.root, width=side_frame_width, height=screen_height, corner_radius=0, fg_color='#212121')
        self.side_frame.pack(side="left", fill="y")

        self.main_frame = ctk.CTkFrame(self.root, corner_radius=0, fg_color='#3b3b3b')
        self.main_frame.pack(side="right", fill="both", expand=True)

        self.image_path = r"C:\Users\VICTUS\Downloads\headline berita.png"  # Ganti dengan path ke gambar Anda
        image = Image.open(self.image_path)
        image = ImageOps.fit(image, (700, 200), method=Image.Resampling.LANCZOS)  # Sesuaikan ukuran gambar jika perlu
        photo = ImageTk.PhotoImage(image)

        self.image_label = Label(self.main_frame, image=photo, borderwidth=0)
        self.image_label.image = photo  # Menyimpan referensi gambar agar tidak dihapus oleh garbage collector
        self.image_label.place(x=120, y=120)

        # Menambahkan frame untuk membedakan kotak teks dari main_frame
        text_frame_width = (screen_width - 5) // 2
        text_frame_height = (screen_height - 5) // 2

        self.text_frame = ctk.CTkFrame(self.main_frame, corner_radius=10, fg_color="#2E2E2E",
                                        width=text_frame_width, height=text_frame_height)
        self.text_frame.place(x=120, y=400)

        # Membuat scrollbar vertikal untuk text widget
        scrollbar = ctk.CTkScrollbar(self.text_frame)
        scrollbar.pack(side="right", fill="y")

        # Membuat text widget untuk menampilkan berita panjang
        self.text_widget = ctk.CTkTextbox(self.text_frame, wrap="word", font=("Arial", 15), fg_color="#2E2E2E", text_color="#FFFFFF", padx=10, pady=10, yscrollcommand=scrollbar.set)
        berita_text = """
Kementerian Badan Usaha Milik Negara (BUMN) menekankan pentingnya pertumbuhan Usaha Mikro, Kecil, 
dan Menengah (UMKM) dalam mendukung perekonomian Indonesia. Loto Srinaita Ginting, staf ahli di 
Kementerian BUMN, menyatakan bahwa peningkatan kapasitas pelaku UMKM, seperti melalui pelatihan, 
adalah kunci untuk kemajuan bisnis mereka. Salah satu contohnya adalah pelatihan digital marketing 
yang diselenggarakan oleh BUMN PT Peruri, yang fokus pada pemanfaatan media sosial. Pelatihan 
kewirausahaan juga ditawarkan untuk penyandang disabilitas, bekerja sama dengan Yayasan Kreasi Tuli 
dan Generasi Baru Indonesia (GenBI) Universitas Singaperbangsa Karawang. Tujuan dari pelatihan ini 
adalah agar peserta dapat menjadi lebih mandiri dan membantu mempercepat pertumbuhan ekonomi nasional.

Ratih Sukma Pratiwi, Kepala Biro Strategic Corporate Branding & TJSL PT Peruri, menyatakan bahwa Peruri 
secara rutin menyelenggarakan pelatihan UMKM di Rumah BUMN Karawang. Program ini bertujuan membangun 
ekosistem ekonomi digital dan meningkatkan kapasitas UMKM. Pelatihan ini diadakan setiap bulan dan diikuti 
oleh UMKM binaan serta pelaku UMKM lainnya. Ratih menekankan bahwa UMKM adalah inti dari perekonomian 
Indonesia, dan kegiatan ini mendukung Tujuan Pembangunan Berkelanjutan nomor 8 yang berkaitan dengan 
pekerjaan layak dan pertumbuhan ekonomi. Peruri berkomitmen untuk terus mengadakan pelatihan secara 
rutin guna mendorong UMKM berkembang hingga mampu bersaing secara global.

Wakil Menteri Perdagangan Jerry Sambuaga mengajak pelaku usaha, termasuk UMKM, untuk memanfaatkan 
perjanjian dagang yang telah Indonesia jalin dengan negara lain guna meningkatkan ekspor. Saat pembukaan 
Inabuyer 2024 di Jakarta, Rabu, Jerry menyebut Indonesia memiliki 37 perjanjian dagang yang bisa 
dimanfaatkan. Salah satu perjanjian tersebut adalah IA-CEPA (Indonesia-Australia Comprehensive Economic 
Partnership Agreement), yang memberikan akses pasar dan meningkatkan daya saing produk Indonesia, khususnya 
di sektor pertanian, perikanan, industri, dan kehutanan.

Dengan IA-CEPA yang berlaku sejak Juli 2020, Australia menghapus 6.474 pos tarif, sehingga produk Indonesia
yang diekspor ke Australia bebas bea masuk, mengurangi biaya hingga 20-25 persen. Jerry menegaskan Kementerian 
Perdagangan terus berupaya menjalin lebih banyak perjanjian dagang untuk membuka akses pasar bagi produk 
Indonesia. Pemanfaatan perjanjian ini diharapkan tidak hanya meningkatkan ekspor pelaku UMKM, tetapi juga 
berkontribusi pada pertumbuhan ekonomi nasional, khususnya dalam hal devisa dan surplus neraca perdagangan.
        """
        self.text_widget.insert("1.0", berita_text)  # Ganti dengan berita_text
        self.text_widget.configure(state="disabled")  # Membuat Text widget hanya-baca
        self.text_widget.pack(expand=True, fill="both", padx=(0, 10), pady=(0, 10))  # Menambahkan padding kanan dan bawah

        # Mengatur ukuran widget text frame menjadi setengah dari geometry
        self.text_widget.configure(width=text_frame_width, height=text_frame_height)

        # Menghubungkan scrollbar dengan text widget
        scrollbar.configure(command=self.text_widget.yview)

    def create_side_menu(self):
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\halaman utama.png", "Halaman Utama", 20, 170, self.controller.halutama_action)
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\news.png", "Berita", 20, 270, self.controller.berita_action)
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\+ umkm.png", "Daftar UKM", 20, 370, self.controller.daftar_ukm)
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\profil.png", "Profil", 20, 470, self.controller.profil_action)

    def create_main_menu(self):
        custom_font = ("Lucida Fax", 50)

        menu = ctk.CTkLabel(self.side_frame, text='Menu', text_color="#483D8B", font=custom_font)
        menu.place(x=75, y=70)

        heading_berita = ctk.CTkLabel(self.main_frame, text='Tolak UU TAPERA', text_color="#FFFFFF", font=custom_font)
        heading_berita.place(x=125, y=70)

        judul_label = ctk.CTkLabel(self.main_frame, text='Tolak UU Tapera', text_color="#FFFFFF", font=('Arial', 20))
        judul_label.place(x=125, y=300)     

        name_creator_label = ctk.CTkLabel(self.main_frame, text='Ditulis oleh: Ozza Rangkuti', text_color="#FFFFFF", font=('Arial', 20))
        name_creator_label.place(x=125, y=347)

    def show(self):
        self.root.mainloop()

    def create_label_with_image(self, frame, image_path, text, x, y, action):
        image = Image.open(image_path)
        image = ImageOps.fit(image, (80, 80), method=Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        label = Label(frame, text=text, image=photo, compound="left", font=("Arial", 15), fg="#FFFFFF", bg="#212121", cursor="hand2")
        label.image = photo
        label.place(x=x, y=y)
        label.bind("<Button-1>", action)

    def create_label_with_image2(self, frame, image_path, x, y):
        image = Image.open(image_path)
        image = ImageOps.fit(image, (600, 200), method=Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        label = Label(frame, image=photo, borderwidth=0)
        label.image = photo
        label.place(x=x, y=y)

class RegUMKMView:
    def __init__(self, controller):
        self.controller = controller
        self.root = Tk()
        self.root.title("SideBar Menu")
        self.root.attributes('-fullscreen', True)
        self.fullscreen = True

        # Bind the Escape key to end fullscreen mode
        self.root.bind("<Escape>", self.controller.end_fullscreen)
        
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Menghitung lebar untuk side frame sebagai 25% dari lebar layar
        side_frame_width = int(screen_width * 0.21)

        # Membuat side_frame dengan lebar yang ditentukan
        self.side_frame = ctk.CTkFrame(self.root, width=side_frame_width, height=screen_height, corner_radius=0, fg_color='#212121')
        self.side_frame.pack(side="left", fill="y")

        self.main_frame = ctk.CTkFrame(self.root, corner_radius=0, fg_color='#3b3b3b')
        self.main_frame.pack(side="right", fill="both", expand=True)

    def create_side_menu(self):
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\halaman utama.png", "Halaman Utama", 20, 170, self.controller.halutama_action)
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\news.png", "Berita", 20, 270, self.controller.berita_action)
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\+ umkm.png", "Daftar UKM", 20, 370, self.controller.daftar_ukm)
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\profil.png", "Profil", 20, 470, self.controller.profil_action)

    def create_main_menu(self):
        custom_font = ("Lucida Fax", 50)

        menu = ctk.CTkLabel(self.side_frame, text='Menu', text_color="#483D8B", font=custom_font)
        menu.place(x=75, y=70)

        reg_umkm = ctk.CTkLabel(self.main_frame, text='REGISTRASI UMKM', text_color="#FFFFFF", font=custom_font)
        reg_umkm.place(x=250, y=70)

        nama_label = ctk.CTkLabel(self.main_frame, text='Nama UMKM', text_color="#FFFFFF", font=('Arial', 30))
        nama_label.place(x=150, y=200)
        self.nama_entry = ctk.CTkEntry(self.main_frame, width=550, height=30)
        self.nama_entry.place(x=400, y=200)

        category = ctk.CTkLabel(self.main_frame, text='Kategori', text_color="#FFFFFF", font=('Arial', 30))
        category.place(x=150, y=300)
        self.category_entry = ctk.CTkEntry(self.main_frame, width=550, height=30)
        self.category_entry.place(x=400, y=300)

        number = ctk.CTkLabel(self.main_frame, text='Kontak', text_color="#FFFFFF", font=('Arial', 30))
        number.place(x=150, y=400)
        self.number_entry = ctk.CTkEntry(self.main_frame, width=550, height=30)
        self.number_entry.place(x=400, y=400)

        desc = ctk.CTkLabel(self.main_frame, text='Deskripsi', text_color="#FFFFFF", font=('Arial', 30))
        desc.place(x=150, y=500)
        self.desc_entry = ctk.CTkEntry(self.main_frame, width=550, height=30)
        self.desc_entry.place(x=400, y=500)

        address = ctk.CTkLabel(self.main_frame, text='Alamat', text_color="#FFFFFF", font=('Arial', 30))
        address.place(x=150, y=600)
        self.address_entry = ctk.CTkEntry(self.main_frame, width=550, height=30)
        self.address_entry.place(x=400, y=600)

        submit_btn2 = ctk.CTkButton(self.main_frame, text="Submit", text_color="white", fg_color='#212121', command=self.controller.submit, font=('Arial', 30))
        submit_btn2.place(x=820, y=675)
    
    def create_label_with_image(self, frame, image_path, text, x, y, action):
        image = Image.open(image_path)
        image = ImageOps.fit(image, (80, 80), method=Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        label = Label(frame, text=text, image=photo, compound="left", font=("Arial", 15), fg="#FFFFFF", bg="#212121", cursor="hand2")
        label.image = photo
        label.place(x=x, y=y)
        label.bind("<Button-1>", action)

    def create_label_with_image2(self, frame, image_path, x, y):
        image = Image.open(image_path)
        image = ImageOps.fit(image, (600, 200), method=Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        label = Label(frame, image=photo, borderwidth=0)
        label.image = photo
        label.place(x=x, y=y)

    def show(self):
        self.root.mainloop()

class ProfileView:
    def __init__(self, controller):
        self.controller = controller
        self.root = Tk()
        self.root.title("SideBar Menu")
        self.root.attributes('-fullscreen', True)
        self.fullscreen = True

        # Bind the Escape key to end fullscreen mode
        self.root.bind("<Escape>", self.controller.exit)

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        side_frame_width = int(screen_width * 0.21)
        self.side_frame = ctk.CTkFrame(self.root, width=side_frame_width, height=screen_height, corner_radius=0, fg_color='#212121')
        self.side_frame.pack(side="left", fill="y")

        self.main_frame = ctk.CTkFrame(self.root, corner_radius=0, fg_color='#3b3b3b')
        self.main_frame.pack(side="right", fill="both", expand=True)

    def create_side_menu(self):
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\halaman utama.png", "Halaman Utama", 20, 170, self.controller.halutama_action)
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\news.png", "Berita", 20, 270, self.controller.berita_action)
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\+ umkm.png", "Daftar UKM", 20, 370, self.controller.daftar_ukm)
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\profil.png", "Profil", 20, 470, self.controller.profil_action)

    def create_main_menu(self):
        custom_font = ("Lucida Fax", 50)

        reg_umkm = ctk.CTkLabel(self.main_frame, text='Profile', text_color="#FFFFFF", font=custom_font)
        reg_umkm.place(x=500, y=70)

        menu = ctk.CTkLabel(self.side_frame, text='Menu', text_color="#483D8B", font=custom_font)
        menu.place(x=75, y=70)

        image_path = r"C:\Users\VICTUS\Downloads\profil pengguna.png"  # Ganti dengan path ke gambar Anda
        image = Image.open(image_path)
        image = ImageOps.fit(image, (250, 250), method=Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        image_label = Label(self.main_frame, image=photo, borderwidth=0)
        image_label.image = photo
        image_label.place(x=450, y=150)

        self.nama_akun_label = ctk.CTkLabel(self.main_frame, text='Nama Akun', text_color="#FFFFFF", font=('Arial', 30))
        self.nama_akun_label.place(x=500, y=400)

        self.nama_akun_entry = ctk.CTkEntry(self.main_frame, width=450, height=50)
        self.nama_akun_entry.place(x=350, y=440)
        self.nama_akun_entry.insert(0, 'Alice')

        self.email_label = ctk.CTkLabel(self.main_frame, text='Email', text_color="#FFFFFF", font=('Arial', 30))
        self.email_label.place(x=530, y=520)

        self.email_entry = ctk.CTkEntry(self.main_frame, width=450, height=50)
        self.email_entry.place(x=350, y=560)
        self.email_entry.insert(0, "alice@ugm.ac.id")

        signout_btn = ctk.CTkButton(self.main_frame, text='Sign Out', bg_color="black", fg_color='#212121', width=100, height=50, command=self.controller.exit, font=('Arial', 30))
        signout_btn.place(x=510, y=700)

    def create_label_with_image(self, frame, image_path, text, x, y, action):
        image = Image.open(image_path)
        image = ImageOps.fit(image, (80, 80), method=Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        label = Label(frame, text=text, image=photo, compound="left", font=("Arial", 15), fg="#FFFFFF", bg="#212121", cursor="hand2")
        label.image = photo
        label.place(x=x, y=y)
        label.bind("<Button-1>", action)

    def create_option_box(self):
        options = ['Profile Akun', 'Profile Toko']
        self.option_var = StringVar(value=options[0])
        self.option_var.trace("w", self.controller.switch_profile)
        option_box = ctk.CTkOptionMenu(self.main_frame, variable=self.option_var, values=options, font=('Arial', 20), width=150, height=50)
        option_box.place(x=1000, y=20)

    def show_profile(self, user):
        self.nama_akun_entry.delete(0, END)
        self.nama_akun_entry.insert(0, user['nama'])
        self.email_entry.delete(0, END)
        self.email_entry.insert(0, user['email'])

    def show(self):
        self.root.mainloop()

class ProfileTokoView:
    def __init__(self, controller):
        self.controller = controller
        self.root = Tk()
        self.root.title("SideBar Menu")
        self.root.attributes('-fullscreen', True)
        self.fullscreen = True

        # Bind the Escape key to end fullscreen mode
        self.root.bind("<Escape>", self.controller.end_fullscreen)
        
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Menghitung lebar untuk side frame sebagai 21% dari lebar layar
        side_frame_width = int(screen_width * 0.21)

        # Membuat side_frame dengan lebar yang ditentukan
        self.side_frame = ctk.CTkFrame(self.root, width=side_frame_width, height=screen_height, corner_radius=0, fg_color='#212121')
        self.side_frame.pack(side="left", fill="y")

        self.main_frame = ctk.CTkFrame(self.root, corner_radius=0, fg_color='#3b3b3b')
        self.main_frame.pack(side="right", fill="both", expand=True)

    def create_side_menu(self):
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\halaman utama.png", "Halaman Utama", 20, 170, self.controller.halutama_action)
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\news.png", "Berita", 20, 270, self.controller.berita_action)
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\+ umkm.png", "Daftar UKM", 20, 370, self.controller.daftar_ukm)
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\profil.png", "Profil", 20, 470, self.controller.profil_action)

        custom_font = ("Lucida Fax", 50)

        menu = ctk.CTkLabel(self.side_frame, text='Menu', text_color="#483D8B", font=custom_font)
        menu.place(x=75, y=70)

        reg_umkm = ctk.CTkLabel(self.main_frame, text='Profile Toko', text_color="#FFFFFF", font=("Arial", 60))
        reg_umkm.place(x=425, y=70)

        image_path = r"C:\Users\VICTUS\Downloads\profil umkm.png"  # Ganti dengan path ke gambar Anda
        image = Image.open(image_path)
        image = ImageOps.fit(image, (250, 250), method=Image.Resampling.LANCZOS)  # Sesuaikan ukuran gambar jika perlu
        photo = ImageTk.PhotoImage(image)

        image_label = Label(self.main_frame, image=photo, borderwidth=0)
        image_label.image = photo  # Menyimpan referensi gambar agar tidak dihapus oleh garbage collector
        image_label.place(x=450, y=150)

    def create_main_menu(self):
        self.nama_toko_label = ctk.CTkLabel(self.main_frame, text='Nama Toko', text_color="#FFFFFF", font=('Arial', 30))
        self.nama_toko_label.place(x=500, y=400)

        self.nama_toko_entry = ctk.CTkEntry(self.main_frame, width=450, height=50)
        self.nama_toko_entry.place(x=350, y=440)

        self.alamat_label = ctk.CTkLabel(self.main_frame, text='Alamat', text_color="#FFFFFF", font=('Arial', 30))
        self.alamat_label.place(x=530, y=520)

        self.alamat_entry = ctk.CTkEntry(self.main_frame, width=450, height=50)
        self.alamat_entry.place(x=350, y=560)

        self.kontak_label = ctk.CTkLabel(self.main_frame, text='Kontak', text_color="#FFFFFF", font=('Arial', 30))
        self.kontak_label.place(x=520, y=640)

        self.kontak_entry = ctk.CTkEntry(self.main_frame, width=450, height=50)
        self.kontak_entry.place(x=350, y=680)

        self.edit_btn = ctk.CTkButton(self.main_frame, text='Detail', bg_color="black", fg_color='#212121', width=100, height=50, command=self.controller.detail, font=('Arial', 30))
        self.edit_btn.place(x=525, y=750)

    def update_profile(self, data):
        self.nama_toko_entry.delete(0, 'end')
        self.alamat_entry.delete(0, 'end')
        self.kontak_entry.delete(0, 'end')

        self.nama_toko_entry.insert(0, data.get('nama', ''))
        self.alamat_entry.insert(0, data.get('alamat', ''))
        self.kontak_entry.insert(0, data.get('telepon', ''))

    def create_label_with_image(self, frame, image_path, text, x, y, action):
        image = Image.open(image_path)
        image = ImageOps.fit(image, (80, 80), method=Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        label = Label(frame, text=text, image=photo, compound="left", font=("Arial", 15), fg="#FFFFFF", bg="#212121", cursor="hand2")
        label.image = photo
        label.place(x=x, y=y)
        label.bind("<Button-1>", action)

    def create_option_box(self):
        # Membuat option box
        options = ['Profile Toko', 'Profile Akun']
        self.option_var = StringVar(value=options[0])
        self.option_var.trace("w", self.controller.switch_profile)  # Menghubungkan opsi dengan switch_profile
        option_box = ctk.CTkOptionMenu(self.main_frame, variable=self.option_var, values=options, font=('Arial', 20), width=150, height=50)
        option_box.place(x=1000, y=20)

    def show(self):
        self.root.mainloop()

class DetailTokoView:
    def __init__(self, controller):
        self.controller = controller
        self.root = Tk()
        self.root.title("SideBar Menu")
        self.root.attributes('-fullscreen', True)
        self.fullscreen = True

        # Bind the Escape key to end fullscreen mode
        self.root.bind("<Escape>", self.controller.end_fullscreen)
        
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Menghitung lebar untuk side frame sebagai 25% dari lebar layar
        side_frame_width = int(screen_width * 0.21)

        # Membuat side_frame dengan lebar yang ditentukan
        self.side_frame = ctk.CTkFrame(self.root, width=side_frame_width, height=screen_height, corner_radius=0, fg_color='#212121')
        self.side_frame.pack(side="left", fill="y")

        self.main_frame = ctk.CTkFrame(self.root, corner_radius=0, fg_color='#3b3b3b')
        self.main_frame.pack(side="right", fill="both", expand=True)

        self.image_path = r"C:\Users\VICTUS\Downloads\Profile toko.png"  # Ganti dengan path ke gambar Anda
        image = Image.open(self.image_path)
        image = ImageOps.fit(image, (900, 520), method=Image.Resampling.LANCZOS)  # Sesuaikan ukuran gambar jika perlu
        photo = ImageTk.PhotoImage(image)

        self.image_label = Label(self.main_frame, image=photo, borderwidth=0)
        self.image_label.image = photo  # Menyimpan referensi gambar agar tidak dihapus oleh garbage collector
        self.image_label.place(x=90, y=90)

    def create_side_menu(self):
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\halaman utama.png", "Halaman Utama", 20, 170, self.controller.halutama_action)
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\news.png", "Berita", 20, 270, self.controller.berita_action)
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\+ umkm.png", "Daftar UKM", 20, 370, self.controller.daftar_ukm)
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\profil.png", "Profil", 20, 470, self.controller.profil_action)

    def create_main_menu(self):
        custom_font = ("Lucida Fax", 50)

        self.menu_label = ctk.CTkLabel(self.side_frame, text='Menu', text_color="#483D8B", font=("Arial", 50))
        self.menu_label.place(x=75, y=70)

        self.namaumkmtext_box = Text(self.main_frame, width=20, height=1, wrap="word", font=("Arial", 50), bg="#3b3b3b", fg="#FFFFFF", borderwidth=0)
        self.namaumkmtext_box.place(x=290, y=70)

        self.desc_umkm_label = ctk.CTkLabel(self.main_frame, text='Deskripsi', text_color="#FFFFFF", font=("Arial", 30))
        self.desc_umkm_label.place(x=185, y=530)

        self.desctext_box = Text(self.main_frame, width=35, height=10, wrap="word", font=("Arial", 15), bg="#3b3b3b", fg="#FFFFFF", borderwidth=0)
        self.desctext_box.place(x=185, y=570)

        self.alamat_umkm_label = ctk.CTkLabel(self.main_frame, text='Alamat', text_color="#FFFFFF", font=("Arial", 30))
        self.alamat_umkm_label.place(x=600, y=530)

        self.alamattext_box = Text(self.main_frame, width=30, height=20, wrap="word", font=("Arial", 15), bg="#3b3b3b", fg="#FFFFFF", borderwidth=0)
        self.alamattext_box.place(x=600, y=570)

        self.contact_umkm_label = ctk.CTkLabel(self.main_frame, text='Kontak', text_color="#FFFFFF", font=("Arial", 30))
        self.contact_umkm_label.place(x=600, y=680)

        self.contacttext_box = Text(self.main_frame, width=20, height=1, wrap="word", font=("Arial", 15), bg="#3b3b3b", fg="#FFFFFF", borderwidth=0)
        self.contacttext_box.place(x=600, y=720)

        self.barrier_frame = ctk.CTkFrame(self.main_frame, width=3, height=260, corner_radius=0, fg_color="white")
        self.barrier_frame.place(x=575, y=550)

    def update_profile(self, data):
        self.namaumkmtext_box.delete(1.0, 'end')
        self.desctext_box.delete(1.0, 'end')
        self.contacttext_box.delete(1.0, 'end')
        self.alamattext_box.delete(1.0, 'end')

        self.namaumkmtext_box.insert(1.0, data.get('nama', ''))
        self.desctext_box.insert(1.0, data.get('deskripsi', ''))
        self.contacttext_box.insert(1.0, data.get('telepon', ''))
        self.alamattext_box.insert(1.0, data.get('alamat', ''))

    def create_label_with_image(self, frame, image_path, text, x, y, action):
        image = Image.open(image_path)
        image = ImageOps.fit(image, (80, 80), method=Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        label = Label(frame, text=text, image=photo, compound="left", font=("Arial", 15), fg="#FFFFFF", bg="#212121", cursor="hand2")
        label.image = photo
        label.place(x=x, y=y)
        label.bind("<Button-1>", action)

    def create_label_with_image2(self, frame, image_path, x, y):
        image = Image.open(image_path)
        image = ImageOps.fit(image, (600, 200), method=Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        label = Label(frame, image=photo, borderwidth=0)
        label.image = photo
        label.place(x=x, y=y)

    def show(self):
        self.root.mainloop()

class FnbView:
    def __init__(self, controller):
        self.controller = controller
        self.root = Tk()
        self.root.title("SideBar Menu")
        self.root.attributes('-fullscreen', True)
        self.fullscreen = True

        # Bind the Escape key to end fullscreen mode
        self.root.bind("<Escape>", self.controller.end_fullscreen)
        
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Menghitung lebar untuk side frame sebagai 25% dari lebar layar
        side_frame_width = int(screen_width * 0.21)

        # Membuat side_frame dengan lebar yang ditentukan
        self.side_frame = ctk.CTkFrame(self.root, width=side_frame_width, height=screen_height, corner_radius=0, fg_color='#212121')
        self.side_frame.pack(side="left", fill="y")

        self.main_frame = ctk.CTkFrame(self.root, corner_radius=0, fg_color='#3b3b3b')
        self.main_frame.pack(side="right", fill="both", expand=True)

    def create_side_menu(self):
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\halaman utama.png", "Halaman Utama", 20, 170, self.controller.halutama_action)
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\news.png", "Berita", 20, 270, self.controller.berita_action)
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\+ umkm.png", "Daftar UKM", 20, 370, self.controller.daftar_ukm)
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\profil.png", "Profil", 20, 470, self.controller.profil_action)

        menu = ctk.CTkLabel(self.side_frame, text='Menu', text_color="#483D8B", font=("Arial", 50))
        menu.place(x=75, y=70)

        fnb = ctk.CTkLabel(self.main_frame, text='Food & Beverage', text_color="#FFFFFF", font=("Arial", 50))
        fnb.place(x=125, y=80)

    def create_main_menu(self):
        self.create_label_with_image2(self.main_frame, r"C:\Users\VICTUS\Downloads\list umkm makanan.png", 125, 150)
        self.create_label_with_image2(self.main_frame, r"C:\Users\VICTUS\Downloads\list umkm makanan.png", 125, 310)
        self.create_label_with_image2(self.main_frame, r"C:\Users\VICTUS\Downloads\list umkm makanan.png", 125, 460)

        self.create_label_with_image3(self.main_frame, r"C:\Users\VICTUS\Downloads\seemore.png", 980, 90, self.controller.detail)
        self.create_label_with_image3(self.main_frame, r"C:\Users\VICTUS\Downloads\seemore.png", 980, 280, self.controller.detail)
        self.create_label_with_image3(self.main_frame, r"C:\Users\VICTUS\Downloads\seemore.png", 980, 480, self.controller.detail)

        self.create_label_with_image4(self.main_frame, r"C:\Users\VICTUS\Downloads\bintang.png", 700, 150)
        self.create_label_with_image4(self.main_frame, r"C:\Users\VICTUS\Downloads\bintang.png", 700, 300)
        self.create_label_with_image4(self.main_frame, r"C:\Users\VICTUS\Downloads\bintang.png", 700, 470)

        Headinga = ctk.CTkLabel(self.main_frame, text='UMKM A', text_color="#FFFFFF", font=("Arial", 40))
        Headinga.place(x=750, y=190)

        headingb = ctk.CTkLabel(self.main_frame, text='UMKM B', text_color="#FFFFFF", font=("Arial", 40))
        headingb.place(x=750, y=350)

        Headingc = ctk.CTkLabel(self.main_frame, text='UMKM C', text_color="#FFFFFF", font=("Arial", 40))
        Headingc.place(x=750, y=520)

    def show(self):
        self.root.mainloop()

    def create_label_with_image(self, frame, image_path, text, x, y, action):
        image = Image.open(image_path)
        image = ImageOps.fit(image, (80, 80), method=Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        label = Label(frame, text=text, image=photo, compound="left", font=("Arial", 15), fg="#FFFFFF", bg="#212121", cursor="hand2")
        label.image = photo
        label.place(x=x, y=y)
        label.bind("<Button-1>", action)

    def create_label_with_image2(self, frame, image_path, x, y):
        image = Image.open(image_path)
        image = ImageOps.fit(image, (600, 200), method=Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        label = Label(frame, image=photo, borderwidth=0)
        label.image = photo
        label.place(x=x, y=y)

    def create_label_with_image3(self, frame, image_path, x, y, action):
        image = Image.open(image_path)
        image = ImageOps.fit(image, (250, 250), method=Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        label = Label(frame, image=photo, bd=0)
        label.image = photo  # Menyimpan referensi gambar
        label.place(x=x, y=y)
        label.bind("<Button-1>", action)

    def create_label_with_image4(self, frame, image_path, x, y):
        image = Image.open(image_path)
        image = ImageOps.fit(image, (250, 250), method=Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        label = Label(frame, image=photo, bd=0)
        label.image = photo  # Menyimpan referensi gambar
        label.place(x=x, y=y)
        label.bind("<Button-1>")

class DetailFnbView:
    def __init__(self, controller):
        self.controller = controller
        self.root = Tk()
        self.root.title("SideBar Menu")
        self.root.attributes('-fullscreen', True)
        self.fullscreen = True

        # Bind the Escape key to end fullscreen mode
        self.root.bind("<Escape>", self.controller.end_fullscreen)
        
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Menghitung lebar untuk side frame sebagai 25% dari lebar layar
        side_frame_width = int(screen_width * 0.21)

        # Membuat side_frame dengan lebar yang ditentukan
        self.side_frame = ctk.CTkFrame(self.root, width=side_frame_width, height=screen_height, corner_radius=0, fg_color='#212121')
        self.side_frame.pack(side="left", fill="y")

        self.main_frame = ctk.CTkFrame(self.root, corner_radius=0, fg_color='#3b3b3b')
        self.main_frame.pack(side="right", fill="both", expand=True)

        self.image_path = r"C:\Users\VICTUS\Downloads\example.jpg"  # Ganti dengan path ke gambar Anda
        image = Image.open(self.image_path)
        image = ImageOps.fit(image, (700, 320), method=Image.Resampling.LANCZOS)  # Sesuaikan ukuran gambar jika perlu
        photo = ImageTk.PhotoImage(image)

        self.image_label = Label(self.main_frame, image=photo, borderwidth=0)
        self.image_label.image = photo  # Menyimpan referensi gambar agar tidak dihapus oleh garbage collector
        self.image_label.place(x=180, y=180)

    def create_side_menu(self):
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\halaman utama.png", "Halaman Utama", 20, 170, self.controller.halutama_action)
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\news.png", "Berita", 20, 270, self.controller.berita_action)
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\+ umkm.png", "Daftar UKM", 20, 370, self.controller.daftar_ukm)
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\profil.png", "Profil", 20, 470, self.controller.profil_action)

    def create_main_menu(self):
        custom_font = ("Lucida Fax", 50)

        menu = ctk.CTkLabel(self.side_frame, text='Menu', text_color="#483D8B", font=("Arial", 50))
        menu.place(x=75, y=70)

        reg_umkm = ctk.CTkLabel(self.main_frame, text='UMKM A', text_color="#FFFFFF", font=custom_font)
        reg_umkm.place(x=445, y=70)

        desc_umkm = ctk.CTkLabel(self.main_frame, text='Deskripsi', text_color="#FFFFFF", font=("Arial", 30))
        desc_umkm.place(x=185, y=530)

        alamat_umkm = ctk.CTkLabel(self.main_frame, text='Alamat', text_color="#FFFFFF", font=("Arial", 30))
        alamat_umkm.place(x=600, y=530)

        alamat_umkm = ctk.CTkLabel(self.main_frame, text='Jl. Jalan 20, Yogyakarta, Indonesia', text_color="#FFFFFF", font=("Arial", 15))
        alamat_umkm.place(x=600, y=570)

        alamat_umkm = ctk.CTkLabel(self.main_frame, text='Contact', text_color="#FFFFFF", font=("Arial", 30))
        alamat_umkm.place(x=600, y=610)

        alamat_umkm = ctk.CTkLabel(self.main_frame, text='08123456789', text_color="#FFFFFF", font=("Arial", 20))
        alamat_umkm.place(x=600, y=650)

        text_box = Text(self.main_frame, width=35, height=10, wrap="word", font=("Arial", 15), bg="#3b3b3b", fg="#FFFFFF", borderwidth=0)
        text_box.place(x=185, y=590)
        text_box.insert("1.0", "Ini adalah contoh teks yang.\n" 
                "diinputkan ke dalam kotak teks.\n"
                "Anda bisa menambahkan lebih\n" 
                "banyak teks di sini sesuai kebutuhan.")

        barrier_frame = ctk.CTkFrame(self.main_frame, width=3, height=150, corner_radius=0, fg_color="white")
        barrier_frame.place(x=570, y=550)

    def show(self):
        self.root.mainloop()

    def create_label_with_image(self, frame, image_path, text, x, y, action):
        image = Image.open(image_path)
        image = ImageOps.fit(image, (80, 80), method=Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        label = Label(frame, text=text, image=photo, compound="left", font=("Arial", 15), fg="#FFFFFF", bg="#212121", cursor="hand2")
        label.image = photo
        label.place(x=x, y=y)
        label.bind("<Button-1>", action)

    def create_label_with_image2(self, frame, image_path, x, y):
        image = Image.open(image_path)
        image = ImageOps.fit(image, (600, 200), method=Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        label = Label(frame, image=photo, borderwidth=0)
        label.image = photo
        label.place(x=x, y=y)

class JasaView:
    def __init__(self, controller):
        self.controller = controller
        self.root = Tk()
        self.root.title("SideBar Menu")
        self.root.attributes('-fullscreen', True)
        self.fullscreen = True

        # Bind the Escape key to end fullscreen mode
        self.root.bind("<Escape>", self.controller.end_fullscreen)
        
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Menghitung lebar untuk side frame sebagai 25% dari lebar layar
        side_frame_width = int(screen_width * 0.21)

        # Membuat side_frame dengan lebar yang ditentukan
        self.side_frame = ctk.CTkFrame(self.root, width=side_frame_width, height=screen_height, corner_radius=0, fg_color='#212121')
        self.side_frame.pack(side="left", fill="y")

        self.main_frame = ctk.CTkFrame(self.root, corner_radius=0, fg_color='#3b3b3b')
        self.main_frame.pack(side="right", fill="both", expand=True)

    def create_side_menu(self):
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\halaman utama.png", "Halaman Utama", 20, 170, self.controller.halutama_action)
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\news.png", "Berita", 20, 270, self.controller.berita_action)
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\+ umkm.png", "Daftar UKM", 20, 370, self.controller.daftar_ukm)
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\profil.png", "Profil", 20, 470, self.controller.profil_action)

        menu = ctk.CTkLabel(self.side_frame, text='Menu', text_color="#483D8B", font=("Arial", 50))
        menu.place(x=75, y=70)

        fnb = ctk.CTkLabel(self.main_frame, text='Jasa', text_color="#FFFFFF", font=("Arial", 50))
        fnb.place(x=125, y=80)

    def create_main_menu(self):
        self.create_label_with_image2(self.main_frame, r"C:\Users\VICTUS\Downloads\list umkm jasa.png", 125, 150)
        self.create_label_with_image2(self.main_frame, r"C:\Users\VICTUS\Downloads\list umkm jasa.png", 125, 300)
        self.create_label_with_image2(self.main_frame, r"C:\Users\VICTUS\Downloads\list umkm jasa.png", 125, 450)
        self.create_label_with_image3(self.main_frame, r"C:\Users\VICTUS\Downloads\seemore.png", 1000, 70)
        self.create_label_with_image3(self.main_frame, r"C:\Users\VICTUS\Downloads\seemore.png", 1000, 260)
        self.create_label_with_image3(self.main_frame, r"C:\Users\VICTUS\Downloads\seemore.png", 1000, 460)
        self.create_label_with_image4(self.main_frame, r"C:\Users\VICTUS\Downloads\bintang.png", 700, 150)
        self.create_label_with_image4(self.main_frame, r"C:\Users\VICTUS\Downloads\bintang.png", 700, 300)
        self.create_label_with_image4(self.main_frame, r"C:\Users\VICTUS\Downloads\bintang.png", 700, 470)

        Headinga = ctk.CTkLabel(self.main_frame, text='UMKM A', text_color="#FFFFFF", font=("Arial", 40))
        Headinga.place(x=750, y=210)

        headingb = ctk.CTkLabel(self.main_frame, text='UMKM B', text_color="#FFFFFF", font=("Arial", 40))
        headingb.place(x=750, y=360)

        Headingc = ctk.CTkLabel(self.main_frame, text='UMKM C', text_color="#FFFFFF", font=("Arial", 40))
        Headingc.place(x=750, y=530)

    def show(self):
        self.root.mainloop()

    def create_label_with_image(self, frame, image_path, text, x, y, action):
        image = Image.open(image_path)
        image = ImageOps.fit(image, (80, 80), method=Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        label = Label(frame, text=text, image=photo, compound="left", font=("Arial", 15), fg="#FFFFFF", bg="#212121", cursor="hand2")
        label.image = photo
        label.place(x=x, y=y)
        label.bind("<Button-1>", action)

    def create_label_with_image2(self, frame, image_path, x, y):
        image = Image.open(image_path)
        image = ImageOps.fit(image, (600, 200), method=Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        label = Label(frame, image=photo, borderwidth=0)
        label.image = photo
        label.place(x=x, y=y)

    def create_label_with_image3(self, frame, image_path, x, y):
        image = Image.open(image_path)
        image = ImageOps.fit(image, (250, 250), method=Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        label = Label(frame, image=photo, bd=0)
        label.image = photo  # Menyimpan referensi gambar
        label.place(x=x, y=y)

    def create_label_with_image4(self, frame, image_path, x, y):
        image = Image.open(image_path)
        image = ImageOps.fit(image, (250, 250), method=Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        label = Label(frame, image=photo, bd=0)
        label.image = photo  # Menyimpan referensi gambar
        label.place(x=x, y=y)
        label.bind("<Button-1>")

class FashionView:
    def __init__(self, controller):
        self.controller = controller
        self.root = Tk()
        self.root.title("SideBar Menu")
        self.root.attributes('-fullscreen', True)
        self.fullscreen = True

        # Bind the Escape key to end fullscreen mode
        self.root.bind("<Escape>", self.controller.end_fullscreen)
        
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Menghitung lebar untuk side frame sebagai 25% dari lebar layar
        side_frame_width = int(screen_width * 0.21)

        # Membuat side_frame dengan lebar yang ditentukan
        self.side_frame = ctk.CTkFrame(self.root, width=side_frame_width, height=screen_height, corner_radius=0, fg_color='#212121')
        self.side_frame.pack(side="left", fill="y")

        self.main_frame = ctk.CTkFrame(self.root, corner_radius=0, fg_color='#3b3b3b')
        self.main_frame.pack(side="right", fill="both", expand=True)

    def create_side_menu(self):
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\halaman utama.png", "Halaman Utama", 20, 170, self.controller.halutama_action)
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\news.png", "Berita", 20, 270, self.controller.berita_action)
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\+ umkm.png", "Daftar UKM", 20, 370, self.controller.daftar_ukm)
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\profil.png", "Profil", 20, 470, self.controller.profil_action)

        menu = ctk.CTkLabel(self.side_frame, text='Menu', text_color="#483D8B", font=("Arial", 50))
        menu.place(x=75, y=70)

        fnb = ctk.CTkLabel(self.main_frame, text='Fashion', text_color="#FFFFFF", font=("Arial", 50))
        fnb.place(x=125, y=80)

    def create_main_menu(self):
        self.create_label_with_image2(self.main_frame, r"C:\Users\VICTUS\Downloads\list umkm pakaian.png", 125, 150)
        self.create_label_with_image2(self.main_frame, r"C:\Users\VICTUS\Downloads\list umkm pakaian.png", 125, 300)
        self.create_label_with_image2(self.main_frame, r"C:\Users\VICTUS\Downloads\list umkm pakaian.png", 125, 450)
        self.create_label_with_image3(self.main_frame, r"C:\Users\VICTUS\Downloads\seemore.png", 1000, 70)
        self.create_label_with_image3(self.main_frame, r"C:\Users\VICTUS\Downloads\seemore.png", 1000, 260)
        self.create_label_with_image3(self.main_frame, r"C:\Users\VICTUS\Downloads\seemore.png", 1000, 460)
        self.create_label_with_image4(self.main_frame, r"C:\Users\VICTUS\Downloads\bintang.png", 700, 150)
        self.create_label_with_image4(self.main_frame, r"C:\Users\VICTUS\Downloads\bintang.png", 700, 300)
        self.create_label_with_image4(self.main_frame, r"C:\Users\VICTUS\Downloads\bintang.png", 700, 470)

        Headinga = ctk.CTkLabel(self.main_frame, text='UMKM A', text_color="#FFFFFF", font=("Arial", 40))
        Headinga.place(x=750, y=210)

        headingb = ctk.CTkLabel(self.main_frame, text='UMKM B', text_color="#FFFFFF", font=("Arial", 40))
        headingb.place(x=750, y=360)

        Headingc = ctk.CTkLabel(self.main_frame, text='UMKM C', text_color="#FFFFFF", font=("Arial", 40))
        Headingc.place(x=750, y=530)

    def show(self):
        self.root.mainloop()

    def create_label_with_image(self, frame, image_path, text, x, y, action):
        image = Image.open(image_path)
        image = ImageOps.fit(image, (80, 80), method=Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        label = Label(frame, text=text, image=photo, compound="left", font=("Arial", 15), fg="#FFFFFF", bg="#212121", cursor="hand2")
        label.image = photo
        label.place(x=x, y=y)
        label.bind("<Button-1>", action)

    def create_label_with_image2(self, frame, image_path, x, y):
        image = Image.open(image_path)
        image = ImageOps.fit(image, (600, 200), method=Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        label = Label(frame, image=photo, borderwidth=0)
        label.image = photo
        label.place(x=x, y=y)

    def create_label_with_image3(self, frame, image_path, x, y):
        image = Image.open(image_path)
        image = ImageOps.fit(image, (250, 250), method=Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        label = Label(frame, image=photo, bd=0)
        label.image = photo  # Menyimpan referensi gambar
        label.place(x=x, y=y)

    def create_label_with_image4(self, frame, image_path, x, y):
        image = Image.open(image_path)
        image = ImageOps.fit(image, (250, 250), method=Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        label = Label(frame, image=photo, bd=0)
        label.image = photo  # Menyimpan referensi gambar
        label.place(x=x, y=y)
        label.bind("<Button-1>")

class RandomCatView:
    def __init__(self, controller):
        self.controller = controller
        self.root = Tk()
        self.root.title("SideBar Menu")
        self.root.attributes('-fullscreen', True)
        self.fullscreen = True

        # Bind the Escape key to end fullscreen mode
        self.root.bind("<Escape>", self.controller.end_fullscreen)
        
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Menghitung lebar untuk side frame sebagai 25% dari lebar layar
        side_frame_width = int(screen_width * 0.21)

        # Membuat side_frame dengan lebar yang ditentukan
        self.side_frame = ctk.CTkFrame(self.root, width=side_frame_width, height=screen_height, corner_radius=0, fg_color='#212121')
        self.side_frame.pack(side="left", fill="y")

        self.main_frame = ctk.CTkFrame(self.root, corner_radius=0, fg_color='#3b3b3b')
        self.main_frame.pack(side="right", fill="both", expand=True)

    def create_side_menu(self):
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\halaman utama.png", "Halaman Utama", 20, 170, self.controller.halutama_action)
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\news.png", "Berita", 20, 270, self.controller.berita_action)
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\+ umkm.png", "Daftar UKM", 20, 370, self.controller.daftar_ukm)
        self.create_label_with_image(self.side_frame, r"C:\Users\VICTUS\Downloads\profil.png", "Profil", 20, 470, self.controller.profil_action)

        menu = ctk.CTkLabel(self.side_frame, text='Menu', text_color="#483D8B", font=("Arial", 50))
        menu.place(x=75, y=70)

        fnb = ctk.CTkLabel(self.main_frame, text='Random Category', text_color="#FFFFFF", font=("Arial", 50))
        fnb.place(x=125, y=80)

    def create_main_menu(self):
        self.create_label_with_image2(self.main_frame, r"C:\Users\VICTUS\Downloads\list umkm pakaian.png", 125, 150)
        self.create_label_with_image2(self.main_frame, r"C:\Users\VICTUS\Downloads\list umkm jasa.png", 125, 300)
        self.create_label_with_image2(self.main_frame, r"C:\Users\VICTUS\Downloads\list umkm makanan.png", 125, 450)
        self.create_label_with_image3(self.main_frame, r"C:\Users\VICTUS\Downloads\seemore.png", 1000, 70)
        self.create_label_with_image3(self.main_frame, r"C:\Users\VICTUS\Downloads\seemore.png", 1000, 260)
        self.create_label_with_image3(self.main_frame, r"C:\Users\VICTUS\Downloads\seemore.png", 1000, 460)
        self.create_label_with_image4(self.main_frame, r"C:\Users\VICTUS\Downloads\bintang.png", 700, 150)
        self.create_label_with_image4(self.main_frame, r"C:\Users\VICTUS\Downloads\bintang.png", 700, 300)
        self.create_label_with_image4(self.main_frame, r"C:\Users\VICTUS\Downloads\bintang.png", 700, 470)

        Headinga = ctk.CTkLabel(self.main_frame, text='UMKM A', text_color="#FFFFFF", font=("Arial", 40))
        Headinga.place(x=750, y=210)

        headingb = ctk.CTkLabel(self.main_frame, text='UMKM B', text_color="#FFFFFF", font=("Arial", 40))
        headingb.place(x=750, y=360)

        Headingc = ctk.CTkLabel(self.main_frame, text='UMKM C', text_color="#FFFFFF", font=("Arial", 40))
        Headingc.place(x=750, y=530)

    def show(self):
        self.root.mainloop()

    def create_label_with_image(self, frame, image_path, text, x, y, action):
        image = Image.open(image_path)
        image = ImageOps.fit(image, (80, 80), method=Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        label = Label(frame, text=text, image=photo, compound="left", font=("Arial", 15), fg="#FFFFFF", bg="#212121", cursor="hand2")
        label.image = photo
        label.place(x=x, y=y)
        label.bind("<Button-1>", action)

    def create_label_with_image2(self, frame, image_path, x, y):
        image = Image.open(image_path)
        image = ImageOps.fit(image, (600, 200), method=Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        label = Label(frame, image=photo, borderwidth=0)
        label.image = photo
        label.place(x=x, y=y)

    def create_label_with_image3(self, frame, image_path, x, y):
        image = Image.open(image_path)
        image = ImageOps.fit(image, (250, 250), method=Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        label = Label(frame, image=photo, bd=0)
        label.image = photo  # Menyimpan referensi gambar
        label.place(x=x, y=y)

    def create_label_with_image4(self, frame, image_path, x, y):
        image = Image.open(image_path)
        image = ImageOps.fit(image, (250, 250), method=Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        label = Label(frame, image=photo, bd=0)
        label.image = photo  # Menyimpan referensi gambar
        label.place(x=x, y=y)
        label.bind("<Button-1>")
