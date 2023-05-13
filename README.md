# Ohjelmistotekniikka, harjoitustyö

Sovellus on muistipeli, jossa pelaaja voi valita itse vaikeustason kolmesta vaihtoehdosta. Laattoja käännellään hiiren klikkauksella. Pelaaja näkee oman parhaan tuloksensa joka tason kohdalla erikseen.

[Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](dokumentaatio/tyoaikakirjanpito.md)

[Changelog](dokumentaatio/changelog.md)

[Käyttöohje](dokumentaatio/kaytto.md)

[Testausdokumentti](dokumentaatio/testaus.md)

[Sovellusarkkitehtuuri](dokumentaatio/arkkitehtuuri.md)

[Releaset](https://github.com/sonjasil/ot-harjoitustyo/releases)

## Käynnistysohje

Asenna ensin sovelluksen riippuvuudet komennolla:

```bash
poetry install
```

Sovellus käynnistyy komennolla:

```bash
poetry run invoke start
```

## Muut komentorivikomennot

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