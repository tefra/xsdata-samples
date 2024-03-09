from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.uimeta_data_modify_req import UimetaDataModifyReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class UimetaDataModifyPortTypeServiceInput:
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
    body: None | UimetaDataModifyPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        uimeta_data_modify_req: None | UimetaDataModifyReq = field(
            default=None,
            metadata={
                "name": "UIMetaDataModifyReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
            },
        )
