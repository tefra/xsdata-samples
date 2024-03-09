from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.error_info_1 import ErrorInfo1
from travelport.models.universal_record_cancel_rsp import (
    UniversalRecordCancelRsp,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class UniversalRecordCancelServicePortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | UniversalRecordCancelServicePortTypeServiceOutput.Body = (
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
        universal_record_cancel_rsp: None | UniversalRecordCancelRsp = field(
            default=None,
            metadata={
                "name": "UniversalRecordCancelRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/universal_v52_0",
            },
        )
        fault: (
            None | UniversalRecordCancelServicePortTypeServiceOutput.Body.Fault
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
                | UniversalRecordCancelServicePortTypeServiceOutput.Body.Fault.Detail
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
