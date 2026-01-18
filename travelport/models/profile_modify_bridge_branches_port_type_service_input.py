from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.profile_modify_bridge_branches_req import (
    ProfileModifyBridgeBranchesReq,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class ProfileModifyBridgeBranchesPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: ProfileModifyBridgeBranchesPortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        profile_modify_bridge_branches_req: ProfileModifyBridgeBranchesReq = field(
            metadata={
                "name": "ProfileModifyBridgeBranchesReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            }
        )
