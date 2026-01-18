from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.org.crossref.schema.pkg_5.pkg_3.collection_multi_resolution import (
    CollectionMultiResolution,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.collection_property import (
    CollectionProperty,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.item import Item

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass(kw_only=True)
class Collection:
    """
    Container for item elements containing non-primary URIs associated with
    the item being registered.

    Collections are supported for the following (defined in the property
    attribute): <ul xmlns=""> <li>list-based: Multiple Resolution, more
    info:
    https://www.crossref.org/education/content-registration/creating-and-managing-dois/multiple-resolution/</li>
    <li>country-based: more info:
    https://www.crossref.org/education/content-registration/creating-and-managing-dois/multiple-resolution/#00130</li>
    <li>crawler-based: for Similarity Check URLs, more info:
    https://www.crossref.org/education/similarity-check/participate/urls-for-new-deposits/</li>
    <li>text-mining: supply specific URLs for text and data mining, more
    info:
    https://www.crossref.org/education/retrieve-metadata/rest-api/text-and-data-mining-for-members/</li>
    <li>unspecified: can be used for additional URLs</li> <li>syndication:
    identifies resources to be used for syndication</li> <li>link-header:
    identifies resources to be used as an endpoint</li> </ul>.
    """

    class Meta:
        name = "collection"
        namespace = "http://www.crossref.org/schema/5.3.1"

    item: list[Item] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    property: CollectionProperty = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    multi_resolution: None | CollectionMultiResolution = field(
        default=None,
        metadata={
            "name": "multi-resolution",
            "type": "Attribute",
        },
    )
