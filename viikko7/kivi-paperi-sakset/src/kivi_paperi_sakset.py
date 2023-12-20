from tuomari import Tuomari
from konsoli_io import KonsoliIO 

class KiviPaperiSakset:
    def pelaa(self):
        tuomari = Tuomari()
        self.konsoli_io = KonsoliIO()

        ekan_siirto = self.konsoli_io.lue("Ensimmäisen pelaajan siirto: ")
        tokan_siirto = self._toisen_siirto(ekan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            self.konsoli_io.kirjoita(tuomari)

            ekan_siirto = self.konsoli_io.lue("Ensimmäisen pelaajan siirto: ")
            tokan_siirto = self._toisen_siirto(ekan_siirto)

        self.konsoli_io.kirjoita("Kiitos!")
        self.konsoli_io.kirjoita(tuomari)


    # tämän metodin toteutus vaihtelee eri pelityypeissä
    def _toisen_siirto(self, ensimmaisen_siirto):
        # metodin oletustoteutus
        return "k"

    def _onko_ok_siirto(self, siirto):
        return siirto in ("k", "p", "s")