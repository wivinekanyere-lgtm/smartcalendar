# Exercice 1
## Implémentation des DAOs des modèles DTO suivant le diagramme class_comp.puml

class BaseDAO:

    def _init_(self):
        self.data = []

    def save(self, obj):
        self.data.append(obj)

    def get_all(self):
        return self.data


class EtudiantDAO(BaseDAO):

    def get_by_promotion(self, id_promotion):
        return [
            etudiant
            for etudiant in self.data
            if etudiant.id_promotion == id_promotion
        ]


class EnseignantDAO(BaseDAO):

    def get_by_id(self, id_enseignant):

        for enseignant in self.data:

            if enseignant.id_enseignant == id_enseignant:
                return enseignant

        return None


class UniteEnseignementDAO(BaseDAO):

    def get_by_promotion(self, id_promotion):

        return [
            ue
            for ue in self.data
            if ue.id_promotion == id_promotion
        ]



class CoursDAO(BaseDAO):

    def get_by_ue(self, id_ue):

        return [
            cours
            for cours in self.data
            if cours.id_ue == id_ue
        ]



class SeanceDAO(BaseDAO):

    def get_by_date(self, date):

        return [
            seance
            for seance in self.data
            if seance.date == date
        ]

    def update_sync_status(self, id_seance, statut):

        for seance in self.data:

            if seance.id_seance == id_seance:
                seance.synchro = statut
                return True

        return False