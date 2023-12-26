from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_1 import BaseReq1
from travelport.models.file_finishing_info_1 import FileFinishingInfo1

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class UniversalRecordImportReq(BaseReq1):
    """
    Imports a external reservation into a G2 Universal Record.

    Parameters
    ----------
    file_finishing_info
    provider_code
    provider_locator_code
    universal_record_locator_code
        Required if to be imported in existing UniversalRecord.
    return_unmasked_data
        When set as True in the request and AAT settings are set to display
        Unmasked details in the host, then details will be shown in the
        response. Only supports credit card and debit card. Default value of
        ReturnUnmaskedData is false.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    file_finishing_info: None | FileFinishingInfo1 = field(
        default=None,
        metadata={
            "name": "FileFinishingInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        },
    )
    provider_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "required": True,
            "max_length": 15,
        },
    )
    universal_record_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "UniversalRecordLocatorCode",
            "type": "Attribute",
            "min_length": 5,
            "max_length": 8,
        },
    )
    return_unmasked_data: None | bool = field(
        default=None,
        metadata={
            "name": "ReturnUnmaskedData",
            "type": "Attribute",
        },
    )
