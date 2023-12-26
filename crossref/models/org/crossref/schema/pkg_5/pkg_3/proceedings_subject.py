from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class ProceedingsSubject:
    """
    The subject of the conference proceeding, e.g. "Computer Graphics" is the
    subject matter of SIGGRAPH.
    """

    class Meta:
        name = "proceedings_subject"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "min_length": 1,
            "max_length": 255,
        },
    )
