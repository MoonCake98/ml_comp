## Wijze van inleveren van je classifier

Om het automatisch runnen en testen van je classifier mogelijk te maken moet de wijze van inleveren aan een aantal eisen voldoen.

Maak een directory met de naam van je team (die naam moet dus voldoen aan [de PEP8-standaarden van naamgeving van packages](https://peps.python.org/pep-0008/#package-and-module-names)). Maak in deze directory een bestand `__init__.py` waarin je een methode `model_factory()` maakt. Deze methode moet een instantie van je classifier teruggeven. De classifier is de klasse die een methode `predict(self, filename='competition-test.csv)` bevat:

Parameters:
    **filename : string** default='competition-test.csv'
    Location of the filename to be used in the prediction. 
    This can be either a relative of an absolute path.

Returns:
    ***y_pred : ndarray of shape (n_samples,)***
    Vector containing the class labels for each sample.

Behalve deze factory heeft `__init__.py` ook een *docstring* waarin je wat informatie over je groep en je classifier hebt staan. Zorg ervoor dat deze hele directory als zip op eJournal komt; de algemene structuur van je directory is dat als onderstaand. Zie de bijgaande `trash`-directory voor een uitgewerkt voorbeeld.

```shell
/group_name
    __init__.py          <-- Deze bevat docstring en methode model_factory()
    AwesomeClassifier.py <-- Een instantie hiervan wordt teruggegeven door model_factory()
    AndereKlasse.py      <-- Deze wordt gebruikt door AwesomeClassifier, maar verder niet geëxporteerd
    NogAndereKlasse.py   <-- Deze ook niet
```

