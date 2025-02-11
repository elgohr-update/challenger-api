from typing import Any, List, Optional, Union

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.models import SpeciesCommonNames, SpeciesSynonyms

router = APIRouter()


@router.get("/", response_model=schemas.SpeciesSummaryPagination)
def read_species(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    order_by: Optional[List[str]] = Query(None),
) -> Any:
    """Retrieve species."""
    species = crud.species.get_multi(db, skip=skip, limit=limit, order_by=order_by)
    return species


@router.get("/all/", response_model=List[schemas.SpeciesSummary])
def read_all_species(
    db: Session = Depends(deps.get_db), order_by: Optional[List[str]] = Query(None)
) -> Any:
    """Retrieve all species."""
    species = crud.species.get_all(db, order_by=order_by)
    return species


@router.post("/search/", response_model=List[schemas.SpeciesSummary])
def read_species_by_search(
    expressions: Union[schemas.Expression, schemas.ExpressionGroup],
    db: Session = Depends(deps.get_db),
    limit: int = 0,
    order_by: Optional[List[str]] = Query(None),
) -> Any:
    """Retrieves the species based on the given search expressions."""
    species = crud.species.search(
        db,
        expressions=expressions,
        order_by=order_by,
        limit=limit,
    )
    return species


@router.get("/fuzzymatch/", response_model=List[schemas.SpeciesSummary])
def read_fuzzy_species_by_search(
    query_str: str,
    db: Session = Depends(deps.get_db),
    min_string_similarity_score: float = 0.2,
    limit: int = 0,
    order_by: Optional[List[str]] = Query(None),
) -> Any:

    expressions_dict: dict = {
        "join": "OR",
        "expressions": [
            {
                "column_name": "matched_canonical_full_name",
                "search_term": query_str,
                "operator": "eq",
                "fuzzy": True,
                "min_string_similarity": min_string_similarity_score,
            },
            {
                "column_name": "current_name",
                "search_term": query_str,
                "operator": "eq",
                "fuzzy": True,
                "min_string_similarity": min_string_similarity_score,
            },
            {
                "column_name": "name",
                "search_term": query_str,
                "operator": "eq",
                "fuzzy": True,
                "min_string_similarity": min_string_similarity_score,
            },
            {
                "column_name": "scientific_name",
                "search_term": query_str,
                "operator": "eq",
                "fuzzy": True,
                "min_string_similarity": min_string_similarity_score,
            },
        ],
    }

    expressions = schemas.ExpressionGroup(**expressions_dict)

    """Retrieves the species based on the given search expressions."""
    species = crud.species.search(
        db,
        expressions=expressions,
        relations=[SpeciesCommonNames, SpeciesSynonyms],
        order_by=order_by,
        limit=limit,
    )
    return species


@router.get(
    "/{species_id}",
    response_model=schemas.SpeciesDetails,
)
def read_species_by_id(
    species_id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get a specific species by id."""
    species = crud.species.get(db, id=species_id)
    if not species:
        raise HTTPException(status_code=404, detail=f"Species not found: ${species_id}")
    return species
