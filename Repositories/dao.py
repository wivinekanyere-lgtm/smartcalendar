# Exercice 1
## Implémentation des DAOs des modèles DTO suivant le diagramme class_comp.puml

# Avec Python, les class Interfaces peuvent être implémentées comme des classes abstraites
# heritant de Protocol
import sqlite3
from typing import Protocol

from Models import EnseignantDTO, EtudiantDTO, UserDTO


class DAO:
    def __init__(self, db_path: str = ":memory:"):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self._setup_db()

    def _setup_db(self):
        cursor = self.conn.cursor()

        # Réquêtes de création lors de l'initialisation des tables si elles n'existent pas
        # 1. Création de la table Users sur base de la classe UserDTO

        cursor.execute(
            "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, role TEXT, email TEXT, google_linked BOOLEAN)"
        )

        # 2. Création de la table Etudiant
        # 3. Création de la table Enseignant
        # 4. Création de la table Promotion
        # 5. Création de la table UniteEnseignement
        # 6. Création de la table Cours
        # 7. Création de la table Seance

        # Confirmation des réquêtes dans la transaction
        self.conn.commit()


class BaseDAO(Protocol):
    def get_by_id(self, id) -> DAO: ...

    def get_all(self) -> list[DAO]: ...

    def save(self, obj) -> None: ...

    def delete(self, id) -> None: ...


class UserDAO(DAO):
    def __init__(
        self,
    ):
        pass

    def get_by_id(self, id) -> UserDTO: ...

    def get_all(self) -> list[UserDTO]: ...

    def save(self, UserDTO) -> None: ...

    def delete(self, id: int) -> None: ...

    def get_by_email(self, email) -> UserDTO: ...


class EtudiantDAO(DAO):
    def __init__(self):
        pass

    def get_by_id(self, id) -> EtudiantDTO: ...

    def get_all(self) -> list[EtudiantDTO]: ...

    def save(self, UserDTO) -> None: ...

    def delete(self, id: int) -> None: ...

    def get_by_promotion(self, promotion_id) -> list[EtudiantDTO]: ...


class EnseignantDAO(DAO):
    def __init__(self):
        pass

    def get_by_id(self, id) -> EnseignantDTO: ...

    def get_all(self) -> list[EnseignantDTO]: ...

    def save(self, EnseignantDAO) -> None: ...

    def delete(self, id_enseignant) -> None: ...

    def get_by_ue(self, ue_id) -> list[EnseignantDTO]: ...


class PromotionDAO(DAO):
    def __init__(self) -> None:
        pass


class EventDAO(DAO):
    def __init__(
        self,
    ):
        pass
