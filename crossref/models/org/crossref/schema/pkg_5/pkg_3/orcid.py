from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Orcid:
    """
    The ORCID iD for an author.
    """
    class Meta:
        name = "ORCID"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"https?://orcid.org/[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[X0-9]{1}",
        }
    )
    authenticated: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
