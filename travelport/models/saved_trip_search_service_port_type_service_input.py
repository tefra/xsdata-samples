from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.saved_trip_search_req import SavedTripSearchReq
from travelport.models.supported_versions import SupportedVersions

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class SavedTripSearchServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: None | SavedTripSearchServicePortTypeServiceInput.Header = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
        },
    )
    body: None | SavedTripSearchServicePortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Header:
        supported_versions: None | SupportedVersions = field(
            default=None,
            metadata={
                "name": "SupportedVersions",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/universal_v52_0",
            },
        )

    @dataclass
    class Body:
        saved_trip_search_req: None | SavedTripSearchReq = field(
            default=None,
            metadata={
                "name": "SavedTripSearchReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/universal_v52_0",
            },
        )
