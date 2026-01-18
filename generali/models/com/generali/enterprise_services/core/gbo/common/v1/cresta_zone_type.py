from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.idtype import (
    Idtype,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


@dataclass
class CrestaZoneType:
    cresta_zone_identifier: Idtype | None = field(
        default=None,
        metadata={
            "name": "CrestaZoneIdentifier",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
            "required": True,
        },
    )
    cresta_zone_name: Idtype | None = field(
        default=None,
        metadata={
            "name": "CrestaZoneName",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    cresta_sub_zone_identifier: Idtype | None = field(
        default=None,
        metadata={
            "name": "CrestaSubZoneIdentifier",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
    cresta_sub_zone_name: Idtype | None = field(
        default=None,
        metadata={
            "name": "CrestaSubZoneName",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/common/v1",
        },
    )
