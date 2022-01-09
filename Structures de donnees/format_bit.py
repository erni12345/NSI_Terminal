


with open("essai.txt", "wb") as f:
    f.write((int('101010', 2)).to_bytes(1, 'big'))
