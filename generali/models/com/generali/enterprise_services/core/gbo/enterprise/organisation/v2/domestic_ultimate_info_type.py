from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.amount_type import (
    AmountType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.code_type import (
    CodeType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2"


@dataclass
class DomesticUltimateInfoType:
    gunsnumber_du: Optional[str] = field(
        default=None,
        metadata={
            "name": "GUNSNumberDU",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
            "length": 10,
            "pattern": r"G([0-9]{9})",
        },
    )
    full_name_du: Optional[str] = field(
        default=None,
        metadata={
            "name": "FullNameDU",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    dunsnumber_du: Optional[str] = field(
        default=None,
        metadata={
            "name": "DUNSNumberDU",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
            "length": 9,
            "pattern": r"([0-9]{9})",
        },
    )
    assigned_turnover_domestic_group: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "AssignedTurnoverDomesticGroup",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
            "nillable": True,
        },
    )
    assigned_number_of_employees_domestic_group: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AssignedNumberOfEmployeesDomesticGroup",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    assigned_sicdu: Optional[str] = field(
        default=None,
        metadata={
            "name": "AssignedSICDU",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    assigned_sicname_du: Optional[str] = field(
        default=None,
        metadata={
            "name": "AssignedSICNameDU",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    assigned_sicduproportion_code: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "AssignedSICDUProportionCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    number_of_sites_dugroup: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfSitesDUGroup",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    number_of_sites_dugroup_exc_branches: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfSitesDUGroupExcBranches",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
