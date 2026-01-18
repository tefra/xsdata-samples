from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.brand_type import BrandType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class InterlineBrandsType:
    """
    Attributes:
        brand: Brand list to be returned
        change_brand_for_soldout: If specific XX brand is not available
            for requested date/flight, another cheapest brand will be
            returned combined with available XX brand.
    """

    brand: list[BrandType] = field(
        default_factory=list,
        metadata={
            "name": "Brand",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    change_brand_for_soldout: bool = field(
        default=False,
        metadata={
            "name": "ChangeBrandForSoldout",
            "type": "Attribute",
        },
    )
