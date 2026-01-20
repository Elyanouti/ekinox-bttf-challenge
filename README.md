---

# 🎬 Back to the Future - Billing System

Solution automatisée pour le calcul des prix et remises DVD.

---

### Structure du Projet

```text
ekinox-bttf-challenge/
│
├── core/              # Moteur de calcul (Logique métier)
├── screenshots/       # Preuves (Tests ✅ & Interface )
├── app.py             # Interface Streamlit
├── tests.py           # Tests automatisés
├── Dockerfile         # Environnement isolé
└── README.md          # Documentation

```

---

###  Lancement Rapide (Docker)

1. **Build** : `docker build -t bttf-app .`
2. **Run** : `docker run -p 8501:8501 bttf-app`
3. **Accès** : `http://localhost:8501`

---

###  Pourquoi Docker ?

* **Cohésion de Team** : Environnement identique pour tous les développeurs.
* **Zéro Config** : Aucune installation manuelle requise (Python, dépendances).
* **Isolation** : Garantie de fonctionnement instantané.

---

### ✅ Tests & Validation

Exécuter les tests unitaires :

```bash
python tests.py

```

---

###  Méthodologie (Screenshots)

Des preuves de réalisation sont disponibles dans **/screenshots** :

* **Interface** : Capture du calcul réussi pour le cas complexe (56€).
* **Technique** : Capture du terminal montrant 100% des tests validés (✅ OK).
* **Parsing** : Algorithme capable de traiter des listes brutes (Bulk Input).

---
