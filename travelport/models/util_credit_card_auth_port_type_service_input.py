from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.credit_card_auth_req import CreditCardAuthReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class UtilCreditCardAuthPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: UtilCreditCardAuthPortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        credit_card_auth_req: CreditCardAuthReq = field(
            metadata={
                "name": "CreditCardAuthReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/util_v52_0",
            }
        )
