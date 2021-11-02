from datetime import date  # noqa
from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null

from app.db.base_class import Base

if TYPE_CHECKING:
    from app.models import Species


class DataSource(Base):
    """The data source used by Global Names"""

    __tablename__ = "data_sources"

    id: int = Column(Integer, primary_key=True, index=True)
    title: str = Column(String(150), nullable=False, index=True)
    title_short: str = Column(String(150), nullable=False)
    description: Optional[str] = Column(String(length=900))
    curation: str = Column(String(90), nullable=False)
    record_count: Optional[int] = Column(Integer)
    updated_at: date = Column(Date, nullable=False)  # noqa: F811
    is_out_link_ready: bool = Column(Boolean, nullable=False)
    home_url: Optional[str] = Column(String(length=200))
    url_template: Optional[str] = Column(String(length=200))

    species: List["Species"] = relationship(
        "Species", back_populates="data_source", cascade="all, delete"
    )
