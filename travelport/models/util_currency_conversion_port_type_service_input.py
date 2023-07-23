from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.currency_conversion_req import CurrencyConversionReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class UtilCurrencyConversionPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | UtilCurrencyConversionPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        currency_conversion_req: None | CurrencyConversionReq = field(
            default=None,
            metadata={
                "name": "CurrencyConversionReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/util_v52_0",
            }
        )
