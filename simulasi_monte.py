import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import streamlit as st


# Baca data harga saham dari file CSV
df = pd.read_csv('TSLA.csv')
df2 = pd.read_csv('TSLA.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Hitung log return
df['LogReturn'] = np.log(df['Close'] / df['Close'].shift(1))
df.dropna(inplace=True)


# Pisahkan data untuk simulasi dan validasi
train_data = df['Close'][:-30]
test_data = df['Close'][-30:]



# Menentukan distribusi probabilitas (mean dan std deviasi dari log return)
mu = df['LogReturn'].mean()
sigma = df['LogReturn'].std()

print("Nilai mu : ", mu)
print("Nilai sigma : ", sigma)


# Menentukan interval angka acak dan membangkitkan angka acak
num_simulations = 100
num_days = 30
simulations = np.zeros((num_simulations, num_days))


last_price = train_data[-1]

for i in range(num_simulations):
    daily_returns = np.random.normal(mu, sigma, num_days)
    price_series = [last_price]
    for x in daily_returns:
        price_series.append(price_series[-1] * np.exp(x))
    simulations[i, :] = price_series[1:]


simulationsV = pd.DataFrame(simulations)
# simulationsV

# Menjalankan simulasi
simulated_end_prices = simulations[:, -1]

# simulated_end_prices

# simulend = pd.DataFrame(simulated_end_prices)
# csvsimulend = simulend.to_csv("out.csv", index = False)


# Menampilkan hasil simulasi
plt.figure(figsize=(10, 6))
plt.plot(simulations.T)
plt.title('Simulasi Monte Carlo Prediksi Harga Saham Tesla')
plt.xlabel('Hari')
plt.ylabel('Harga Penutupan')
plt.show()


# Kesimpulan
predicted_mean_price = np.mean(simulated_end_prices)
predicted_median_price = np.median(simulated_end_prices)
predicted_std_price = np.std(simulated_end_prices)

print(f"Prediksi harga akhir rata-rata: ${predicted_mean_price:.2f}")
print(f"Prediksi harga akhir median: ${predicted_median_price:.2f}")
print(f"Standard deviasi dari harga akhir prediksi: ${predicted_std_price:.2f}")


# Hitung harga prediksi dari hasil simulasi (rata-rata dari simulasi)
predicted_prices = np.mean(simulations, axis=0)

# Hitung persentase kesesuaian dan error
percentage_accuracy = 100 - (np.abs((test_data.values - predicted_prices) / test_data.values) * 100)
error = test_data.values - predicted_prices


# Buat tabel untuk 30 hari prediksi dan harga sebenarnya
comparison_df = pd.DataFrame({
    'Tanggal': test_data.index,
    'Harga Sebenarnya': test_data.values,
    'Harga Prediksi': predicted_prices,
    'Persentase Kesesuaian': percentage_accuracy,
    'Error': error
})

# Tampilkan tabel
# comparison_df


# Plot kesesuaian harga prediksi dan harga sebenarnya
plt.figure(figsize=(10, 6))
plt.plot(test_data.index, test_data.values, label='Harga Sebenarnya')
plt.plot(test_data.index, predicted_prices, label='Harga Prediksi')
plt.fill_between(test_data.index, test_data.values, predicted_prices, where=(predicted_prices > test_data.values), color='red', alpha=0.3, interpolate=True)
plt.fill_between(test_data.index, test_data.values, predicted_prices, where=(predicted_prices < test_data.values), color='green', alpha=0.3, interpolate=True)
plt.title('Kesesuaian Harga Prediksi dengan Harga Sebenarnya')
plt.xlabel('Tanggal')
plt.ylabel('Harga Penutupan')
plt.legend()
plt.show()

# Kesimpulan
predicted_mean_price = np.mean(simulated_end_prices)
predicted_median_price = np.median(simulated_end_prices)
predicted_std_price = np.std(simulated_end_prices)


# Hitung harga prediksi dari hasil simulasi (rata-rata dari simulasi)
predicted_prices = np.mean(simulations, axis=0)

# Hitung persentase kesesuaian dan error
percentage_accuracy = 100 - (np.abs((test_data.values - predicted_prices) / test_data.values) * 100)
error = test_data.values - predicted_prices

# Buat tabel untuk 30 hari prediksi dan harga sebenarnya
comparison_df = pd.DataFrame({
    'Tanggal': test_data.index,
    'Harga Sebenarnya': test_data.values,
    'Harga Prediksi': predicted_prices,
    'Persentase Kesesuaian': percentage_accuracy,
    'Error': error
})

# Tampilkan tabel
# comparison_df

st.title("Simulasi Monte Carlo IF - 7")
st.subheader("Dosen Pembimbing: Sri Nurhayati, MT")
st.subheader("Anggota Kelompok: ")

col1, col2 = st.columns([1,2])
with col1: 
      st.write("Nim")
      st.write("10122269")
      st.write("10122510")
with col2: 
      st.write("Nama")
      st.write("Erwin Hafiz Triadi")
      st.write("Fikkry Ihza Fachrezi")


st.subheader("Data set yang digunakan : ")
st.write(df2)  
st.write("Merupakan data set dari harga saham TSLA. Simulasi yang akan dilakukan yaitu penentuan atau prediksi harga dari saham TSLA 30 hari kedepan dengan menerapkan monte carlo simulation")

st.subheader("Static Monte Carlo Simulation")

st.subheader("Langkah ke - 1: ")
st.write("Mencari nilai log return harian: ")
st.write(df)
st.subheader("Langkah ke - 2: ")
st.write("Melakukan split data sebagai data latih dan data test")
col3, col4 = st.columns(2)
with col3:
  st.write("data latih ")
  st.write(train_data) 
with col4: 
  st.write("data test")
  st.write(test_data) 

st.write("Tujuan dari split data yaitu ketika diakhir simulasi akan dilakukan pengujian terhadap hasil simulasi untuk mengetahui ketepatan/kesesuaian dan erorr")
st.subheader("Langkah ke - 3: ")
st.write("Mencari nilai miu dan sigma dari nilai log return harian")
st.write("Nilai miu : " ,mu)
st.write("Nilai sigma : ",sigma)

st.subheader("Langkah ke - 4: ")
st.write("Menentukan interval angka acak dan membangkitkan angka acak")
st.write("Number of simulation : ", num_simulations)
st.write("Number of days :  ", num_days)
st.write("Menjalankan simulasi : ")
st.write(simulationsV)

st.write("Menjalankan simulasi untuk harga akhir / clossing sebanyak 100 kali percobaan: ")
simm = pd.DataFrame(simulated_end_prices)
st.write(simm)

st.write("Menampilkan hasil dari simulasi")
# Menampilkan hasil simulasi
plt.figure(figsize=(10, 6))
plt.plot(simulations.T)
plt.title('Simulasi Monte Carlo Prediksi Harga Saham Tesla')
plt.xlabel('Hari')
plt.ylabel('Harga Penutupan')
st.pyplot(plt)


st.write(f"Prediksi harga akhir rata-rata: ${predicted_mean_price:.2f}")
st.write(f"Prediksi harga akhir median: ${predicted_median_price:.2f}")
st.write(f"Standard deviasi dari harga akhir prediksi: ${predicted_std_price:.2f}")

st.subheader("Ringkasan data prediksi dan harga sebenarnya")
st.write(comparison_df)



st.subheader("Grafik kesesuaian harga prediksi dengan harga sebenarnya dan tingkat erorrnya")    
plt.figure(figsize=(10, 6))
plt.plot(test_data.index, test_data.values, label='Harga Sebenarnya')
plt.plot(test_data.index, predicted_prices, label='Harga Prediksi')
plt.fill_between(test_data.index, test_data.values, predicted_prices, where=(predicted_prices > test_data.values), color='red', alpha=0.3, interpolate=True)
plt.fill_between(test_data.index, test_data.values, predicted_prices, where=(predicted_prices < test_data.values), color='green', alpha=0.3, interpolate=True)
plt.title('Kesesuaian Harga Prediksi dengan Harga Sebenarnya')
plt.xlabel('Tanggal')
plt.ylabel('Harga Penutupan')
plt.legend()
st.pyplot(plt)

st.subheader("Kesimpulan simulasi")
st.write("Secara keseluruhan, hasil ini dapat memberikan panduan untuk pengambilan keputusan investasi, dikarenakan dapat memberikan gambaran mengenai harga saham TSLA untuk 30 hari kedepan. Meskipun sebenarnya masih banyak faktor yang menjadi penentu untuk harga suatu saham seperti peningkatan harga yang disebabkan oleh faktor tertentu ataupun penurunan karena adanya faktor tertentu sebagai contoh yaitu pandemi covid. Dalam simulasi ini belum ada memberikan gambaran spesifik terhadap gangguan dari faktor luar. Namun meskipun begitu model simulasi ini dapat memberikan gambaran yang baik dan tergantung banyaknya data yang diberikan sebagai data latih dari model simulasi ini.")
