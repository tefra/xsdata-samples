from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_1 import BaseReq1
from travelport.models.service_fee_info_1 import ServiceFeeInfo1

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class AgencyServiceFeeCreateReq(BaseReq1):
    """
    Creates an Agency Service Fee to be charged through BSP or Airline Reporting
    Corporation (ARC)..

    Parameters
    ----------
    service_fee_info
    universal_record_locator_code
        Service Fee to be applied to the UniversalRecord.
    provider_locator_code
        Service Fees to be applied to the provider locator code of the PNR .
    provider_code
        To be used with ProviderLocatorCode, which host the reservation
        being added to belongs to.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    service_fee_info: list[ServiceFeeInfo1] = field(
        default_factory=list,
        metadata={
            "name": "ServiceFeeInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    universal_record_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "UniversalRecordLocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        },
    )
    provider_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        },
    )
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
        },
    )
