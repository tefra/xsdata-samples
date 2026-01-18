from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.error_info_1 import ErrorInfo1
from travelport.models.profile_modify_bridge_branches_rsp import (
    ProfileModifyBridgeBranchesRsp,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class ProfileModifyBridgeBranchesPortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: ProfileModifyBridgeBranchesPortTypeServiceOutput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        profile_modify_bridge_branches_rsp: (
            None | ProfileModifyBridgeBranchesRsp
        ) = field(
            default=None,
            metadata={
                "name": "ProfileModifyBridgeBranchesRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            },
        )
        fault: (
            None | ProfileModifyBridgeBranchesPortTypeServiceOutput.Body.Fault
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
                | ProfileModifyBridgeBranchesPortTypeServiceOutput.Body.Fault.Detail
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
