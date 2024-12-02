from dataclasses import dataclass, field
from typing import Optional

from crossref.models.org.crossref.schema.pkg_5.pkg_3.collection import (
    Collection,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.doi import Doi
from crossref.models.org.crossref.schema.pkg_5.pkg_3.resource import Resource
from crossref.models.org.crossref.schema.pkg_5.pkg_3.timestamp import Timestamp

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class DoiData:
    """
    The container for elements related directly to a DOI.
    """

    class Meta:
        name = "doi_data"
        namespace = "http://www.crossref.org/schema/5.3.1"

    doi: Optional[Doi] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    timestamp: Optional[Timestamp] = field(
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
    collection: list[Collection] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
