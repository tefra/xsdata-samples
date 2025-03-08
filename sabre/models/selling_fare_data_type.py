from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.handling_markup_summary_type import HandlingMarkupSummaryType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class SellingFareDataType:
    handling_markup_summary: list[HandlingMarkupSummaryType] = field(
        default_factory=list,
        metadata={
            "name": "HandlingMarkupSummary",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    layer_type_name: None | str = field(
        default=None,
        metadata={
            "name": "LayerTypeName",
            "type": "Attribute",
            "required": True,
        },
    )
