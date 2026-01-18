from __future__ import annotations

from dataclasses import dataclass

from sdmx_ml.models.item_type import GeoRefCodeType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True, kw_only=True)
class GeoRefCode(GeoRefCodeType):
    """
    GeoRefCode is the abstract base from which specific types of geographic
    codes will be derived.
    """

    class Meta:
        namespace = (
            "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"
        )
