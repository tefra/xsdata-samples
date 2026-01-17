from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class CrossmarkPolicy:
    """
    A DOI which points to a publisher's CrossMark policy document.

    Publishers might have different policies for different publications.
    """

    class Meta:
        name = "crossmark_policy"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 6,
            "max_length": 2048,
            "pattern": r"10\.[0-9]{4,9}/.{1,200}",
        },
    )
