from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass(kw_only=True)
class ConferenceSponsor:
    """
    The sponsoring organization(s) of a conference.

    Multiple sponsors may be given if a conference is hosted by more than
    one organization.
    """

    class Meta:
        name = "conference_sponsor"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "min_length": 1,
            "max_length": 255,
        },
    )
