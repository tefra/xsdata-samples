from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.etr import Etr
from travelport.models.mco_1 import Mco1
from travelport.models.service_fee_info_1 import ServiceFeeInfo1
from travelport.models.tcr import Tcr
from travelport.models.type_failure_info import TypeFailureInfo

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirRetrieveDocumentRsp(BaseRsp1):
    """
    Parameters
    ----------
    etr
        Provider: 1G,1V,1P.
    mco
        Provider: 1G,1V,1P.
    tcr
        Provider: 1G,1V,1P.
    document_failure_info
        Provider: 1G,1V,1P-Will be optionally returned if there are
        duplicate ticket numbers.
    service_fee_info
        Provider: 1G,1V
    universal_record_locator_code
        Provider: 1G,1V,1P-Represents a valid Universal Record locator code.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    etr: list[Etr] = field(
        default_factory=list,
        metadata={
            "name": "ETR",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    mco: list[Mco1] = field(
        default_factory=list,
        metadata={
            "name": "MCO",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    tcr: list[Tcr] = field(
        default_factory=list,
        metadata={
            "name": "TCR",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    document_failure_info: list[TypeFailureInfo] = field(
        default_factory=list,
        metadata={
            "name": "DocumentFailureInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    service_fee_info: list[ServiceFeeInfo1] = field(
        default_factory=list,
        metadata={
            "name": "ServiceFeeInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
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
