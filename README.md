# taiko
Auto Swap Taiko 

Cara Penggunaan di Visual Studio Code:

Siapkan VS Code dan Python: Pastikan Anda sudah mengikuti langkah-langkah instalasi di penjelasan sebelumnya.
Install web3.py: Pastikan library web3.py terinstal dengan perintah:

pip install web3

Masukkan Kode: Salin kode di atas ke dalam file Python (misalnya tx_bot.py).
Jalankan Program: Buka terminal di VS Code, navigasikan ke direktori tempat file Python Anda, dan jalankan:
bash
Copy code
python tx_bot.py
Setelah menjalankan, ikuti instruksi di terminal untuk memasukkan URL provider RPC, private key, alamat penerima, jumlah ETH yang akan dikirim, serta interval waktu minimal dan maksimal.

Penjelasan Input:
Provider URL: URL dari Ethereum node (seperti Infura atau Alchemy).
Private Key: Private key dari akun Ethereum yang akan mengirimkan transaksi.
Receiver Wallets: Daftar alamat dompet penerima.
Amount to Send: Jumlah ETH yang akan dikirim dalam setiap transaksi.
Interval Time: Rentang interval waktu dalam milidetik antara transaksi agar tidak terlihat seperti bot.
