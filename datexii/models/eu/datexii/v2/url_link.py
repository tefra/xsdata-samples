from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString
from datexii.models.eu.datexii.v2.url_link_type_enum import UrlLinkTypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class UrlLink:
    """
    Details of a Uniform Resource Locator (URL) address pointing to a
    resource available on the Internet from where further relevant
    information may be obtained.

    :ivar url_link_address: A Uniform Resource Locator (URL) address
        pointing to a resource available on the Internet from where
        further relevant information may be obtained.
    :ivar url_link_description: Description of the relevant information
        available on the Internet from the URL link.
    :ivar url_link_type: Details of the type of relevant information
        available on the Internet from the URL link.
    :ivar url_link_extension:
    """

    url_link_address: str | None = field(
        default=None,
        metadata={
            "name": "urlLinkAddress",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    url_link_description: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "urlLinkDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    url_link_type: UrlLinkTypeEnum | None = field(
        default=None,
        metadata={
            "name": "urlLinkType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    url_link_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "urlLinkExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
