from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.instalment_basis_enum import InstalmentBasisEnum
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.agreement.v1.instalment_date_enum import InstalmentDateEnum

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"


@dataclass
class InstalmentPlansType:
    instalment_plan: List["InstalmentPlansType.InstalmentPlan"] = field(
        default_factory=list,
        metadata={
            "name": "InstalmentPlan",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
        }
    )

    @dataclass
    class InstalmentPlan:
        start_date: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "name": "StartDate",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            }
        )
        end_date: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "name": "EndDate",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
            }
        )
        number_of_instalment: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "NumberOfInstalment",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
                "required": True,
            }
        )
        instalment_basis: Optional[InstalmentBasisEnum] = field(
            default=None,
            metadata={
                "name": "InstalmentBasis",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
                "required": True,
            }
        )
        instalment_date: Optional[InstalmentDateEnum] = field(
            default=None,
            metadata={
                "name": "InstalmentDate",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1",
                "required": True,
            }
        )
