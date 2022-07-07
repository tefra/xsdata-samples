from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_create import (
    Country,
    Currency,
    Language,
    Pobox,
    Region,
    Timezone,
    ValidityDates,
)
from xcbl.models.trading_partner_organization_delete import (
    Identifications,
    TradingPartnerIdentifications,
)


@dataclass
class AddressType:
    address_type_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddressTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    address_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddressTypeCodedOther",
            "type": "Element",
        }
    )


@dataclass
class TradingPartnerOrganizationPurpose:
    trading_partner_organization_purpose_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradingPartnerOrganizationPurposeCoded",
            "type": "Element",
            "required": True,
        }
    )
    trading_partner_organization_purpose_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradingPartnerOrganizationPurposeCodedOther",
            "type": "Element",
        }
    )


@dataclass
class TradingPartnerOrganizationVisibility:
    trading_partner_organization_visibility_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradingPartnerOrganizationVisibilityCoded",
            "type": "Element",
            "required": True,
        }
    )
    trading_partner_organization_visibility_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradingPartnerOrganizationVisibilityCodedOther",
            "type": "Element",
        }
    )


@dataclass
class TradingPartnerType:
    trading_partner_type_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradingPartnerTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    trading_partner_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradingPartnerTypeCodedOther",
            "type": "Element",
        }
    )


@dataclass
class BankCountry:
    country: Optional[Country] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ListOfTradingPartnerType:
    trading_partner_type: List[TradingPartnerType] = field(
        default_factory=list,
        metadata={
            "name": "TradingPartnerType",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class OrganizationCurrency:
    currency: Optional[Currency] = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class OrganizationLanguage:
    language: Optional[Language] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ParentTradingPartnerIdentifications:
    identifications: Optional[Identifications] = field(
        default=None,
        metadata={
            "name": "Identifications",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TradingPartnerTimezone:
    timezone: Optional[Timezone] = field(
        default=None,
        metadata={
            "name": "Timezone",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class BankDetail:
    bank_country: Optional[BankCountry] = field(
        default=None,
        metadata={
            "name": "BankCountry",
            "type": "Element",
            "required": True,
        }
    )
    bank_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "BankKey",
            "type": "Element",
        }
    )
    swiftcode: Optional[str] = field(
        default=None,
        metadata={
            "name": "SWIFTCode",
            "type": "Element",
        }
    )
    bank_account_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "BankAccountNumber",
            "type": "Element",
            "required": True,
        }
    )
    international_bank_account_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "InternationalBankAccountNumber",
            "type": "Element",
        }
    )
    trading_partner_account_holder: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradingPartnerAccountHolder",
            "type": "Element",
        }
    )
    bank_account_control_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "BankAccountControlKey",
            "type": "Element",
        }
    )
    bank_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "BankReference",
            "type": "Element",
        }
    )


@dataclass
class OrganizationAddress:
    address_type: Optional[AddressType] = field(
        default=None,
        metadata={
            "name": "AddressType",
            "type": "Element",
        }
    )
    external_address_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExternalAddressID",
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
    trading_partner_timezone: Optional[TradingPartnerTimezone] = field(
        default=None,
        metadata={
            "name": "TradingPartnerTimezone",
            "type": "Element",
        }
    )


@dataclass
class TradingPartnerOrganizationHeader:
    validity_dates: Optional[ValidityDates] = field(
        default=None,
        metadata={
            "name": "ValidityDates",
            "type": "Element",
        }
    )
    list_of_trading_partner_type: Optional[ListOfTradingPartnerType] = field(
        default=None,
        metadata={
            "name": "ListOfTradingPartnerType",
            "type": "Element",
            "required": True,
        }
    )
    trading_partner_identifications: Optional[TradingPartnerIdentifications] = field(
        default=None,
        metadata={
            "name": "TradingPartnerIdentifications",
            "type": "Element",
            "required": True,
        }
    )
    trading_partner_display_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradingPartnerDisplayName",
            "type": "Element",
            "required": True,
        }
    )
    name1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    name2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    name3: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    organization_language: Optional[OrganizationLanguage] = field(
        default=None,
        metadata={
            "name": "OrganizationLanguage",
            "type": "Element",
            "required": True,
        }
    )
    organization_currency: Optional[OrganizationCurrency] = field(
        default=None,
        metadata={
            "name": "OrganizationCurrency",
            "type": "Element",
            "required": True,
        }
    )
    trading_partner_organization_visibility: Optional[TradingPartnerOrganizationVisibility] = field(
        default=None,
        metadata={
            "name": "TradingPartnerOrganizationVisibility",
            "type": "Element",
            "required": True,
        }
    )
    parent_trading_partner_identifications: Optional[ParentTradingPartnerIdentifications] = field(
        default=None,
        metadata={
            "name": "ParentTradingPartnerIdentifications",
            "type": "Element",
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
class ListOfBankDetail:
    bank_detail: Optional[BankDetail] = field(
        default=None,
        metadata={
            "name": "BankDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ListOfOrganizationAddress:
    organization_address: List[OrganizationAddress] = field(
        default_factory=list,
        metadata={
            "name": "OrganizationAddress",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class PrimaryOrganizationAddress:
    organization_address: Optional[OrganizationAddress] = field(
        default=None,
        metadata={
            "name": "OrganizationAddress",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class OrganizationAddresses:
    primary_organization_address: Optional[PrimaryOrganizationAddress] = field(
        default=None,
        metadata={
            "name": "PrimaryOrganizationAddress",
            "type": "Element",
            "required": True,
        }
    )
    list_of_organization_address: Optional[ListOfOrganizationAddress] = field(
        default=None,
        metadata={
            "name": "ListOfOrganizationAddress",
            "type": "Element",
        }
    )


@dataclass
class TradingPartnerOrganization:
    trading_partner_organization_header: Optional[TradingPartnerOrganizationHeader] = field(
        default=None,
        metadata={
            "name": "TradingPartnerOrganizationHeader",
            "type": "Element",
            "required": True,
        }
    )
    organization_addresses: Optional[OrganizationAddresses] = field(
        default=None,
        metadata={
            "name": "OrganizationAddresses",
            "type": "Element",
            "required": True,
        }
    )
    list_of_bank_detail: List[ListOfBankDetail] = field(
        default_factory=list,
        metadata={
            "name": "ListOfBankDetail",
            "type": "Element",
        }
    )


@dataclass
class ListOfTradingPartnerOrganization:
    trading_partner_organization: List[TradingPartnerOrganization] = field(
        default_factory=list,
        metadata={
            "name": "TradingPartnerOrganization",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class TradingPartnerOrganizationInformation:
    trading_partner_organization_purpose: Optional[TradingPartnerOrganizationPurpose] = field(
        default=None,
        metadata={
            "name": "TradingPartnerOrganizationPurpose",
            "type": "Element",
            "required": True,
        }
    )
    list_of_trading_partner_organization: Optional[ListOfTradingPartnerOrganization] = field(
        default=None,
        metadata={
            "name": "ListOfTradingPartnerOrganization",
            "type": "Element",
            "required": True,
        }
    )
