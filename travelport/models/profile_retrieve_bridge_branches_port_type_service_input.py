from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.profile_retrieve_bridge_branches_req import (
    ProfileRetrieveBridgeBranchesReq,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class ProfileRetrieveBridgeBranchesPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: ProfileRetrieveBridgeBranchesPortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        profile_retrieve_bridge_branches_req: ProfileRetrieveBridgeBranchesReq = field(
            metadata={
                "name": "ProfileRetrieveBridgeBranchesReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            }
        )
