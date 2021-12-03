from app.crud.base import CRUDBase
from app.models import Species
from app.schemas import SpeciesCreate, SpeciesUpdate, SpeciesSummaryPagination


class CRUDSpecies(
    CRUDBase[Species, SpeciesCreate, SpeciesUpdate, SpeciesSummaryPagination]
):
    pass


species = CRUDSpecies(Species)
