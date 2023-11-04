from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class FullTitle:
    """
    The full title by which a journal is commonly known or cited.
    """
    class Meta:
        name = "full_title"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "min_length": 1,
            "max_length": 255,
        }
    )
