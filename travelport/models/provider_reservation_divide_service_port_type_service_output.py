from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.error_info_1 import ErrorInfo1
from travelport.models.provider_reservation_divide_rsp import (
    ProviderReservationDivideRsp,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class ProviderReservationDivideServicePortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | ProviderReservationDivideServicePortTypeServiceOutput.Body = (
        field(
            default=None,
            metadata={
                "name": "Body",
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body:
        provider_reservation_divide_rsp: (
            None | ProviderReservationDivideRsp
        ) = field(
            default=None,
            metadata={
                "name": "ProviderReservationDivideRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/universal_v52_0",
            },
        )
        fault: (
            None
            | ProviderReservationDivideServicePortTypeServiceOutput.Body.Fault
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
                | ProviderReservationDivideServicePortTypeServiceOutput.Body.Fault.Detail
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
