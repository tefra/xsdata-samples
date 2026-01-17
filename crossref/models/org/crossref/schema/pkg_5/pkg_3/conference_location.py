from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class ConferenceLocation:
    """
    The location of the conference.

    The city, state, province or country of the conference may be provided
    as appropriate.
    """

    class Meta:
        name = "conference_location"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "min_length": 2,
            "max_length": 255,
        },
    )
