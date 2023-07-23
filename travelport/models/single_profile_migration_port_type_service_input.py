from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.single_profile_migration_req_1 import SingleProfileMigrationReq1

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class SingleProfileMigrationPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: None | object = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
        }
    )
    body: None | SingleProfileMigrationPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        single_profile_migration_req: None | SingleProfileMigrationReq1 = field(
            default=None,
            metadata={
                "name": "SingleProfileMigrationReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
            }
        )
