from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.error_info_1 import ErrorInfo1
from travelport.models.profile_delete_hierarchy_level_rsp import (
    ProfileDeleteHierarchyLevelRsp,
)
from travelport.models.profile_summary_error_info_1 import (
    ProfileSummaryErrorInfo1,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class ProfileDeleteHierarchyLevelPortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | ProfileDeleteHierarchyLevelPortTypeServiceOutput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        profile_delete_hierarchy_level_rsp: (
            None | ProfileDeleteHierarchyLevelRsp
        ) = field(
            default=None,
            metadata={
                "name": "ProfileDeleteHierarchyLevelRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            },
        )
        fault: (
            None | ProfileDeleteHierarchyLevelPortTypeServiceOutput.Body.Fault
        ) = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            },
        )

        @dataclass
        class Fault:
            faultcode: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultstring: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
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
                | ProfileDeleteHierarchyLevelPortTypeServiceOutput.Body.Fault.Detail
            ) = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )

            @dataclass
            class Detail:
                error_info: None | ErrorInfo1 = field(
                    default=None,
                    metadata={
                        "name": "ErrorInfo",
                        "type": "Element",
                        "namespace": "http://www.travelport.com/schema/common_v52_0",
                    },
                )
                profile_summary_error_info: None | ProfileSummaryErrorInfo1 = (
                    field(
                        default=None,
                        metadata={
                            "name": "ProfileSummaryErrorInfo",
                            "type": "Element",
                            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
                        },
                    )
                )
