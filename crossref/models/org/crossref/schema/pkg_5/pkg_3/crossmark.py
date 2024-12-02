from dataclasses import dataclass, field
from typing import Optional

from crossref.models.org.crossref.schema.pkg_5.pkg_3.crossmark_domain_exclusive import (
    CrossmarkDomainExclusive,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.crossmark_domains import (
    CrossmarkDomains,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.crossmark_policy import (
    CrossmarkPolicy,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.crossmark_version import (
    CrossmarkVersion,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.custom_metadata import (
    CustomMetadata,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.updates import Updates

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Crossmark:
    """
    Container element for CrossMark data.

    :ivar crossmark_version:
    :ivar crossmark_policy:
    :ivar crossmark_domains:
    :ivar crossmark_domain_exclusive: Some publishers encourage broad
        third party hosting of the publisher's content. Other publishers
        do not. And still others vary their policy depending on whether
        a particular article has been published under an OA policy or
        not. This boolean flag allows the publisher to indicate whether
        the Crossmarked content will only legitimately be updated on the
        Crossmark domain (true) or whether the publisher encourages
        updating the content on other sites as well (false).
    :ivar updates:
    :ivar custom_metadata:
    """

    class Meta:
        name = "crossmark"
        namespace = "http://www.crossref.org/schema/5.3.1"

    crossmark_version: Optional[CrossmarkVersion] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    crossmark_policy: Optional[CrossmarkPolicy] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    crossmark_domains: list[CrossmarkDomains] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    crossmark_domain_exclusive: Optional[CrossmarkDomainExclusive] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    updates: Optional[Updates] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    custom_metadata: Optional[CustomMetadata] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
