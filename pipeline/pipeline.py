import sys
#memanggil modul sys dari python

import pandas as pd
#memanggil modul pandas dengan alias pd

print('arguments:', sys.argv)
#sys.argv mengambil argumen sebelum dijalankan. jadi pastikan sebelum run harus ada argumennya

month = int(sys.argv[1])
#variabel yang argumen pertama diambil dan di ubah menjadi integer

df = pd.DataFrame({"Day": ['monday', 'wednesday'], "Passengers": [100,200]})

#variabel df yang mengambil dataframe dari pandas dengan kolom yang di buat
print(df.head())

#menampilkan data teratas dari df

df.to_parquet(f"output_{month}.parquet")
#membuat fileparquet dan menyimpan df ke dalamnya dengan format parquet

print(f'hello pipeline, month={month}')
#nothing