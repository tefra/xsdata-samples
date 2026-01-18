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
class GlobalUltimateInfoType:
    """
    :ivar gunsnumber_gu:
    :ivar full_name_gu:
    :ivar dunsnumber_gu:
    :ivar country_code_gu:
    :ivar assigned_turnover_global_group:
    :ivar assigned_number_of_employees_global_group:
    :ivar assigned_sicgu:
    :ivar assigned_sicname_gu:
    :ivar assigned_sicguproportion_code:
    :ivar number_of_level_in_corporate_tree:
    :ivar number_of_countries_in_group: Number of countries in the
        corporate tree. Blank if this is a standalone company or no data
        is available
    :ivar is_multinational:
    :ivar is_multinational_exc_branches:
    :ivar number_of_sites_gugroup:
    :ivar number_of_sites_gugroup_exc_branches:
    :ivar number_of_sites_gugroup_in_this_country:
    :ivar number_of_sites_gugroup_in_this_country_exc_branches:
    :ivar number_of_eusites_gugroup:
    :ivar number_of_eusites_gugroup_exc_branches:
    """

    gunsnumber_gu: str | None = field(
        default=None,
        metadata={
            "name": "GUNSNumberGU",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
            "length": 10,
            "pattern": r"G([0-9]{9})",
        },
    )
    full_name_gu: str | None = field(
        default=None,
        metadata={
            "name": "FullNameGU",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    dunsnumber_gu: str | None = field(
        default=None,
        metadata={
            "name": "DUNSNumberGU",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
            "length": 9,
            "pattern": r"([0-9]{9})",
        },
    )
    country_code_gu: str | None = field(
        default=None,
        metadata={
            "name": "CountryCodeGU",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
            "pattern": r"[A-Z][A-Z]",
        },
    )
    assigned_turnover_global_group: AmountType | None = field(
        default=None,
        metadata={
            "name": "AssignedTurnoverGlobalGroup",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
            "nillable": True,
        },
    )
    assigned_number_of_employees_global_group: Decimal | None = field(
        default=None,
        metadata={
            "name": "AssignedNumberOfEmployeesGlobalGroup",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    assigned_sicgu: str | None = field(
        default=None,
        metadata={
            "name": "AssignedSICGU",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    assigned_sicname_gu: str | None = field(
        default=None,
        metadata={
            "name": "AssignedSICNameGU",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    assigned_sicguproportion_code: CodeType | None = field(
        default=None,
        metadata={
            "name": "AssignedSICGUProportionCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    number_of_level_in_corporate_tree: int | None = field(
        default=None,
        metadata={
            "name": "NumberOfLevelInCorporateTree",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    number_of_countries_in_group: int | None = field(
        default=None,
        metadata={
            "name": "NumberOfCountriesInGroup",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    is_multinational: bool | None = field(
        default=None,
        metadata={
            "name": "IsMultinational",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    is_multinational_exc_branches: bool | None = field(
        default=None,
        metadata={
            "name": "IsMultinationalExcBranches",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    number_of_sites_gugroup: int | None = field(
        default=None,
        metadata={
            "name": "NumberOfSitesGUGroup",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    number_of_sites_gugroup_exc_branches: int | None = field(
        default=None,
        metadata={
            "name": "NumberOfSitesGUGroupExcBranches",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    number_of_sites_gugroup_in_this_country: int | None = field(
        default=None,
        metadata={
            "name": "NumberOfSitesGUGroupInThisCountry",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    number_of_sites_gugroup_in_this_country_exc_branches: int | None = (
        field(
            default=None,
            metadata={
                "name": "NumberOfSitesGUGroupInThisCountryExcBranches",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
            },
        )
    )
    number_of_eusites_gugroup: int | None = field(
        default=None,
        metadata={
            "name": "NumberOfEUSitesGUGroup",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    number_of_eusites_gugroup_exc_branches: int | None = field(
        default=None,
        metadata={
            "name": "NumberOfEUSitesGUGroupExcBranches",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
