from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.profile_modify_bridge_branches_req import ProfileModifyBridgeBranchesReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class ProfileModifyBridgeBranchesPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | ProfileModifyBridgeBranchesPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        profile_modify_bridge_branches_req: None | ProfileModifyBridgeBranchesReq = field(
            default=None,
            metadata={
                "name": "ProfileModifyBridgeBranchesReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            }
        )
