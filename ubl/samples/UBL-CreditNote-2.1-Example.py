from decimal import Decimal
from ubl.models.common.ubl_common_aggregate_components_2_1 import AccountingCustomerParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import AccountingSupplierParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import AdditionalDocumentReference
from ubl.models.common.ubl_common_aggregate_components_2_1 import AdditionalItemProperty
from ubl.models.common.ubl_common_aggregate_components_2_1 import AllowanceCharge
from ubl.models.common.ubl_common_aggregate_components_2_1 import Attachment
from ubl.models.common.ubl_common_aggregate_components_2_1 import ClassifiedTaxCategory
from ubl.models.common.ubl_common_aggregate_components_2_1 import CommodityClassification
from ubl.models.common.ubl_common_aggregate_components_2_1 import Contact
from ubl.models.common.ubl_common_aggregate_components_2_1 import ContractDocumentReference
from ubl.models.common.ubl_common_aggregate_components_2_1 import Country
from ubl.models.common.ubl_common_aggregate_components_2_1 import CreditNoteLine
from ubl.models.common.ubl_common_aggregate_components_2_1 import ExternalReference
from ubl.models.common.ubl_common_aggregate_components_2_1 import InvoicePeriod
from ubl.models.common.ubl_common_aggregate_components_2_1 import Item
from ubl.models.common.ubl_common_aggregate_components_2_1 import LegalMonetaryTotal
from ubl.models.common.ubl_common_aggregate_components_2_1 import OrderReference
from ubl.models.common.ubl_common_aggregate_components_2_1 import Party
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyLegalEntity
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyName
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyTaxScheme
from ubl.models.common.ubl_common_aggregate_components_2_1 import PayeeParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import Person
from ubl.models.common.ubl_common_aggregate_components_2_1 import PostalAddress
from ubl.models.common.ubl_common_aggregate_components_2_1 import Price
from ubl.models.common.ubl_common_aggregate_components_2_1 import RegistrationAddress
from ubl.models.common.ubl_common_aggregate_components_2_1 import SellersItemIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import StandardItemIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import TaxCategory
from ubl.models.common.ubl_common_aggregate_components_2_1 import TaxScheme
from ubl.models.common.ubl_common_aggregate_components_2_1 import TaxSubtotal
from ubl.models.common.ubl_common_aggregate_components_2_1 import TaxTotal
from ubl.models.common.ubl_common_basic_components_2_1 import AccountingCost
from ubl.models.common.ubl_common_basic_components_2_1 import AdditionalStreetName
from ubl.models.common.ubl_common_basic_components_2_1 import AllowanceChargeReason
from ubl.models.common.ubl_common_basic_components_2_1 import AllowanceTotalAmount
from ubl.models.common.ubl_common_basic_components_2_1 import Amount
from ubl.models.common.ubl_common_basic_components_2_1 import BaseAmount
from ubl.models.common.ubl_common_basic_components_2_1 import BaseQuantity
from ubl.models.common.ubl_common_basic_components_2_1 import BuildingNumber
from ubl.models.common.ubl_common_basic_components_2_1 import ChargeTotalAmount
from ubl.models.common.ubl_common_basic_components_2_1 import CityName
from ubl.models.common.ubl_common_basic_components_2_1 import CompanyId
from ubl.models.common.ubl_common_basic_components_2_1 import CountrySubentity
from ubl.models.common.ubl_common_basic_components_2_1 import CountrySubentityCode
from ubl.models.common.ubl_common_basic_components_2_1 import CreditedQuantity
from ubl.models.common.ubl_common_basic_components_2_1 import Department
from ubl.models.common.ubl_common_basic_components_2_1 import Description
from ubl.models.common.ubl_common_basic_components_2_1 import DocumentCurrencyCode
from ubl.models.common.ubl_common_basic_components_2_1 import DocumentType
from ubl.models.common.ubl_common_basic_components_2_1 import ElectronicMail
from ubl.models.common.ubl_common_basic_components_2_1 import EmbeddedDocumentBinaryObject
from ubl.models.common.ubl_common_basic_components_2_1 import EndpointId
from ubl.models.common.ubl_common_basic_components_2_1 import FamilyName
from ubl.models.common.ubl_common_basic_components_2_1 import FirstName
from ubl.models.common.ubl_common_basic_components_2_1 import Id
from ubl.models.common.ubl_common_basic_components_2_1 import IdentificationCode
from ubl.models.common.ubl_common_basic_components_2_1 import ItemClassificationCode
from ubl.models.common.ubl_common_basic_components_2_1 import JobTitle
from ubl.models.common.ubl_common_basic_components_2_1 import LineExtensionAmount
from ubl.models.common.ubl_common_basic_components_2_1 import MiddleName
from ubl.models.common.ubl_common_basic_components_2_1 import MultiplierFactorNumeric
from ubl.models.common.ubl_common_basic_components_2_1 import Name
from ubl.models.common.ubl_common_basic_components_2_1 import Note
from ubl.models.common.ubl_common_basic_components_2_1 import PayableAmount
from ubl.models.common.ubl_common_basic_components_2_1 import PayableRoundingAmount
from ubl.models.common.ubl_common_basic_components_2_1 import Percent
from ubl.models.common.ubl_common_basic_components_2_1 import PostalZone
from ubl.models.common.ubl_common_basic_components_2_1 import Postbox
from ubl.models.common.ubl_common_basic_components_2_1 import PrepaidAmount
from ubl.models.common.ubl_common_basic_components_2_1 import PriceAmount
from ubl.models.common.ubl_common_basic_components_2_1 import RegistrationName
from ubl.models.common.ubl_common_basic_components_2_1 import StreetName
from ubl.models.common.ubl_common_basic_components_2_1 import TaxAmount
from ubl.models.common.ubl_common_basic_components_2_1 import TaxExclusiveAmount
from ubl.models.common.ubl_common_basic_components_2_1 import TaxExemptionReason
from ubl.models.common.ubl_common_basic_components_2_1 import TaxExemptionReasonCode
from ubl.models.common.ubl_common_basic_components_2_1 import TaxInclusiveAmount
from ubl.models.common.ubl_common_basic_components_2_1 import TaxableAmount
from ubl.models.common.ubl_common_basic_components_2_1 import Telefax
from ubl.models.common.ubl_common_basic_components_2_1 import Telephone
from ubl.models.common.ubl_common_basic_components_2_1 import UblversionId
from ubl.models.common.ubl_common_basic_components_2_1 import Uri
from ubl.models.common.ubl_common_basic_components_2_1 import Value
from ubl.models.maindoc.ubl_credit_note_2_1 import CreditNote
from xsdata.models.datatype import XmlDate


obj = CreditNote(
    ublversion_id=UblversionId(
        value="2.1"
    ),
    id=Id(
        value="TOSL108"
    ),
    issue_date=XmlDate(2009, 12, 15),
    note=[
        Note(
            value="Ordered in our booth at the convention.",
            language_id="en"
        ),
    ],
    document_currency_code=DocumentCurrencyCode(
        value="EUR",
        list_id="ISO 4217 Alpha",
        list_agency_id="6"
    ),
    accounting_cost=AccountingCost(
        value="Project cost code 123"
    ),
    invoice_period=[
        InvoicePeriod(
            start_date=XmlDate(2009, 11, 1),
            end_date=XmlDate(2009, 11, 30)
        ),
    ],
    order_reference=OrderReference(
        id=Id(
            value="123"
        )
    ),
    contract_document_reference=[
        ContractDocumentReference(
            id=Id(
                value="Contract321"
            ),
            document_type=DocumentType(
                value="Framework agreement"
            )
        ),
    ],
    additional_document_reference=[
        AdditionalDocumentReference(
            id=Id(
                value="Doc1"
            ),
            document_type=DocumentType(
                value="Timesheet"
            ),
            attachment=Attachment(
                external_reference=ExternalReference(
                    uri=Uri(
                        value="http://www.suppliersite.eu/sheet001.html"
                    )
                )
            )
        ),
        AdditionalDocumentReference(
            id=Id(
                value="Doc2"
            ),
            document_type=DocumentType(
                value="Drawing"
            ),
            attachment=Attachment(
                embedded_document_binary_object=EmbeddedDocumentBinaryObject(
                    value=b"R0lGODlhcgGSALMAAAQCAEMmCZtuMFQxDS8b",
                    mime_code="application/pdf"
                )
            )
        ),
    ],
    accounting_supplier_party=AccountingSupplierParty(
        party=Party(
            endpoint_id=EndpointId(
                value="1234567890123",
                scheme_id="GLN",
                scheme_agency_id="9"
            ),
            party_identification=[
                PartyIdentification(
                    id=Id(
                        value="Supp123",
                        scheme_id="ZZZ"
                    )
                ),
            ],
            party_name=[
                PartyName(
                    name=Name(
                        value="Salescompany ltd."
                    )
                ),
            ],
            postal_address=PostalAddress(
                id=Id(
                    value="1231412341324",
                    scheme_id="GLN",
                    scheme_agency_id="9"
                ),
                postbox=Postbox(
                    value="5467"
                ),
                street_name=StreetName(
                    value="Main street"
                ),
                additional_street_name=AdditionalStreetName(
                    value="Suite 123"
                ),
                building_number=BuildingNumber(
                    value="1"
                ),
                department=Department(
                    value="Revenue department"
                ),
                city_name=CityName(
                    value="Big city"
                ),
                postal_zone=PostalZone(
                    value="54321"
                ),
                country_subentity_code=CountrySubentityCode(
                    value="RegionA"
                ),
                country=Country(
                    identification_code=IdentificationCode(
                        value="DK",
                        list_id="ISO3166-1",
                        list_agency_id="6"
                    )
                )
            ),
            party_tax_scheme=[
                PartyTaxScheme(
                    company_id=CompanyId(
                        value="DK12345",
                        scheme_id="DKVAT",
                        scheme_agency_id="ZZZ"
                    ),
                    tax_scheme=TaxScheme(
                        id=Id(
                            value="VAT",
                            scheme_id="UN/ECE 5153",
                            scheme_agency_id="6"
                        )
                    )
                ),
            ],
            party_legal_entity=[
                PartyLegalEntity(
                    registration_name=RegistrationName(
                        value="The Sellercompany Incorporated"
                    ),
                    company_id=CompanyId(
                        value="5402697509",
                        scheme_id="CVR",
                        scheme_agency_id="ZZZ"
                    ),
                    registration_address=RegistrationAddress(
                        city_name=CityName(
                            value="Big city"
                        ),
                        country_subentity=CountrySubentity(
                            value="RegionA"
                        ),
                        country=Country(
                            identification_code=IdentificationCode(
                                value="DK"
                            )
                        )
                    )
                ),
            ],
            contact=Contact(
                telephone=Telephone(
                    value="4621230"
                ),
                telefax=Telefax(
                    value="4621231"
                ),
                electronic_mail=ElectronicMail(
                    value="antonio@salescompany.dk"
                )
            ),
            person=[
                Person(
                    first_name=FirstName(
                        value="Antonio"
                    ),
                    family_name=FamilyName(
                        value="M"
                    ),
                    middle_name=MiddleName(
                        value="Salemacher"
                    ),
                    job_title=JobTitle(
                        value="Sales manager"
                    )
                ),
            ]
        )
    ),
    accounting_customer_party=AccountingCustomerParty(
        party=Party(
            endpoint_id=EndpointId(
                value="1234567987654",
                scheme_id="GLN",
                scheme_agency_id="9"
            ),
            party_identification=[
                PartyIdentification(
                    id=Id(
                        value="345KS5324",
                        scheme_id="ZZZ"
                    )
                ),
            ],
            party_name=[
                PartyName(
                    name=Name(
                        value="Buyercompany ltd"
                    )
                ),
            ],
            postal_address=PostalAddress(
                id=Id(
                    value="1238764941386",
                    scheme_id="GLN",
                    scheme_agency_id="9"
                ),
                postbox=Postbox(
                    value="123"
                ),
                street_name=StreetName(
                    value="Anystreet"
                ),
                additional_street_name=AdditionalStreetName(
                    value="Back door"
                ),
                building_number=BuildingNumber(
                    value="8"
                ),
                department=Department(
                    value="Accounting department"
                ),
                city_name=CityName(
                    value="Anytown"
                ),
                postal_zone=PostalZone(
                    value="101"
                ),
                country_subentity=CountrySubentity(
                    value="RegionB"
                ),
                country=Country(
                    identification_code=IdentificationCode(
                        value="BE",
                        list_id="ISO3166-1",
                        list_agency_id="6"
                    )
                )
            ),
            party_tax_scheme=[
                PartyTaxScheme(
                    company_id=CompanyId(
                        value="BE54321",
                        scheme_id="BEVAT",
                        scheme_agency_id="ZZZ"
                    ),
                    tax_scheme=TaxScheme(
                        id=Id(
                            value="VAT",
                            scheme_id="UN/ECE 5153",
                            scheme_agency_id="6"
                        )
                    )
                ),
            ],
            party_legal_entity=[
                PartyLegalEntity(
                    registration_name=RegistrationName(
                        value="The buyercompany inc."
                    ),
                    company_id=CompanyId(
                        value="5645342123",
                        scheme_id="ZZZ",
                        scheme_agency_id="ZZZ"
                    ),
                    registration_address=RegistrationAddress(
                        city_name=CityName(
                            value="Mainplace"
                        ),
                        country_subentity=CountrySubentity(
                            value="RegionB"
                        ),
                        country=Country(
                            identification_code=IdentificationCode(
                                value="BE"
                            )
                        )
                    )
                ),
            ],
            contact=Contact(
                telephone=Telephone(
                    value="5121230"
                ),
                telefax=Telefax(
                    value="5121231"
                ),
                electronic_mail=ElectronicMail(
                    value="john@buyercompany.eu"
                )
            ),
            person=[
                Person(
                    first_name=FirstName(
                        value="John"
                    ),
                    family_name=FamilyName(
                        value="X"
                    ),
                    middle_name=MiddleName(
                        value="Doe"
                    ),
                    job_title=JobTitle(
                        value="Purchasing manager"
                    )
                ),
            ]
        )
    ),
    payee_party=PayeeParty(
        party_identification=[
            PartyIdentification(
                id=Id(
                    value="098740918237",
                    scheme_id="GLN",
                    scheme_agency_id="9"
                )
            ),
        ],
        party_name=[
            PartyName(
                name=Name(
                    value="Ebeneser Scrooge Inc."
                )
            ),
        ],
        party_legal_entity=[
            PartyLegalEntity(
                company_id=CompanyId(
                    value="6411982340",
                    scheme_id="UK:CH",
                    scheme_agency_id="ZZZ"
                )
            ),
        ]
    ),
    allowance_charge=[
        AllowanceCharge(
            charge_indicator=True,
            allowance_charge_reason=[
                AllowanceChargeReason(
                    value="Packing cost"
                ),
            ],
            amount=Amount(
                value=Decimal("100"),
                currency_id="EUR"
            )
        ),
        AllowanceCharge(
            charge_indicator=False,
            allowance_charge_reason=[
                AllowanceChargeReason(
                    value="Promotion discount"
                ),
            ],
            amount=Amount(
                value=Decimal("100"),
                currency_id="EUR"
            )
        ),
    ],
    tax_total=[
        TaxTotal(
            tax_amount=TaxAmount(
                value=Decimal("292.20"),
                currency_id="EUR"
            ),
            tax_subtotal=[
                TaxSubtotal(
                    taxable_amount=TaxableAmount(
                        value=Decimal("1460.5"),
                        currency_id="EUR"
                    ),
                    tax_amount=TaxAmount(
                        value=Decimal("292.1"),
                        currency_id="EUR"
                    ),
                    tax_category=TaxCategory(
                        id=Id(
                            value="S",
                            scheme_id="UN/ECE 5305",
                            scheme_agency_id="6"
                        ),
                        percent=Percent(
                            value=Decimal("20")
                        ),
                        tax_scheme=TaxScheme(
                            id=Id(
                                value="VAT",
                                scheme_id="UN/ECE 5153",
                                scheme_agency_id="6"
                            )
                        )
                    )
                ),
                TaxSubtotal(
                    taxable_amount=TaxableAmount(
                        value=Decimal("1"),
                        currency_id="EUR"
                    ),
                    tax_amount=TaxAmount(
                        value=Decimal("0.1"),
                        currency_id="EUR"
                    ),
                    tax_category=TaxCategory(
                        id=Id(
                            value="AA",
                            scheme_id="UN/ECE 5305",
                            scheme_agency_id="6"
                        ),
                        percent=Percent(
                            value=Decimal("10")
                        ),
                        tax_scheme=TaxScheme(
                            id=Id(
                                value="VAT",
                                scheme_id="UN/ECE 5153",
                                scheme_agency_id="6"
                            )
                        )
                    )
                ),
                TaxSubtotal(
                    taxable_amount=TaxableAmount(
                        value=Decimal("-25"),
                        currency_id="EUR"
                    ),
                    tax_amount=TaxAmount(
                        value=Decimal("0"),
                        currency_id="EUR"
                    ),
                    tax_category=TaxCategory(
                        id=Id(
                            value="E",
                            scheme_id="UN/ECE 5305",
                            scheme_agency_id="6"
                        ),
                        percent=Percent(
                            value=Decimal("0")
                        ),
                        tax_exemption_reason_code=TaxExemptionReasonCode(
                            value="AAM",
                            list_id="CWA 15577",
                            list_agency_id="ZZZ"
                        ),
                        tax_exemption_reason=[
                            TaxExemptionReason(
                                value="Exempt New Means of Transport"
                            ),
                        ],
                        tax_scheme=TaxScheme(
                            id=Id(
                                value="VAT",
                                scheme_id="UN/ECE 5153",
                                scheme_agency_id="6"
                            )
                        )
                    )
                ),
            ]
        ),
    ],
    legal_monetary_total=LegalMonetaryTotal(
        line_extension_amount=LineExtensionAmount(
            value=Decimal("1436.5"),
            currency_id="EUR"
        ),
        tax_exclusive_amount=TaxExclusiveAmount(
            value=Decimal("1436.5"),
            currency_id="EUR"
        ),
        tax_inclusive_amount=TaxInclusiveAmount(
            value=Decimal("1729"),
            currency_id="EUR"
        ),
        allowance_total_amount=AllowanceTotalAmount(
            value=Decimal("100"),
            currency_id="EUR"
        ),
        charge_total_amount=ChargeTotalAmount(
            value=Decimal("100"),
            currency_id="EUR"
        ),
        prepaid_amount=PrepaidAmount(
            value=Decimal("1000"),
            currency_id="EUR"
        ),
        payable_rounding_amount=PayableRoundingAmount(
            value=Decimal("0.30"),
            currency_id="EUR"
        ),
        payable_amount=PayableAmount(
            value=Decimal("729"),
            currency_id="EUR"
        )
    ),
    credit_note_line=[
        CreditNoteLine(
            id=Id(
                value="1"
            ),
            note=[
                Note(
                    value="Scratch on box"
                ),
            ],
            credited_quantity=CreditedQuantity(
                value=Decimal("1"),
                unit_code="C62"
            ),
            line_extension_amount=LineExtensionAmount(
                value=Decimal("1273"),
                currency_id="EUR"
            ),
            accounting_cost=AccountingCost(
                value="BookingCode001"
            ),
            tax_total=[
                TaxTotal(
                    tax_amount=TaxAmount(
                        value=Decimal("254.6"),
                        currency_id="EUR"
                    )
                ),
            ],
            item=Item(
                description=[
                    Description(
                        value="Processor: Intel Core 2 Duo SU9400 LV (1.4GHz). RAM:\n\t\t\t\t3MB. Screen 1440x900",
                        language_id="EN"
                    ),
                ],
                name=Name(
                    value="Labtop computer"
                ),
                sellers_item_identification=SellersItemIdentification(
                    id=Id(
                        value="JB007"
                    )
                ),
                standard_item_identification=StandardItemIdentification(
                    id=Id(
                        value="1234567890124",
                        scheme_id="GTIN",
                        scheme_agency_id="9"
                    )
                ),
                commodity_classification=[
                    CommodityClassification(
                        item_classification_code=ItemClassificationCode(
                            value="12344321",
                            list_id="UNSPSC",
                            list_agency_id="113"
                        )
                    ),
                    CommodityClassification(
                        item_classification_code=ItemClassificationCode(
                            value="65434568",
                            list_id="CPV",
                            list_agency_id="2"
                        )
                    ),
                ],
                classified_tax_category=[
                    ClassifiedTaxCategory(
                        id=Id(
                            value="S",
                            scheme_id="UN/ECE 5305",
                            scheme_agency_id="6"
                        ),
                        percent=Percent(
                            value=Decimal("20")
                        ),
                        tax_scheme=TaxScheme(
                            id=Id(
                                value="VAT",
                                scheme_id="UN/ECE 5153",
                                scheme_agency_id="6"
                            )
                        )
                    ),
                ],
                additional_item_property=[
                    AdditionalItemProperty(
                        name=Name(
                            value="Color"
                        ),
                        value=Value(
                            value="black"
                        )
                    ),
                ]
            ),
            price=Price(
                price_amount=PriceAmount(
                    value=Decimal("1273"),
                    currency_id="EUR"
                ),
                base_quantity=BaseQuantity(
                    value=Decimal("1"),
                    unit_code="C62"
                ),
                allowance_charge=[
                    AllowanceCharge(
                        charge_indicator=False,
                        allowance_charge_reason=[
                            AllowanceChargeReason(
                                value="Contract"
                            ),
                        ],
                        multiplier_factor_numeric=MultiplierFactorNumeric(
                            value=Decimal("0.15")
                        ),
                        amount=Amount(
                            value=Decimal("225"),
                            currency_id="EUR"
                        ),
                        base_amount=BaseAmount(
                            value=Decimal("1500"),
                            currency_id="EUR"
                        )
                    ),
                ]
            )
        ),
        CreditNoteLine(
            id=Id(
                value="2"
            ),
            note=[
                Note(
                    value="Cover is slightly damaged."
                ),
            ],
            credited_quantity=CreditedQuantity(
                value=Decimal("-1"),
                unit_code="C62"
            ),
            line_extension_amount=LineExtensionAmount(
                value=Decimal("-3.96"),
                currency_id="EUR"
            ),
            tax_total=[
                TaxTotal(
                    tax_amount=TaxAmount(
                        value=Decimal("-0.396"),
                        currency_id="EUR"
                    )
                ),
            ],
            item=Item(
                name=Name(
                    value='Returned "Advanced computing" book'
                ),
                sellers_item_identification=SellersItemIdentification(
                    id=Id(
                        value="JB008"
                    )
                ),
                standard_item_identification=StandardItemIdentification(
                    id=Id(
                        value="1234567890125",
                        scheme_id="GTIN",
                        scheme_agency_id="9"
                    )
                ),
                commodity_classification=[
                    CommodityClassification(
                        item_classification_code=ItemClassificationCode(
                            value="32344324",
                            list_id="UNSPSC",
                            list_agency_id="113"
                        )
                    ),
                    CommodityClassification(
                        item_classification_code=ItemClassificationCode(
                            value="65434567",
                            list_id="CPV",
                            list_agency_id="2"
                        )
                    ),
                ],
                classified_tax_category=[
                    ClassifiedTaxCategory(
                        id=Id(
                            value="AA",
                            scheme_id="UN/ECE 5305",
                            scheme_agency_id="6"
                        ),
                        percent=Percent(
                            value=Decimal("10")
                        ),
                        tax_scheme=TaxScheme(
                            id=Id(
                                value="VAT",
                                scheme_id="UN/ECE 5153",
                                scheme_agency_id="6"
                            )
                        )
                    ),
                ]
            ),
            price=Price(
                price_amount=PriceAmount(
                    value=Decimal("3.96"),
                    currency_id="EUR"
                ),
                base_quantity=BaseQuantity(
                    value=Decimal("1"),
                    unit_code="C62"
                )
            )
        ),
        CreditNoteLine(
            id=Id(
                value="3"
            ),
            credited_quantity=CreditedQuantity(
                value=Decimal("2"),
                unit_code="C62"
            ),
            line_extension_amount=LineExtensionAmount(
                value=Decimal("4.96"),
                currency_id="EUR"
            ),
            tax_total=[
                TaxTotal(
                    tax_amount=TaxAmount(
                        value=Decimal("0.496"),
                        currency_id="EUR"
                    )
                ),
            ],
            item=Item(
                name=Name(
                    value='"Computing for dummies" book'
                ),
                sellers_item_identification=SellersItemIdentification(
                    id=Id(
                        value="JB009"
                    )
                ),
                standard_item_identification=StandardItemIdentification(
                    id=Id(
                        value="1234567890126",
                        scheme_id="GTIN",
                        scheme_agency_id="9"
                    )
                ),
                commodity_classification=[
                    CommodityClassification(
                        item_classification_code=ItemClassificationCode(
                            value="32344324",
                            list_id="UNSPSC",
                            list_agency_id="113"
                        )
                    ),
                    CommodityClassification(
                        item_classification_code=ItemClassificationCode(
                            value="65434566",
                            list_id="CPV",
                            list_agency_id="2"
                        )
                    ),
                ],
                classified_tax_category=[
                    ClassifiedTaxCategory(
                        id=Id(
                            value="AA",
                            scheme_id="UN/ECE 5305",
                            scheme_agency_id="6"
                        ),
                        percent=Percent(
                            value=Decimal("10")
                        ),
                        tax_scheme=TaxScheme(
                            id=Id(
                                value="VAT",
                                scheme_id="UN/ECE 5153",
                                scheme_agency_id="6"
                            )
                        )
                    ),
                ]
            ),
            price=Price(
                price_amount=PriceAmount(
                    value=Decimal("2.48"),
                    currency_id="EUR"
                ),
                base_quantity=BaseQuantity(
                    value=Decimal("1"),
                    unit_code="C62"
                ),
                allowance_charge=[
                    AllowanceCharge(
                        charge_indicator=False,
                        allowance_charge_reason=[
                            AllowanceChargeReason(
                                value="Contract"
                            ),
                        ],
                        multiplier_factor_numeric=MultiplierFactorNumeric(
                            value=Decimal("0.1")
                        ),
                        amount=Amount(
                            value=Decimal("0.275"),
                            currency_id="EUR"
                        ),
                        base_amount=BaseAmount(
                            value=Decimal("2.75"),
                            currency_id="EUR"
                        )
                    ),
                ]
            )
        ),
        CreditNoteLine(
            id=Id(
                value="4"
            ),
            credited_quantity=CreditedQuantity(
                value=Decimal("-1"),
                unit_code="C62"
            ),
            line_extension_amount=LineExtensionAmount(
                value=Decimal("-25"),
                currency_id="EUR"
            ),
            tax_total=[
                TaxTotal(
                    tax_amount=TaxAmount(
                        value=Decimal("0"),
                        currency_id="EUR"
                    )
                ),
            ],
            item=Item(
                name=Name(
                    value="Returned IBM 5150 desktop"
                ),
                sellers_item_identification=SellersItemIdentification(
                    id=Id(
                        value="JB010"
                    )
                ),
                standard_item_identification=StandardItemIdentification(
                    id=Id(
                        value="1234567890127",
                        scheme_id="GTIN",
                        scheme_agency_id="9"
                    )
                ),
                commodity_classification=[
                    CommodityClassification(
                        item_classification_code=ItemClassificationCode(
                            value="12344322",
                            list_id="UNSPSC",
                            list_agency_id="113"
                        )
                    ),
                    CommodityClassification(
                        item_classification_code=ItemClassificationCode(
                            value="65434565",
                            list_id="CPV",
                            list_agency_id="2"
                        )
                    ),
                ],
                classified_tax_category=[
                    ClassifiedTaxCategory(
                        id=Id(
                            value="E",
                            scheme_id="UN/ECE 5305",
                            scheme_agency_id="6"
                        ),
                        percent=Percent(
                            value=Decimal("0")
                        ),
                        tax_scheme=TaxScheme(
                            id=Id(
                                value="VAT",
                                scheme_id="UN/ECE 5153",
                                scheme_agency_id="6"
                            )
                        )
                    ),
                ]
            ),
            price=Price(
                price_amount=PriceAmount(
                    value=Decimal("25"),
                    currency_id="EUR"
                ),
                base_quantity=BaseQuantity(
                    value=Decimal("1"),
                    unit_code="C62"
                )
            )
        ),
        CreditNoteLine(
            id=Id(
                value="5"
            ),
            credited_quantity=CreditedQuantity(
                value=Decimal("250"),
                unit_code="C62"
            ),
            line_extension_amount=LineExtensionAmount(
                value=Decimal("187.5"),
                currency_id="EUR"
            ),
            accounting_cost=AccountingCost(
                value="BookingCode002"
            ),
            tax_total=[
                TaxTotal(
                    tax_amount=TaxAmount(
                        value=Decimal("37.5"),
                        currency_id="EUR"
                    )
                ),
            ],
            item=Item(
                name=Name(
                    value="Network cable"
                ),
                sellers_item_identification=SellersItemIdentification(
                    id=Id(
                        value="JB011"
                    )
                ),
                standard_item_identification=StandardItemIdentification(
                    id=Id(
                        value="1234567890128",
                        scheme_id="GTIN",
                        scheme_agency_id="9"
                    )
                ),
                commodity_classification=[
                    CommodityClassification(
                        item_classification_code=ItemClassificationCode(
                            value="12344325",
                            list_id="UNSPSC",
                            list_agency_id="113"
                        )
                    ),
                    CommodityClassification(
                        item_classification_code=ItemClassificationCode(
                            value="65434564",
                            list_id="CPV",
                            list_agency_id="2"
                        )
                    ),
                ],
                classified_tax_category=[
                    ClassifiedTaxCategory(
                        id=Id(
                            value="S",
                            scheme_id="UN/ECE 5305",
                            scheme_agency_id="6"
                        ),
                        percent=Percent(
                            value=Decimal("20")
                        ),
                        tax_scheme=TaxScheme(
                            id=Id(
                                value="VAT",
                                scheme_id="UN/ECE 5153",
                                scheme_agency_id="6"
                            )
                        )
                    ),
                ],
                additional_item_property=[
                    AdditionalItemProperty(
                        name=Name(
                            value="Type"
                        ),
                        value=Value(
                            value="Cat5"
                        )
                    ),
                ]
            ),
            price=Price(
                price_amount=PriceAmount(
                    value=Decimal("0.75"),
                    currency_id="EUR"
                ),
                base_quantity=BaseQuantity(
                    value=Decimal("1"),
                    unit_code="C62"
                )
            )
        ),
    ]
)
