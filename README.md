# Tugas PBP Django

## Identitas
- **Nama**: Muhammad Azzam Fathurrahman  
- **NPM**: 2406412152  
- **Kelas**: B
- **Link PWS**: [muhammad-azzam42-thecorner.pbp.cs.ui.ac.id](https://muhammad-azzam42-thecorner.pbp.cs.ui.ac.id/)

-----------------------------

# Tugas 2 

## Implementasi Checklist
1. Membuat proyek Django baru dengan `django-admin startproject`.
2. Membuat aplikasi `main` dengan `python manage.py startapp main` dan menambahkannya di `INSTALLED_APPS`.
3. Menambahkan routing di `urls.py` agar aplikasi `main` bisa diakses.
4. Membuat model `Product` dengan atribut: name, price, description, thumbnail, category, is_featured, stock, rating.
5. Membuat fungsi di `views.py` untuk menampilkan nama aplikasi dan identitas.
6. Membuat routing di `main/urls.py` untuk fungsi tersebut.
7. Deploy ke PWS sehingga aplikasi bisa diakses melalui link.


## Bagan Request–Response
![Bagan Request Response](bagan.png)


## Jawaban Pertanyaan
1. **Peran settings.py**: pusat konfigurasi proyek (database, apps, middleware, dll).  
2. **Migrasi database**: `makemigrations` membuat file migrasi, `migrate` menerapkan ke database.  
3. **Kenapa Django dipilih**: mudah dipahami (pakai Python), konsep MVT jelas, fitur bawaan lengkap, dokumentasi bagus.  
4. **Feedback asisten**: sudah baik.  

-----------------------------

# Tugas 3 

## Implementasi Checklist
1. Menambahkan **empat fungsi views**: XML, JSON, XML by ID, JSON by ID.  
2. Menambahkan routing URL untuk masing-masing views.  
3. Membuat halaman utama dengan tombol **Add** (form) dan **Detail** (halaman detail).  
4. Membuat halaman form menggunakan `ModelForm`.  
5. Membuat halaman detail objek.  
6. Menjawab pertanyaan pada README.  
7. Mengakses endpoint dengan Postman dan menambahkan screenshot.  
8. Melakukan add-commit-push ke GitHub.  


## Jawaban Pertanyaan
1. **Data delivery**: agar data dari server bisa dikirim ke client dengan format standar.  
2. **JSON vs XML**: JSON lebih populer karena ringan, mudah dibaca, cepat diproses.  
3. **is_valid()**: memeriksa validasi form sebelum data disimpan.  
4. **csrf_token**: melindungi dari serangan CSRF, tanpa ini form bisa dimanfaatkan penyerang.  
5. **Step by step**: buat views → routing → halaman index + tombol → form → detail → test di Postman → push ke GitHub.  
6. **Feedback**: sudah baik, penjelasan jelas.  


## Screenshot Postman
- JSON Endpoint: ![JSON Screenshot](json.png)  
- XML Endpoint: ![XML Screenshot](xml.png)  
- JSON by ID Endpoint: ![JSON by ID Screenshot](json-id.png)  
- XML by ID Endpoint: ![XML by ID Screenshot](xml-id.png)  


-----------------------------

# Tugas 4

## Implementasi Checklist

1. Menambahkan django.contrib.auth dan django.contrib.sessions di INSTALLED_APPS.
2. Mengatur LOGIN_URL, LOGIN_REDIRECT_URL, dan LOGOUT_REDIRECT_URL di settings.py.
3. Menambahkan accounts/ routing dengan django.contrib.auth.urls.
4. Membuat template login dengan {% csrf_token %} menggunakan AuthenticationForm atau custom form.
5. Menggunakan @login_required atau LoginRequiredMixin untuk proteksi halaman tertentu.
6. Menguji login dan logout, lalu mengecek cookies dan session di browser.
7. Menambahkan jawaban pertanyaan di README dan melakukan add-commit-push ke GitHub.

## Jawaban Pertanyaan

1. **Django AuthenticationForm** 
AuthenticationForm adalah form bawaan Django untuk login dengan username dan password.
Kelebihan: aman, mudah digunakan, langsung terintegrasi dengan sistem auth Django.
Kekurangan: hanya mendukung username-password, tampilan default sederhana, perlu kustomisasi jika butuh fitur lanjutan.

2. **Autentikasi vs Otorisasi**
Autentikasi: proses memverifikasi identitas pengguna (misalnya login).
Otorisasi: proses menentukan hak akses atau izin yang dimiliki pengguna.
Di Django: autentikasi menggunakan User, session, dan authenticate(). Otorisasi menggunakan permissions, groups, dan decorator @login_required.

3. **Perbedaan Session dan Cookies**
Session: data disimpan di server, lebih aman, bisa menyimpan banyak data, tapi membutuhkan storage server.
Cookies: data disimpan di browser, simpel dan ringan, tetapi kapasitas terbatas dan lebih rentan dicuri.

4. **Apakah cookies aman?**
Cookies tidak sepenuhnya aman. Risiko seperti XSS, CSRF, atau cookie theft bisa terjadi. Django mengurangi risiko dengan CSRF middleware, session server-side, enkripsi/tanda tangan cookie, serta opsi HttpOnly, Secure, dan SameSite.