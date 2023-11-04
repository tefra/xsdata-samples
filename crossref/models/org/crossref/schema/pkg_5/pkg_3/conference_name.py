from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class ConferenceName:
    """
    The official name of the conference, excluding numbers commonly provided in
    conference.
    """
    class Meta:
        name = "conference_name"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "min_length": 3,
            "max_length": 512,
        }
    )
