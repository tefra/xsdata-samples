from __future__ import annotations

from dataclasses import dataclass

from sdmx_ml.models.xhtmltype import Xhtmltype

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/common"


@dataclass(frozen=True, kw_only=True)
class StructuredText(Xhtmltype):
    """
    StructuredText is a reusable element, used for providing a language
    specific text value structured as XHTML.
    """

    class Meta:
        namespace = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/common"
