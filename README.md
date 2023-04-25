# Ohjelmistotekniikka, harjoitustyö

Sovellus on muistipeli, jossa pelaaja voi valita itse vaikeustason kolmesta vaihtoehdosta.

[Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](dokumentaatio/tyoaikakirjanpito.md)

[Changelog](dokumentaatio/changelog.md)

[Rakenne](dokumentaatio/arkkitehtuuri.md)

[Release](https://github.com/sonjasil/ot-harjoitustyo/releases/tag/viikko5)

## Käynnistysohje

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

Testikattavuusraportti luodaan hakemistoon __htmlcov__ komennolla:

```bash
poetry run invoke coverage-report
```

Pylint-tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```