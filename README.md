# Génération de texte avec vos données messenger

## But du projet

Le but de ce projet est de créer un générateur de texte parlant comme vous ! 
Pour cela, vous pouvez récupérer vos données Messenger sur Facebook puis entrainé le modèle avec. 
Ensuite, vous pourrez générer vos conversations.

Ce projet a été réalisé pour l'EC de Machine Learning encadré par [Clément Chatelain](https://pagesperso.litislab.fr/cchatelain/), enseignant chercheur en Machine Learning. 
Il a été réalisé par [Nathan Astegiano](https://github.com/nastegiano), [Louis Dispa](https://github.com/LouisDISPA) et [Lucas Scellos](https://github.com/LucasScellos).

## Utilisation

Le projet utilise :

- **JavaScript** : pour parser les données de Facebook
- **python** : pour entrainer et tester le modèle

Les données téléchargées de Facebook doivent être au format JSON.  
Il faut mettre le dossier `inbox`, contenant les conversations, dans le répertoire `code` pour ensuite parser les fichiers.

Les commandes:

```bash
cd code

# preparer les conversations dans un fichier texte
node parse_message.js


cd model_training

# regroupe les messages en courte conversation
# et separe les données en jeu de d'entrainement et test
python3 prepare_data.py

# entraine le modèle
python3 train.py

# (optionnel) monitore le training
tensorboard --logdir runs/

# teste le modèle
python3 test.py
```

## Sources

[Technical Paper de GPT-2 par OpenAI, Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, Ilya Sutskever](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)