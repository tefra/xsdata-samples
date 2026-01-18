from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass(kw_only=True)
class GivenName:
    """
    A contributor's given name.
    """

    class Meta:
        name = "given_name"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "min_length": 1,
            "max_length": 60,
            "white_space": "collapse",
            "pattern": r"[^\d\?]*[^\?\s]+[^\d]*",
        },
    )
