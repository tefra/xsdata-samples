from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.error_info_1 import ErrorInfo1
from travelport.models.price_match_error import PriceMatchError
from travelport.models.vehicle_create_reservation_rsp import (
    VehicleCreateReservationRsp,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class VehicleReservationServicePortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | VehicleReservationServicePortTypeServiceOutput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        vehicle_create_reservation_rsp: None | VehicleCreateReservationRsp = (
            field(
                default=None,
                metadata={
                    "name": "VehicleCreateReservationRsp",
                    "type": "Element",
                    "namespace": "http://www.travelport.com/schema/universal_v52_0",
                },
            )
        )
        fault: (
            None | VehicleReservationServicePortTypeServiceOutput.Body.Fault
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
                | VehicleReservationServicePortTypeServiceOutput.Body.Fault.Detail
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
                price_match_error: None | PriceMatchError = field(
                    default=None,
                    metadata={
                        "name": "PriceMatchError",
                        "type": "Element",
                        "namespace": "http://www.travelport.com/schema/common_v52_0",
                    },
                )
