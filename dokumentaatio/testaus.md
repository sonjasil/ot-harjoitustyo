# Testausdokumentti

Ohjelmaa on testattu sekä unittestin avulla että manuaalisesti.

## Järjestelmätestaus

Järjestelmätestausta on suoritettu manuaalisesti.

### Toiminnallisuus

Jokaisen tason toimivuus on testattu. Sovellus ei lue käyttäjän luomia syötteitä, vaan pelkästään hiiren liikkeitä, joten käyttäjän toiminta ei voi juuri saada aikaan virhetilanteita.

## Ratkaisemattomat ongelmat

Kun kaksi korttia on käännetty, ne kääntyvät itsestään takaisin 2,5 sekunnin päästä. Tämä ajastin on kuitenkin tällä hetkellä sidoksissa näppäimistön tai hiiren tapahtumiin. Kortit eivät siis käänny takaisin ympäri, ellei käyttäjä liikuta hiirtä tai paina jotakin hiiren tai näppäimistön painiketta.