from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.engineering_maintenance_type_years import (
    EngineeringMaintenanceTypeYears,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class EngineeringMaintenanceType:
    inception_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "InceptionDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    expiry_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ExpiryDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    years: Optional[EngineeringMaintenanceTypeYears] = field(
        default=None,
        metadata={
            "name": "Years",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
