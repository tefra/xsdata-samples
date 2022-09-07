from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class StdSupersedes:
    """
    Designator for standard being replaced by the standard being deposited.
    """
    class Meta:
        name = "std_supersedes"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 2,
            "max_length": 150,
        }
    )
