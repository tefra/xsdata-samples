from dataclasses import dataclass, field
from typing import List, Optional
from crossref.models.org.crossref.schema.pkg_5.pkg_3.conference_date import ConferenceDate

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class EventMetadata:
    """A container for all information that applies to a conference event.

    event_metadata captures information about a conference event. Data
    about conference proceedings is captured in proceedings_metadata.
    """
    class Meta:
        name = "event_metadata"
        namespace = "http://www.crossref.org/schema/5.3.1"

    conference_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 3,
            "max_length": 512,
        }
    )
    conference_theme: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 1,
            "max_length": 255,
        }
    )
    conference_acronym: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 1,
            "max_length": 127,
        }
    )
    conference_sponsor: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 10,
            "min_length": 1,
            "max_length": 255,
        }
    )
    conference_number: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 1,
            "max_length": 15,
        }
    )
    conference_location: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 2,
            "max_length": 255,
        }
    )
    conference_date: Optional[ConferenceDate] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
