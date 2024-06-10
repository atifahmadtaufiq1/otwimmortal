meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "SHEESH":"sedikit ketidaksetujuan"
            }
word = input("masukkan kata mu")
if word.upper() in meme_dict.keys():
    print(meme_dict[word.upper()])
else:
    print("eror")
