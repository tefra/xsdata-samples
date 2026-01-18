from dataclasses import dataclass, field
from typing import Optional

from crossref.models.org.crossref.schema.pkg_5.pkg_3.component_list import (
    ComponentList,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.content_item import (
    ContentItem,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.standard_metadata import (
    StandardMetadata,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.standard_publication_type import (
    StandardPublicationType,
)

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Standard:
    """
    standard is the top level element for deposit of metadata about
    standards developed by Standards Development Organizations (SDOs) or
    Consortia.
    """

    class Meta:
        name = "standard"
        namespace = "http://www.crossref.org/schema/5.3.1"

    standard_metadata: StandardMetadata | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    content_item: list[ContentItem] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    component_list: ComponentList | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    publication_type: StandardPublicationType = field(
        default=StandardPublicationType.FULL_TEXT,
        metadata={
            "type": "Attribute",
        },
    )
