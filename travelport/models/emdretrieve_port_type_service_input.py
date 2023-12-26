from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.emdretrieve_req import EmdretrieveReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class EmdretrievePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | EmdretrievePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        emdretrieve_req: None | EmdretrieveReq = field(
            default=None,
            metadata={
                "name": "EMDRetrieveReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v52_0",
            },
        )
