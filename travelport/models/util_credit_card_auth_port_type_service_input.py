from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.credit_card_auth_req import CreditCardAuthReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class UtilCreditCardAuthPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | UtilCreditCardAuthPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        credit_card_auth_req: None | CreditCardAuthReq = field(
            default=None,
            metadata={
                "name": "CreditCardAuthReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/util_v52_0",
            }
        )
