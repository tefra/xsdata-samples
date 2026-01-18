from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.profile_retrieve_history_req_1 import (
    ProfileRetrieveHistoryReq1,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class ProfileRetrieveHistoryPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: object = field(
        metadata={
            "name": "Header",
            "type": "Element",
        }
    )
    body: ProfileRetrieveHistoryPortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        profile_retrieve_history_req: ProfileRetrieveHistoryReq1 = field(
            metadata={
                "name": "ProfileRetrieveHistoryReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
            }
        )
