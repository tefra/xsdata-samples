from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.currency_conversion_req import CurrencyConversionReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class UtilCurrencyConversionPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: UtilCurrencyConversionPortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        currency_conversion_req: CurrencyConversionReq = field(
            metadata={
                "name": "CurrencyConversionReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/util_v52_0",
            }
        )
