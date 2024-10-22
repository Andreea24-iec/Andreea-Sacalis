import string
text="""Potrivit sursei citate, organele judiciare s-au sesizat din oficiu după ce au vizionat imagini 
        apărute în spaţiul public în legătură cu un accident rutier cu un autoturism marca BMW care intră în coliziune cu un Lamborghini."""
jumatate=len(text) // 2
text_1 = (text [0:jumatate])
text_1 = text_1.upper()
text_1 = text_1.replace(" ","")
text_2 = (text[jumatate:])
text_2 = text_2[::-1]
text_2 = text_2[0]+text_2[1].upper() + text_2[2:]
text_2 = text_2.translate(str.maketrans(" ", " ", string.punctuation))
text_mare = text_1 + text_2
print(text_mare)