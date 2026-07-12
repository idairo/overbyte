# Kamu dapat taruh script game mu di file ini.
# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
image bg black = "images/blck.png"
image bg void = "images/wormhole.png"
image bg bedroom = "images/single bedroom.jpg"
image bg classroom = "images/Class - 1.png"
image bg uks = "images/clinic.jpg"

# Deklarasikan karakter yang digunakan di game.
define q = Character('???', color="#9c9c9c")
define s = Character('Suara aneh', color="#969696")
define a = Character('Ica', color="#e38940")
define b = Character('Vio', color="#4a60dd")
define c = Character('Naili', color="#de566f")
define mc = Character('[%(player_name)s]', color="#293ca7")

# ================================================== Start ==================================================
label start:
"Dunia ini penuh dengan informasi."
"Di mana saja, kapan saja, setiap detik. Tanpa henti. Semuanya ada di dalam genggaman tangan."
"Tetapi..."
"Jika jika selalu mencari informasi baru, apakah akan tersedia ruang untuk pikirna kita sendiri?"
label name:    

    $ player_name = renpy.input("Silakan masukkan nama anda")

    $ player_name = player_name.strip()
# The .strip() instruction removes any extra spaces the player 
# may have typed by accident.

#  If the player can't be bothered to choose a name, then we
#  choose a suitable one for them:
    if player_name == "":
        $ player_name="Marka"
call ShowCineFull
scene bg void with dissolve
call HideCineFull
play music "audio/noise.mp3" fadein 5.0   

"Kamu membuka mata dan mendapati suasana yang asing."
"Tidak ada tanah, hanya kehampaan tak berujung di kejauhan dan gaya gravitasi yang kuat." 
"Puluhan angka 0 dan 1 ditarik ke dalam apa yang disebut lubang hitam ini."
"Kau mencoba memahami apa yang kau dengar, tetapi yang kau dengar hanyalah suara bising aneh yang memusingkan."
"Kau membuka mulut untuk mencari bantuan."
q "HALO??? APAKAH ADA ORANG DI SANA????"
"Percuma. Tidak mungkin ada orang yang bisa mendengarmu."
s "%(player_name)s!"
"Hah??"
s "KAU PUNYA 7 HARI UNTUK MENCARI KEBENARAN."
s "JIKA KAU GAGAL MENEMUKAN KEBENARAN, GELOMBANG MALAPETAKA AKAN MENGHUKUM NEGERIMU."
q "Gelombang malapetaka?"
q "Tunggu! Siapa kau?"
"Sepertinya suara misterius itu tidak bisa mendengarmu."
q "Kebenaran? Apa maksudnya?"
"Kamu terlalu pusing untuk memproses suara misterius itu"
"Apa yang harus kamu lakukan?"

menu:

    "Tutup mata":
        jump eyes

    "Tutup telinga":
        jump ears

label eyes:

    "Suara aneh disekelilingmu tetap membuatmu pusing"
jump dizzy

label ears:

   "Pemandangan kehampaan itu membuatmu pusing, dan kamu masih bisa mendengar semuanya meskipun telingamu tertutup."
jump dizzy

label dizzy:
"Kekosongan itu semakin menjauhkanku dari posisi awalmu."
"Apakah ini kematian?"
stop music fadeout 0.5

call ShowCineFull
scene bg bedroom with dissolve
call HideCineFull
play music calm01
"Kamu terbangun di dalam kamar tidurmu. Sepertinya kamu baru saja terbangun dari mimpi aneh."
"Ponselmu berdering. Kamu menerima telfon dari seseorang."
"Kamu mengecek ponselmu. Nama Ica tertampil."
"Kamu memutuskan untuk mengangkatnya."
a "Pagi, %(player_name)s!"
"Kamu baru ingat bahwa hari ini hari Senin."
"Kamu bergegas ke sekolah dan mengikuti upacara bendera."
call ShowCineFull
scene bg classroom with dissolve
call HideCineFull
"Setelah Upacara bendera, kamu kembali ke kelas dan bertemu dengan Ica."
show ica talk
a "Banyak yang bolos upacara hari ini."
a "Tapi si Vio kali ini ikut. Tumben ya."
a "Trus pingsan."
show ica default
a "Kalo gak kuat ikut seharusnya gausah ikut tau."
a "Apalagi dia Minggu depan ada olimpiade. Pasti harus ikut bimbingan tambahan sama Bu Santi."
a "..."
show ica talk
a "Sebagai anak medis. Aku harus tanggung jawab kalo ada anak yang sakit. Apalagi anak pintar kayak si Vio."
show ica smile
a "%(player_name)s, ke UKS yuk."
stop music
call ShowCineFull
scene bg uks with dissolve
call HideCineFull
"Kamu datang ke UKS untuk mengecek anak-anak yang sakit."
"Ica melihat sekeliling UKS, mengecek jumlah anak yang ada di ruangan."
show ica default
a "Semua anak yang gak ikut upacara udah balik ke kelas."
a "Tapi si Vio masih di sini. Sepertinyua dia sakit beneran."
q "Eh, si Vio lagi gak enak badan ya?"
"Seorang perempuan berjas merah duduk di seberang ruangan."
a "Iya ih. Ada apa, Naili?"
c "Dia dicari sama Bu Santi. Kata beliau jika tidak baikan hari ini bimbingannya bisa diundur pas jam istirahat besok"
a "Aneh. Biasanya jam segini udah main ff tau."
"Ica mendekati tempat Vio tidur, lalu menggerak-gerakkan pundaknya."
show ica talk
a "Vioo?"
"Tidak ada respons sama sekali."
a "WOI. BANGUN! Dicari Bu Santi tau!"
"Sepertinya dia masih tertidur dengan nyenyak."
a "Jangan-jangan..."
show ica default
"Ica tiba tiba terdiam, lalu menggelengkan kepala dan mengecek denyutnya"
"Nafas lega keluar dari mulutnya."
a "Dia masih hidup. Tapi dia tak merespons sama sekali."
c "Memang terakhir dia melakukan apa sebelum pingsan?"
a "Gatau. Yang jelas main hp."
a "..."
a "%(player_name)s, coba cek hp-nya Vio. Ada notifikasi yang aneh gak?"
"Kamu melihat ponselnya. terdapat barisan-barisan kode yang tidak bisa kamu pahami."
"Pada baris paling terakhir, tertulis "
"NAMA: VIO. USIA: 17 TAHUN. STATUS: BERHASIL."
show ica talk
a "%(player_name)s, ada apa dengan hp Vio?"
default virus = 0
menu:
     "Hp Vio diserang virus.":
         $ virus += 1
         a "HAH?? HP ORANG JAGO IT KAYAK DIA BISA DISERANG VIRUS??"
         jump ending_evaluation

     "Tidak ada apa-apa.":
        a "Oh. Oke deh..."
        "Kamu mengembalikan hp Vio pada tempatnya dan meninggalkan UKS."
        $ virus == 0
        jump ending_evaluation

label ending_evaluation:
    if virus == 1:
        jump good_start
    else:
        jump bad_ending_1


label good_start:
    show ica smile
    a "Oke. Berarti kita harus pecahkan sumber dari virus tersebut." 
    a "Mungkin itu sebabnya Vio jatuh pingsan tadi pagi."
    "Kamu memutuskan untuk mengambil hp Vio untuk sementara waktu"
    "Tugasmu esok hari adalah untuk memecahkan sumber jatuhnya Vio dan virus aneh di hp nya."
    jump demo_end

label bad_ending_1:
call ShowCineFull
call HideCineFull
scene bg black
play music "audio/noise.mp3" fadein 0.5
"7 hari kemudian" 
"Suara aneh menyelimuti sekelilingmu. Suara sama yang kau dengar dalam mimpi 7 hari yang lalu."
"Kamu memutuskan untuk membuka ponselmu."
"Hanya ada satu aplikasi yang tertampil. OCTODEV."
"Kamu memutuskan untuk membukanya"
"..."
"Virus OCTODEV telah menyerogoti seluruh ponselmu."
"Puluhan video muncul di depan mata. Asli, palsu, kritis, dramatis. Semua tak ada bedanya."
"Kau tidak bisa berpikir lagi. Ruaganmu menjadi gelap, pengap dan berisik."
"STATUS: GAME OVER."
stop music
jump demo_end

label demo_end:
    $ changeTextbox("gui/textbox.png")         # Textbox window: Visible
    "Demo Selesai."

return
