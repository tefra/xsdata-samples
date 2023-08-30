from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Suffix:
    """
    The suffix of an author name, e.g. junior, senior, III.
    """
    class Meta:
        name = "suffix"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "min_length": 1,
            "max_length": 10,
        }
    )
