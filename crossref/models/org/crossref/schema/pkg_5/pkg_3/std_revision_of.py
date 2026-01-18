from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass(kw_only=True)
class StdRevisionOf:
    """
    Designator for the previous revision of the standard being deposited.
    (note: use alt_as_published for revisions within designators having
    common stem).
    """

    class Meta:
        name = "std_revision_of"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 2,
            "max_length": 150,
        },
    )
