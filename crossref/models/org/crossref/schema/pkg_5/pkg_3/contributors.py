from dataclasses import dataclass, field
from typing import List
from crossref.models.org.crossref.schema.pkg_5.pkg_3.anonymous import Anonymous
from crossref.models.org.crossref.schema.pkg_5.pkg_3.organization import (
    Organization,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.person_name import (
    PersonName,
)

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Contributors:
    """
    The container for all who contributed to authoring or editing an item.
    """

    class Meta:
        name = "contributors"
        namespace = "http://www.crossref.org/schema/5.3.1"

    organization: List[Organization] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    person_name: List[PersonName] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    anonymous: List[Anonymous] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
