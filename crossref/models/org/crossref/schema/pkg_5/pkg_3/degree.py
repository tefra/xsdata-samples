from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Degree:
    """
    The degree(s) awarded for a dissertation.
    """

    class Meta:
        name = "degree"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "min_length": 2,
            "max_length": 255,
        },
    )
