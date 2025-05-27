# CroixPharmacie

Ce projet permet de contrôler à distance l'affichage d'une croix de pharmacie. Si vous n'avez pas la chance de posséder une croix de pharmacie chez vous, le code vous permet également de simuler l'affichage localement.

[![Capture d'écran de la vidéo de Sylvqin](example.png)](https://www.youtube.com/watch?v=ghh-28ln-z4)

Ce projet a notamment servi pour la vidéo de Sylvqin sur les croix de pharmacie, cliquez sur l'image ci-dessus pour la regarder sur YouTube !

## Comment contribuer ?

Si vous souhaitez proposer un module (animation, jeu, etc.) pour la croix de pharmacie, c'est très simple : n'hésitez pas à vous inspirer du fichier [example.py](example.py) ou des autres modules.

Tout le contrôle de la croix de pharmacie (réelle ou simulée) passe par l'objet `pharmacontroller.PharmaScreen`. Pour afficher une image sur l'écran, utilisez sa méthode `set_image(img)`, où `img` est un tableau de 48x48 pixels sous formes de nombres flottants, compris entre 0.0 (noir) et 1.0 (vert).

Certaines zones de `img` sont inutilisées, car on affiche les pixels sur une croix et non un carré : vous pouvez y mettre n'importe quelle valeur. Pour vérifier si une coordonnée de pixel est sur la croix, utilisez la méthode `is_drawable` sur l'objet `PharmaScreen`

Pour des raisons matérielles, la croix gère deux modes de couleur :
- `PharmaScreen(color_scale=True)` peut afficher jusqu'à 8 nuances de vert, avec un taux de rafraîchissement de 20 FPS. C'est l'option par défaut.
- `PharmaScreen(color_scale=False)` ne gère que 2 couleurs (noir/vert), mais peut afficher jusqu'à 60 FPS.

![Chute de sable sur une croix de pharmacie](img/Sandfall.gif)

## Liste des modules

- Exemple - [example.py](example.py)
- Affichage d'une vidéo avec le son - [videoplayer.py](src/videoplayer.py)
- Jeu pong imaginé par [le_egar](https://twitter.com/le_egar/status/1517539004627001346), avec 4 joueurs - [pong.py](src/pong.py)
- Doom (voir instructions ci-dessous) - [doom.py](src/doom.py)
- Simulation de chute de sable - [falling_sand_simulation.py](src/falling_sand_simulation.py)
- Simon says - [simon.py](src/simon.py)
- Snake - [snake.py](src/snake.py)
- Animation d'un cube rotatif - [cube.py](src/cube.py)
- Affichage de texte - [textwriter.py](src/textwriter.py)
- Effets visuels - [visual_effects.py](src/visual_effects.py)
- Spirale hypnotique - [youreundercontrol.py](src/youreundercontrol.py)
- Plasma - [plasma.py](src/plasma.py)
- Rotozoom - [rotozoom.py](src/rotozoom.py)

Pour installer les dépendances Python, exécutez les commandes :

- `python -m venv venv`
- `source ./venv/bin/activate`
- `pip install -r requirements.txt`

## Une idée à ajouter ?

Les pull requests sont les bienvenues sur ce dépôt ! Les contributions ajoutées avant juin 2024 sont apparues sur la [vidéo de Sylvqin](https://www.youtube.com/watch?v=ghh-28ln-z4) sur le sujet 😉

Pour soumettre une idée si vous n'êtes pas en mesure de coder, n'hésitez pas à créer [une issue GitHub](https://github.com/MathisHammel/CroixPharmacie/issues), ou m'envoyer des propositions en [DM sur Twitter](https://twitter.com/MathisHammel).

## Comment exécuter Doom ?

L'exécution du module Doom est dépendante de cyDoomGeneric, un wrapper de DoomGeneric. L'installation se fait en plusieurs étapes :

```bash
git clone https://github.com/wojciech-graj/cydoomgeneric
cd cydoomgeneric/cydoomgeneric
python setup.py install
```

Vous pouvez maintenant exécuter doom.py pour le lancer sur la croix de pharmacie ! Utilisez les flèches pour vous déplacer, Ctrl gauche pour tirer, et la barre espace pour ouvrir les portes.
