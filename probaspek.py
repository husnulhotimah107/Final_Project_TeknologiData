class ProbAspek:

    def __init__(self, nama_aspek: str, nilai_aspek: str):
        pass
    # TODO: [LANGKAH-1] Buat class untuk menampung nilai matriks probabilitas

        self.nama_aspek = nama_aspek
        self.nilai_aspek = nilai_aspek
        self.jml_menang = 0
        self.jml_kalah = 0
        self.p_aspek_menang = 0
        self.p_aspek_kalah = 0

    def hitung_p_aspek_menang(self, jml_total_menang_aspek):
        self.p_aspek_menang = self.jml_menang / jml_total_menang_aspek
        return self

    def hitung_p_aspek_kalah(self, jml_total_kalah_aspek):
        self.p_aspek_kalah = self.jml_kalah / jml_total_kalah_aspek
        return self
#probabilitas
    def print(self):
        print('Aspek    : {}'.format(self.nama_aspek))
        print('Nilai    : {}'.format(self.nilai_aspek))
        print('Jml Menang: {}'.format(self.jml_menang))
        print('Jml kalah: {}'.format(self.jml_kalah))
        print('P({}|Menang): {}'.format(self.nilai_aspek, self.p_aspek_menang))
        print('P({}|kalah): {}'.format(self.nilai_aspek, self.p_aspek_kalah))
        print('------------------------------------------')

    @staticmethod
    def hitung_jml_total_aspek(pa_list: list) -> dict:
        jumlah = {'menang': 0, 'kalah': 0}
        for pa in pa_list:
            jumlah['menang'] += pa.jml_menang
            jumlah['kalah'] += pa.jml_kalah
        return jumlah

    @staticmethod
    def print_matrix_probabilitas(pa_list: list):
        for pa in pa_list:
            pa.print()
