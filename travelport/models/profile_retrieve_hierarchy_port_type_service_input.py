from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.profile_retrieve_hierarchy_req import ProfileRetrieveHierarchyReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class ProfileRetrieveHierarchyPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | ProfileRetrieveHierarchyPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        profile_retrieve_hierarchy_req: None | ProfileRetrieveHierarchyReq = field(
            default=None,
            metadata={
                "name": "ProfileRetrieveHierarchyReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            }
        )
