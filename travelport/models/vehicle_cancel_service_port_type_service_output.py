from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.error_info_1 import ErrorInfo1
from travelport.models.vehicle_cancel_rsp import VehicleCancelRsp

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class VehicleCancelServicePortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | VehicleCancelServicePortTypeServiceOutput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        vehicle_cancel_rsp: None | VehicleCancelRsp = field(
            default=None,
            metadata={
                "name": "VehicleCancelRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/universal_v52_0",
            },
        )
        fault: None | VehicleCancelServicePortTypeServiceOutput.Body.Fault = (
            field(
                default=None,
                metadata={
                    "name": "Fault",
                    "type": "Element",
                },
            )
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
                | VehicleCancelServicePortTypeServiceOutput.Body.Fault.Detail
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
