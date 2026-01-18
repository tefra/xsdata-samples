from dataclasses import dataclass, field

from crossref.models.org.crossref.schema.pkg_5.pkg_3.domain import Domain
from crossref.models.org.crossref.schema.pkg_5.pkg_3.filter import Filter

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class CrossmarkDomain:
    """
    This should be a simple Internet domain name or subdomain name (e.g.
    www.psychoceramics.org or psychoceramics.org).

    It is used to identify when a referring URL is coming from a Crossmark
    domain. A "crossmark_domain" is made up of two subelements; a "domain"
    and a "filter". The filter is only needed for use in situations where
    content from multiple publishers/publications is on the same host with
    the same domain name (e.g. an aggregator) and one needs to use the
    referrer's URI "path" to further determine whether the content in a
    crossmark domain.
    """

    class Meta:
        name = "crossmark_domain"
        namespace = "http://www.crossref.org/schema/5.3.1"

    domain: Domain | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    filter: Filter | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
