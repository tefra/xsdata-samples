from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.error_info_4 import ErrorInfo4
from travelport.models.terminal_rsp import TerminalRsp

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class TerminalServicePortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | TerminalServicePortTypeServiceOutput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        terminal_rsp: None | TerminalRsp = field(
            default=None,
            metadata={
                "name": "TerminalRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/terminal_v33_0",
            },
        )
        fault: None | TerminalServicePortTypeServiceOutput.Body.Fault = field(
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
                None | TerminalServicePortTypeServiceOutput.Body.Fault.Detail
            ) = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )

            @dataclass
            class Detail:
                error_info: None | ErrorInfo4 = field(
                    default=None,
                    metadata={
                        "name": "ErrorInfo",
                        "type": "Element",
                        "namespace": "http://www.travelport.com/schema/common_v33_0",
                    },
                )
