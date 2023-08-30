from dataclasses import dataclass, field
from typing import List
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.institution import Institution

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Affiliations:
    class Meta:
        name = "affiliations"
        namespace = "http://www.crossref.org/schema/5.3.1"

    institution: List[Institution] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
