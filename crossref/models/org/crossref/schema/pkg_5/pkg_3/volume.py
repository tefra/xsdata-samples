from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Volume:
    """
    The volume number of a published journal, or the number of a printed
    volume for a book or conference proceedings.
    """

    class Meta:
        name = "volume"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "min_length": 1,
            "max_length": 32,
        },
    )
