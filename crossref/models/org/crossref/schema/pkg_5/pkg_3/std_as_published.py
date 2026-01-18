from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.org.crossref.schema.pkg_5.pkg_3.std_designator_t import (
    StdDesignatorT,
)

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class StdAsPublished(StdDesignatorT):
    """
    Designator or other primary identifier for the standard being
    deposited.
    """

    class Meta:
        name = "std_as_published"
        namespace = "http://www.crossref.org/schema/5.3.1"

    family: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    set: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    undated: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
