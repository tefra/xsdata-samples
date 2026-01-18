from __future__ import annotations

from dataclasses import dataclass

from sdmx_ml.models.link_type import LinkType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common"


@dataclass(frozen=True, kw_only=True)
class Link(LinkType):
    """
    Allows for the linking of other resources to identifiable objects.

    For example, if there is reference metadata associated with a
    structure, a link to the meatadata report can be dynamically inserted
    in the structure metadata.
    """

    class Meta:
        namespace = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common"
