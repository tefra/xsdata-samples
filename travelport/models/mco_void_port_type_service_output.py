from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.error_info_1 import ErrorInfo1
from travelport.models.mco_void_rsp import McoVoidRsp

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class McoVoidPortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | McoVoidPortTypeServiceOutput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        mco_void_rsp: None | McoVoidRsp = field(
            default=None,
            metadata={
                "name": "McoVoidRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/util_v52_0",
            },
        )
        fault: None | McoVoidPortTypeServiceOutput.Body.Fault = field(
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
            detail: None | McoVoidPortTypeServiceOutput.Body.Fault.Detail = (
                field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "",
                    },
                )
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
