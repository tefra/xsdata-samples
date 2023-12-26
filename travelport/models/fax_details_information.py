from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_pricing_info_ref import AirPricingInfoRef
from travelport.models.fax_details import FaxDetails

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class FaxDetailsInformation:
    """
    Container to send Fax details Information for ticketing.

    Parameters
    ----------
    air_pricing_info_ref
        Returns related air pricing infos.
    fax_details
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_pricing_info_ref: list[AirPricingInfoRef] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingInfoRef",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    fax_details: None | FaxDetails = field(
        default=None,
        metadata={
            "name": "FaxDetails",
            "type": "Element",
            "required": True,
        },
    )
