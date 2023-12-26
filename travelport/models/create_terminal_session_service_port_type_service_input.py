from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.create_terminal_session_req import (
    CreateTerminalSessionReq,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class CreateTerminalSessionServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | CreateTerminalSessionServicePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        create_terminal_session_req: None | CreateTerminalSessionReq = field(
            default=None,
            metadata={
                "name": "CreateTerminalSessionReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/terminal_v33_0",
            },
        )
