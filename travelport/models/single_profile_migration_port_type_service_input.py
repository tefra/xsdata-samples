from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.single_profile_migration_req_1 import (
    SingleProfileMigrationReq1,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class SingleProfileMigrationPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: object = field(
        metadata={
            "name": "Header",
            "type": "Element",
        }
    )
    body: SingleProfileMigrationPortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Body:
        single_profile_migration_req: SingleProfileMigrationReq1 = field(
            metadata={
                "name": "SingleProfileMigrationReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
            }
        )
