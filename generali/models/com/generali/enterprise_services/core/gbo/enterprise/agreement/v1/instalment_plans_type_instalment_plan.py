from dataclasses import dataclass, field
from typing import Optional

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.date_time_type import (
    DateTimeType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.numeric_type import (
    NumericType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.instalment_basis_enum import (
    InstalmentBasisEnum,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.instalment_date_enum import (
    InstalmentDateEnum,
)

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


@dataclass
class InstalmentPlansTypeInstalmentPlan:
    class Meta:
        global_type = False

    start_date: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    end_date: Optional[DateTimeType] = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        },
    )
    number_of_instalment: Optional[NumericType] = field(
        default=None,
        metadata={
            "name": "NumberOfInstalment",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    instalment_basis: Optional[InstalmentBasisEnum] = field(
        default=None,
        metadata={
            "name": "InstalmentBasis",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
    instalment_date: Optional[InstalmentDateEnum] = field(
        default=None,
        metadata={
            "name": "InstalmentDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            "required": True,
        },
    )
