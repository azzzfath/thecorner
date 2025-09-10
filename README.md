Nama: Muhammad Azzam Fathurrahman 
NPM: 2406412152
Kelas: C  

https://muhammad-azzam42-thecorner.pbp.cs.ui.ac.id/


## Implementasi Checklist
1. Membuat proyek Django baru dengan `django-admin startproject`.
2. Membuat aplikasi `main` dengan `python manage.py startapp main` dan menambahkannya di `INSTALLED_APPS`.
3. Menambahkan routing di `urls.py` agar aplikasi `main` bisa diakses.
4. Membuat model `Product` dengan atribut: name, price, description, thumbnail, category, is_featured, stock, rating
5. Membuat fungsi di `views.py` untuk menampilkan nama aplikasi dan identitas.
6. Membuat routing di `main/urls.py` untuk fungsi tersebut.
7. Deploy ke PWS sehingga aplikasi bisa diakses melalui link.


## Bagan Request–Response
![Bagan Request Response](bagan.png)


## Jawaban Pertanyaan
1. *Peran settings.py*: pusat konfigurasi proyek (database, apps, middleware, dll) 
2. *Migrasi database*: makemigrations membuat file migrasi, migrate menerapkan ke database  
3. *Kenapa Django dipilih*: mudah dipahami (pakai Python), konsep MVT jelas, fitur bawaan lengkap, dokumentasi bagus
4. **Feedback asisten**: sudah baik
