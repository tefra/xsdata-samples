from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from xsdata.models.datatype import XmlDateTime

from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.amount_type import (
    AmountType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.legal_status_code_type import (
    LegalStatusCodeType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.organisation.v1.extended_record_type_business_lines import (
    ExtendedRecordTypeBusinessLines,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.organisation.v1.extended_record_type_company_levels import (
    ExtendedRecordTypeCompanyLevels,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.organisation.v1.extended_record_type_duplicated_gunsnumbers import (
    ExtendedRecordTypeDuplicatedGunsnumbers,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.organisation.v1.extended_record_type_local_ids import (
    ExtendedRecordTypeLocalIds,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.organisation.v1.extended_record_type_party_local_ids import (
    ExtendedRecordTypePartyLocalIds,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.organisation.v1.extended_record_type_senders import (
    ExtendedRecordTypeSenders,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1"


@dataclass
class ExtendedRecordType:
    """
    :ivar domestic_ultimate_dunsnumber:
    :ivar domestic_ultimate_gunsnumber:
    :ivar domestic_ultimate_gunsname:
    :ivar global_ultimate_country_code:
    :ivar company_levels:
    :ivar company_legal_status:
    :ivar year_started:
    :ivar turnover:
    :ivar turnover_currency:
    :ivar turnover_accuracy:
    :ivar number_of_employees:
    :ivar employee_accuracy:
    :ivar assigned_turnover_tree_below_eur: Turnover value (EUR at
        today's FX rate?????) assigned by D&amp;B to this legal entity
        and all entities below in the in the corporate tree. Only
        available for legal entities that are part of a corporate
        family, blank for all standalone or unlinked entities
    :ivar assigned_turnover_domestic_group_eur:
    :ivar assigned_turnover_global_group_eur:
    :ivar assigned_number_of_employees_tree_below: Number of employees
        assigned by D&amp;B to this legal entity and all entities below
        in the corporate tree.
    :ivar assigned_number_of_employees_domestic_group:
    :ivar assigned_number_of_employees_global_group:
    :ivar assigned_sic4_du:
    :ivar assigned_sic4_name_du:
    :ivar assigned_sic2_du:
    :ivar assigned_sic2_name_du:
    :ivar assigned_sicduproportion_code:
    :ivar assigned_sic4_gu:
    :ivar assigned_sic4_name_gu:
    :ivar assigned_sic2_gu:
    :ivar assigned_sic2_name_gu:
    :ivar assigned_sicguproportion_code:
    :ivar is_part_of_corporate_tree:
    :ivar is_standalone:
    :ivar this_level_in_corporate_tree:
    :ivar number_of_level_in_corporate_tree:
    :ivar number_of_countries_in_group: Number of countries in the
        corporate tree. Blank if this is a standalone company or no data
        is available
    :ivar national_or_multinational_code:
    :ivar national_or_multinational_code_exc_branches:
    :ivar tree_below_sites:
    :ivar tree_below_sites_excluding_branch:
    :ivar number_of_sites_gugroup:
    :ivar number_of_sites_gugroup_exc_branches:
    :ivar number_of_sites_gugroup_in_this_country:
    :ivar number_of_sites_gugroup_in_this_country_exc_branches:
    :ivar number_of_sites_dugroup:
    :ivar number_of_sites_dugroup_exc_branches:
    :ivar number_of_eusites_gugroup:
    :ivar number_of_eusites_gugroup_exc_branches:
    :ivar business_lines: <description xmlns="">ID is the business line
        this legal entity is in use e.g. EAGCS (Europe Assistance - GCS
        division)</description>
    :ivar domestic_ultimate:
    :ivar global_ultimate:
    :ivar senders:
    :ivar duplicated_gunsnumbers:
    :ivar acquired_from_dn_b: <description xmlns=""> The date on which
        the organisation was incorporated, i.e. registered with the
        local Companies House or similar. </description>
    :ivar refreshed_by_dand_b:
    :ivar refresh_count:
    :ivar user_created_by:
    :ivar exported_date:
    :ivar local_ids: @deprecated: keep for local reference, should be
        removed soon
    :ivar party_local_ids:
    """

    domestic_ultimate_dunsnumber: str | None = field(
        default=None,
        metadata={
            "name": "DomesticUltimateDUNSNumber",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
            "length": 9,
            "pattern": r"([0-9]{9})",
        },
    )
    domestic_ultimate_gunsnumber: str | None = field(
        default=None,
        metadata={
            "name": "DomesticUltimateGUNSNumber",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
            "length": 10,
            "pattern": r"G([0-9]{9})",
        },
    )
    domestic_ultimate_gunsname: str | None = field(
        default=None,
        metadata={
            "name": "DomesticUltimateGUNSName",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    global_ultimate_country_code: str | None = field(
        default=None,
        metadata={
            "name": "GlobalUltimateCountryCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
            "pattern": r"[A-Z][A-Z]",
        },
    )
    company_levels: ExtendedRecordTypeCompanyLevels | None = field(
        default=None,
        metadata={
            "name": "CompanyLevels",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    company_legal_status: LegalStatusCodeType | None = field(
        default=None,
        metadata={
            "name": "CompanyLegalStatus",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    year_started: int | None = field(
        default=None,
        metadata={
            "name": "YearStarted",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    turnover: AmountType | None = field(
        default=None,
        metadata={
            "name": "Turnover",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    turnover_currency: str | None = field(
        default=None,
        metadata={
            "name": "TurnoverCurrency",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    turnover_accuracy: int | None = field(
        default=None,
        metadata={
            "name": "TurnoverAccuracy",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    number_of_employees: int | None = field(
        default=None,
        metadata={
            "name": "NumberOfEmployees",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    employee_accuracy: int | None = field(
        default=None,
        metadata={
            "name": "EmployeeAccuracy",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    assigned_turnover_tree_below_eur: AmountType | None = field(
        default=None,
        metadata={
            "name": "AssignedTurnoverTreeBelowEUR",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
            "nillable": True,
        },
    )
    assigned_turnover_domestic_group_eur: AmountType | None = field(
        default=None,
        metadata={
            "name": "AssignedTurnoverDomesticGroupEUR",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
            "nillable": True,
        },
    )
    assigned_turnover_global_group_eur: AmountType | None = field(
        default=None,
        metadata={
            "name": "AssignedTurnoverGlobalGroupEUR",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
            "nillable": True,
        },
    )
    assigned_number_of_employees_tree_below: Decimal | None = field(
        default=None,
        metadata={
            "name": "AssignedNumberOfEmployeesTreeBelow",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    assigned_number_of_employees_domestic_group: Decimal | None = field(
        default=None,
        metadata={
            "name": "AssignedNumberOfEmployeesDomesticGroup",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    assigned_number_of_employees_global_group: Decimal | None = field(
        default=None,
        metadata={
            "name": "AssignedNumberOfEmployeesGlobalGroup",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    assigned_sic4_du: str | None = field(
        default=None,
        metadata={
            "name": "AssignedSIC4DU",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    assigned_sic4_name_du: str | None = field(
        default=None,
        metadata={
            "name": "AssignedSIC4NameDU",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    assigned_sic2_du: str | None = field(
        default=None,
        metadata={
            "name": "AssignedSIC2DU",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    assigned_sic2_name_du: str | None = field(
        default=None,
        metadata={
            "name": "AssignedSIC2NameDU",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    assigned_sicduproportion_code: int | None = field(
        default=None,
        metadata={
            "name": "AssignedSICDUProportionCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    assigned_sic4_gu: str | None = field(
        default=None,
        metadata={
            "name": "AssignedSIC4GU",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    assigned_sic4_name_gu: str | None = field(
        default=None,
        metadata={
            "name": "AssignedSIC4NameGU",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    assigned_sic2_gu: str | None = field(
        default=None,
        metadata={
            "name": "AssignedSIC2GU",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    assigned_sic2_name_gu: str | None = field(
        default=None,
        metadata={
            "name": "AssignedSIC2NameGU",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    assigned_sicguproportion_code: int | None = field(
        default=None,
        metadata={
            "name": "AssignedSICGUProportionCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    is_part_of_corporate_tree: bool | None = field(
        default=None,
        metadata={
            "name": "IsPartOfCorporateTree",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    is_standalone: bool | None = field(
        default=None,
        metadata={
            "name": "IsStandalone",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    this_level_in_corporate_tree: int | None = field(
        default=None,
        metadata={
            "name": "ThisLevelInCorporateTree",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    number_of_level_in_corporate_tree: int | None = field(
        default=None,
        metadata={
            "name": "NumberOfLevelInCorporateTree",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    number_of_countries_in_group: int | None = field(
        default=None,
        metadata={
            "name": "NumberOfCountriesInGroup",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    national_or_multinational_code: int | None = field(
        default=None,
        metadata={
            "name": "NationalOrMultinationalCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    national_or_multinational_code_exc_branches: int | None = field(
        default=None,
        metadata={
            "name": "NationalOrMultinationalCodeExcBranches",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    tree_below_sites: Decimal | None = field(
        default=None,
        metadata={
            "name": "TreeBelowSites",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    tree_below_sites_excluding_branch: Decimal | None = field(
        default=None,
        metadata={
            "name": "TreeBelowSitesExcludingBranch",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    number_of_sites_gugroup: int | None = field(
        default=None,
        metadata={
            "name": "NumberOfSitesGUGroup",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    number_of_sites_gugroup_exc_branches: int | None = field(
        default=None,
        metadata={
            "name": "NumberOfSitesGUGroupExcBranches",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    number_of_sites_gugroup_in_this_country: int | None = field(
        default=None,
        metadata={
            "name": "NumberOfSitesGUGroupInThisCountry",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    number_of_sites_gugroup_in_this_country_exc_branches: int | None = field(
        default=None,
        metadata={
            "name": "NumberOfSitesGUGroupInThisCountryExcBranches",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    number_of_sites_dugroup: int | None = field(
        default=None,
        metadata={
            "name": "NumberOfSitesDUGroup",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    number_of_sites_dugroup_exc_branches: int | None = field(
        default=None,
        metadata={
            "name": "NumberOfSitesDUGroupExcBranches",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    number_of_eusites_gugroup: int | None = field(
        default=None,
        metadata={
            "name": "NumberOfEUSitesGUGroup",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    number_of_eusites_gugroup_exc_branches: int | None = field(
        default=None,
        metadata={
            "name": "NumberOfEUSitesGUGroupExcBranches",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    business_lines: ExtendedRecordTypeBusinessLines | None = field(
        default=None,
        metadata={
            "name": "BusinessLines",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    domestic_ultimate: bool | None = field(
        default=None,
        metadata={
            "name": "DomesticUltimate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    global_ultimate: bool | None = field(
        default=None,
        metadata={
            "name": "GlobalUltimate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    senders: ExtendedRecordTypeSenders | None = field(
        default=None,
        metadata={
            "name": "Senders",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    duplicated_gunsnumbers: ExtendedRecordTypeDuplicatedGunsnumbers | None = (
        field(
            default=None,
            metadata={
                "name": "DuplicatedGUNSNumbers",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
            },
        )
    )
    acquired_from_dn_b: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "AcquiredFromDnB",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    refreshed_by_dand_b: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "RefreshedByDandB",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    refresh_count: int | None = field(
        default=None,
        metadata={
            "name": "RefreshCount",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    user_created_by: str | None = field(
        default=None,
        metadata={
            "name": "UserCreatedBy",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    exported_date: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "ExportedDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    local_ids: ExtendedRecordTypeLocalIds | None = field(
        default=None,
        metadata={
            "name": "LocalIds",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    party_local_ids: ExtendedRecordTypePartyLocalIds | None = field(
        default=None,
        metadata={
            "name": "PartyLocalIds",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
