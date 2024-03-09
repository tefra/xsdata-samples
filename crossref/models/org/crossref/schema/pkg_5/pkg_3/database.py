from dataclasses import dataclass, field
from typing import List, Optional

from crossref.models.org.crossref.schema.pkg_5.pkg_3.component_list import (
    ComponentList,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.database_metadata import (
    DatabaseMetadata,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.dataset import Dataset

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Database:
    """
    Database is the top level element for deposit of metadata about one or more
    datasets or records in a database.
    """

    class Meta:
        name = "database"
        namespace = "http://www.crossref.org/schema/5.3.1"

    database_metadata: Optional[DatabaseMetadata] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    dataset: List[Dataset] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    component_list: Optional[ComponentList] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
