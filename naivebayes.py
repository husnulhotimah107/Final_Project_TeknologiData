import pandas as pd
from probaspek import ProbAspek

class NaiveBayes:
    def __init__(self):
        pass

        # TODO: [LANGKAH-2] Buat property untuk menampung data dari file CSV
        self.data_training = None

        # TODO: [Langkah-3] Buat variabel dictionary untuk menampung matriks Probabilitas untuk semua aspek
        self.aspek_pelatih = {'Pengertian': None, 'Menekan': None}
        self.aspek_kandang_sendiri = {'Ya': None, 'Tidak': None}
        self.aspek_latihan = {'Rutin': None, 'Jarang': None, 'Jarang': None}
        self.aspek_stamina = {'Kuat': None, 'Lemah': None}
        self.aspek_mental = {'PD': None, 'Gerogi': None}

        # TODO: [Langkah-4] Buat variabel untuk menampung Prior Probability
        self.prior_probability = {'Menang': 0, 'Kalah': 0}

    # TODO: [LANGKAH-5] Load data training dari file CSV
    def load_data_training(self):
        self.data_training = pd.read_csv('dataset.csv', sep=';')
        print(self.data_training)
        print('-------------------------------------------------------------')

    # TODO: [LANGKAH-6] Membuat object ProbAspek untuk semua nilai pada aspek, sekaligus menghitung jumlah menang dan kalahnya
    def buat_prob_aspek(self, nama_aspek: str, nilai_aspek: str) -> ProbAspek:
        #probilitas aspek kosong
        prob_aspek = ProbAspek(nama_aspek, nilai_aspek)
        #menghitung jumlah menang dan kalah
        pengertian_menang = self.data_training.loc[(self.data_training[nama_aspek] == nilai_aspek) &
                                             (self.data_training['hasil'] == 'Menang')]
        pengertian_kalah = self.data_training.loc[(self.data_training[nama_aspek] == nilai_aspek) &
                                             (self.data_training['hasil'] == 'Kalah')]
        prob_aspek.jml_menang = len(pengertian_menang)
        prob_aspek.jml_kalah = len(pengertian_kalah)
        return prob_aspek

    # TODO: [LANGKAH-7] Mengisi semua nilai pada matris probabilitas aspek
    def mulai_training(self):
        # Aspek Pelatih
        pp_pengertian = self.buat_prob_aspek('pelatih', 'Pengertian')
        pp_menekan = self.buat_prob_aspek('pelatih', 'Menekan')
        # Jadikan array
        arr_pp = [pp_pengertian, pp_menekan]
        # Hitung total masing-masing nilai aspek berapa kali muncul di menang dan kalah
        total_p = ProbAspek.hitung_jml_total_aspek(arr_pp)
        # Hitung probabilitas aspek untuk masing-masing nilai aspek
        pp_pengertian.hitung_p_aspek_menang(total_p['menang']).hitung_p_aspek_kalah(total_p['kalah'])
        pp_menekan.hitung_p_aspek_menang(total_p['menang']).hitung_p_aspek_kalah(total_p['kalah'])
        # Print matrix probabilitas, tetapi bentuknya vertikal, bukan tabel
        ProbAspek.print_matrix_probabilitas(arr_pp)
        self.aspek_pelatih['Pengertian'] = pp_pengertian
        self.aspek_pelatih['Menekan'] = pp_menekan

        # TODO: [SOAL-1] Lengkapi fungsi ini untuk semua aspek!

        # Aspek Kandang Sendiri
        pks_ya = self.buat_prob_aspek('kandang_sendiri', 'Ya')
        pks_tidak = self.buat_prob_aspek('kandang_sendiri', 'Tidak')
        # Jadikan array
        arr_pks = [pks_ya, pks_tidak]
        # Hitung total masing-masing nilai aspek berapa kali muncul di menang dan kalah
        total_ks = ProbAspek.hitung_jml_total_aspek(arr_pks)
        # Hitung probabilitas aspek untuk masing-masing nilai aspek
        pks_ya.hitung_p_aspek_menang(total_ks['menang']).hitung_p_aspek_kalah(total_ks['kalah'])
        pks_tidak.hitung_p_aspek_menang(total_ks['menang']).hitung_p_aspek_kalah(total_ks['kalah'])
        # Print matrix probabilitas, tetapi bentuknya vertikal, bukan tabel
        ProbAspek.print_matrix_probabilitas(arr_pks)
        self.aspek_kandang_sendiri['Ya'] = pks_ya
        self.aspek_kandang_sendiri['Tidak'] = pks_tidak

        # Aspek Latihan
        pl_rutin = self.buat_prob_aspek('latihan', 'Rutin')
        pl_jarang = self.buat_prob_aspek('latihan', 'Jarang')
        pl_tidakada = self.buat_prob_aspek('latihan', 'Tidak Ada')
        # Jadikan array
        arr_pl = [pl_rutin, pl_jarang, pl_tidakada]
        # Hitung total masing-masing nilai aspek berapa kali muncul di menang dan kalah
        total_l = ProbAspek.hitung_jml_total_aspek(arr_pl)
        # Hitung probabilitas aspek untuk masing-masing nilai aspek
        pl_rutin.hitung_p_aspek_menang(total_l['menang']).hitung_p_aspek_kalah(total_l['kalah'])
        pl_jarang.hitung_p_aspek_menang(total_l['menang']).hitung_p_aspek_kalah(total_l['kalah'])
        pl_tidakada.hitung_p_aspek_menang(total_l['menang']).hitung_p_aspek_kalah(total_l['kalah'])
        # Print matrix probabilitas, tetapi bentuknya vertikal, bukan tabel
        ProbAspek.print_matrix_probabilitas(arr_pl)
        self.aspek_latihan['Rutin'] = pl_rutin
        self.aspek_latihan['Jarang'] = pl_jarang
        self.aspek_latihan['Tidak Ada'] = pl_tidakada

        # Aspek Stamina
        ps_kuat = self.buat_prob_aspek('stamina', 'Kuat')
        ps_lemah = self.buat_prob_aspek('stamina', 'Lemah')
        # Jadikan array
        arr_ps = [ps_kuat, ps_lemah]
        # Hitung total masing-masing nilai aspek berapa kali muncul di menang dan kalah
        total_s = ProbAspek.hitung_jml_total_aspek(arr_ps)
        # Hitung probabilitas aspek untuk masing-masing nilai aspek
        ps_kuat.hitung_p_aspek_menang(total_s['menang']).hitung_p_aspek_kalah(total_s['kalah'])
        ps_lemah.hitung_p_aspek_menang(total_s['menang']).hitung_p_aspek_kalah(total_s['kalah'])
        # Print matrix probabilitas, tetapi bentuknya vertikal, bukan tabel
        ProbAspek.print_matrix_probabilitas(arr_ps)
        self.aspek_stamina['Kuat'] = ps_kuat
        self.aspek_stamina['Lemah'] = ps_lemah

        # Aspek Mental
        pm_pd = self.buat_prob_aspek('mental', 'PD')
        pm_gerogi = self.buat_prob_aspek('mental', 'Gerogi')
        # Jadikan array
        arr_pm = [pm_pd, pm_gerogi]
        # Hitung total masing-masing nilai aspek berapa kali muncul di menang dan kalah
        total_m = ProbAspek.hitung_jml_total_aspek(arr_pm)
        # Hitung probabilitas aspek untuk masing-masing nilai aspek
        pm_pd.hitung_p_aspek_menang(total_m['menang']).hitung_p_aspek_kalah(total_m['kalah'])
        pm_gerogi.hitung_p_aspek_menang(total_m['menang']).hitung_p_aspek_kalah(total_m['kalah'])
        # Print matrix probabilitas, tetapi bentuknya vertikal, bukan tabel
        ProbAspek.print_matrix_probabilitas(arr_pm)
        self.aspek_mental['PD'] = pm_pd
        self.aspek_mental['Gerogi'] = pm_gerogi

    # TODO: [LANGKAH-8] Menghitung prior probability
    def hitung_prior_probability(self):
        pp_menang = self.buat_prob_aspek('hasil', 'Menang')
        pp_kalah = self.buat_prob_aspek('hasil', 'Kalah')
        arr_pp = (pp_menang, pp_kalah)
        total_pp = ProbAspek.hitung_jml_total_aspek(arr_pp)
        self.prior_probability['Menang'] = total_pp['menang'] / (total_pp['menang'] + total_pp['kalah'])
        self.prior_probability['Kalah'] = total_pp['kalah'] / (total_pp['menang'] + total_pp['kalah'])
        # TODO: [SOAL-2] Prior Probability-nya masih 0, hitunglah prior probability yang sebenarnya!

    # TODO: [LANGKAH-9] Membuat method untuk memprediksi hasil akhir berdasarkan nilai aspek
    def prediksi(self, nilai_pelatih: str, nilai_kandang_sendiri: str, nilai_latihan: str, nilai_stamina: str, nilai_mental: str):

        self.hitung_prior_probability()
        predict_menang = self.prior_probability['Menang'] * \
                        self.aspek_pelatih[nilai_pelatih].p_aspek_menang * \
                        self.aspek_kandang_sendiri[nilai_kandang_sendiri].p_aspek_menang * \
                        self.aspek_latihan[nilai_latihan].p_aspek_menang * \
                        self.aspek_stamina[nilai_stamina].p_aspek_menang * \
                        self.aspek_mental[nilai_mental].p_aspek_menang
        print('Peluang Menang: {}'.format(predict_menang))

        predict_kalah = self.prior_probability['Kalah'] * \
                        self.aspek_pelatih[nilai_pelatih].p_aspek_kalah * \
                        self.aspek_kandang_sendiri[nilai_kandang_sendiri].p_aspek_kalah * \
                        self.aspek_latihan[nilai_latihan].p_aspek_kalah * \
                        self.aspek_stamina[nilai_stamina].p_aspek_kalah * \
                        self.aspek_mental[nilai_mental].p_aspek_kalah
        print('Peluang Kalah: {}'.format(predict_kalah))

        if predict_kalah > predict_menang:
            hasil = "Kalah"
            peluang = predict_kalah
        else:
            hasil = "Menang"
            peluang = predict_menang
        return {'hasil': hasil, 'peluang': peluang}