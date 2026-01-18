from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.amount_type import (
    AmountType,
)
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.code_type import (
    CodeType,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2"


@dataclass
class CompanyInfoType:
    company_legal_status: None | str = field(
        default=None,
        metadata={
            "name": "CompanyLegalStatus",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    year_started: None | int = field(
        default=None,
        metadata={
            "name": "YearStarted",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    turnover: None | AmountType = field(
        default=None,
        metadata={
            "name": "Turnover",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    turnover_currency: None | str = field(
        default=None,
        metadata={
            "name": "TurnoverCurrency",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    turnover_accuracy: None | CodeType = field(
        default=None,
        metadata={
            "name": "TurnoverAccuracy",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    number_of_employees: None | Decimal = field(
        default=None,
        metadata={
            "name": "NumberOfEmployees",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    employee_accuracy: None | CodeType = field(
        default=None,
        metadata={
            "name": "EmployeeAccuracy",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    is_part_of_corporate_tree: None | bool = field(
        default=None,
        metadata={
            "name": "IsPartOfCorporateTree",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    is_standalone: None | bool = field(
        default=None,
        metadata={
            "name": "IsStandalone",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    this_level_in_corporate_tree: None | int = field(
        default=None,
        metadata={
            "name": "ThisLevelInCorporateTree",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    is_domestic_ultimate: None | bool = field(
        default=None,
        metadata={
            "name": "IsDomesticUltimate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    is_global_ultimate: None | bool = field(
        default=None,
        metadata={
            "name": "IsGlobalUltimate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
