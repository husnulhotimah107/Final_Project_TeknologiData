from naivebayes import NaiveBayes


class Main:
    @staticmethod
    def main():
        nb = NaiveBayes()
        nb.load_data_training()
        nb.mulai_training()

        # TODO: [LANGKAH-10] Cobalah untuk melakukan prediksi!
        # Apabila Pelatih 'Pengertian', Kandang Sendiri 'Tidak', Latihannya 'Rutin', Staminanya 'Kuat', dan Mentalnya 'PD',
        # Tim sepakbolanya menang atau kalah?

        hasil_prediksi = nb.prediksi(nilai_pelatih='Pengertian',
                    nilai_kandang_sendiri='Tidak',
                    nilai_latihan='Rutin',
                    nilai_stamina='Kuat',
                    nilai_mental='PD')
        print('=====================================')
        
        print('Hasil akhir prediksi = {}, dengan peluang sebesar {}%'.format(hasil_prediksi['hasil'], hasil_prediksi['peluang']))

Main.main()
