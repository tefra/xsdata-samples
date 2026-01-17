from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class ConferenceNumber:
    """
    The number of a conference. conference_number should include only the
    number of the conference without any extra text.
    """

    class Meta:
        name = "conference_number"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "min_length": 1,
            "max_length": 15,
        },
    )
