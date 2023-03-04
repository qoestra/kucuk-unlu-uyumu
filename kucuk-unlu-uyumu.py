kelime = input("Bir kelime girin: ")

son_unlu_harf = None

unlu_harfler = "aeıioöuü"

for harf in kelime:
    if harf in unlu_harfler:
        son_unlu_harf = harf

if son_unlu_harf in "ei":
    print("Küçük ünlü uyumu sağlanmıştır.")
else:
    print("Küçük ünlü uyumu sağlanmamıştır.")
