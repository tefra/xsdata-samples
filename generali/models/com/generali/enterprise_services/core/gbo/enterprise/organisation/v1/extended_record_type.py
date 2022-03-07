from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from generali.models.com.generali.enterprise_services.core.gbo.common.core_types.v1.amount_type import AmountType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.common.v1.legal_status_code_type import LegalStatusCodeType
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.organisation.v1.party_local_id_type import PartyLocalIdType

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
    domestic_ultimate_dunsnumber: Optional[str] = field(
        default=None,
        metadata={
            "name": "DomesticUltimateDUNSNumber",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
            "length": 9,
            "pattern": r"([0-9]{9})",
        }
    )
    domestic_ultimate_gunsnumber: Optional[str] = field(
        default=None,
        metadata={
            "name": "DomesticUltimateGUNSNumber",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
            "length": 10,
            "pattern": r"G([0-9]{9})",
        }
    )
    domestic_ultimate_gunsname: Optional[str] = field(
        default=None,
        metadata={
            "name": "DomesticUltimateGUNSName",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    global_ultimate_country_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "GlobalUltimateCountryCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
            "pattern": r"[A-Z][A-Z]",
        }
    )
    company_levels: Optional["ExtendedRecordType.CompanyLevels"] = field(
        default=None,
        metadata={
            "name": "CompanyLevels",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    company_legal_status: Optional[LegalStatusCodeType] = field(
        default=None,
        metadata={
            "name": "CompanyLegalStatus",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    year_started: Optional[int] = field(
        default=None,
        metadata={
            "name": "YearStarted",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    turnover: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "Turnover",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    turnover_currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "TurnoverCurrency",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    turnover_accuracy: Optional[int] = field(
        default=None,
        metadata={
            "name": "TurnoverAccuracy",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    number_of_employees: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfEmployees",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    employee_accuracy: Optional[int] = field(
        default=None,
        metadata={
            "name": "EmployeeAccuracy",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    assigned_turnover_tree_below_eur: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "AssignedTurnoverTreeBelowEUR",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
            "nillable": True,
        }
    )
    assigned_turnover_domestic_group_eur: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "AssignedTurnoverDomesticGroupEUR",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
            "nillable": True,
        }
    )
    assigned_turnover_global_group_eur: Optional[AmountType] = field(
        default=None,
        metadata={
            "name": "AssignedTurnoverGlobalGroupEUR",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
            "nillable": True,
        }
    )
    assigned_number_of_employees_tree_below: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AssignedNumberOfEmployeesTreeBelow",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    assigned_number_of_employees_domestic_group: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AssignedNumberOfEmployeesDomesticGroup",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    assigned_number_of_employees_global_group: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AssignedNumberOfEmployeesGlobalGroup",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    assigned_sic4_du: Optional[str] = field(
        default=None,
        metadata={
            "name": "AssignedSIC4DU",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    assigned_sic4_name_du: Optional[str] = field(
        default=None,
        metadata={
            "name": "AssignedSIC4NameDU",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    assigned_sic2_du: Optional[str] = field(
        default=None,
        metadata={
            "name": "AssignedSIC2DU",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    assigned_sic2_name_du: Optional[str] = field(
        default=None,
        metadata={
            "name": "AssignedSIC2NameDU",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    assigned_sicduproportion_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "AssignedSICDUProportionCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    assigned_sic4_gu: Optional[str] = field(
        default=None,
        metadata={
            "name": "AssignedSIC4GU",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    assigned_sic4_name_gu: Optional[str] = field(
        default=None,
        metadata={
            "name": "AssignedSIC4NameGU",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    assigned_sic2_gu: Optional[str] = field(
        default=None,
        metadata={
            "name": "AssignedSIC2GU",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    assigned_sic2_name_gu: Optional[str] = field(
        default=None,
        metadata={
            "name": "AssignedSIC2NameGU",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    assigned_sicguproportion_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "AssignedSICGUProportionCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    is_part_of_corporate_tree: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsPartOfCorporateTree",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    is_standalone: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsStandalone",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    this_level_in_corporate_tree: Optional[int] = field(
        default=None,
        metadata={
            "name": "ThisLevelInCorporateTree",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    number_of_level_in_corporate_tree: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfLevelInCorporateTree",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    number_of_countries_in_group: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfCountriesInGroup",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    national_or_multinational_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "NationalOrMultinationalCode",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    national_or_multinational_code_exc_branches: Optional[int] = field(
        default=None,
        metadata={
            "name": "NationalOrMultinationalCodeExcBranches",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    tree_below_sites: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TreeBelowSites",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    tree_below_sites_excluding_branch: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TreeBelowSitesExcludingBranch",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    number_of_sites_gugroup: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfSitesGUGroup",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    number_of_sites_gugroup_exc_branches: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfSitesGUGroupExcBranches",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    number_of_sites_gugroup_in_this_country: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfSitesGUGroupInThisCountry",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    number_of_sites_gugroup_in_this_country_exc_branches: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfSitesGUGroupInThisCountryExcBranches",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    number_of_sites_dugroup: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfSitesDUGroup",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    number_of_sites_dugroup_exc_branches: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfSitesDUGroupExcBranches",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    number_of_eusites_gugroup: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfEUSitesGUGroup",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    number_of_eusites_gugroup_exc_branches: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfEUSitesGUGroupExcBranches",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    business_lines: Optional["ExtendedRecordType.BusinessLines"] = field(
        default=None,
        metadata={
            "name": "BusinessLines",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    domestic_ultimate: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DomesticUltimate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    global_ultimate: Optional[bool] = field(
        default=None,
        metadata={
            "name": "GlobalUltimate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    senders: Optional["ExtendedRecordType.Senders"] = field(
        default=None,
        metadata={
            "name": "Senders",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    duplicated_gunsnumbers: Optional["ExtendedRecordType.DuplicatedGunsnumbers"] = field(
        default=None,
        metadata={
            "name": "DuplicatedGUNSNumbers",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    acquired_from_dn_b: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "AcquiredFromDnB",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    refreshed_by_dand_b: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RefreshedByDandB",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    refresh_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "RefreshCount",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    user_created_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "UserCreatedBy",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    exported_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ExportedDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    local_ids: Optional["ExtendedRecordType.LocalIds"] = field(
        default=None,
        metadata={
            "name": "LocalIds",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )
    party_local_ids: Optional["ExtendedRecordType.PartyLocalIds"] = field(
        default=None,
        metadata={
            "name": "PartyLocalIds",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        }
    )

    @dataclass
    class CompanyLevels:
        company_level: List[str] = field(
            default_factory=list,
            metadata={
                "name": "CompanyLevel",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
            }
        )

    @dataclass
    class BusinessLines:
        business_line: List[str] = field(
            default_factory=list,
            metadata={
                "name": "BusinessLine",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
            }
        )

    @dataclass
    class Senders:
        sender: List[str] = field(
            default_factory=list,
            metadata={
                "name": "Sender",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
            }
        )

    @dataclass
    class DuplicatedGunsnumbers:
        duplicated_gunsnumber: List[str] = field(
            default_factory=list,
            metadata={
                "name": "DuplicatedGUNSNumber",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
                "length": 10,
                "pattern": r"G([0-9]{9})",
            }
        )

    @dataclass
    class LocalIds:
        local_id: List[str] = field(
            default_factory=list,
            metadata={
                "name": "LocalId",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
            }
        )

    @dataclass
    class PartyLocalIds:
        party_local_id: List[PartyLocalIdType] = field(
            default_factory=list,
            metadata={
                "name": "PartyLocalId",
                "type": "Element",
                "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
            }
        )
