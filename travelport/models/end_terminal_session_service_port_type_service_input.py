from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.end_terminal_session_req import EndTerminalSessionReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class EndTerminalSessionServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: EndTerminalSessionServicePortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        end_terminal_session_req: EndTerminalSessionReq = field(
            metadata={
                "name": "EndTerminalSessionReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/terminal_v33_0",
            }
        )
