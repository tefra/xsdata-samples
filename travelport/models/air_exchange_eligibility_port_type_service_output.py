from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_exchange_eligibility_rsp import (
    AirExchangeEligibilityRsp,
)
from travelport.models.error_info_1 import ErrorInfo1

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class AirExchangeEligibilityPortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | AirExchangeEligibilityPortTypeServiceOutput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        air_exchange_eligibility_rsp: None | AirExchangeEligibilityRsp = field(
            default=None,
            metadata={
                "name": "AirExchangeEligibilityRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v52_0",
            },
        )
        fault: (
            None | AirExchangeEligibilityPortTypeServiceOutput.Body.Fault
        ) = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            },
        )

        @dataclass
        class Fault:
            faultcode: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultstring: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultactor: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            detail: (
                None
                | AirExchangeEligibilityPortTypeServiceOutput.Body.Fault.Detail
            ) = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )

            @dataclass
            class Detail:
                error_info: None | ErrorInfo1 = field(
                    default=None,
                    metadata={
                        "name": "ErrorInfo",
                        "type": "Element",
                        "namespace": "http://www.travelport.com/schema/common_v52_0",
                    },
                )
