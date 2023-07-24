from decimal import Decimal
from ubl.models.common.ubl_common_aggregate_components_2_1 import Address
from ubl.models.common.ubl_common_aggregate_components_2_1 import AddressLine
from ubl.models.common.ubl_common_aggregate_components_2_1 import AllowanceCharge
from ubl.models.common.ubl_common_aggregate_components_2_1 import BuyersItemIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import Contact
from ubl.models.common.ubl_common_aggregate_components_2_1 import Country
from ubl.models.common.ubl_common_aggregate_components_2_1 import Delivery
from ubl.models.common.ubl_common_aggregate_components_2_1 import DeliveryAddress
from ubl.models.common.ubl_common_aggregate_components_2_1 import DeliveryTerms
from ubl.models.common.ubl_common_aggregate_components_2_1 import DestinationCountry
from ubl.models.common.ubl_common_aggregate_components_2_1 import FinancialInstitution
from ubl.models.common.ubl_common_aggregate_components_2_1 import FinancialInstitutionBranch
from ubl.models.common.ubl_common_aggregate_components_2_1 import Item
from ubl.models.common.ubl_common_aggregate_components_2_1 import LineItem
from ubl.models.common.ubl_common_aggregate_components_2_1 import OriginatorCustomerParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import Party
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyName
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyTaxScheme
from ubl.models.common.ubl_common_aggregate_components_2_1 import PayeeFinancialAccount
from ubl.models.common.ubl_common_aggregate_components_2_1 import PaymentMeans
from ubl.models.common.ubl_common_aggregate_components_2_1 import PostalAddress
from ubl.models.common.ubl_common_aggregate_components_2_1 import Price
from ubl.models.common.ubl_common_aggregate_components_2_1 import QuotationLine
from ubl.models.common.ubl_common_aggregate_components_2_1 import QuotedMonetaryTotal
from ubl.models.common.ubl_common_aggregate_components_2_1 import RequestForQuotationDocumentReference
from ubl.models.common.ubl_common_aggregate_components_2_1 import RequestedDeliveryPeriod
from ubl.models.common.ubl_common_aggregate_components_2_1 import SellerSupplierParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import SellersItemIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import TaxCategory
from ubl.models.common.ubl_common_aggregate_components_2_1 import TaxScheme
from ubl.models.common.ubl_common_aggregate_components_2_1 import TaxSubtotal
from ubl.models.common.ubl_common_aggregate_components_2_1 import TaxTotal
from ubl.models.common.ubl_common_aggregate_components_2_1 import TransactionConditions
from ubl.models.common.ubl_common_aggregate_components_2_1 import ValidityPeriod
from ubl.models.common.ubl_common_basic_components_2_1 import AccountTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import AllowanceChargeReasonCode
from ubl.models.common.ubl_common_basic_components_2_1 import Amount
from ubl.models.common.ubl_common_basic_components_2_1 import BaseQuantity
from ubl.models.common.ubl_common_basic_components_2_1 import BuildingName
from ubl.models.common.ubl_common_basic_components_2_1 import BuildingNumber
from ubl.models.common.ubl_common_basic_components_2_1 import CityName
from ubl.models.common.ubl_common_basic_components_2_1 import CompanyId
from ubl.models.common.ubl_common_basic_components_2_1 import CountrySubentity
from ubl.models.common.ubl_common_basic_components_2_1 import CurrencyCode
from ubl.models.common.ubl_common_basic_components_2_1 import CustomerAssignedAccountId
from ubl.models.common.ubl_common_basic_components_2_1 import CustomizationId
from ubl.models.common.ubl_common_basic_components_2_1 import Description
from ubl.models.common.ubl_common_basic_components_2_1 import ElectronicMail
from ubl.models.common.ubl_common_basic_components_2_1 import ExemptionReason
from ubl.models.common.ubl_common_basic_components_2_1 import Id
from ubl.models.common.ubl_common_basic_components_2_1 import IdentificationCode
from ubl.models.common.ubl_common_basic_components_2_1 import Line
from ubl.models.common.ubl_common_basic_components_2_1 import LineExtensionAmount
from ubl.models.common.ubl_common_basic_components_2_1 import MultiplierFactorNumeric
from ubl.models.common.ubl_common_basic_components_2_1 import Name
from ubl.models.common.ubl_common_basic_components_2_1 import Note
from ubl.models.common.ubl_common_basic_components_2_1 import PayableAmount
from ubl.models.common.ubl_common_basic_components_2_1 import PaymentMeansCode
from ubl.models.common.ubl_common_basic_components_2_1 import PostalZone
from ubl.models.common.ubl_common_basic_components_2_1 import PriceAmount
from ubl.models.common.ubl_common_basic_components_2_1 import ProfileId
from ubl.models.common.ubl_common_basic_components_2_1 import Quantity
from ubl.models.common.ubl_common_basic_components_2_1 import RegistrationName
from ubl.models.common.ubl_common_basic_components_2_1 import SpecialTerms
from ubl.models.common.ubl_common_basic_components_2_1 import StreetName
from ubl.models.common.ubl_common_basic_components_2_1 import TaxAmount
from ubl.models.common.ubl_common_basic_components_2_1 import TaxExclusiveAmount
from ubl.models.common.ubl_common_basic_components_2_1 import TaxTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import TaxableAmount
from ubl.models.common.ubl_common_basic_components_2_1 import Telefax
from ubl.models.common.ubl_common_basic_components_2_1 import Telephone
from ubl.models.common.ubl_common_basic_components_2_1 import TotalTaxAmount
from ubl.models.common.ubl_common_basic_components_2_1 import UblversionId
from ubl.models.common.ubl_common_basic_components_2_1 import Uuid
from ubl.models.maindoc.ubl_quotation_2_1 import Quotation
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlTime


obj = Quotation(
    ublversion_id=UblversionId(
        value="2.0"
    ),
    customization_id=CustomizationId(
        value="urn:oasis:names:specification:ubl:schema:xsd:Quotation-2-draft"
    ),
    profile_id=ProfileId(
        value="bpid:urn:oasis:names:draft:bpss:ubl-2-sbs-request-for-quotation-draft"
    ),
    id=Id(
        value="QIY7655"
    ),
    copy_indicator=False,
    uuid=Uuid(
        value="4D07786B-DA6D-439F-82D1-6FFFC7F4E3B1"
    ),
    issue_date=XmlDate(2005, 6, 20),
    note=[
        Note(
            value="sample"
        ),
    ],
    validity_period=ValidityPeriod(
        start_date=XmlDate(2005, 6, 20),
        end_date=XmlDate(2005, 7, 20)
    ),
    request_for_quotation_document_reference=RequestForQuotationDocumentReference(
        id=Id(
            value="G867B"
        ),
        uuid=Uuid(
            value="8D076867-AE6D-439F-8281-5AAFC7F4E3B1"
        ),
        issue_date=XmlDate(2005, 6, 19)
    ),
    seller_supplier_party=SellerSupplierParty(
        customer_assigned_account_id=CustomerAssignedAccountId(
            value="CO001"
        ),
        party=Party(
            party_name=[
                PartyName(
                    name=Name(
                        value="Consortial"
                    )
                ),
            ],
            postal_address=PostalAddress(
                street_name=StreetName(
                    value="Busy Street"
                ),
                building_name=BuildingName(
                    value="Thereabouts"
                ),
                building_number=BuildingNumber(
                    value="56A"
                ),
                city_name=CityName(
                    value="Farthing"
                ),
                postal_zone=PostalZone(
                    value="AA99 1BB"
                ),
                country_subentity=CountrySubentity(
                    value="Heremouthshire"
                ),
                address_line=[
                    AddressLine(
                        line=Line(
                            value="The Roundabout"
                        )
                    ),
                ],
                country=Country(
                    identification_code=IdentificationCode(
                        value="GB"
                    )
                )
            ),
            party_tax_scheme=[
                PartyTaxScheme(
                    registration_name=RegistrationName(
                        value="Farthing Purchasing Consortium"
                    ),
                    company_id=CompanyId(
                        value="175 269 2355"
                    ),
                    exemption_reason=[
                        ExemptionReason(
                            value="N/A"
                        ),
                    ],
                    tax_scheme=TaxScheme(
                        id=Id(
                            value="VAT"
                        ),
                        tax_type_code=TaxTypeCode(
                            value="VAT"
                        )
                    )
                ),
            ],
            contact=Contact(
                name=Name(
                    value="Mrs Bouquet"
                ),
                telephone=Telephone(
                    value="0158 1233714"
                ),
                telefax=Telefax(
                    value="0158 1233856"
                ),
                electronic_mail=ElectronicMail(
                    value="bouquet@fpconsortial.co.uk"
                )
            )
        )
    ),
    originator_customer_party=OriginatorCustomerParty(
        party=Party(
            party_name=[
                PartyName(
                    name=Name(
                        value="The Terminus"
                    )
                ),
            ],
            postal_address=PostalAddress(
                street_name=StreetName(
                    value="Avon Way"
                ),
                building_name=BuildingName(
                    value="Thereabouts"
                ),
                building_number=BuildingNumber(
                    value="56A"
                ),
                city_name=CityName(
                    value="Bridgtow"
                ),
                postal_zone=PostalZone(
                    value="ZZ99 1ZZ"
                ),
                country_subentity=CountrySubentity(
                    value="Avon"
                ),
                address_line=[
                    AddressLine(
                        line=Line(
                            value="3rd Floor, Room 5"
                        )
                    ),
                ],
                country=Country(
                    identification_code=IdentificationCode(
                        value="GB"
                    )
                )
            ),
            party_tax_scheme=[
                PartyTaxScheme(
                    registration_name=RegistrationName(
                        value="Bridgtow District Council"
                    ),
                    company_id=CompanyId(
                        value="12356478"
                    ),
                    exemption_reason=[
                        ExemptionReason(
                            value="Local Authority"
                        ),
                    ],
                    tax_scheme=TaxScheme(
                        id=Id(
                            value="UK VAT"
                        ),
                        tax_type_code=TaxTypeCode(
                            value="VAT"
                        )
                    )
                ),
            ],
            contact=Contact(
                name=Name(
                    value="S Massiah"
                ),
                telephone=Telephone(
                    value="0127 98876545"
                ),
                telefax=Telefax(
                    value="0127 98876546"
                ),
                electronic_mail=ElectronicMail(
                    value="smassiah@the-email.co.uk"
                )
            )
        )
    ),
    delivery=[
        Delivery(
            delivery_address=DeliveryAddress(
                street_name=StreetName(
                    value="Avon Way"
                ),
                building_name=BuildingName(
                    value="Thereabouts"
                ),
                building_number=BuildingNumber(
                    value="56A"
                ),
                city_name=CityName(
                    value="Bridgtow"
                ),
                postal_zone=PostalZone(
                    value="ZZ99 1ZZ"
                ),
                country_subentity=CountrySubentity(
                    value="Avon"
                ),
                address_line=[
                    AddressLine(
                        line=Line(
                            value="3rd Floor, Room 5"
                        )
                    ),
                ],
                country=Country(
                    identification_code=IdentificationCode(
                        value="GB"
                    )
                )
            ),
            requested_delivery_period=RequestedDeliveryPeriod(
                start_date=XmlDate(2005, 6, 29),
                start_time=XmlTime(9, 30, 47, 0, 0),
                end_date=XmlDate(2005, 6, 29),
                end_time=XmlTime(9, 30, 47, 0, 0)
            )
        ),
    ],
    delivery_terms=DeliveryTerms(
        special_terms=[
            SpecialTerms(
                value="1% deduction for late delivery as per contract"
            ),
        ]
    ),
    payment_means=PaymentMeans(
        payment_means_code=PaymentMeansCode(
            value="20"
        ),
        payee_financial_account=PayeeFinancialAccount(
            id=Id(
                value="12345678"
            ),
            name=Name(
                value="Farthing Purchasing Consortium"
            ),
            account_type_code=AccountTypeCode(
                value="Current"
            ),
            currency_code=CurrencyCode(
                value="GBP"
            ),
            financial_institution_branch=FinancialInstitutionBranch(
                id=Id(
                    value="10-26-58"
                ),
                name=Name(
                    value="Open Bank Ltd, Bridgstow Branch "
                ),
                financial_institution=FinancialInstitution(
                    id=Id(
                        value="10-26-58"
                    ),
                    name=Name(
                        value="Open Bank Ltd"
                    ),
                    address=Address(
                        street_name=StreetName(
                            value="City Road"
                        ),
                        building_name=BuildingName(
                            value="Banking House"
                        ),
                        building_number=BuildingNumber(
                            value="12"
                        ),
                        city_name=CityName(
                            value="London"
                        ),
                        postal_zone=PostalZone(
                            value="AQ1 6TH"
                        ),
                        country_subentity=CountrySubentity(
                            value="London&#10;"
                        ),
                        address_line=[
                            AddressLine(
                                line=Line(
                                    value="5th Floor"
                                )
                            ),
                        ],
                        country=Country(
                            identification_code=IdentificationCode(
                                value="GB"
                            )
                        )
                    )
                ),
                address=Address(
                    street_name=StreetName(
                        value="Busy Street"
                    ),
                    building_name=BuildingName(
                        value="The Mall"
                    ),
                    building_number=BuildingNumber(
                        value="152"
                    ),
                    city_name=CityName(
                        value="Farthing"
                    ),
                    postal_zone=PostalZone(
                        value="AA99 1BB"
                    ),
                    country_subentity=CountrySubentity(
                        value="Heremouthshire"
                    ),
                    address_line=[
                        AddressLine(
                            line=Line(
                                value="West Wing"
                            )
                        ),
                    ],
                    country=Country(
                        identification_code=IdentificationCode(
                            value="GB"
                        )
                    )
                )
            ),
            country=Country(
                identification_code=IdentificationCode(
                    value="GB"
                )
            )
        )
    ),
    transaction_conditions=TransactionConditions(
        description=[
            Description(
                value="order response required; payment is by BACS or by cheque"
            ),
        ]
    ),
    allowance_charge=[
        AllowanceCharge(
            charge_indicator=False,
            allowance_charge_reason_code=AllowanceChargeReasonCode(
                value="17"
            ),
            multiplier_factor_numeric=MultiplierFactorNumeric(
                value=Decimal("0.10")
            ),
            amount=Amount(
                value=Decimal("10.00"),
                currency_id="GBP"
            )
        ),
    ],
    destination_country=DestinationCountry(
        identification_code=IdentificationCode(
            value="GB"
        ),
        name=Name(
            value="Great Britain"
        )
    ),
    tax_total=[
        TaxTotal(
            tax_amount=TaxAmount(
                value=Decimal("17.50"),
                currency_id="GBP"
            ),
            tax_evidence_indicator=False,
            tax_subtotal=[
                TaxSubtotal(
                    taxable_amount=TaxableAmount(
                        value=Decimal("100.00"),
                        currency_id="GBP"
                    ),
                    tax_amount=TaxAmount(
                        value=Decimal("17.50"),
                        currency_id="GBP"
                    ),
                    tax_category=TaxCategory(
                        id=Id(
                            value="A"
                        ),
                        tax_scheme=TaxScheme(
                            id=Id(
                                value="UK VAT"
                            ),
                            tax_type_code=TaxTypeCode(
                                value="VAT"
                            )
                        )
                    )
                ),
            ]
        ),
    ],
    quoted_monetary_total=QuotedMonetaryTotal(
        line_extension_amount=LineExtensionAmount(
            value=Decimal("100.00"),
            currency_id="GBP"
        ),
        tax_exclusive_amount=TaxExclusiveAmount(
            value=Decimal("90.00"),
            currency_id="GBP"
        ),
        payable_amount=PayableAmount(
            value=Decimal("107.50"),
            currency_id="GBP"
        )
    ),
    quotation_line=[
        QuotationLine(
            id=Id(
                value="1"
            ),
            note=[
                Note(
                    value="sample"
                ),
            ],
            line_item=LineItem(
                id=Id(
                    value="1"
                ),
                quantity=Quantity(
                    value=Decimal("100"),
                    unit_code="KGM"
                ),
                line_extension_amount=LineExtensionAmount(
                    value=Decimal("100.00"),
                    currency_id="GBP"
                ),
                total_tax_amount=TotalTaxAmount(
                    value=Decimal("17.50"),
                    currency_id="GBP"
                ),
                price=Price(
                    price_amount=PriceAmount(
                        value=Decimal("100.00"),
                        currency_id="GBP"
                    ),
                    base_quantity=BaseQuantity(
                        value=Decimal("1"),
                        unit_code="KGM"
                    )
                ),
                item=Item(
                    description=[
                        Description(
                            value="Acme beeswax"
                        ),
                    ],
                    name=Name(
                        value="beeswax"
                    ),
                    buyers_item_identification=BuyersItemIdentification(
                        id=Id(
                            value="6578489"
                        )
                    ),
                    sellers_item_identification=SellersItemIdentification(
                        id=Id(
                            value="17589683"
                        )
                    )
                )
            )
        ),
    ]
)
