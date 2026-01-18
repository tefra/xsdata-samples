from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.saved_trip_retrieve_req import SavedTripRetrieveReq
from travelport.models.supported_versions import SupportedVersions

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class SavedTripRetrieveServicePortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: SavedTripRetrieveServicePortTypeServiceInput.Header = field(
        metadata={
            "name": "Header",
            "type": "Element",
        }
    )
    body: SavedTripRetrieveServicePortTypeServiceInput.Body = field(
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
        saved_trip_retrieve_req: SavedTripRetrieveReq = field(
            metadata={
                "name": "SavedTripRetrieveReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/universal_v52_0",
            }
        )
