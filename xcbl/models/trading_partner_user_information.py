from dataclasses import dataclass, field
from typing import List, Optional


@dataclass(kw_only=True)
class AcademicTitle:
    academic_title_coded: str = field(
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


@dataclass(kw_only=True)
class Agency:
    agency_coded: str = field(
        metadata={
            "name": "AgencyCoded",
            "type": "Element",
            "required": True,
        }
    )
    agency_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgencyCodedOther",
            "type": "Element",
        }
    )
    agency_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgencyDescription",
            "type": "Element",
        }
    )
    code_list_identifier_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodeListIdentifierCoded",
            "type": "Element",
        }
    )
    code_list_identifier_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodeListIdentifierCodedOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class CertificatePurpose:
    certificate_purpose_coded: str = field(
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


@dataclass(kw_only=True)
class ContactRelationType:
    contact_relation_type_coded: str = field(
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


@dataclass(kw_only=True)
class Country:
    country_coded: str = field(
        metadata={
            "name": "CountryCoded",
            "type": "Element",
            "required": True,
        }
    )
    country_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "CountryCodedOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class DateFormat:
    date_format_coded: str = field(
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


@dataclass(kw_only=True)
class Language:
    language_dependent: Optional[str] = field(
        default=None,
        metadata={
            "name": "LanguageDependent",
            "type": "Attribute",
        }
    )
    language_coded: str = field(
        metadata={
            "name": "LanguageCoded",
            "type": "Element",
            "required": True,
        }
    )
    language_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "LanguageCodedOther",
            "type": "Element",
        }
    )
    locale_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocaleCoded",
            "type": "Element",
        }
    )
    locale_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocaleCodedOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Pobox:
    class Meta:
        name = "POBox"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    pobox_postal_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "POBoxPostalCode",
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class PersonCommunicationType:
    person_communication_type_coded: str = field(
        metadata={
            "name": "PersonCommunicationTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    person_communication_type_coded_other: str = field(
        metadata={
            "name": "PersonCommunicationTypeCodedOther",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Region:
    region_coded: str = field(
        metadata={
            "name": "RegionCoded",
            "type": "Element",
            "required": True,
        }
    )
    region_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegionCodedOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Timezone:
    timezone_coded: str = field(
        metadata={
            "name": "TimezoneCoded",
            "type": "Element",
            "required": True,
        }
    )
    timezone_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "TimezoneCodedOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Title:
    title_coded: str = field(
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


@dataclass(kw_only=True)
class TradingPartnerUserPurpose:
    trading_partner_user_purpose_coded: str = field(
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


@dataclass(kw_only=True)
class UserId:
    class Meta:
        name = "UserID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    user_short_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "UserShortID",
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class UserRole:
    user_role_authority: Optional[str] = field(
        default=None,
        metadata={
            "name": "UserRoleAuthority",
            "type": "Element",
        }
    )
    user_role_name: str = field(
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


@dataclass(kw_only=True)
class UserStatus:
    user_status_coded: str = field(
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


@dataclass(kw_only=True)
class ValidityDates:
    start_date: str = field(
        metadata={
            "name": "StartDate",
            "type": "Element",
            "required": True,
        }
    )
    end_date: str = field(
        metadata={
            "name": "EndDate",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class X509CertificateInfo:
    x509_subject: str = field(
        metadata={
            "name": "X509Subject",
            "type": "Element",
            "required": True,
        }
    )
    x509_issuer: str = field(
        metadata={
            "name": "X509Issuer",
            "type": "Element",
            "required": True,
        }
    )
    x509_serial_number: str = field(
        metadata={
            "name": "X509SerialNumber",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class CommunicationDetail:
    communication_detail_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "CommunicationDetailDescription",
            "type": "Element",
        }
    )
    person_communication_type: PersonCommunicationType = field(
        metadata={
            "name": "PersonCommunicationType",
            "type": "Element",
            "required": True,
        }
    )
    communication_value: str = field(
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


@dataclass(kw_only=True)
class CorrespondenceLanguage:
    language: Language = field(
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Identifier:
    agency: Agency = field(
        metadata={
            "name": "Agency",
            "type": "Element",
            "required": True,
        }
    )
    ident: str = field(
        metadata={
            "name": "Ident",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfCertificatePurpose:
    certificate_purpose: List[CertificatePurpose] = field(
        default_factory=list,
        metadata={
            "name": "CertificatePurpose",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ListOfContactRelationType:
    contact_relation_type: ContactRelationType = field(
        metadata={
            "name": "ContactRelationType",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfUserRole:
    user_role: List[UserRole] = field(
        default_factory=list,
        metadata={
            "name": "UserRole",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class PersonTimezone:
    timezone: Timezone = field(
        metadata={
            "name": "Timezone",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PrimaryId:
    class Meta:
        name = "PrimaryID"

    agency: Agency = field(
        metadata={
            "name": "Agency",
            "type": "Element",
            "required": True,
        }
    )
    ident: str = field(
        metadata={
            "name": "Ident",
            "type": "Element",
            "required": True,
        }
    )
    short_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShortID",
            "type": "Element",
        }
    )
    primary_idurn: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrimaryIDURN",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
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


@dataclass(kw_only=True)
class ListOfCommunicationDetail:
    communication_detail: List[CommunicationDetail] = field(
        default_factory=list,
        metadata={
            "name": "CommunicationDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class TradingPartnerId:
    class Meta:
        name = "TradingPartnerID"

    identifier: Identifier = field(
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
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
        }
    )
    x509_certificate_info: Optional[X509CertificateInfo] = field(
        default=None,
        metadata={
            "name": "X509CertificateInfo",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ListOfTradingPartnerId:
    class Meta:
        name = "ListOfTradingPartnerID"

    trading_partner_id: List[TradingPartnerId] = field(
        default_factory=list,
        metadata={
            "name": "TradingPartnerID",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfX509Certificate:
    x509_certificate: List[X509Certificate] = field(
        default_factory=list,
        metadata={
            "name": "X509Certificate",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class PersonAddress:
    organization_address_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrganizationAddressID",
            "type": "Element",
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
    list_of_communication_detail: ListOfCommunicationDetail = field(
        metadata={
            "name": "ListOfCommunicationDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Identifications:
    primary_id: Optional[PrimaryId] = field(
        default=None,
        metadata={
            "name": "PrimaryID",
            "type": "Element",
        }
    )
    list_of_trading_partner_id: Optional[ListOfTradingPartnerId] = field(
        default=None,
        metadata={
            "name": "ListOfTradingPartnerID",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
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
    last_name: str = field(
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
    person_address: PersonAddress = field(
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


@dataclass(kw_only=True)
class TradingPartnerOrganizationReference:
    identifications: Identifications = field(
        metadata={
            "name": "Identifications",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TradingPartnerUser:
    trading_partner_organization_reference: TradingPartnerOrganizationReference = field(
        metadata={
            "name": "TradingPartnerOrganizationReference",
            "type": "Element",
            "required": True,
        }
    )
    user_id: UserId = field(
        metadata={
            "name": "UserID",
            "type": "Element",
            "required": True,
        }
    )
    person_profile: PersonProfile = field(
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


@dataclass(kw_only=True)
class ListOfTradingPartnerUser:
    trading_partner_user: List[TradingPartnerUser] = field(
        default_factory=list,
        metadata={
            "name": "TradingPartnerUser",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class TradingPartnerUserInformation:
    trading_partner_user_purpose: TradingPartnerUserPurpose = field(
        metadata={
            "name": "TradingPartnerUserPurpose",
            "type": "Element",
            "required": True,
        }
    )
    list_of_trading_partner_user: ListOfTradingPartnerUser = field(
        metadata={
            "name": "ListOfTradingPartnerUser",
            "type": "Element",
            "required": True,
        }
    )
