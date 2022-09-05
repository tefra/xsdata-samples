from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.order_request import ListOfPackageDetail
from xcbl.models.shipping_schedule_response import (
    LocationGroupedShippingDetail,
    MaterialGroupedShippingDetail,
    ShippingScheduleHeader,
    ShippingScheduleSummary,
)


@dataclass(kw_only=True)
class ListOfLocationGroupedShippingDetail:
    location_grouped_shipping_detail: List[LocationGroupedShippingDetail] = field(
        default_factory=list,
        metadata={
            "name": "LocationGroupedShippingDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfMaterialGroupedShippingDetail:
    material_grouped_shipping_detail: List[MaterialGroupedShippingDetail] = field(
        default_factory=list,
        metadata={
            "name": "MaterialGroupedShippingDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ShippingSchedule:
    shipping_schedule_header: ShippingScheduleHeader = field(
        metadata={
            "name": "ShippingScheduleHeader",
            "type": "Element",
            "required": True,
        }
    )
    list_of_location_grouped_shipping_detail: Optional[ListOfLocationGroupedShippingDetail] = field(
        default=None,
        metadata={
            "name": "ListOfLocationGroupedShippingDetail",
            "type": "Element",
        }
    )
    list_of_material_grouped_shipping_detail: Optional[ListOfMaterialGroupedShippingDetail] = field(
        default=None,
        metadata={
            "name": "ListOfMaterialGroupedShippingDetail",
            "type": "Element",
        }
    )
    list_of_package_detail: Optional[ListOfPackageDetail] = field(
        default=None,
        metadata={
            "name": "ListOfPackageDetail",
            "type": "Element",
        }
    )
    shipping_schedule_summary: Optional[ShippingScheduleSummary] = field(
        default=None,
        metadata={
            "name": "ShippingScheduleSummary",
            "type": "Element",
        }
    )
