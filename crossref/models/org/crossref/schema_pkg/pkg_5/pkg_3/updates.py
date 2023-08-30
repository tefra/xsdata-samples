from dataclasses import dataclass, field
from typing import List
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.update import Update

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Updates:
    """A document might provide updates (e.g. corrections, clarifications,
    retractions) to several other documents.

    When this is the case, the DOIs of the documents that are being
    *updated* should be listed here.
    """
    class Meta:
        name = "updates"
        namespace = "http://www.crossref.org/schema/5.3.1"

    update: List[Update] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
