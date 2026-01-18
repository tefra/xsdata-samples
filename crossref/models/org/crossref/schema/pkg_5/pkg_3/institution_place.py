from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass(kw_only=True)
class InstitutionPlace:
    """
    The primary city location of the institution. institution_place gives
    the primary city location of the institution.

    When the location is a major city (e.g. New York, Amsterdam), no
    qualifying country or U.S. state need be given. If the city is not a
    major city, the appropriate country and/or state or province should be
    added.
    """

    class Meta:
        name = "institution_place"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "min_length": 2,
            "max_length": 255,
        },
    )
