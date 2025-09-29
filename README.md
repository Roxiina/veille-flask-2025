# Veille Technologique : Flask (2025)

## Introduction
Flask est un micro-framework Python léger, orienté vers la simplicité et l’extensibilité. Malgré l’émergence de solutions plus performantes comme FastAPI, Flask demeure largement utilisé pour le prototypage rapide, la mise en œuvre de microservices et les projets nécessitant un contrôle fin sur les composants.

Cette veille met en évidence les évolutions récentes, les bonnes pratiques associées ainsi que les principaux défis liés à l’utilisation de Flask en 2025.

---

## Points Clés de la Veille

### 1. Correctif de sécurité : CVE-2025-47278
- **Lien** : [Flask 3.1.1 Release](https://github.com/pallets/flask/releases/tag/3.1.1)  
- **Résumé** : La vulnérabilité affectait Flask 3.1.0 et provenait d’une mauvaise gestion des clés de repli (`SECRET_KEY_FALLBACKS`), pouvant entraîner l’utilisation de clés périmées pour la signature des sessions.  
- **Impact** : Obligation de mettre à jour vers 3.1.1 pour corriger le problème.

### 2. Migration SQLAlchemy 2.0
- **Lien** : [Flask-SQLAlchemy Documentation](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/queries/#select)  
- **Résumé** : L’ancienne API `Query` est désormais dépréciée. Les requêtes doivent être construites avec `select()` et traitées via `Session.scalars()`.  
- **Impact** : Adaptation du code existant et formation des équipes aux nouvelles pratiques.

### 3. Dockerisation de Flask
- **Concept** : Utilisation de conteneurs Docker pour la portabilité et l’isolation.  
- **Résumé** : Création d’un `Dockerfile` basé sur une image Python slim et utilisation de `docker-compose` pour orchestrer plusieurs services (par ex. Flask + PostgreSQL).  
- **Impact** : Standardisation des environnements et simplification du déploiement.

### 4. API RESTful et Sécurité
- **Concept** : Extension Flask-RESTful pour structurer les APIs.  
- **Résumé** : Définition des endpoints via la classe `Resource` et sécurisation avec des outils tels que `flask-httpauth`.  
- **Impact** : Meilleure organisation des APIs et renforcement de la sécurité par authentification.

### 5. Gestion des dépendances et tests unitaires
- **Résumé** : Les dépendances doivent être explicitement fixées (`Flask>=2.3.0,<3.0.0`) afin d’éviter les ruptures de compatibilité avec les extensions (ex. Flask-Login).  
- **Impact** : Mise en place de tests unitaires systématiques pour garantir la stabilité des applications et valider les réponses HTTP.

### 6. Comparaison Flask vs FastAPI (2025)
- **Résumé** :  
  - *Flask* : flexibilité, légèreté, idéal pour les microservices.  
  - *FastAPI* : performance accrue (support natif asynchrone/ASGI), validation de schémas (Pydantic), auto-documentation via OpenAPI.  
- **Impact** : Le choix dépend du contexte : rapidité de prototypage (Flask) ou performances et scalabilité (FastAPI).

### 7. Techniques avancées (Jinja2 et décorateurs)
- **Résumé** :  
  - Utilisation de Jinja2 pour la génération dynamique d’HTML.  
  - Décorateurs comme `@app.route` pour transformer des fonctions Python en vues.  
  - Décorateurs personnalisés possibles pour ajouter de la logique (ex. suivi des IP, contrôle des cookies).  
- **Impact** : Renforcement de l’extensibilité et personnalisation des comportements applicatifs.

---

## Ressources utilisées
1. [Flask 3.1.1 Release Notes (GitHub)](https://github.com/pallets/flask/releases/tag/3.1.1)  
2. [Flask-SQLAlchemy Queries Documentation](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/queries/#select)  
3. [Documentation officielle Flask](https://flask.palletsprojects.com)  
4. [Tutoriel Flask REST API avec Flask-RESTful (Analytics Vidhya)](https://www.analyticsvidhya.com/blog/2022/01/rest-api-with-python-and-flask/)  
5. [Comparatif Flask vs Node/Frameworks backend (Ingenious Minds Lab, 2025)](https://ingeniousmindslab.com/blogs/python-vs-node-best-backend-framework/)  
6. [Discussion sur Flask-Login et compatibilité (GitHub Commit)](https://github.com/pallets/flask/commit/7d98a49bc38d0849367b348bfe37a2b689323419)  
7. [Bootstrap 4.3.1 CDN (pour intégration Flask)](https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css)  


---

## Conclusion
Flask conserve en 2025 une pertinence certaine grâce à sa simplicité et sa flexibilité. Toutefois, son utilisation doit s’accompagner d’une gestion rigoureuse des dépendances, d’une prise en compte des nouvelles pratiques liées à SQLAlchemy 2.0, et d’une vigilance particulière sur la sécurité. L’évaluation de son emploi face à FastAPI demeure un enjeu stratégique selon les priorités de performance, de scalabilité et de rapidité de développement.
