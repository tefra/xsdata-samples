from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.error_info_1 import ErrorInfo1
from travelport.models.hotel_media_links_rsp import HotelMediaLinksRsp

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class HotelMediaLinksServicePortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: HotelMediaLinksServicePortTypeServiceOutput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        hotel_media_links_rsp: None | HotelMediaLinksRsp = field(
            default=None,
            metadata={
                "name": "HotelMediaLinksRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            },
        )
        fault: (
            None | HotelMediaLinksServicePortTypeServiceOutput.Body.Fault
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
                | HotelMediaLinksServicePortTypeServiceOutput.Body.Fault.Detail
            ) = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )

            @dataclass(kw_only=True)
            class Detail:
                error_info: None | ErrorInfo1 = field(
                    default=None,
                    metadata={
                        "name": "ErrorInfo",
                        "type": "Element",
                        "namespace": "http://www.travelport.com/schema/common_v52_0",
                    },
                )
