from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Surname:
    """
    The family_name of a contributor.
    """
    class Meta:
        name = "surname"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "min_length": 1,
            "max_length": 60,
            "white_space": "collapse",
            "pattern": r"[^\d\?]*[^\?\s]+[^\d]*",
        }
    )
