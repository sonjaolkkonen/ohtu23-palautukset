class IntJoukko:
    KAPASITEETTI = 5
    OLETUSKASVATUS = 5

    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = kapasiteetti or self.KAPASITEETTI
        self.kasvatuskoko = kasvatuskoko or self.OLETUSKASVATUS
        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def _luo_lista(self, koko):
        return [0] * koko

    def _varmista_kapasiteetti(self):
        if self.alkioiden_lkm % len(self.ljono) == 0:
            uusi_koko = self.alkioiden_lkm + self.kasvatuskoko
            uusi_lista = self._luo_lista(uusi_koko)
            self._kopioi_lista(self.ljono, uusi_lista)
            self.ljono = uusi_lista

    def kuuluu(self, n):
        return n in self.ljono[:self.alkioiden_lkm]

    def lisaa(self, n):
        if not self.kuuluu(n):
            self._varmista_kapasiteetti()
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1
            return True
        return False

    def poista(self, n):
        if n in self.ljono[:self.alkioiden_lkm]:
            indeksi = self.ljono.index(n)
            self.ljono[indeksi:self.alkioiden_lkm-1] = self.ljono[indeksi+1:self.alkioiden_lkm]
            self.alkioiden_lkm -= 1
            return True
        return False

    def _kopioi_lista(self, lahde, kohde):
        kohde[:len(lahde)] = lahde

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[:self.alkioiden_lkm]

    @staticmethod
    def _yhdiste_leikkaus_eroitus(a, b, operaatio):
        tulos = IntJoukko()
        a_taulu, b_taulu = a.to_int_list(), b.to_int_list()

        for i in range(len(a_taulu)):
            for j in range(len(b_taulu)):
                if operaatio(a_taulu[i], b_taulu[j]):
                    tulos.lisaa(a_taulu[i])

        return tulos

    @staticmethod
    def yhdiste(a, b):
        tulos = IntJoukko()

        for joukko in [a, b]:
            for luku in joukko.to_int_list():
                tulos.lisaa(luku)

        return tulos

    @staticmethod
    def leikkaus(a, b):
        return IntJoukko._yhdiste_leikkaus_eroitus(a, b, lambda x, y: x == y)

    @staticmethod
    def erotus(a, b):
        return IntJoukko._yhdiste_leikkaus_eroitus(a, b, lambda x, y: not x in b.to_int_list())

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            return "{" + ", ".join(map(str, self.ljono[:self.alkioiden_lkm])) + "}"


