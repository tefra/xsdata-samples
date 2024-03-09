from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.supported_versions import SupportedVersions
from travelport.models.universal_record_import_req import (
    UniversalRecordImportReq,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class UniversalRecordImportServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: None | UniversalRecordImportServicePortTypeServiceInput.Header = (
        field(
            default=None,
            metadata={
                "name": "Header",
                "type": "Element",
            },
        )
    )
    body: None | UniversalRecordImportServicePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Header:
        supported_versions: None | SupportedVersions = field(
            default=None,
            metadata={
                "name": "SupportedVersions",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/universal_v52_0",
            },
        )

    @dataclass
    class Body:
        universal_record_import_req: None | UniversalRecordImportReq = field(
            default=None,
            metadata={
                "name": "UniversalRecordImportReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/universal_v52_0",
            },
        )
