from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.availability_error_info import AvailabilityErrorInfo
from travelport.models.error_info_1 import ErrorInfo1
from travelport.models.universal_modify_error_info import (
    UniversalModifyErrorInfo,
)
from travelport.models.universal_record_modify_rsp import (
    UniversalRecordModifyRsp,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class UniversalRecordModifyServicePortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: UniversalRecordModifyServicePortTypeServiceOutput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        universal_record_modify_rsp: None | UniversalRecordModifyRsp = field(
            default=None,
            metadata={
                "name": "UniversalRecordModifyRsp",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/universal_v52_0",
            },
        )
        fault: (
            None | UniversalRecordModifyServicePortTypeServiceOutput.Body.Fault
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
                | UniversalRecordModifyServicePortTypeServiceOutput.Body.Fault.Detail
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
                availability_error_info: None | AvailabilityErrorInfo = field(
                    default=None,
                    metadata={
                        "name": "AvailabilityErrorInfo",
                        "type": "Element",
                        "namespace": "http://www.travelport.com/schema/air_v52_0",
                    },
                )
                universal_modify_error_info: (
                    None | UniversalModifyErrorInfo
                ) = field(
                    default=None,
                    metadata={
                        "name": "UniversalModifyErrorInfo",
                        "type": "Element",
                        "namespace": "http://www.travelport.com/schema/universal_v52_0",
                    },
                )
