from dataclasses import dataclass, field
from typing import List, Optional
from crossref.models.org.crossref.schema.pkg_5.pkg_3.collection import (
    Collection,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.resource import Resource

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class DoiData:
    """
    The container for elements related directly to a DOI.
    """

    class Meta:
        name = "doi_data"
        namespace = "http://www.crossref.org/schema/5.3.1"

    doi: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 6,
            "max_length": 2048,
            "pattern": r"10\.[0-9]{4,9}/.{1,200}",
        },
    )
    timestamp: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    resource: Optional[Resource] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    collection: List[Collection] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
