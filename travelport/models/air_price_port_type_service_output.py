from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_price_rsp import AirPriceRsp
from travelport.models.error_info_1 import ErrorInfo1

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class AirPricePortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: AirPricePortTypeServiceOutput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        air_price_rsp: None | AirPriceRsp = field(
            default=None,
            metadata={
                "name": "AirPriceRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v52_0",
            },
        )
        fault: None | AirPricePortTypeServiceOutput.Body.Fault = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            },
        )

        @dataclass(kw_only=True)
        class Fault:
            faultcode: str = field(
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: str = field(
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            detail: None | AirPricePortTypeServiceOutput.Body.Fault.Detail = (
                field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                    },
                )
            )

            @dataclass(kw_only=True)
            class Detail:
                error_info: None | ErrorInfo1 = field(
                    default=None,
                    metadata={
                        "name": "ErrorInfo",
                        "type": "Element",
                        "namespace": "http://www.travelport.com/schema/common_v52_0",
                    },
                )
