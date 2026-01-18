from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.uimeta_data_retrieve_req import UimetaDataRetrieveReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class UimetaDataRetrievePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: object = field(
        metadata={
            "name": "Header",
            "type": "Element",
        }
    )
    body: UimetaDataRetrievePortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        uimeta_data_retrieve_req: UimetaDataRetrieveReq = field(
            metadata={
                "name": "UIMetaDataRetrieveReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
            }
        )
