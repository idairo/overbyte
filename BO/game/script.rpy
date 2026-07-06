# Kamu dapat taruh script game mu di file ini.
# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
image bg blck = "images/blck.png"
image bg void = "images/wormhole.png"
image bg bedroom = "images/single bedroom.jpg"

# Deklarasikan karakter yang digunakan di game.
define q = Character('???', color="#9c9c9c")
define h = Character('Red', color="#e22d2d")
define a = Character('Orange', color="#d17325")
define b = Character('Blue', color="#293ca7")

# ================================================== Start ==================================================
label start:

"Dunia ini penuh dengan informasi."
"Di mana saja, kapan saja, setiap detik. Tanpa henti. Semuanya ada di dalam genggaman tangan."
"Tapi masih aja ada yang tidak kita pahami."

q "Pernah mendengar gak tentang kacamata pintar dari Meta?"

q "Sudah ada Kacamata Google sepuluh tahun yang lalu."

q "Pusing gak sih lihat layar hp terus? Kalo punya duit, pasti aku beli."

q "AI ini masa depan teknologi. Semuanya tak serahin ke CatGPT."

q "Aku juga make sih, tapi token akhir-akhir ini makin mahal."

q "Beneran? Trus siapa yang ngerjain PR ku?"

q "Santai aja, itu buat yg bayar doang"

q "Suatu hari nanti komputer akan ditanamkan ke dalam otak kita!"

q "Serem banget ih."

q "Kedengarannya kayak mimpi buruk."

q "Tapi mungkin itu bakal jadi kenyataan."

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

    #label nama: 
    #$ player_name = renpy.input("What is your name?", default="Marka").strip()
    #$ player = Character(player_name, color="#E6E6FA")
   
    #player '"I am %(player_name)s."'
    #player 'Blah blah blah.'

# The phrase in the brackets is the text that the game will display to prompt 
# the player to enter the name they've chosen.
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
    "Kamu mengecek ponselmu, terdapat nama Orange"
    "Kamu memutuskan untuk mengangkatnya."
    a "Pagi, %(player_name)s!"
    # ----------------------------------------------------------------------------------------------------
    $ changeTextbox("gui/textbox.png")         # Textbox window: Visible
    "Demo completed"
    return

# ====================================================================================================