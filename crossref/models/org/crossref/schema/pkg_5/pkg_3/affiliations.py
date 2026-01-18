from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.org.crossref.schema.pkg_5.pkg_3.institution import (
    Institution,
)

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass(kw_only=True)
class Affiliations:
    class Meta:
        name = "affiliations"
        namespace = "http://www.crossref.org/schema/5.3.1"

    institution: list[Institution] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
