from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass(kw_only=True)
class Timestamp:
    """
    An integer representation of date and time that serves as a version
    number for the record that is being deposited, used to uniquely
    identify batch files and DOI values when a DOI has been updated one or
    more times.
    """

    class Meta:
        name = "timestamp"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: int = field(
        metadata={
            "required": True,
        }
    )
