# Kamu dapat taruh script game mu di file ini.
# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
image bg blck = "images/blck.png"
image bg void = "images/wormhole.png"
image bg bedroom = "images/single bedroom.jpg"

# Deklarasikan karakter yang digunakan di game.
define q = Character('???', color="#9c9c9c")
define h = Character('Red', color="#e22d2d")
define a = Character('Ica', color="#d17325")
define b = Character('Blue', color="#293ca7")
define mc = Character('[%(player_name)]', color="#293ca7")
define y = Character('Yosuke', color="#293ca7", image="yosuke")
image define yosuke = "side yosuke.png"

# ================================================== Start ==================================================
label start:
"Dunia ini penuh dengan informasi."
"Di mana saja, kapan saja, setiap detik. Tanpa henti. Semuanya ada di dalam genggaman tangan."
"Tapi masih aja ada yang tidak kita pahami."
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
"KAU PUNYA 7 HARI UNTUK MENCARI KEBENARAN."
"Hah??"
"JIKA KAU GAGAL MENEMUKAN KEBENARAN, GELOMBANG MALAPETAKA AKAN MENGHUKUM NEGERIMU."
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
    "Aku benar-benar tidak tahu harus berbuat apa."
"Kekosongan itu semakin menjauhkanku dari posisi awalku."
"Apakah ini kematian?"
stop music fadeout 0.5

call ShowCineFull
scene bg bedroom with dissolve
call HideCineFull
"Kamu terbangun di dalam kamar tidurmu. Sepertinya kamu baru saja terbangun dari mimpi aneh."
play music calm01

label name:    

    $ player_name = renpy.input("Silakan masukkan nama anda")

    $ player_name = player_name.strip()
# The .strip() instruction removes any extra spaces the player 
# may have typed by accident.

#  If the player can't be bothered to choose a name, then we
#  choose a suitable one for them:
    if player_name == "":
        $ player_name="Marka"

# And get a nostalgic sigh from Seasons of Sakura fans!
    
# Now the other characters in the game can greet the player.
    "Ponselmu berdering. Kamu menerima telfon dari seseorang."
    "Kamu mengecek ponselmu. Nama Ica tertampil."
    "Kamu memutuskan untuk mengangkatnya."
    a "Pagi, %(player_name)s!"
    scene bg sekolah with dissolve
    "Kamu bergegas ke sekolah dan mengikuti upacara bendera."
    "Setelah itu, kamu langsung kembali ke kelas dan bertemu dengan Ica."
    show ica talk
    a "Banyak yang bolos upacara hari ini."
    a "Tapi si Vio kali ini ikut. Tumben ya."
    a "Trus pingsan."
    a "Gatau ya. Perasaan dia habis sekolah ini ada bimbingan olimpiade."
    show ica smile
    a "%(player_name)s, ke UKS yuk."
    scene bg poskes with dissolve
    "Kamu datang ke poskes untuk mengunjungi Vio"
    a "Vioo?"
    a "WOI. BANGUN! Dicari Bu Santi tau!"
    
    menu:
    "Sepertinya dia masih tertidur."
        jump weird
    label weird:
    a "Aneh. Biasanya jam segini udah main ff tau."
        jump bangun
    label bangun:
    a "Jangan-jangan..."
    "Ica tiba tiba terdiam, lalu menggelengkan kepala dan mengecek denyutnya"
    "Nafas lega keluar dari mulutnya."
    a "Dia masih hidup. Tapi dia tak respons sama sekali."
    a "Coba cek ponselnya"
    "Kamu melihat ponselnya. terdapat tulisan yang sulit dikenali."
    "Apakah ponselnmya diserang virus?"
    "HAH???"
    a "APA INI??"
    "Terdapat gambar simbol yang meragukan. Sepertinya sebuah virus telah menyerang handphone."
    a "Sebelum Vio pingsan dia melihat hp dan tiba-tiba pusing sekali. Seperti melihat suatu yang memusingkan."

    a "Layar ini aneh sekali."
    "Kamu memutuskan untuk mengambil hp Vio untuk sementara waktu"
    "Tugasmu sekarang adalah untuk menemukan sumber dari virus tersebut"
     # ----------------------------------------------------------------------------------------------------
    $ changeTextbox("gui/textbox.png")         # Textbox window: Visible
    #"Demo completed"


return


# ====================================================================================================
