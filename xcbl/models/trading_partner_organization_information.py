from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.trading_partner_user_information import (
    Country,
    Identifications,
    Language,
    Pobox,
    Region,
    Timezone,
    ValidityDates,
)


@dataclass(kw_only=True)
class AddressType:
    address_type_coded: str = field(
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
        },
    )


@dataclass(kw_only=True)
class Currency:
    currency_coded: str = field(
        metadata={
            "name": "CurrencyCoded",
            "type": "Element",
            "required": True,
        }
    )
    currency_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "CurrencyCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class TradingPartnerOrganizationPurpose:
    trading_partner_organization_purpose_coded: str = field(
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
        },
    )


@dataclass(kw_only=True)
class TradingPartnerOrganizationVisibility:
    trading_partner_organization_visibility_coded: str = field(
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
        },
    )


@dataclass(kw_only=True)
class TradingPartnerType:
    trading_partner_type_coded: str = field(
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
        },
    )


@dataclass(kw_only=True)
class BankCountry:
    country: Country = field(
        metadata={
            "name": "Country",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfTradingPartnerType:
    trading_partner_type: List[TradingPartnerType] = field(
        default_factory=list,
        metadata={
            "name": "TradingPartnerType",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class OrganizationCurrency:
    currency: Currency = field(
        metadata={
            "name": "Currency",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrganizationLanguage:
    language: Language = field(
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ParentTradingPartnerIdentifications:
    identifications: Identifications = field(
        metadata={
            "name": "Identifications",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TradingPartnerIdentifications:
    identifications: Identifications = field(
        metadata={
            "name": "Identifications",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TradingPartnerTimezone:
    timezone: Timezone = field(
        metadata={
            "name": "Timezone",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class BankDetail:
    bank_country: BankCountry = field(
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
        },
    )
    swiftcode: Optional[str] = field(
        default=None,
        metadata={
            "name": "SWIFTCode",
            "type": "Element",
        },
    )
    bank_account_number: str = field(
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
        },
    )
    trading_partner_account_holder: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradingPartnerAccountHolder",
            "type": "Element",
        },
    )
    bank_account_control_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "BankAccountControlKey",
            "type": "Element",
        },
    )
    bank_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "BankReference",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class OrganizationAddress:
    address_type: Optional[AddressType] = field(
        default=None,
        metadata={
            "name": "AddressType",
            "type": "Element",
        },
    )
    external_address_id: str = field(
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
        },
    )
    street: Optional[str] = field(
        default=None,
        metadata={
            "name": "Street",
            "type": "Element",
        },
    )
    house_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "HouseNumber",
            "type": "Element",
        },
    )
    street_supplement1: Optional[str] = field(
        default=None,
        metadata={
            "name": "StreetSupplement1",
            "type": "Element",
        },
    )
    street_supplement2: Optional[str] = field(
        default=None,
        metadata={
            "name": "StreetSupplement2",
            "type": "Element",
        },
    )
    postal_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PostalCode",
            "type": "Element",
        },
    )
    city: str = field(
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
        },
    )
    region: Optional[Region] = field(
        default=None,
        metadata={
            "name": "Region",
            "type": "Element",
        },
    )
    district: Optional[str] = field(
        default=None,
        metadata={
            "name": "District",
            "type": "Element",
        },
    )
    country: Country = field(
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
        },
    )


@dataclass(kw_only=True)
class TradingPartnerOrganizationHeader:
    validity_dates: Optional[ValidityDates] = field(
        default=None,
        metadata={
            "name": "ValidityDates",
            "type": "Element",
        },
    )
    list_of_trading_partner_type: ListOfTradingPartnerType = field(
        metadata={
            "name": "ListOfTradingPartnerType",
            "type": "Element",
            "required": True,
        }
    )
    trading_partner_identifications: TradingPartnerIdentifications = field(
        metadata={
            "name": "TradingPartnerIdentifications",
            "type": "Element",
            "required": True,
        }
    )
    trading_partner_display_name: str = field(
        metadata={
            "name": "TradingPartnerDisplayName",
            "type": "Element",
            "required": True,
        }
    )
    name1: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    name2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    name3: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    organization_language: OrganizationLanguage = field(
        metadata={
            "name": "OrganizationLanguage",
            "type": "Element",
            "required": True,
        }
    )
    organization_currency: OrganizationCurrency = field(
        metadata={
            "name": "OrganizationCurrency",
            "type": "Element",
            "required": True,
        }
    )
    trading_partner_organization_visibility: TradingPartnerOrganizationVisibility = field(
        metadata={
            "name": "TradingPartnerOrganizationVisibility",
            "type": "Element",
            "required": True,
        }
    )
    parent_trading_partner_identifications: Optional[
        ParentTradingPartnerIdentifications
    ] = field(
        default=None,
        metadata={
            "name": "ParentTradingPartnerIdentifications",
            "type": "Element",
        },
    )
    general_notes: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeneralNotes",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfBankDetail:
    bank_detail: BankDetail = field(
        metadata={
            "name": "BankDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfOrganizationAddress:
    organization_address: List[OrganizationAddress] = field(
        default_factory=list,
        metadata={
            "name": "OrganizationAddress",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class PrimaryOrganizationAddress:
    organization_address: OrganizationAddress = field(
        metadata={
            "name": "OrganizationAddress",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrganizationAddresses:
    primary_organization_address: PrimaryOrganizationAddress = field(
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
        },
    )


@dataclass(kw_only=True)
class TradingPartnerOrganization:
    trading_partner_organization_header: TradingPartnerOrganizationHeader = (
        field(
            metadata={
                "name": "TradingPartnerOrganizationHeader",
                "type": "Element",
                "required": True,
            }
        )
    )
    organization_addresses: OrganizationAddresses = field(
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
        },
    )


@dataclass(kw_only=True)
class ListOfTradingPartnerOrganization:
    trading_partner_organization: List[TradingPartnerOrganization] = field(
        default_factory=list,
        metadata={
            "name": "TradingPartnerOrganization",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class TradingPartnerOrganizationInformation:
    trading_partner_organization_purpose: TradingPartnerOrganizationPurpose = (
        field(
            metadata={
                "name": "TradingPartnerOrganizationPurpose",
                "type": "Element",
                "required": True,
            }
        )
    )
    list_of_trading_partner_organization: ListOfTradingPartnerOrganization = (
        field(
            metadata={
                "name": "ListOfTradingPartnerOrganization",
                "type": "Element",
                "required": True,
            }
        )
    )
