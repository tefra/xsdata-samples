from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Domain:
    """A domain name or subdomain name (e.g. www.psychoceramics.org or
    psychoceramics.org).

    It is used to identify when a referring URL is coming from a
    Crossmark domain.
    """
    class Meta:
        name = "domain"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 4,
            "max_length": 1024,
            "pattern": r"[A-Za-z0-9_]+([-.][A-Za-z0-9_]+)*\.[A-Za-z0-9_]+([-.][A-Za-z0-9_]+)*",
        }
    )
