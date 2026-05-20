# Exercice 1
## Implémentation des DAOs des modèles DTO suivant le diagramme class_comp.puml

from Models import EnseignantDTO, EtudiantDTO, UserDTO


class BaseDAO:
    def get_by_id(self, id) -> object: ...

    def get_all(self) -> list[object]: ...

    def save(self, obj) -> None: ...

    def delete(self, id) -> None: ...


class UserDAO:
    def __init__(
        self,
    ):
        pass

    def get_by_id(self, id) -> UserDTO: ...

    def get_all(self) -> list[UserDTO]: ...

    def save(self, UserDTO) -> None: ...

    def delete(self, id: int) -> None: ...

    def get_by_email(self, email) -> UserDTO: ...


class EtudiantDAO:
    def __init__(self):
        pass

    def get_by_id(self, id) -> EtudiantDTO: ...

    def get_all(self) -> list[EtudiantDTO]: ...

    def save(self, UserDTO) -> None: ...

    def delete(self, id: int) -> None: ...

    def get_by_promotion(self, promotion_id) -> list[EtudiantDTO]: ...


class EnseignantDAO:
    def __init__(self):
        pass

    def get_by_id(self, id) -> EnseignantDTO: ...

    def get_all(self) -> list[EnseignantDTO]: ...

    def save(self, EnseignantDAO) -> None: ...

    def delete(self, id_enseignant) -> None: ...

    def get_by_ue(self, ue_id) -> list[EnseignantDTO]: ...


class PromotionDAO:
    def __init__(self) -> None:
        pass


class EventDAO:
    def __init__(
        self,
    ):
        pass
