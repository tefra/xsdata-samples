from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.uimeta_data_delete_req import UimetaDataDeleteReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class UimetaDataDeletePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: None | object = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
        },
    )
    body: UimetaDataDeletePortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        uimeta_data_delete_req: UimetaDataDeleteReq = field(
            metadata={
                "name": "UIMetaDataDeleteReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
            }
        )
