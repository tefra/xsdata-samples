from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.supported_versions import SupportedVersions
from travelport.models.universal_record_history_search_req import UniversalRecordHistorySearchReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class UniversalRecordHistorySearchPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: None | UniversalRecordHistorySearchPortTypeServiceInput.Header = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
        }
    )
    body: None | UniversalRecordHistorySearchPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Header:
        supported_versions: None | SupportedVersions = field(
            default=None,
            metadata={
                "name": "SupportedVersions",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/universal_v52_0",
            }
        )

    @dataclass
    class Body:
        universal_record_history_search_req: None | UniversalRecordHistorySearchReq = field(
            default=None,
            metadata={
                "name": "UniversalRecordHistorySearchReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/universal_v52_0",
            }
        )
