from dataclasses import dataclass, field
from typing import Optional


@dataclass(kw_only=True)
class AcademicTitleCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AcademicTitleCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AgencyCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AgencyCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AgencyDescription:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Building:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CertificatePurposeCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CertificatePurposeCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class City:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CodeListIdentifierCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CodeListIdentifierCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CommunicationDetailDescription:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CommunicationValue:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ContactRelationTypeCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ContactRelationTypeCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CountryCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CountryCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class County:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class DateFormatCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class DateFormatCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class DefaultCommunication:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Department:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class District:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class EndDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class FirstName:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Floor:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class FullName:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class GeneralNotes:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class HouseNumber:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Ident:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class InhouseMail:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class LanguageCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class LanguageCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class LastName:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class LocaleCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class LocaleCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class MiddleName:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class NumberFormat:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class OrganizationAddressId:
    class Meta:
        name = "OrganizationAddressID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Pobox:
    class Meta:
        name = "POBox"

    pobox_postal_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "POBoxPostalCode",
            "type": "Attribute",
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PersonCommunicationTypeCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PersonCommunicationTypeCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PostalCode:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PrimaryIdurn:
    class Meta:
        name = "PrimaryIDURN"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class RegionCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class RegionCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class RoomNumber:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ShortId:
    class Meta:
        name = "ShortID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class StartDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Street:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class StreetSupplement1:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class StreetSupplement2:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TimeFormat:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TimezoneCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TimezoneCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TitleCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TitleCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TradingPartnerUserPurposeCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TradingPartnerUserPurposeCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class UserId:
    class Meta:
        name = "UserID"

    user_short_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "UserShortID",
            "type": "Attribute",
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class UserRoleAuthority:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class UserRoleId:
    class Meta:
        name = "UserRoleID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class UserRoleName:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class UserStatusCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class UserStatusCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class X509Cert:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class X509Issuer:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class X509SerialNumber:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class X509Subject:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AcademicTitle:
    academic_title_coded: AcademicTitleCoded = field(
        metadata={
            "name": "AcademicTitleCoded",
            "type": "Element",
            "required": True,
        }
    )
    academic_title_coded_other: Optional[AcademicTitleCodedOther] = field(
        default=None,
        metadata={
            "name": "AcademicTitleCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Agency:
    agency_coded: AgencyCoded = field(
        metadata={
            "name": "AgencyCoded",
            "type": "Element",
            "required": True,
        }
    )
    agency_coded_other: Optional[AgencyCodedOther] = field(
        default=None,
        metadata={
            "name": "AgencyCodedOther",
            "type": "Element",
        },
    )
    agency_description: Optional[AgencyDescription] = field(
        default=None,
        metadata={
            "name": "AgencyDescription",
            "type": "Element",
        },
    )
    code_list_identifier_coded: Optional[CodeListIdentifierCoded] = field(
        default=None,
        metadata={
            "name": "CodeListIdentifierCoded",
            "type": "Element",
        },
    )
    code_list_identifier_coded_other: Optional[
        CodeListIdentifierCodedOther
    ] = field(
        default=None,
        metadata={
            "name": "CodeListIdentifierCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class CertificatePurpose:
    certificate_purpose_coded: CertificatePurposeCoded = field(
        metadata={
            "name": "CertificatePurposeCoded",
            "type": "Element",
            "required": True,
        }
    )
    certificate_purpose_coded_other: Optional[CertificatePurposeCodedOther] = (
        field(
            default=None,
            metadata={
                "name": "CertificatePurposeCodedOther",
                "type": "Element",
            },
        )
    )


@dataclass(kw_only=True)
class ContactRelationType:
    contact_relation_type_coded: ContactRelationTypeCoded = field(
        metadata={
            "name": "ContactRelationTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    contact_relation_type_coded_other: Optional[
        ContactRelationTypeCodedOther
    ] = field(
        default=None,
        metadata={
            "name": "ContactRelationTypeCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Country:
    country_coded: CountryCoded = field(
        metadata={
            "name": "CountryCoded",
            "type": "Element",
            "required": True,
        }
    )
    country_coded_other: Optional[CountryCodedOther] = field(
        default=None,
        metadata={
            "name": "CountryCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class DateFormat:
    date_format_coded: DateFormatCoded = field(
        metadata={
            "name": "DateFormatCoded",
            "type": "Element",
            "required": True,
        }
    )
    date_format_coded_other: Optional[DateFormatCodedOther] = field(
        default=None,
        metadata={
            "name": "DateFormatCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Language:
    language_dependent: Optional[str] = field(
        default=None,
        metadata={
            "name": "LanguageDependent",
            "type": "Attribute",
        },
    )
    language_coded: LanguageCoded = field(
        metadata={
            "name": "LanguageCoded",
            "type": "Element",
            "required": True,
        }
    )
    language_coded_other: Optional[LanguageCodedOther] = field(
        default=None,
        metadata={
            "name": "LanguageCodedOther",
            "type": "Element",
        },
    )
    locale_coded: Optional[LocaleCoded] = field(
        default=None,
        metadata={
            "name": "LocaleCoded",
            "type": "Element",
        },
    )
    locale_coded_other: Optional[LocaleCodedOther] = field(
        default=None,
        metadata={
            "name": "LocaleCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class PersonCommunicationType:
    person_communication_type_coded: PersonCommunicationTypeCoded = field(
        metadata={
            "name": "PersonCommunicationTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    person_communication_type_coded_other: PersonCommunicationTypeCodedOther = field(
        metadata={
            "name": "PersonCommunicationTypeCodedOther",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Region:
    region_coded: RegionCoded = field(
        metadata={
            "name": "RegionCoded",
            "type": "Element",
            "required": True,
        }
    )
    region_coded_other: Optional[RegionCodedOther] = field(
        default=None,
        metadata={
            "name": "RegionCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Timezone:
    timezone_coded: TimezoneCoded = field(
        metadata={
            "name": "TimezoneCoded",
            "type": "Element",
            "required": True,
        }
    )
    timezone_coded_other: Optional[TimezoneCodedOther] = field(
        default=None,
        metadata={
            "name": "TimezoneCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Title:
    title_coded: TitleCoded = field(
        metadata={
            "name": "TitleCoded",
            "type": "Element",
            "required": True,
        }
    )
    title_coded_other: Optional[TitleCodedOther] = field(
        default=None,
        metadata={
            "name": "TitleCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class TradingPartnerUserPurpose:
    trading_partner_user_purpose_coded: TradingPartnerUserPurposeCoded = field(
        metadata={
            "name": "TradingPartnerUserPurposeCoded",
            "type": "Element",
            "required": True,
        }
    )
    trading_partner_user_purpose_coded_other: Optional[
        TradingPartnerUserPurposeCodedOther
    ] = field(
        default=None,
        metadata={
            "name": "TradingPartnerUserPurposeCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class UserRole:
    user_role_authority: Optional[UserRoleAuthority] = field(
        default=None,
        metadata={
            "name": "UserRoleAuthority",
            "type": "Element",
        },
    )
    user_role_name: UserRoleName = field(
        metadata={
            "name": "UserRoleName",
            "type": "Element",
            "required": True,
        }
    )
    user_role_id: Optional[UserRoleId] = field(
        default=None,
        metadata={
            "name": "UserRoleID",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class UserStatus:
    user_status_coded: UserStatusCoded = field(
        metadata={
            "name": "UserStatusCoded",
            "type": "Element",
            "required": True,
        }
    )
    user_status_coded_other: Optional[UserStatusCodedOther] = field(
        default=None,
        metadata={
            "name": "UserStatusCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ValidityDates:
    start_date: StartDate = field(
        metadata={
            "name": "StartDate",
            "type": "Element",
            "required": True,
        }
    )
    end_date: EndDate = field(
        metadata={
            "name": "EndDate",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class X509CertificateInfo:
    x509_subject: X509Subject = field(
        metadata={
            "name": "X509Subject",
            "type": "Element",
            "required": True,
        }
    )
    x509_issuer: X509Issuer = field(
        metadata={
            "name": "X509Issuer",
            "type": "Element",
            "required": True,
        }
    )
    x509_serial_number: X509SerialNumber = field(
        metadata={
            "name": "X509SerialNumber",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class CommunicationDetail:
    communication_detail_description: Optional[
        CommunicationDetailDescription
    ] = field(
        default=None,
        metadata={
            "name": "CommunicationDetailDescription",
            "type": "Element",
        },
    )
    person_communication_type: PersonCommunicationType = field(
        metadata={
            "name": "PersonCommunicationType",
            "type": "Element",
            "required": True,
        }
    )
    communication_value: CommunicationValue = field(
        metadata={
            "name": "CommunicationValue",
            "type": "Element",
            "required": True,
        }
    )
    default_communication: Optional[DefaultCommunication] = field(
        default=None,
        metadata={
            "name": "DefaultCommunication",
            "type": "Element",
        },
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
    ident: Ident = field(
        metadata={
            "name": "Ident",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfCertificatePurpose:
    certificate_purpose: list[CertificatePurpose] = field(
        default_factory=list,
        metadata={
            "name": "CertificatePurpose",
            "type": "Element",
        },
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
    user_role: list[UserRole] = field(
        default_factory=list,
        metadata={
            "name": "UserRole",
            "type": "Element",
            "min_occurs": 1,
        },
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
    ident: Ident = field(
        metadata={
            "name": "Ident",
            "type": "Element",
            "required": True,
        }
    )
    short_id: Optional[ShortId] = field(
        default=None,
        metadata={
            "name": "ShortID",
            "type": "Element",
        },
    )
    primary_idurn: Optional[PrimaryIdurn] = field(
        default=None,
        metadata={
            "name": "PrimaryIDURN",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class UserAdministration:
    validity_dates: Optional[ValidityDates] = field(
        default=None,
        metadata={
            "name": "ValidityDates",
            "type": "Element",
        },
    )
    user_status: Optional[UserStatus] = field(
        default=None,
        metadata={
            "name": "UserStatus",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfCommunicationDetail:
    communication_detail: list[CommunicationDetail] = field(
        default_factory=list,
        metadata={
            "name": "CommunicationDetail",
            "type": "Element",
            "min_occurs": 1,
        },
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
    list_of_certificate_purpose: list[ListOfCertificatePurpose] = field(
        default_factory=list,
        metadata={
            "name": "ListOfCertificatePurpose",
            "type": "Element",
        },
    )
    x509_cert: Optional[X509Cert] = field(
        default=None,
        metadata={
            "name": "X509Cert",
            "type": "Element",
        },
    )
    x509_certificate_info: Optional[X509CertificateInfo] = field(
        default=None,
        metadata={
            "name": "X509CertificateInfo",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfTradingPartnerId:
    class Meta:
        name = "ListOfTradingPartnerID"

    trading_partner_id: list[TradingPartnerId] = field(
        default_factory=list,
        metadata={
            "name": "TradingPartnerID",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ListOfX509Certificate:
    x509_certificate: list[X509Certificate] = field(
        default_factory=list,
        metadata={
            "name": "X509Certificate",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class PersonAddress:
    organization_address_id: Optional[OrganizationAddressId] = field(
        default=None,
        metadata={
            "name": "OrganizationAddressID",
            "type": "Element",
        },
    )
    pobox: Optional[Pobox] = field(
        default=None,
        metadata={
            "name": "POBox",
            "type": "Element",
        },
    )
    street: Optional[Street] = field(
        default=None,
        metadata={
            "name": "Street",
            "type": "Element",
        },
    )
    house_number: Optional[HouseNumber] = field(
        default=None,
        metadata={
            "name": "HouseNumber",
            "type": "Element",
        },
    )
    street_supplement1: Optional[StreetSupplement1] = field(
        default=None,
        metadata={
            "name": "StreetSupplement1",
            "type": "Element",
        },
    )
    street_supplement2: Optional[StreetSupplement2] = field(
        default=None,
        metadata={
            "name": "StreetSupplement2",
            "type": "Element",
        },
    )
    postal_code: Optional[PostalCode] = field(
        default=None,
        metadata={
            "name": "PostalCode",
            "type": "Element",
        },
    )
    city: Optional[City] = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Element",
        },
    )
    county: Optional[County] = field(
        default=None,
        metadata={
            "name": "County",
            "type": "Element",
        },
    )
    region: Optional[Region] = field(
        default=None,
        metadata={
            "name": "Region",
            "type": "Element",
        },
    )
    district: Optional[District] = field(
        default=None,
        metadata={
            "name": "District",
            "type": "Element",
        },
    )
    country: Optional[Country] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
        },
    )
    building: Optional[Building] = field(
        default=None,
        metadata={
            "name": "Building",
            "type": "Element",
        },
    )
    floor: Optional[Floor] = field(
        default=None,
        metadata={
            "name": "Floor",
            "type": "Element",
        },
    )
    room_number: Optional[RoomNumber] = field(
        default=None,
        metadata={
            "name": "RoomNumber",
            "type": "Element",
        },
    )
    inhouse_mail: Optional[InhouseMail] = field(
        default=None,
        metadata={
            "name": "InhouseMail",
            "type": "Element",
        },
    )
    department: Optional[Department] = field(
        default=None,
        metadata={
            "name": "Department",
            "type": "Element",
        },
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
        },
    )
    list_of_trading_partner_id: Optional[ListOfTradingPartnerId] = field(
        default=None,
        metadata={
            "name": "ListOfTradingPartnerID",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class PersonProfile:
    title: Optional[Title] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Element",
        },
    )
    academic_title: Optional[AcademicTitle] = field(
        default=None,
        metadata={
            "name": "AcademicTitle",
            "type": "Element",
        },
    )
    last_name: LastName = field(
        metadata={
            "name": "LastName",
            "type": "Element",
            "required": True,
        }
    )
    first_name: Optional[FirstName] = field(
        default=None,
        metadata={
            "name": "FirstName",
            "type": "Element",
        },
    )
    middle_name: Optional[MiddleName] = field(
        default=None,
        metadata={
            "name": "MiddleName",
            "type": "Element",
        },
    )
    full_name: Optional[FullName] = field(
        default=None,
        metadata={
            "name": "FullName",
            "type": "Element",
        },
    )
    correspondence_language: Optional[CorrespondenceLanguage] = field(
        default=None,
        metadata={
            "name": "CorrespondenceLanguage",
            "type": "Element",
        },
    )
    number_format: Optional[NumberFormat] = field(
        default=None,
        metadata={
            "name": "NumberFormat",
            "type": "Element",
        },
    )
    date_format: Optional[DateFormat] = field(
        default=None,
        metadata={
            "name": "DateFormat",
            "type": "Element",
        },
    )
    time_format: Optional[TimeFormat] = field(
        default=None,
        metadata={
            "name": "TimeFormat",
            "type": "Element",
        },
    )
    person_timezone: Optional[PersonTimezone] = field(
        default=None,
        metadata={
            "name": "PersonTimezone",
            "type": "Element",
        },
    )
    list_of_x509_certificate: Optional[ListOfX509Certificate] = field(
        default=None,
        metadata={
            "name": "ListOfX509Certificate",
            "type": "Element",
        },
    )
    person_address: PersonAddress = field(
        metadata={
            "name": "PersonAddress",
            "type": "Element",
            "required": True,
        }
    )
    general_notes: Optional[GeneralNotes] = field(
        default=None,
        metadata={
            "name": "GeneralNotes",
            "type": "Element",
        },
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
        },
    )
    user_administration: Optional[UserAdministration] = field(
        default=None,
        metadata={
            "name": "UserAdministration",
            "type": "Element",
        },
    )
    list_of_contact_relation_type: Optional[ListOfContactRelationType] = field(
        default=None,
        metadata={
            "name": "ListOfContactRelationType",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfTradingPartnerUser:
    trading_partner_user: list[TradingPartnerUser] = field(
        default_factory=list,
        metadata={
            "name": "TradingPartnerUser",
            "type": "Element",
            "min_occurs": 1,
        },
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
