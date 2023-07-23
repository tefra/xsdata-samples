from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.terminal_req import TerminalReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class TerminalServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | TerminalServicePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        terminal_req: None | TerminalReq = field(
            default=None,
            metadata={
                "name": "TerminalReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/terminal_v33_0",
            }
        )
