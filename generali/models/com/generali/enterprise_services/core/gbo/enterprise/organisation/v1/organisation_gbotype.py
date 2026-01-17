from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from generali.models.com.generali.enterprise_services.core.gbo.common.v1.address_type import (
    AddressType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.organisation.v1.extended_record_type import (
    ExtendedRecordType,
)
from generali.models.com.generali.enterprise_services.core.gbo.enterprise.organisation.v1.organisation_gbotype_party_roles import (
    OrganisationGbotypePartyRoles,
)

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1"


@dataclass
class OrganisationGbotype:
    """
    - <xs:description
    xmlns:xs="http://www.w3.org/2001/XMLSchema">Documentation for the
    elements below can be found at
    https://itservices.generali.co.uk/workspace/display/BPR/Organization+Data+Dictionary
    </xs:description>.

    :ivar dunsnumber:
    :ivar gunsnumber:
    :ivar full_name: The legal name of the Organisation
    :ivar primary_address:
    :ivar gen_global_ultimate_guns:
    :ivar ultimate_gunsname:
    :ivar ultimate_dunsnumber:
    :ivar national_id:
    :ivar national_idtype:
    :ivar sic:
    :ivar out_of_business:
    :ivar party_roles:
    :ivar duplicate:
    :ivar is_linked:
    :ivar active:
    :ivar creation_date: <description xmlns=""> The date and time the
        business object or component was created. A date and time
        formatted in compliance with the ISO8601 standard must be used.
        </description>
    :ivar date_last_update: <description xmlns=""> The date and time the
        business object or component was last modified. A date and time
        formatted in compliance with the ISO8601 standard must be used.
        </description>
    :ivar user_last_change_by:
    :ivar extended_record:
    """

    class Meta:
        name = "OrganisationGBOType"

    dunsnumber: Optional[str] = field(
        default=None,
        metadata={
            "name": "DUNSNumber",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
            "length": 9,
            "pattern": r"([0-9]{9})",
        },
    )
    gunsnumber: Optional[str] = field(
        default=None,
        metadata={
            "name": "GUNSNumber",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
            "length": 10,
            "pattern": r"G([0-9]{9})",
        },
    )
    full_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "FullName",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    primary_address: Optional[AddressType] = field(
        default=None,
        metadata={
            "name": "PrimaryAddress",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
            "required": True,
        },
    )
    gen_global_ultimate_guns: Optional[str] = field(
        default=None,
        metadata={
            "name": "GenGlobalUltimateGUNS",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
            "length": 10,
            "pattern": r"G([0-9]{9})",
        },
    )
    ultimate_gunsname: Optional[str] = field(
        default=None,
        metadata={
            "name": "UltimateGUNSName",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    ultimate_dunsnumber: Optional[str] = field(
        default=None,
        metadata={
            "name": "UltimateDUNSNumber",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
            "length": 9,
            "pattern": r"([0-9]{9})",
        },
    )
    national_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "NationalID",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    national_idtype: Optional[str] = field(
        default=None,
        metadata={
            "name": "NationalIDType",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    sic: Optional[str] = field(
        default=None,
        metadata={
            "name": "SIC",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    out_of_business: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OutOfBusiness",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    party_roles: Optional[OrganisationGbotypePartyRoles] = field(
        default=None,
        metadata={
            "name": "PartyRoles",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    duplicate: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Duplicate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    is_linked: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsLinked",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    active: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Active",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    creation_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreationDate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    date_last_update: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DateLastUpdate",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    user_last_change_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "UserLastChangeBy",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
    extended_record: Optional[ExtendedRecordType] = field(
        default=None,
        metadata={
            "name": "ExtendedRecord",
            "type": "Element",
            "namespace": "http://generali.com/enterprise-services/core/gbo/enterprise/organisation/v1",
        },
    )
