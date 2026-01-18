from __future__ import annotations

from dataclasses import dataclass, field

from xcbl.models.trading_partner_user_information import (
    City,
    Country,
    County,
    District,
    GeneralNotes,
    HouseNumber,
    Identifications,
    Language,
    Pobox,
    PostalCode,
    Region,
    Street,
    StreetSupplement1,
    StreetSupplement2,
    Timezone,
    ValidityDates,
)


@dataclass(kw_only=True)
class AddressTypeCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AddressTypeCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class BankAccountControlKey:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class BankAccountNumber:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class BankKey:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class BankReference:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CurrencyCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CurrencyCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ExternalAddressId:
    class Meta:
        name = "ExternalAddressID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class InternationalBankAccountNumber:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Swiftcode:
    class Meta:
        name = "SWIFTCode"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TradingPartnerAccountHolder:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TradingPartnerDisplayName:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TradingPartnerOrganizationPurposeCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TradingPartnerOrganizationPurposeCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TradingPartnerOrganizationVisibilityCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TradingPartnerOrganizationVisibilityCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TradingPartnerTypeCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TradingPartnerTypeCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Name12:
    class Meta:
        name = "name1"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Name22:
    class Meta:
        name = "name2"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Name32:
    class Meta:
        name = "name3"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AddressType:
    address_type_coded: AddressTypeCoded = field(
        metadata={
            "name": "AddressTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    address_type_coded_other: AddressTypeCodedOther | None = field(
        default=None,
        metadata={
            "name": "AddressTypeCodedOther",
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
class Currency:
    currency_coded: CurrencyCoded = field(
        metadata={
            "name": "CurrencyCoded",
            "type": "Element",
            "required": True,
        }
    )
    currency_coded_other: CurrencyCodedOther | None = field(
        default=None,
        metadata={
            "name": "CurrencyCodedOther",
            "type": "Element",
        },
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
class TradingPartnerOrganizationPurpose:
    trading_partner_organization_purpose_coded: TradingPartnerOrganizationPurposeCoded = field(
        metadata={
            "name": "TradingPartnerOrganizationPurposeCoded",
            "type": "Element",
            "required": True,
        }
    )
    trading_partner_organization_purpose_coded_other: (
        TradingPartnerOrganizationPurposeCodedOther | None
    ) = field(
        default=None,
        metadata={
            "name": "TradingPartnerOrganizationPurposeCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class TradingPartnerOrganizationVisibility:
    trading_partner_organization_visibility_coded: TradingPartnerOrganizationVisibilityCoded = field(
        metadata={
            "name": "TradingPartnerOrganizationVisibilityCoded",
            "type": "Element",
            "required": True,
        }
    )
    trading_partner_organization_visibility_coded_other: (
        TradingPartnerOrganizationVisibilityCodedOther | None
    ) = field(
        default=None,
        metadata={
            "name": "TradingPartnerOrganizationVisibilityCodedOther",
            "type": "Element",
        },
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
class TradingPartnerType:
    trading_partner_type_coded: TradingPartnerTypeCoded = field(
        metadata={
            "name": "TradingPartnerTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    trading_partner_type_coded_other: TradingPartnerTypeCodedOther | None = (
        field(
            default=None,
            metadata={
                "name": "TradingPartnerTypeCodedOther",
                "type": "Element",
            },
        )
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
    bank_key: BankKey | None = field(
        default=None,
        metadata={
            "name": "BankKey",
            "type": "Element",
        },
    )
    swiftcode: Swiftcode | None = field(
        default=None,
        metadata={
            "name": "SWIFTCode",
            "type": "Element",
        },
    )
    bank_account_number: BankAccountNumber = field(
        metadata={
            "name": "BankAccountNumber",
            "type": "Element",
            "required": True,
        }
    )
    international_bank_account_number: (
        InternationalBankAccountNumber | None
    ) = field(
        default=None,
        metadata={
            "name": "InternationalBankAccountNumber",
            "type": "Element",
        },
    )
    trading_partner_account_holder: TradingPartnerAccountHolder | None = field(
        default=None,
        metadata={
            "name": "TradingPartnerAccountHolder",
            "type": "Element",
        },
    )
    bank_account_control_key: BankAccountControlKey | None = field(
        default=None,
        metadata={
            "name": "BankAccountControlKey",
            "type": "Element",
        },
    )
    bank_reference: BankReference | None = field(
        default=None,
        metadata={
            "name": "BankReference",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfTradingPartnerType:
    trading_partner_type: list[TradingPartnerType] = field(
        default_factory=list,
        metadata={
            "name": "TradingPartnerType",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class OrganizationAddress:
    address_type: AddressType | None = field(
        default=None,
        metadata={
            "name": "AddressType",
            "type": "Element",
        },
    )
    external_address_id: ExternalAddressId = field(
        metadata={
            "name": "ExternalAddressID",
            "type": "Element",
            "required": True,
        }
    )
    pobox: Pobox | None = field(
        default=None,
        metadata={
            "name": "POBox",
            "type": "Element",
        },
    )
    street: Street | None = field(
        default=None,
        metadata={
            "name": "Street",
            "type": "Element",
        },
    )
    house_number: HouseNumber | None = field(
        default=None,
        metadata={
            "name": "HouseNumber",
            "type": "Element",
        },
    )
    street_supplement1: StreetSupplement1 | None = field(
        default=None,
        metadata={
            "name": "StreetSupplement1",
            "type": "Element",
        },
    )
    street_supplement2: StreetSupplement2 | None = field(
        default=None,
        metadata={
            "name": "StreetSupplement2",
            "type": "Element",
        },
    )
    postal_code: PostalCode | None = field(
        default=None,
        metadata={
            "name": "PostalCode",
            "type": "Element",
        },
    )
    city: City = field(
        metadata={
            "name": "City",
            "type": "Element",
            "required": True,
        }
    )
    county: County | None = field(
        default=None,
        metadata={
            "name": "County",
            "type": "Element",
        },
    )
    region: Region | None = field(
        default=None,
        metadata={
            "name": "Region",
            "type": "Element",
        },
    )
    district: District | None = field(
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
    trading_partner_timezone: TradingPartnerTimezone | None = field(
        default=None,
        metadata={
            "name": "TradingPartnerTimezone",
            "type": "Element",
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
    organization_address: list[OrganizationAddress] = field(
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
class TradingPartnerOrganizationHeader:
    validity_dates: ValidityDates | None = field(
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
    trading_partner_display_name: TradingPartnerDisplayName = field(
        metadata={
            "name": "TradingPartnerDisplayName",
            "type": "Element",
            "required": True,
        }
    )
    name1: Name12 = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    name2: Name22 | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    name3: Name32 | None = field(
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
    parent_trading_partner_identifications: (
        ParentTradingPartnerIdentifications | None
    ) = field(
        default=None,
        metadata={
            "name": "ParentTradingPartnerIdentifications",
            "type": "Element",
        },
    )
    general_notes: GeneralNotes | None = field(
        default=None,
        metadata={
            "name": "GeneralNotes",
            "type": "Element",
        },
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
    list_of_organization_address: ListOfOrganizationAddress | None = field(
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
    list_of_bank_detail: list[ListOfBankDetail] = field(
        default_factory=list,
        metadata={
            "name": "ListOfBankDetail",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfTradingPartnerOrganization:
    trading_partner_organization: list[TradingPartnerOrganization] = field(
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
