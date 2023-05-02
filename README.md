# Ohjelmistotekniikka, harjoitustyö

Sovellus on muistipeli, jossa pelaaja voi valita itse vaikeustason kolmesta vaihtoehdosta. Laattoja käännellään hiiren klikkauksella. Pelaaja näkee oman parhaan tuloksensa joka tason kohdalla erikseen.

[Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](dokumentaatio/tyoaikakirjanpito.md)

[Changelog](dokumentaatio/changelog.md)

[Rakenne](dokumentaatio/arkkitehtuuri.md)

[Releaset](https://github.com/sonjasil/ot-harjoitustyo/releases)

## Käyttöohje

Asenna ensin sovelluksen riippuvuudet komennolla:

```bash
poetry install
```

Sovellus käynnistyy komennolla:

```bash
poetry run invoke start
```

Testien suoritus tapahtuu komennolla:

```bash
poetry run invoke test
```

Testikattavuusraportti luodaan __htmlcov__-hakemistoon komennolla:

```bash
poetry run invoke coverage-report
```

Pylint-tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```

Peli käynnistyy valikkoon, josta valitaan vaikeustaso. Vaikeustaso vaikuttaa muistipelin korttien määrään. Alin taso on 1. Kortteja käännetään hiirellä klikkaamalla. Kortit kääntyvät itsestään ympäri hetken päästä, jos hiireä liikauttaa toisen kortin klikkaamisen jälkeen. Tason alalaidassa näkyy käännettyjen korttiparien määrä. Tavoitteena on saada mahdollisimman pieni tulos.
