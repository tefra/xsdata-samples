from dataclasses import dataclass, field
from typing import List
from crossref.models.org.crossref.schema.pkg_5.pkg_3.crossmark_domain import (
    CrossmarkDomain,
)

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class CrossmarkDomains:
    """Container element for crossmark_domain.

    A list of domains where the publisher maintains updates and
    corrections to their content. Minimally, one of these should include
    the Internet domain name of the publisher's web site(s), but the
    publisher might also decide to include 3rd party aggregators (e.g.
    Ebsco, IngentaConnect) or archives with which the publisher has
    agreements to update the content
    """

    class Meta:
        name = "crossmark_domains"
        namespace = "http://www.crossref.org/schema/5.3.1"

    crossmark_domain: List[CrossmarkDomain] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
