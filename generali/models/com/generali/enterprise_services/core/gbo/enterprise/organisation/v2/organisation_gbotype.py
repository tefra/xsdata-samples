from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from generali.models.com.generali.enterprise_services.core.gbo.common.v1.address_type import (
    AddressType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.organisation.v2.extended_record_type import (
    ExtendedRecordType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.organisation.v2.national_ids_type import (
    NationalIdsType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.organisation.v2.organisation_gbotype_company_levels import (
    OrganisationGbotypeCompanyLevels,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2"


@dataclass
class OrganisationGbotype:
    """
    - <xs:description
    xmlns:xs="http://www.w3.org/2001/XMLSchema">Documentation for the
    elements below can be found at
    https://itservices.generali.co.uk/workspace/display/BPR/Organization+Data+Dictionary
    </xs:description>.

    :ivar gunsnumber:
    :ivar full_name: The legal name of the Organisation
    :ivar dunsnumber:
    :ivar primary_address:
    :ivar global_ultimate_guns:
    :ivar global_ultimate_name:
    :ivar national_ids:
    :ivar sic:
    :ivar is_out_of_business:
    :ivar company_levels:
    :ivar is_individual:
    :ivar creation_date: <description xmlns=""> The date and time the
        business object or component was created. A date and time
        formatted in compliance with the ISO8601 standard must be used.
        </description>
    :ivar date_last_update: <description xmlns=""> The date and time the
        business object or component was last modified. A date and time
        formatted in compliance with the ISO8601 standard must be used.
        </description>
    :ivar extended_record:
    """

    class Meta:
        name = "OrganisationGBOType"

    gunsnumber: str | None = field(
        default=None,
        metadata={
            "name": "GUNSNumber",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
            "length": 10,
            "pattern": r"G([0-9]{9})",
        },
    )
    full_name: str | None = field(
        default=None,
        metadata={
            "name": "FullName",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    dunsnumber: str | None = field(
        default=None,
        metadata={
            "name": "DUNSNumber",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
            "length": 9,
            "pattern": r"([0-9]{9})",
        },
    )
    primary_address: AddressType | None = field(
        default=None,
        metadata={
            "name": "PrimaryAddress",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
            "required": True,
        },
    )
    global_ultimate_guns: str | None = field(
        default=None,
        metadata={
            "name": "GlobalUltimateGUNS",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
            "length": 10,
            "pattern": r"G([0-9]{9})",
        },
    )
    global_ultimate_name: str | None = field(
        default=None,
        metadata={
            "name": "GlobalUltimateName",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    national_ids: NationalIdsType | None = field(
        default=None,
        metadata={
            "name": "NationalIds",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    sic: str | None = field(
        default=None,
        metadata={
            "name": "SIC",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    is_out_of_business: bool | None = field(
        default=None,
        metadata={
            "name": "IsOutOfBusiness",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    company_levels: OrganisationGbotypeCompanyLevels | None = field(
        default=None,
        metadata={
            "name": "CompanyLevels",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    is_individual: bool | None = field(
        default=None,
        metadata={
            "name": "IsIndividual",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
            "required": True,
        },
    )
    creation_date: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "CreationDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    date_last_update: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "DateLastUpdate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
    extended_record: ExtendedRecordType | None = field(
        default=None,
        metadata={
            "name": "ExtendedRecord",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v2",
        },
    )
