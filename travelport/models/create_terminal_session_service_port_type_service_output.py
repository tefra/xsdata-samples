from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.create_terminal_session_rsp import (
    CreateTerminalSessionRsp,
)
from travelport.models.error_info_4 import ErrorInfo4

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class CreateTerminalSessionServicePortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: CreateTerminalSessionServicePortTypeServiceOutput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        create_terminal_session_rsp: None | CreateTerminalSessionRsp = field(
            default=None,
            metadata={
                "name": "CreateTerminalSessionRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/terminal_v33_0",
            },
        )
        fault: (
            None | CreateTerminalSessionServicePortTypeServiceOutput.Body.Fault
        ) = field(
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
            detail: (
                None
                | CreateTerminalSessionServicePortTypeServiceOutput.Body.Fault.Detail
            ) = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )

            @dataclass(kw_only=True)
            class Detail:
                error_info: None | ErrorInfo4 = field(
                    default=None,
                    metadata={
                        "name": "ErrorInfo",
                        "type": "Element",
                        "namespace": "http://www.travelport.com/schema/common_v33_0",
                    },
                )
