from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.create_terminal_session_req import (
    CreateTerminalSessionReq,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class CreateTerminalSessionServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: CreateTerminalSessionServicePortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        create_terminal_session_req: CreateTerminalSessionReq = field(
            metadata={
                "name": "CreateTerminalSessionReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/terminal_v33_0",
            }
        )
