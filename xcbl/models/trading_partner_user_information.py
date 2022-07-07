from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_create import (
    CorrespondenceLanguage,
    Country,
    Pobox,
    Region,
    Timezone,
    ValidityDates,
)
from xcbl.models.trading_partner_user_delete import (
    TradingPartnerOrganizationReference,
    UserId,
)


@dataclass
class AcademicTitle:
    academic_title_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcademicTitleCoded",
            "type": "Element",
            "required": True,
        }
    )
    academic_title_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcademicTitleCodedOther",
            "type": "Element",
        }
    )


@dataclass
class CertificatePurpose:
    certificate_purpose_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertificatePurposeCoded",
            "type": "Element",
            "required": True,
        }
    )
    certificate_purpose_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertificatePurposeCodedOther",
            "type": "Element",
        }
    )


@dataclass
class ContactRelationType:
    contact_relation_type_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContactRelationTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    contact_relation_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContactRelationTypeCodedOther",
            "type": "Element",
        }
    )


@dataclass
class DateFormat:
    date_format_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "DateFormatCoded",
            "type": "Element",
            "required": True,
        }
    )
    date_format_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "DateFormatCodedOther",
            "type": "Element",
        }
    )


@dataclass
class PersonCommunicationType:
    person_communication_type_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "PersonCommunicationTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    person_communication_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "PersonCommunicationTypeCodedOther",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Title:
    title_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "TitleCoded",
            "type": "Element",
            "required": True,
        }
    )
    title_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "TitleCodedOther",
            "type": "Element",
        }
    )


@dataclass
class TradingPartnerUserPurpose:
    trading_partner_user_purpose_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradingPartnerUserPurposeCoded",
            "type": "Element",
            "required": True,
        }
    )
    trading_partner_user_purpose_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradingPartnerUserPurposeCodedOther",
            "type": "Element",
        }
    )


@dataclass
class UserRole:
    user_role_authority: Optional[str] = field(
        default=None,
        metadata={
            "name": "UserRoleAuthority",
            "type": "Element",
        }
    )
    user_role_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "UserRoleName",
            "type": "Element",
            "required": True,
        }
    )
    user_role_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "UserRoleID",
            "type": "Element",
        }
    )


@dataclass
class UserStatus:
    user_status_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "UserStatusCoded",
            "type": "Element",
            "required": True,
        }
    )
    user_status_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "UserStatusCodedOther",
            "type": "Element",
        }
    )


@dataclass
class X509CertificateInfo:
    x509_subject: Optional[str] = field(
        default=None,
        metadata={
            "name": "X509Subject",
            "type": "Element",
            "required": True,
        }
    )
    x509_issuer: Optional[str] = field(
        default=None,
        metadata={
            "name": "X509Issuer",
            "type": "Element",
            "required": True,
        }
    )
    x509_serial_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "X509SerialNumber",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class CommunicationDetail:
    communication_detail_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "CommunicationDetailDescription",
            "type": "Element",
        }
    )
    person_communication_type: Optional[PersonCommunicationType] = field(
        default=None,
        metadata={
            "name": "PersonCommunicationType",
            "type": "Element",
            "required": True,
        }
    )
    communication_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "CommunicationValue",
            "type": "Element",
            "required": True,
        }
    )
    default_communication: Optional[str] = field(
        default=None,
        metadata={
            "name": "DefaultCommunication",
            "type": "Element",
        }
    )


@dataclass
class ListOfCertificatePurpose:
    certificate_purpose: List[CertificatePurpose] = field(
        default_factory=list,
        metadata={
            "name": "CertificatePurpose",
            "type": "Element",
        }
    )


@dataclass
class ListOfContactRelationType:
    contact_relation_type: Optional[ContactRelationType] = field(
        default=None,
        metadata={
            "name": "ContactRelationType",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ListOfUserRole:
    user_role: List[UserRole] = field(
        default_factory=list,
        metadata={
            "name": "UserRole",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class PersonTimezone:
    timezone: Optional[Timezone] = field(
        default=None,
        metadata={
            "name": "Timezone",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class UserAdministration:
    validity_dates: Optional[ValidityDates] = field(
        default=None,
        metadata={
            "name": "ValidityDates",
            "type": "Element",
        }
    )
    user_status: Optional[UserStatus] = field(
        default=None,
        metadata={
            "name": "UserStatus",
            "type": "Element",
        }
    )


@dataclass
class ListOfCommunicationDetail:
    communication_detail: List[CommunicationDetail] = field(
        default_factory=list,
        metadata={
            "name": "CommunicationDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class X509Certificate:
    list_of_certificate_purpose: List[ListOfCertificatePurpose] = field(
        default_factory=list,
        metadata={
            "name": "ListOfCertificatePurpose",
            "type": "Element",
        }
    )
    x509_cert: Optional[str] = field(
        default=None,
        metadata={
            "name": "X509Cert",
            "type": "Element",
            "required": True,
        }
    )
    x509_certificate_info: Optional[X509CertificateInfo] = field(
        default=None,
        metadata={
            "name": "X509CertificateInfo",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ListOfX509Certificate:
    x509_certificate: List[X509Certificate] = field(
        default_factory=list,
        metadata={
            "name": "X509Certificate",
            "type": "Element",
        }
    )


@dataclass
class PersonAddress:
    organization_address_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrganizationAddressID",
            "type": "Element",
            "required": True,
        }
    )
    pobox: Optional[Pobox] = field(
        default=None,
        metadata={
            "name": "POBox",
            "type": "Element",
        }
    )
    street: Optional[str] = field(
        default=None,
        metadata={
            "name": "Street",
            "type": "Element",
        }
    )
    house_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "HouseNumber",
            "type": "Element",
        }
    )
    street_supplement1: Optional[str] = field(
        default=None,
        metadata={
            "name": "StreetSupplement1",
            "type": "Element",
        }
    )
    street_supplement2: Optional[str] = field(
        default=None,
        metadata={
            "name": "StreetSupplement2",
            "type": "Element",
        }
    )
    postal_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PostalCode",
            "type": "Element",
        }
    )
    city: Optional[str] = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Element",
            "required": True,
        }
    )
    county: Optional[str] = field(
        default=None,
        metadata={
            "name": "County",
            "type": "Element",
        }
    )
    region: Optional[Region] = field(
        default=None,
        metadata={
            "name": "Region",
            "type": "Element",
        }
    )
    district: Optional[str] = field(
        default=None,
        metadata={
            "name": "District",
            "type": "Element",
        }
    )
    country: Optional[Country] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "required": True,
        }
    )
    building: Optional[str] = field(
        default=None,
        metadata={
            "name": "Building",
            "type": "Element",
        }
    )
    floor: Optional[str] = field(
        default=None,
        metadata={
            "name": "Floor",
            "type": "Element",
        }
    )
    room_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "RoomNumber",
            "type": "Element",
        }
    )
    inhouse_mail: Optional[str] = field(
        default=None,
        metadata={
            "name": "InhouseMail",
            "type": "Element",
        }
    )
    department: Optional[str] = field(
        default=None,
        metadata={
            "name": "Department",
            "type": "Element",
        }
    )
    list_of_communication_detail: Optional[ListOfCommunicationDetail] = field(
        default=None,
        metadata={
            "name": "ListOfCommunicationDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PersonProfile:
    title: Optional[Title] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Element",
        }
    )
    academic_title: Optional[AcademicTitle] = field(
        default=None,
        metadata={
            "name": "AcademicTitle",
            "type": "Element",
        }
    )
    last_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastName",
            "type": "Element",
            "required": True,
        }
    )
    first_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "FirstName",
            "type": "Element",
        }
    )
    middle_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "MiddleName",
            "type": "Element",
        }
    )
    full_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "FullName",
            "type": "Element",
        }
    )
    correspondence_language: Optional[CorrespondenceLanguage] = field(
        default=None,
        metadata={
            "name": "CorrespondenceLanguage",
            "type": "Element",
        }
    )
    number_format: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumberFormat",
            "type": "Element",
        }
    )
    date_format: Optional[DateFormat] = field(
        default=None,
        metadata={
            "name": "DateFormat",
            "type": "Element",
        }
    )
    time_format: Optional[str] = field(
        default=None,
        metadata={
            "name": "TimeFormat",
            "type": "Element",
        }
    )
    person_timezone: Optional[PersonTimezone] = field(
        default=None,
        metadata={
            "name": "PersonTimezone",
            "type": "Element",
        }
    )
    list_of_x509_certificate: Optional[ListOfX509Certificate] = field(
        default=None,
        metadata={
            "name": "ListOfX509Certificate",
            "type": "Element",
        }
    )
    person_address: Optional[PersonAddress] = field(
        default=None,
        metadata={
            "name": "PersonAddress",
            "type": "Element",
            "required": True,
        }
    )
    general_notes: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeneralNotes",
            "type": "Element",
        }
    )


@dataclass
class TradingPartnerUser:
    trading_partner_organization_reference: Optional[TradingPartnerOrganizationReference] = field(
        default=None,
        metadata={
            "name": "TradingPartnerOrganizationReference",
            "type": "Element",
            "required": True,
        }
    )
    user_id: Optional[UserId] = field(
        default=None,
        metadata={
            "name": "UserID",
            "type": "Element",
            "required": True,
        }
    )
    person_profile: Optional[PersonProfile] = field(
        default=None,
        metadata={
            "name": "PersonProfile",
            "type": "Element",
            "required": True,
        }
    )
    list_of_user_role: Optional[ListOfUserRole] = field(
        default=None,
        metadata={
            "name": "ListOfUserRole",
            "type": "Element",
        }
    )
    user_administration: Optional[UserAdministration] = field(
        default=None,
        metadata={
            "name": "UserAdministration",
            "type": "Element",
        }
    )
    list_of_contact_relation_type: Optional[ListOfContactRelationType] = field(
        default=None,
        metadata={
            "name": "ListOfContactRelationType",
            "type": "Element",
        }
    )


@dataclass
class ListOfTradingPartnerUser:
    trading_partner_user: List[TradingPartnerUser] = field(
        default_factory=list,
        metadata={
            "name": "TradingPartnerUser",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class TradingPartnerUserInformation:
    trading_partner_user_purpose: Optional[TradingPartnerUserPurpose] = field(
        default=None,
        metadata={
            "name": "TradingPartnerUserPurpose",
            "type": "Element",
            "required": True,
        }
    )
    list_of_trading_partner_user: Optional[ListOfTradingPartnerUser] = field(
        default=None,
        metadata={
            "name": "ListOfTradingPartnerUser",
            "type": "Element",
            "required": True,
        }
    )
