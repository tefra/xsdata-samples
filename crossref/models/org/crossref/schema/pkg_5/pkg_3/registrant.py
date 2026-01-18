from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass(kw_only=True)
class Registrant:
    """
    The organization responsible for the information being registered.
    """

    class Meta:
        name = "registrant"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "min_length": 1,
            "max_length": 255,
        },
    )
