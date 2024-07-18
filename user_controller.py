# controller.py
from user_model import find_user
from user_view import LoginView, RegisterView, RegUMKMView
from user_model import save_user, find_user 
from user_view import MenuView, ProfileTokoView, DetailFnbView, DetailTokoView, DetailNewsView, NewsView, RandomCatView, RegUMKMView, ProfileView, FnbView, FashionView, JasaView
import json
from user_model import UMKMModel
from tkinter import StringVar, messagebox

class LoginController:
    def __init__(self):
        self.view = LoginView(self)

    def guest_btn(self):
        self.view.root.destroy()
        RegisterController().run()  # Switch to the registration page

    def log_btn(self):
        email = self.view.nama_entry.get()
        password = self.view.pass_entry.get()

        user = find_user(email, password)
        
        if user:
            self.view.show_message('Success', 'Login Successful')
            self.view.root.destroy()
            MenuController(user=user).run() # Redirect to the dashboard or main application page
        else:
            self.view.show_message('Error', 'Username or password incorrect', error=True)

    def run(self):
        self.view.show()

class RegisterController:
    def __init__(self):
        self.view = RegisterView(self)

    def bck_btn(self):
        self.view.root.destroy()
        LoginController().run()  # Redirect to the login page

    def register_user(self):
        nama = self.view.nama_entry.get()
        email = self.view.email_entry.get()
        password = self.view.pass_entry.get()

        if not (nama and email and password):
            self.view.show_message('Error', 'All fields are required', error=True)
            return

        user = {
            'nama': nama,
            'email': email,
            'password': password,
        }

        try:
            save_user(user)
            self.view.show_message('Success', 'Registration Successful')
            self.view.root.destroy()
            LoginController().run()  # Redirect to the login page after successful registration
        except Exception as e:
            self.view.show_message('Error', f'An error occurred: {e}', error=True)

    def run(self):
        self.view.show()

class MenuController:
    def __init__(self, user=None):
        self.user = user
        self.view = MenuView(self)

    def toggle_fullscreen(self, event=None):
        self.view.fullscreen = not self.view.fullscreen
        self.view.root.attributes("-fullscreen", self.view.fullscreen)
        return "break"

    def end_fullscreen(self, event=None):
        self.view.root.quit()

    def profile_action(self, event):
        self.view.root.destroy()
        ProfileController(user=self.user).run()

    def halutama_action(self, event):
        self.view.root.destroy()
        MenuController().run()

    def berita_action(self, event):
        self.view.root.destroy()
        NewsController().run()
        
    def daftar_ukm(self, event):
        self.view.root.destroy()
        RegUMKMController().run()

    def profil_action(self, event):
        self.view.root.destroy()
        ProfileController().run()

    def fnb(self, event):
        self.view.root.destroy()
        FnbController().run()

    def toko(self, event):
        self.view.root.destroy()
        RandomCatController().run()

    def jasa(self, event):
        self.view.root.destroy()
        JasaController().run()

    def fashion(self, event):
        self.view.root.destroy()
        FasionController().run()

    def run(self):
        self.view.show()

class NewsController:
    def __init__(self):
        self.view = NewsView(self)

    def toggle_fullscreen(self, event=None):
        self.view.fullscreen = not self.view.fullscreen
        self.view.root.attributes("-fullscreen", self.view.fullscreen)
        return "break"

    def end_fullscreen(self, event=None):
        self.view.root.quit()

    def halutama_action(self, event):
        self.view.root.destroy()
        MenuController().run()
    
    def berita_action(self, event):
        self.view.root.destroy()
        NewsController().run()

    def daftar_ukm(self, event):
        self.view.root.destroy()
        RegUMKMController().run()

    def profil_action(self, event):
        self.view.root.destroy()
        ProfileController

    def detail(self, event):
        self.view.root.destroy()
        DetailNewsController().run()

    def run(self):
        self.view.create_side_menu()  # Tampilkan side menu
        self.view.create_main_menu()  # Tampilkan main menu
        self.view.show()

class DetailNewsController:
    def __init__(self):
        self.view = DetailNewsView(self)

    def toggle_fullscreen(self, event=None):
        self.view.fullscreen = not self.view.fullscreen
        self.view.root.attributes("-fullscreen", self.view.fullscreen)
        return "break"

    def end_fullscreen(self, event=None):
        self.view.root.quit()

    def halutama_action(self, event):
        self.view.root.destroy()
        MenuController().run()
    
    def berita_action(self, event):
        self.view.root.destroy()
        NewsController().run()

    def daftar_ukm(self, event):
        self.view.root.destroy()
        RegUMKMController().run()

    def profil_action(self, event):
        self.view.root.destroy()
        ProfileController().run()

    def run(self):
        self.view.create_side_menu()  # Tampilkan side menu
        self.view.create_main_menu()  # Tampilkan main menu
        self.view.show()  

class RegUMKMController:
    def __init__(self):
        self.view = RegUMKMView(self)
        self.model = UMKMModel()

    def toggle_fullscreen(self, event=None):
        self.view.fullscreen = not self.view.fullscreen
        self.view.root.attributes("-fullscreen", self.view.fullscreen)
        return "break"

    def end_fullscreen(self, event=None):
        self.view.root.quit()

    def submit(self):
        nama = self.view.nama_entry.get()
        category = self.view.category_entry.get()
        kontak = self.view.number_entry.get()
        desc = self.view.desc_entry.get()
        alamat = self.view.address_entry.get()

        if nama and category and kontak and desc and alamat:
            data = {
                "nama": nama,
                "kategori": category,
                "telepon": kontak,
                "deskripsi": desc,
                "alamat": alamat
            }
            self.model.save_data(data)
            messagebox.showinfo("Success", "Data berhasil disimpan!")
            self.view.root.destroy()
            ProfileTokoController().run()
        else:
            messagebox.showwarning("Peringatan", "Harap isi semua field.")

    def halutama_action(self, event):
        self.view.root.destroy()
        MenuController().run()

    def berita_action(self, event):
        self.view.root.destroy()
        NewsController().run()
        
    def daftar_ukm(self, event):
        self.view.root.destroy()
        RegUMKMController().run()

    def profil_action(self, event):
        self.view.root.destroy()
        ProfileController().run()

    def run(self):
        self.view.create_side_menu()
        self.view.create_main_menu()
        self.view.show()

class ProfileController:
    def __init__(self, user=None):
        self.user = user
        self.view = ProfileView(self)

    def toggle_fullscreen(self, event=None):
        self.view.fullscreen = not self.view.fullscreen
        self.view.root.attributes("-fullscreen", self.view.fullscreen)
        return "break"

    def end_fullscreen(self, event=None):
        self.view.root.quit()

    def halutama_action(self, event):
        self.view.root.destroy()
        MenuController(user=self.user).run()

    def berita_action(self, event):
        self.view.root.destroy()
        NewsController().run()

    def daftar_ukm(self, event):
        self.view.root.destroy()
        RegUMKMController().run()

    def profil_action(self, event):
        self.view.root.destroy()
        ProfileController(user=self.user).run()

    def exit(self, event=None):
        self.view.root.destroy()

    def switch_profile(self, *args):
        selected_profile = self.view.option_var.get()
        if selected_profile == "Profile Akun":
            self.view.root.destroy()
            ProfileController(user=self.user).run()
        elif selected_profile == "Profile Toko":
            self.view.root.destroy()
            ProfileTokoController().run()

    def run(self):
        self.view.create_side_menu()
        self.view.create_main_menu()
        self.view.create_option_box()
        self.view.show()

class ProfileTokoController:
    def __init__(self):
        self.view = ProfileTokoView(self)
        self.model = UMKMModel()

    def toggle_fullscreen(self, event=None):
        self.view.fullscreen = not self.view.fullscreen
        self.view.root.attributes("-fullscreen", self.view.fullscreen)
        return "break"

    def end_fullscreen(self, event=None):
        self.view.root.quit()

    def halutama_action(self, event):
        self.view.root.destroy()
        MenuController().run()

    def berita_action(self, event):
        self.view.root.destroy()
        NewsController().run()

    def daftar_ukm(self, event):
        self.view.root.destroy()
        RegUMKMController().run()

    def profil_action(self, event):
        self.view.root.destroy()
        ProfileController

    def exit(self):
        self.view.root.destroy()

    def switch_profile(self, *args):
        selected_profile = self.view.option_var.get()
        if selected_profile == "Profile Akun":
            self.view.root.destroy()
            ProfileController().run()
        elif selected_profile == "Profile Toko":
            self.view.root.destroy()
            ProfileTokoController().run()

    def detail(self):
        self.view.root.destroy()
        DetailTokoController().run()
            
    def run(self):
        self.view.create_side_menu()
        self.view.create_main_menu()
        self.view.create_option_box()
        self.load_profile_data()
        self.view.show()

    def load_profile_data(self):
        data = self.model.load_data()
        self.view.update_profile(data)

class DetailTokoController:
    def __init__(self):
        self.view = DetailTokoView(self)
        self.model = UMKMModel()

    def toggle_fullscreen(self, event=None):
        self.view.fullscreen = not self.view.fullscreen
        self.view.root.attributes("-fullscreen", self.view.fullscreen)
        return "break"

    def end_fullscreen(self, event=None):
        self.view.root.quit()

    def halutama_action(self, event):
        self.view.root.destroy()
        MenuController().run()

    def berita_action(self, event):
        self.view.root.destroy()
        NewsController().run()

    def daftar_ukm(self, event):
        self.view.root.destroy()
        RegUMKMController().run()

    def profil_action(self, event):
        self.view.root.destroy()
        ProfileController().run()

    def load_profile_data(self):
        data = self.model.load_data()
        self.view.update_profile(data)
            
    def run(self):
        self.view.create_side_menu()
        self.view.create_main_menu()
        self.load_profile_data()
        self.view.show()

class FnbController:
    def __init__(self):
        self.view = FnbView(self)

    def toggle_fullscreen(self, event=None):
        self.view.fullscreen = not self.view.fullscreen
        self.view.root.attributes("-fullscreen", self.view.fullscreen)
        return "break"

    def end_fullscreen(self, event=None):
        self.view.root.quit()

    def halutama_action(self, event):
        self.view.root.destroy()
        MenuController().run()
    
    def berita_action(self, event):
        self.view.root.destroy()
        NewsController().run()

    def daftar_ukm(self, event):
        self.view.root.destroy()
        RegUMKMController().run()

    def profil_action(self, event):
        self.view.root.destroy()
        ProfileController().run()

    def detail(self, event):
        self.view.root.destroy()
        DetailFnbController().run()

    def run(self):
        self.view.create_side_menu()  # Tampilkan side menu
        self.view.create_main_menu()  # Tampilkan main menu
        self.view.show()  

class DetailFnbController:
    def __init__(self):
        self.view = DetailFnbView(self)

    def toggle_fullscreen(self, event=None):
        self.view.fullscreen = not self.view.fullscreen
        self.view.root.attributes("-fullscreen", self.view.fullscreen)
        return "break"

    def end_fullscreen(self, event=None):
        self.view.root.quit()

    def halutama_action(self, event):
        self.view.root.destroy()
        MenuController().run()
    
    def berita_action(self, event):
        self.view.root.destroy()
        NewsController().run()

    def daftar_ukm(self, event):
        self.view.root.destroy()
        RegUMKMController().run()

    def profil_action(self, event):
        self.view.root.destroy()
        ProfileController().run()

    def run(self):
        self.view.create_side_menu()  # Tampilkan side menu
        self.view.create_main_menu()  # Tampilkan main menu
        self.view.show() 

class JasaController:
    def __init__(self):
        self.view = JasaView(self)

    def toggle_fullscreen(self, event=None):
        self.view.fullscreen = not self.view.fullscreen
        self.view.root.attributes("-fullscreen", self.view.fullscreen)
        return "break"

    def end_fullscreen(self, event=None):
        self.view.root.quit()

    def halutama_action(self, event):
        self.view.root.destroy()
        MenuController().run()
    
    def berita_action(self, event):
        self.view.root.destroy()
        NewsController().run()

    def daftar_ukm(self, event):
        self.view.root.destroy()
        RegUMKMController().run()

    def profil_action(self, event):
        self.view.root.destroy()
        ProfileController().run()

    def run(self):
        self.view.create_side_menu()  # Tampilkan side menu
        self.view.create_main_menu()  # Tampilkan main menu
        self.view.show()  

class FasionController:
    def __init__(self):
        self.view = FashionView(self)

    def toggle_fullscreen(self, event=None):
        self.view.fullscreen = not self.view.fullscreen
        self.view.root.attributes("-fullscreen", self.view.fullscreen)
        return "break"

    def end_fullscreen(self, event=None):
        self.view.root.quit()

    def halutama_action(self, event):
        self.view.root.destroy()
        MenuController().run()
    
    def berita_action(self, event):
        self.view.root.destroy()
        NewsController().run()

    def daftar_ukm(self, event):
        self.view.root.destroy()
        RegUMKMController().run()

    def profil_action(self, event):
        self.view.root.destroy()
        ProfileController().run()

    def run(self):
        self.view.create_side_menu()  # Tampilkan side menu
        self.view.create_main_menu()  # Tampilkan main menu
        self.view.show()  

class RandomCatController:
    def __init__(self):
        self.view = RandomCatView(self)

    def toggle_fullscreen(self, event=None):
        self.view.fullscreen = not self.view.fullscreen
        self.view.root.attributes("-fullscreen", self.view.fullscreen)
        return "break"

    def end_fullscreen(self, event=None):
        self.view.root.quit()

    def halutama_action(self, event):
        self.view.root.destroy()
        MenuController().run()
    
    def berita_action(self, event):
        self.view.root.destroy()
        NewsController().run()

    def daftar_ukm(self, event):
        self.view.root.destroy()
        RegUMKMController().run()

    def profil_action(self, event):
        self.view.root.destroy()
        ProfileController().run()

    def run(self):
        self.view.create_side_menu()  # Tampilkan side menu
        self.view.create_main_menu()  # Tampilkan main menu
        self.view.show() 

controller = LoginController()
controller.run()
