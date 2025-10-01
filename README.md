Tautan Aplikasi PWS: [https://maira-azma-footballshop.pbp.cs.ui.ac.id/](https://maira-azma-footballshop.pbp.cs.ui.ac.id/)

# TUGAS 2

**1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**  
Pertama-tama, saya membaca checklist sampai habis, untuk melihat requirement apa yang dibutuhkan sebelum saya memulai. Kemudian, saya melakukan simplifikasi (karena saya melihat ada beberapa step pada tutorial yang tidak perlu dilakukan, contohnya push bisa dilakukan di akhir saja). Pada pengerjaan ini, saya learning by doing. Pada tutorial 0 dan 1, ada beberapa step yang memang sudah saya pahami. Namun, untuk step-step yang belum terlalu saya pahami, saya bertanya kepada teman saya atau mengonfirmasi pemahaman saya dengan bertanya kepada ChatGPT. 

**2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.**  
![alt text](image.png)
Ketika request client diterima, urls.py akan langsung dijalankan untuk memastikan bahwa url yang ingin diakses client tersedia. Ketika url valid, maka akan dipanggil fungsi pada views.py sesuai url masing-masing. Pada views.py, dipastikan terlebih dahulu bahwa client memang memiliki hak akses untuk url tersebut. Jika client sudah punya izin akses, dapat dilakukan pengambilan database, dan pemilihan tampilan. Setiap halaman memiliki tampilannya masing-masing, views.py membantu kita memilah berbagai template untuk berbagai halaman. Ketika data sudah siap, barulah dilakukan query pada models.py. Selanjutnya, begitu tampilan sudah disesuaikan dan data-data yang akan ditampilkan sudah diproses, Django akan menyesuaikan kedua hal itu sesuai file html pada folder 'templates'. Terakhir, barulah halaman bisa ditampilkan kepada client (Response).

**3. Jelaskan peran settings.py dalam proyek Django!**  
Sesuai namanya, settings.py dalam proyek Django memiliki peran sebagai pengaturan utama proyek secara keseluruhan. File tersebut menyimpan environment yang perlu di-install sebelum proyek dijalankan, hal ini untuk memastikan bahwa semua yang mengakses aplikasi tersebut dapat menjalankan semua fitur dengan baik. Pengaturan keamanan juga dikelola di sini, siapa saja yang dapat mengakses, apa saja yang dapat diakses, dan lain-lain. Jadi, settings.py adalah pengaturan, dengan cara apa, seperti apa, dan menggunakan apa aplikasi akan berjalan. 

**4. Bagaimana cara kerja migrasi database di Django?**  
Pertama-tama, ketika file models.py berubah, kita perlu memberitahu sistem bahwa kita melakukan perubahan dengan command 'python manage.py makemigrations'. Kemudian sistem akan mendefinisikan perubahan tersebut. Selanjutnya, ketika command 'python manage.py migrate' dijalankan, sistem barulah membaca pendefinisian perubahan tadi dan menerapkannya ke database. Jadi, perubahan model bisa berdampak pada perubahan database (mungkin dibuat fungsi baru, atau fungsi yang dirubah cara kerjanya). Maka dari itu, setiap melakukan perubahan pada model, kita perlu memastikan bahwa sistem telah memahami perubahan tersebut agar cara kerjanya sudah aman untuk diaplikasikan ke database.

**5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?**  
Menurut saya, struktur file Django yang terorganisir membuat saya lebih mudah memahami alur kerja sebuah web. Penamaan file yang representatif memudahkan developer untuk mengatur file jika nanti jumlahnya sudah banyak (misal sudah ada beberapa aplikasi). Selain itu, setelah saya telusuri lagi, setiap default code diberikan command yang mudah dipahami. Hal ini mendukung developer-developer baru untuk memahami fungsi file, bahkan tiap baris code yang ada pada file tersebut. 

**6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?**  
Gak adaa, sudah jelas kok :D

# TUGAS 3

**1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**  
Data delivery merupakan sebuah sistem bagaimana data-data dikirim antara frontend, backend, external user, dll. Pada dasarnya, sebuah platform hanyalah wadah untuk memberikan data dengan cara yang lebih interaktif. Demikian data adalah pilar utama sebuah platform, cara kita memperlakukan data tersebut juga harus menjadi pertimbangan. Maka dari itu, data delivery menjadi aspek penting dalam pengimplementasian sebuah platform.

**2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?**  
Saya lebih umum bekerja dengan JSON dibandingkan XML, maka menurut saya JSON lebih baik. Jika diperhatikan lagi, struktur JSON lebih mudah dipahami bagi orang-orang yang baru belajar mengenai struktur data karena bentuknya yang lebih mirip set pada bahasa python. Pada pengembangan platform, JSON lebih sering dipakai sebab dia juga merupakan pengembangan dari JavaScript. Kita tahu bahwa JavaScript sudah menjadi bahasa scripting yang sangat umum digunakan di kalangan para developer. Kerelevanan JavaScript dan JSON menjadi suatu kemudahan bagi developer untuk melakukan pengintegrasian data. Dengan demikian, saya rasa JSON masih lebih populer dari XML.

**3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut**  
is_valid() pada form digunakan untuk memastikan bahwa input yang user berikan pada form sudah sesuai. Tiap form biasanya akan meminta data, data tersebut kemudian akan disimpan di database. Maka dari itu, sebelum disimpan, harus dipastikan bahwa data sudah sesuai (tipenya, batas karakternya, dll). Method is_valid() membantu kita untuk mengidentifikasi input, fungsi tersebut dapat memberikan error jika input tidak sesuai. Bila semua input sudah sesuai dengan database yang telah dideklarasikan pada models.py, data sudah bisa dimasukkan ke database.

**4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?**  
csrf_token digunakan untuk meningkatkan keamanan platform. CSRF (Cross-Site Request Forgery) akan mencegah adanya pengiriman form dari cookie yang berbeda (ketika form dikirim dan ketika user login). Jadi ketika user mengawali sebuah sesi, sebuah token akan dibuat dan diberlakukan pada setiap POST. Maka, server hanya akan merespon jika token valid.

Jika tidak ada csrf_token, server tidak akan memastikan kembali cookie sesi dan menerima semua perintah yang di-request. Contoh, seorang penyerang login pada akun pengguna pada link A, kemudian penyerang tersebut mengakses suatu situs lain yang memungkinkannya untuk men-submit form pada link A. Jika tidak ada csrf_token, server akan menganggap form yang masuk adalah valid. Padahal, itu adalah usaha penyerang untuk melakukan submit form melalui situs luar.

**5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**  
Pertama-tama, saya membaca keseluruhan dokumen untuk memberikan gambaran apa saja yang perlu saya kerjakan. Ketika membaca, saya menyadari bahwa alurnya sedikit berbeda dengan tutorial, namun saya pikir step-by-step tidak terlalu penting karena nantinya semua file akan saling terhubung selama fungsinya berjalan. Saya mulai dengan menambahkan 4 fungsi baru di `views.py` untuk memungkinkan saya mengakses database dalam bentuk XML atau JSON, dan mencari data melalui id. Tidak lupa untuk menghubungkannya pada `urls.py` agar fungsi dapat berjalan dan diakses. Ada sedikit kendala ketika membuat page `create_product` dan `product_detail` karena saya sudah mencoba styling HTML sebelumnya. Beberapa penyesuaian saya lakukan, sekali-kali meminta ChatGPT untuk membantu saya. Masalah juga sedikit muncul ketika saya run server pertama kali karena penyesuaian dengn HTML tadi. *Trial and error* tersebut membuat saya lebih memahami alur web development.

**6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?**  
Seperti biasa sudah sangat jelassss.

## Screenshot Postman
### Screenshot akses ../json/
![alt text](image-1.png)

### Screenshot akses ../xml/
![alt text](image-2.png)

### Screenshot akses ../json/[id]
![alt text](image-3.png)

### Screenshot akses ../xml/[id]
![alt text](image-4.png)

# TUGAS 4

**1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.**  
Django AuthenticationForm adalah suatu built-in class dari Django yang dapat membuat form untuk membuka akses bagi sebuah akun user untuk masuk ke suatu situs. Seperti sifat class pada umumnya, AuthenticationForm memiliki atribut `is_active()` berupa nilai boolean. Upaya login akan ditolak jika atribut ini bernilai `false`. Kelebihannya, karena class ini sudah dibuat oleh Django, fitur-fitur keamanan juga sudah ditangani, seperti serangan CSRF (Cross-Site Request Forgery). Sayangnya, karena class ini telah dibuat oleh Django, kustomisasi harus dilakukan secara manual oleh _developer_. Misal, pesan peringatan default perlu kita ubah sendiri pada HTML dan CSS, bagian layout form juga perlu kita kustomisasi manual karena Django hanya membuat sebuah template yang tidak menarik.

Source: [https://docs.djangoproject.com/en/5.2/topics/auth/default/](https://docs.djangoproject.com/en/5.2/topics/auth/default/)

**2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?**  
Autentikasi adalah untuk mengidentifikasi sebuah user, sedangkan otorisasi adalah proses memverifikasi akses-akses apa yang dimiliki sebuah user. Untuk melakukan proses autentikasi, Django membuat beberapa atribut seperti username, password, dan email yang membuat setiap user unik. Atribut-atribut ini akan membantu Django untuk mengidentifikasi user mana yang sedang aktif, yang sedang login, dll. Kemudian untuk proses otorisasi, Django membuat atribut permissions untuk objek user yang dapat dikustomisasi. Django juga menyediakan dekorator untuk fungsi pada `views.py`, contohnya `@login_required`.

**3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?**   
Session dapat menyimpan data sensitif pada lapisan server, seperti user_ID dan attribute sensitif. Namun, karena session disimpan di server, ada batasan session yang dapat ditampung oleh server. Sehingga jika sebuah server diperkirakan akan menyimpan banyak session (akan ada banyak user yang login pada satu waktu), perlu pertimbangan mengenai kapasitas server.

Sementara itu, cookie menyimpan data pada browser masing-masing pengguna. Sehingga tidak akan memberatkan server karena cookie ditanggung masing-masing pengguna. Hanya saja, karena cookie disimpan pada masing-masing pengguna, cookie akan bermasalah jika suatu pengguna misal tidak memiliki/menerima cookie tersebut.

**4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?**  
Cookie menjadi salah satu celah kelamanan suatu website karena disimpan di browser pengguna. Data yang disimpan menjadi rentan terhadap pencurian. Penyerang bisa mengakses cookie dan berpura-pura sebagai user tanpa izin user yang legal. Selain itu, pencurian cookie menjadi bahaya karena data-data yang disimpan bisa jadi diubah seenaknya.

**5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**  
Pertama-tama, saya membaca keseluruhan dokumen untuk memberikan gambaran apa saja yang perlu saya kerjakan. Seperti biasa, step-by-step pada tutorial sebetulnya dapat dijalankan tanpa memerhatikan urutan. Saya mengawali pengerjaan dengan membuat fitur register, login, dan logout, diikuti dengan penyesuaian  template, `views.py`, dan `urls.py`. Setelah itu, barulah saya menghubungkan user dengan objek Product. Begitu semua yang penting sudah dilakukan, saya melanjutkan dengan penyesuaian CSS mengikuti `base.html` yang telah saya rancang sebelumnya. 

# TUGAS 5

**1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!**  
- **!important**  
    Ditulis dengan keterangan `!important` meng-override semua selector.
    ```css
    p { color: #8298c5ff !important; }
    ```
- **Inline Style**  
    Ditulis langsung di bracket elemen.
    ``` html
    <h5 style="color: #404040;">hiluu</h5>
    ```

- **ID Selector**  
    Ditulis dengan keterangan ID.
    ``` css
    #IDSelector { color: #8298c5ff; }
    ```
- **Class, Attribute, Pseudo-class**  
    Ditulis dengan keterangan class, attribute, atau psudo-class.
    ``` css
    .class { color: #8298c5ff; } /* class */
    [type="attribute"] { color: #8298c5ff; } /* attribute */
    a:hover { color: #8298c5ff; } /* pseudo-class */
    ```

- **Element, Pseudo-element**  
    Ditulis keterangan elemennya dan pseudo-element.
    ``` css
    p { color: #8298c5ff; } /* element */
    p::first-line { color: #8298c5ff } /* pseudo-element */
    ```

**2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!**  
Responsive design adalah desain sebuah web yang dapat menyesuaikan beberapa device, utamanya desktop dan mobile. Komponen ini penting karena saat ini, fleksibilitas sebuah web menjadi pertimbangan pada pengguna untuk menggunakannya atau tidak. Web yang reponsif dapat meningkatkan pengalaman pengguna sehingga website dapat lebih 'preferable'

Contoh aplikasi yang sudah menerapkan responsive yaitu berbagai media sosial. Ambil contoh Instagram, meskipun lebih banyak pengguna Instagram mobile, aplikasi ini tetap bisa diakses melalui dekstop dengan tampilan yang baik.

Contoh web yang belum menerapkan yaitu [arngren.net](arngren.net). Jika website ini diakses melalui mobile, tampilannya masih sama dengan yang di-desktop, sehingga pengguna kesulitan untuk mengakses fitur-fitur web (terlepas dari tampilannya yang memang tidak baik).

**3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!**  
- **Margin**  
    Spasi kosong antara elemen dan luar elemen. Margin berguna untuk mengatur posisi antar elemen agak tidak saling bertabrakan.  
    _Cara implementasi:_
    ``` css
    div {
        /* semua sisi*/
        margin: 20px blue
        
        /* specify tiap sisi */
        margin-top: 10px;
        margin-right: 20px;
        margin-bottom: 30px;
        margin-left: 40px;

        /* short cut */
        /* Atas | Kanan | Bawah | Kiri */
        margin: 10px 20px 30px 40px;
    }   
    ```
- **Border**  
    Garis di pada sisi elemen untuk mengidentifikasi bentuk elemen. Border biasanya digunakan untuk memperjelas elemen, biasanya berbentuk garis yang mengelilingi elemen. Border sendiri berada di antara margin dan padding.
    _Cara implementasi:_  
    ``` css
    .card {
        /* semua sisi */
        /* width | style | color */
        border: 2px solid black; 

        /* specify tiap sisi */
        border-top: 2px solid red;
        border-right: 3px dashed green;
        border-bottom: 4px dotted blue;
        border-left: 5px double black;

        /* specify satu-satu */
        border-width: 2px;         
        border-style: solid;      
        border-color: blue;           
        border-width: 2px 4px 6px 8px;   
        border-style: solid dashed none dotted;
        border-color: red green blue black;

        /* lengkungan sudut */
        /* semua sudut */
        border-radius: 10px; 

        /* atas-kiri & bawah-kanan | atas-kanan & bawah-kiri */
        border-radius: 10px 20px; 

        /* masing-masing sudut */
        border-radius: 10px 20px 30px 40px; 
    }

    ```
- **Padding**  
    Ruang kosong di dalam elemen untuk membatasi sampai mana konten dapat diisi. Dengan kata lain, margin dalam. Padding memastikan konten di dalam elemen tidak keluar elemen atau tidak terlalu dekat dengan sisi untuk meningkatkan UI/UX.
    _Cara implementasi:_
    ``` css
    .box {
        /* specify tiap sisi */
        padding-top: 5px;
        padding-right: 15px;
        padding-bottom: 25px;
        padding-left: 35px;

        /* Semua sisi */
        padding: 20px;

        /* Atas & bawah | Kiri & kanan */
        padding: 5px 15px;

        /* Atas | Kiri & kanan | Bawah */
        padding: 5px 10px 15px;

        /* Atas | Kanan | Bawah | Kiri */
        padding: 5px 10px 15px 20px;
    }
    ```

**4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!**  
Flex box adalah konsep penyesuaian konten dalam 1 dimensi, entah akan disusun ke samping (horizontal, secara kolom) atau ke bawah (vertikal, secara baris). Flex box memudahkan developer untuk menyusun konten dalam semua box/container sehingga konten otomatis tersusun rapi. Flex box bisa mengatur ruang antarelemen. Apakah isi konten dapat di-scroll? Atau akan ter-wrap ketika elemen melebihi kapasitas box. Flex box umumnya digunakan untuk enyusun tombol atau navigation bar.

Grid Layout sendiri juga konsep penyesuaian konten, hanya saja dalam 2 dimensi. Grid layout memungkinkan kita menaruh lebih banyak konten dalam satu box/container tanpa khawatir ketidaksesuaian tampilan karena grid layout otomatis membuatnya responsif. Layout ini biasanya digunakan untuk menyusun elemen yang lebih kompleks dan banyak, seperti membuat galeri, dashboard, body page, dan lain-lain. 
 
**5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!**  
Pertama-tama, saya membaca keseluruhan dokumen untuk memberikan gambaran apa saja yang perlu saya kerjakan. Saya pertama menambahkan button edit dan hapus untuk produk terlebih dahulu. Kemudian, karena saya sudah mencoba membuat css sebelumnya, saya memindahkan css tersebut ke file baru yakni `global.css`. Setelah saya berhasil memindahkannya, saya coba membuat navigation bar responsif. Setelah itu, barulah saya melakukan finishing seperti memoles css (karena css yang kemarin masih terlalu basic) sembari meng-explore css bersama ChatGPT.
