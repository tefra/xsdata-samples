from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.booking_seat_assignment_rsp import (
    BookingSeatAssignmentRsp,
)
from travelport.models.error_info_1 import ErrorInfo1

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class BookingSeatAssignmentPortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | BookingSeatAssignmentPortTypeServiceOutput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        booking_seat_assignment_rsp: None | BookingSeatAssignmentRsp = field(
            default=None,
            metadata={
                "name": "BookingSeatAssignmentRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/sharedBooking_v52_0",
            },
        )
        fault: None | BookingSeatAssignmentPortTypeServiceOutput.Body.Fault = (
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
                | BookingSeatAssignmentPortTypeServiceOutput.Body.Fault.Detail
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
