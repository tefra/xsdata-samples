from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.saved_trip_delete_req import SavedTripDeleteReq
from travelport.models.supported_versions import SupportedVersions

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class SavedTripDeleteServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: SavedTripDeleteServicePortTypeServiceInput.Header = field(
        metadata={
            "name": "Header",
            "type": "Element",
        }
    )
    body: SavedTripDeleteServicePortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Header:
        supported_versions: SupportedVersions = field(
            metadata={
                "name": "SupportedVersions",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/universal_v52_0",
            }
        )

    @dataclass(kw_only=True)
    class Body:
        saved_trip_delete_req: SavedTripDeleteReq = field(
            metadata={
                "name": "SavedTripDeleteReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/universal_v52_0",
            }
        )
