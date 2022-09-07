from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class CrossmarkDomain:
    """This should be a simple Internet domain name or subdomain name (e.g.
    www.psychoceramics.org or psychoceramics.org).

    It is used to identify when a referring URL is coming from a
    Crossmark domain. A "crossmark_domain" is made up of two
    subelements; a "domain" and a "filter". The filter is only needed
    for use in situations where content from multiple
    publishers/publications is on the same host with the same domain
    name (e.g. an aggregator) and one needs to use the referrer's URI
    "path" to further determine whether the content in a crossmark
    domain.
    """
    class Meta:
        name = "crossmark_domain"
        namespace = "http://www.crossref.org/schema/5.3.1"

    domain: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 4,
            "max_length": 1024,
            "pattern": r"[A-Za-z0-9_]+([-.][A-Za-z0-9_]+)*\.[A-Za-z0-9_]+([-.][A-Za-z0-9_]+)*",
        }
    )
    filter: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
