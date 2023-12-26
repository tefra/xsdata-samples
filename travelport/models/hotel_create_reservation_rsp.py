from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.hotel_property import HotelProperty
from travelport.models.hotel_rate_detail import HotelRateDetail
from travelport.models.universal_record import UniversalRecord

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class HotelCreateReservationRsp(BaseRsp1):
    """
    Parameters
    ----------
    universal_record
    hotel_rate_changed_info
        Applicable for 1G, 1V, 1P
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    universal_record: None | UniversalRecord = field(
        default=None,
        metadata={
            "name": "UniversalRecord",
            "type": "Element",
        },
    )
    hotel_rate_changed_info: None | HotelCreateReservationRsp.HotelRateChangedInfo = field(
        default=None,
        metadata={
            "name": "HotelRateChangedInfo",
            "type": "Element",
        },
    )

    @dataclass
    class HotelRateChangedInfo:
        """
        Parameters
        ----------
        hotel_property
        hotel_rate_detail
        reason
            Reason to represent whether rate change in hotel
            rules.Applicable for 1G, 1V, 1P
        """

        hotel_property: None | HotelProperty = field(
            default=None,
            metadata={
                "name": "HotelProperty",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/hotel_v52_0",
                "required": True,
            },
        )
        hotel_rate_detail: None | HotelRateDetail = field(
            default=None,
            metadata={
                "name": "HotelRateDetail",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            },
        )
        reason: None | str = field(
            default=None,
            metadata={
                "name": "Reason",
                "type": "Attribute",
            },
        )
