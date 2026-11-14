from PIL import Image


def encode(input_image, message, output_image):
    # Proveruvame dali porakata e prazna.
    # Ako nema tekst, ja prekinuvame funkcijata so greshka.
    if not message:
        raise ValueError("Porakata e prazna.")

    # Ja otvarame slikata i ja pretvorame vo RGB format.
    # Vo ovoj format sekoj piksel ima tri vrednosti: crvena, zelena i sina.
    # Sekoja vrednost e cel broj od 0 do 255, na primer: (120, 53, 200).
    image = Image.open(input_image).convert("RGB")

    # Gi zemame site pikseli i gi smestuvame vo lista za da mozheme da gi menuvame.
    # Primer: [(120, 53, 200), (81, 42, 99), (160, 71, 88), ...]
    pixels = list(image.get_flattened_data())

    # Ja pretvorame porakata od tekst vo bajti so UTF-8.
    # Eden bajt ima 8 bita i negovata brojna vrednost e od 0 do 255.
    # Angliskite bukvi obichno koristat po eden bajt, a kirilichnite po dva.
    # Primer: "A" -> [65], a "T" na kirilica -> [208, 162].
    data = message.encode("utf-8")

    # Za sekoj bajt koristime tri pikseli, odnosno devet RGB vrednosti.
    # Prvite osum vrednosti gi chuvaat osumte bita od bajtot.
    # Devettata vrednost kazhuva dali porakata zavrshuva.
    # Ako nema dovolno pikseli, ja prekinuvame funkcijata.
    if len(data) * 3 > len(pixels):
        raise ValueError("Slikata nema dovolno prostor.")

    # Gi izminuvame bajtite od porakata eden po eden.
    # index e redniot broj, pochnuvajkji od 0.
    # byte e brojna vrednost na tekovniot bajt.
    for index, byte in enumerate(data):

        # Ja presmetuvame pozicijata na prviot piksel za tekovniot bajt.
        # Bajt 0 koristi pikseli 0, 1, 2.
        # Bajt 1 koristi pikseli 3, 4, 5.
        # Bajt 2 koristi pikseli 6, 7, 8, itn.
        start = index * 3

        # Zemame tri sosedni pikseli i gi spojuvame nivnite RGB vrednosti.
        # Kaj tuple, operatorot + gi spojuva elementite, ne gi sobira broevite.
        # Primer:
        # (120, 53, 200) + (81, 42, 99) + (160, 71, 88)
        # -> (120, 53, 200, 81, 42, 99, 160, 71, 88)
        # Rezultatot go pretvorame vo lista za da mozheme da go menuvame.
        colors = list(
            pixels[start] + pixels[start + 1] + pixels[start + 2]
        )

        # Go pretvorame bajtot vo binaren zapis so tochno osum cifri.
        # "b" znachi binaren zapis.
        # "08" znachi najmalku osum cifri, dopolneti so nuli odlevo.
        # Bidejkji byte e od 0 do 255, rezultatot sekogash ima osum cifri.
        # Primer: 65 -> "01000001".
        bits = format(byte, "08b")

        # Gi menuvame prvite osum RGB vrednosti.
        # Sekoja vrednost chuva po eden bit preku svojata parnost:
        # parna vrednost -> bit 0, neparna vrednost -> bit 1.
        for position in range(8):

            # So // 2 * 2 ja pravime vrednosta parna.
            # Potoa go dodavame bitot, pretvoren od tekst vo broj.
            # Primer: 121 // 2 * 2 = 120.
            # Ako bitot e 0 -> 120; ako bitot e 1 -> 121.
            # Vrednosta se menuva najmnogu za 1, pa razlikata vo bojata e mala.
            colors[position] = (
                colors[position] // 2 * 2 + int(bits[position])
            )

        # Proveruvame dali ova e posledniot bajt od porakata.
        # Posledniot indeks e len(data) - 1, bidejkji broenjeto pochnuva od 0.
        # stop = 1 znachi kraj, a stop = 0 znachi deka ima ushte bajti.
        stop = 1 if index == len(data) - 1 else 0

        # Vo devettata RGB vrednost ja zapisuvame oznakata za kraj.
        # Ja pravime neparna za kraj ili parna za prodolzhuvanje.
        colors[8] = colors[8] // 2 * 2 + stop

        # Devette izmeneti vrednosti gi delime nazad vo tri RGB pikseli.
        # colors[0:3] gi zema elementite na pozicii 0, 1 i 2.
        # colors[3:6] gi zema elementite na pozicii 3, 4 i 5.
        # colors[6:9] gi zema elementite na pozicii 6, 7 i 8.
        # Gi pretvorame vo tuple i gi vrakjame na nivnite mesta vo listata.
        pixels[start] = tuple(colors[0:3])
        pixels[start + 1] = tuple(colors[3:6])
        pixels[start + 2] = tuple(colors[6:9])

    # Ja azhurirame slikata so izmenetata lista od pikseli.
    # Pikselite shto ne gi koristevme za porakata ostanuvaat isti.
    image.putdata(pixels)

    # Ja zachuvuvame slikata vo PNG format, koj gi zachuvuva RGB vrednostite.
    # JPEG mozhe da gi promeni vrednostite i da ja unishti skrienata poraka.
    image.save(output_image, format="PNG")


def decode(input_image):
    # Ja otvarame slikata i ja pretvorame vo istiot format kako pri encode.
    image = Image.open(input_image).convert("RGB")

    # Gi zemame site RGB pikseli kako lista.
    pixels = list(image.get_flattened_data())

    # Kreirame prazna kolekcija vo koja kje gi dodavame prochitanite bajti.
    # Koristime bytearray bidejkji dozvoluva dodavanje bajti so append().
    data = bytearray()

    # Gi chitame pikselite vo grupi od po tri: 0, 3, 6, 9, ...
    # Chekorot 3 znachi deka sekoja sledna grupa pochnuva tri pikseli ponatamu.
    # Granicata len(pixels) - 2 obezbeduva sekoja grupa da ima tri pikseli.
    for start in range(0, len(pixels) - 2, 3):

        # Gi spojuvame RGB vrednostite od trite pikseli vo devet vrednosti.
        # Tuka ne ni treba lista, bidejkji samo gi chitame vrednostite.
        colors = (
            pixels[start] + pixels[start + 1] + pixels[start + 2]
        )

        # Pochnuvame so prazen tekst vo koj kje gi spoime osumte bita.
        bits = ""

        # Gi chitame samo prvite osum RGB vrednosti.
        # Devettata e oznaka za kraj i ne e del od bajtot.
        for value in colors[:8]:

            # Ostatokot pri delenje so 2 ja otkriva parnosta:
            # paren broj % 2 = 0, neparen broj % 2 = 1.
            # Go pretvorame rezultatot vo tekst i go dodavame vo bits.
            bits += str(value % 2)

        # Go pretvorame binarniot tekst vo broj so osnova 2.
        # Primer: int("01000001", 2) -> 65.
        # Dobieniot bajt go dodavame vo kolekcijata.
        data.append(int(bits, 2))

        # Ja proveruvame devettata vrednost.
        # Ako e neparna, ova bil posledniot bajt od porakata.
        if colors[8] % 2 == 1:

            # Gi pretvorame site sobrani bajti nazad vo UTF-8 tekst.
            # Dekodirame na kraj bidejkji eden znak mozhe da ima povekje bajti.
            # Ako bajtite ne se validen UTF-8 tekst, Python kje prijavi greshka.
            return data.decode("utf-8")

    # Ako gi prochitavme site celi grupi bez oznaka za kraj, prijavuvame greshka.
    # Ovoj algoritam nema poseben potpis za prepoznavanje skriena poraka:
    # sluchajna slika isto mozhe da sodrzhi neparna vrednost kako lazhen kraj.
    raise ValueError("Ne e pronajdena oznaka za kraj na porakata.")


# Ja krieme porakata vo slika.png i rezultatot go zachuvuvame vo tajna.png.
# Originalnata datoteka slika.png ne se prebrishuva.
#encode("slika.png", "hello", "tajna.png")

# Ja chitame skrienata poraka od novata slika i ja pechatime.
print(decode("jakov_encoded.png"))