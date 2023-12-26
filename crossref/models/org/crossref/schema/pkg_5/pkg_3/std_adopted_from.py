from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class StdAdoptedFrom:
    """
    Designator for standard from which the current deposit is adopted.
    """

    class Meta:
        name = "std_adopted_from"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 2,
            "max_length": 150,
        },
    )
