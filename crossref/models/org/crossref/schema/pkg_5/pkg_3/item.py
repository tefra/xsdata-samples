from dataclasses import dataclass, field
from typing import Optional

from crossref.models.org.crossref.schema.pkg_5.pkg_3.doi import Doi
from crossref.models.org.crossref.schema.pkg_5.pkg_3.item_country import (
    ItemCountry,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.item_crawler import (
    ItemCrawler,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.item_link_header_relationship import (
    ItemLinkHeaderRelationship,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.resource import Resource

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Item:
    """
    A container used to associate a URI with the DOI being registered.
    """

    class Meta:
        name = "item"
        namespace = "http://www.crossref.org/schema/5.3.1"

    doi: Optional[Doi] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    resource: Optional[Resource] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    crawler: Optional[ItemCrawler] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    label: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_length": 3,
            "max_length": 128,
        },
    )
    country: Optional[ItemCountry] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    link_header_relationship: Optional[ItemLinkHeaderRelationship] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
