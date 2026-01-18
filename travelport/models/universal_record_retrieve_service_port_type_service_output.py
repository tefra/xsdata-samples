from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.error_info_1 import ErrorInfo1
from travelport.models.universal_record_error_info import (
    UniversalRecordErrorInfo,
)
from travelport.models.universal_record_retrieve_rsp import (
    UniversalRecordRetrieveRsp,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class UniversalRecordRetrieveServicePortTypeServiceOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: UniversalRecordRetrieveServicePortTypeServiceOutput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        universal_record_retrieve_rsp: None | UniversalRecordRetrieveRsp = (
            field(
                default=None,
                metadata={
                    "name": "UniversalRecordRetrieveRsp",
                    "type": "Element",
                    "namespace": "http://www.travelport.com/schema/universal_v52_0",
                },
            )
        )
        fault: (
            None
            | UniversalRecordRetrieveServicePortTypeServiceOutput.Body.Fault
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
                | UniversalRecordRetrieveServicePortTypeServiceOutput.Body.Fault.Detail
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
                universal_record_error_info: (
                    None | UniversalRecordErrorInfo
                ) = field(
                    default=None,
                    metadata={
                        "name": "UniversalRecordErrorInfo",
                        "type": "Element",
                        "namespace": "http://www.travelport.com/schema/universal_v52_0",
                    },
                )
