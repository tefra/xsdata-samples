from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.org.crossref.schema.pkg_5.pkg_3.std_designator_t import (
    StdDesignatorT,
)

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class StdSetDesignator(StdDesignatorT):
    """
    Provides for defining a DOI for a set of standards (sometimes know as
    truncated form).
    """

    class Meta:
        name = "std_set_designator"
        namespace = "http://www.crossref.org/schema/5.3.1"

    family: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
