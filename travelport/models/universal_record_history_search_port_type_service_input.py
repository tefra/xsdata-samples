from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.supported_versions import SupportedVersions
from travelport.models.universal_record_history_search_req import (
    UniversalRecordHistorySearchReq,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class UniversalRecordHistorySearchPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: UniversalRecordHistorySearchPortTypeServiceInput.Header = field(
        metadata={
            "name": "Header",
            "type": "Element",
        }
    )
    body: UniversalRecordHistorySearchPortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Header:
        supported_versions: SupportedVersions = field(
            metadata={
                "name": "SupportedVersions",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/universal_v52_0",
            }
        )

    @dataclass(kw_only=True)
    class Body:
        universal_record_history_search_req: UniversalRecordHistorySearchReq = field(
            metadata={
                "name": "UniversalRecordHistorySearchReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/universal_v52_0",
            }
        )
