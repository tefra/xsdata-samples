from dataclasses import dataclass, field
from typing import Optional

from crossref.models.org.crossref.schema.pkg_5.pkg_3.conference_acronym import (
    ConferenceAcronym,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.conference_date import (
    ConferenceDate,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.conference_location import (
    ConferenceLocation,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.conference_name import (
    ConferenceName,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.conference_number import (
    ConferenceNumber,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.conference_sponsor import (
    ConferenceSponsor,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.conference_theme import (
    ConferenceTheme,
)

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class EventMetadata:
    """
    A container for all information that applies to a conference event.
    event_metadata captures information about a conference event.

    Data about conference proceedings is captured in proceedings_metadata.
    """

    class Meta:
        name = "event_metadata"
        namespace = "http://www.crossref.org/schema/5.3.1"

    conference_name: Optional[ConferenceName] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    conference_theme: Optional[ConferenceTheme] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    conference_acronym: Optional[ConferenceAcronym] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    conference_sponsor: list[ConferenceSponsor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 10,
        },
    )
    conference_number: Optional[ConferenceNumber] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    conference_location: Optional[ConferenceLocation] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    conference_date: Optional[ConferenceDate] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
