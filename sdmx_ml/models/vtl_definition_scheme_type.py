from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.item_scheme_type import ItemSchemeType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class VtlDefinitionSchemeType(ItemSchemeType):
    """
    VtlDefinitionSchemeType is an abstract extension of the ItemSchemeType
    for VTL schemes.

    :ivar vtl_version: Identifies the VTL version to which the items in
        the defined scheme comply. Note that definition schemes can only
        reference definition schemes using the same VTL version.
    """

    vtl_version: str | None = field(
        default=None,
        metadata={
            "name": "vtlVersion",
            "type": "Attribute",
            "required": True,
        },
    )
