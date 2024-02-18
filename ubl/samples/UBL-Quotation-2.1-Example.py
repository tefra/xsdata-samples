from decimal import Decimal
from ubl.models.common.ubl_common_aggregate_components_2_1 import AddressLine
from ubl.models.common.ubl_common_aggregate_components_2_1 import Contact
from ubl.models.common.ubl_common_aggregate_components_2_1 import Country
from ubl.models.common.ubl_common_aggregate_components_2_1 import Delivery
from ubl.models.common.ubl_common_aggregate_components_2_1 import DeliveryAddress
from ubl.models.common.ubl_common_aggregate_components_2_1 import DeliveryTerms
from ubl.models.common.ubl_common_aggregate_components_2_1 import Item
from ubl.models.common.ubl_common_aggregate_components_2_1 import LineItem
from ubl.models.common.ubl_common_aggregate_components_2_1 import OriginatorCustomerParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import Party
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyLegalEntity
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyName
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyTaxScheme
from ubl.models.common.ubl_common_aggregate_components_2_1 import PostalAddress
from ubl.models.common.ubl_common_aggregate_components_2_1 import Price
from ubl.models.common.ubl_common_aggregate_components_2_1 import QuotationLine
from ubl.models.common.ubl_common_aggregate_components_2_1 import QuotedMonetaryTotal
from ubl.models.common.ubl_common_aggregate_components_2_1 import RequestForQuotationDocumentReference
from ubl.models.common.ubl_common_aggregate_components_2_1 import RequestedDeliveryPeriod
from ubl.models.common.ubl_common_aggregate_components_2_1 import SellerSupplierParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import TaxScheme
from ubl.models.common.ubl_common_aggregate_components_2_1 import ValidityPeriod
from ubl.models.common.ubl_common_basic_components_2_1 import AddressFormatCode
from ubl.models.common.ubl_common_basic_components_2_1 import BaseQuantity
from ubl.models.common.ubl_common_basic_components_2_1 import BuildingNumber
from ubl.models.common.ubl_common_basic_components_2_1 import CityName
from ubl.models.common.ubl_common_basic_components_2_1 import CompanyId
from ubl.models.common.ubl_common_basic_components_2_1 import CopyIndicator
from ubl.models.common.ubl_common_basic_components_2_1 import CustomerAssignedAccountId
from ubl.models.common.ubl_common_basic_components_2_1 import CustomizationId
from ubl.models.common.ubl_common_basic_components_2_1 import Description
from ubl.models.common.ubl_common_basic_components_2_1 import EndDate
from ubl.models.common.ubl_common_basic_components_2_1 import EndTime
from ubl.models.common.ubl_common_basic_components_2_1 import EndpointId
from ubl.models.common.ubl_common_basic_components_2_1 import Id
from ubl.models.common.ubl_common_basic_components_2_1 import IdentificationCode
from ubl.models.common.ubl_common_basic_components_2_1 import IssueDate
from ubl.models.common.ubl_common_basic_components_2_1 import IssueTime
from ubl.models.common.ubl_common_basic_components_2_1 import Line
from ubl.models.common.ubl_common_basic_components_2_1 import LineExtensionAmount
from ubl.models.common.ubl_common_basic_components_2_1 import Name
from ubl.models.common.ubl_common_basic_components_2_1 import Note
from ubl.models.common.ubl_common_basic_components_2_1 import PayableAmount
from ubl.models.common.ubl_common_basic_components_2_1 import PostalZone
from ubl.models.common.ubl_common_basic_components_2_1 import PriceAmount
from ubl.models.common.ubl_common_basic_components_2_1 import ProfileId
from ubl.models.common.ubl_common_basic_components_2_1 import Quantity
from ubl.models.common.ubl_common_basic_components_2_1 import RegistrationName
from ubl.models.common.ubl_common_basic_components_2_1 import SpecialTerms
from ubl.models.common.ubl_common_basic_components_2_1 import StartDate
from ubl.models.common.ubl_common_basic_components_2_1 import StartTime
from ubl.models.common.ubl_common_basic_components_2_1 import StreetName
from ubl.models.common.ubl_common_basic_components_2_1 import TaxExclusiveAmount
from ubl.models.common.ubl_common_basic_components_2_1 import TaxInclusiveAmount
from ubl.models.common.ubl_common_basic_components_2_1 import TotalTaxAmount
from ubl.models.common.ubl_common_basic_components_2_1 import UblversionId
from ubl.models.common.ubl_common_basic_components_2_1 import Uuid
from ubl.models.maindoc.ubl_quotation_2_1 import Quotation
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlTime


obj = Quotation(
    ublversion_id=UblversionId(
        value='2.0'
    ),
    customization_id=CustomizationId(
        value='OIOUBL-2.1'
    ),
    profile_id=ProfileId(
        value='Procurement-QuoSim-1.0',
        scheme_id='urn:oioubl:id:profileid-1.2',
        scheme_agency_id='320'
    ),
    id=Id(
        value='QIY7655'
    ),
    copy_indicator=CopyIndicator(
        value=False
    ),
    uuid=Uuid(
        value='4D07786B-DA6D-439F-82D1-6FFFC7F4E3B1'
    ),
    issue_date=IssueDate(
        value=XmlDate(2008, 5, 1)
    ),
    issue_time=IssueTime(
        value=XmlTime(11, 32, 26, 0, 0)
    ),
    note=[
        Note(
            value='Bestilling af computere',
            language_id='da-dk'
        ),
    ],
    validity_period=ValidityPeriod(
        start_date=StartDate(
            value=XmlDate(2008, 5, 1)
        ),
        end_date=EndDate(
            value=XmlDate(2008, 5, 6)
        )
    ),
    request_for_quotation_document_reference=RequestForQuotationDocumentReference(
        id=Id(
            value='G867B'
        ),
        uuid=Uuid(
            value='93T5G3G5-HYA3-7267-BVG3-GS46SW44WG53'
        ),
        issue_date=IssueDate(
            value=XmlDate(2008, 4, 19)
        )
    ),
    seller_supplier_party=SellerSupplierParty(
        customer_assigned_account_id=CustomerAssignedAccountId(
            value='LEV00123'
        ),
        party=Party(
            endpoint_id=EndpointId(
                value='DK18296799',
                scheme_id='DK:CVR'
            ),
            party_identification=[
                PartyIdentification(
                    id=Id(
                        value='DK18296799',
                        scheme_id='DK:CVR'
                    )
                ),
            ],
            party_name=[
                PartyName(
                    name=Name(
                        value='Delcomputer A/S'
                    )
                ),
            ],
            postal_address=PostalAddress(
                address_format_code=AddressFormatCode(
                    value='StructuredDK',
                    list_id='urn:oioubl:codelist:addressformatcode-1.1',
                    list_agency_id='320'
                ),
                street_name=StreetName(
                    value='Arne Jacobsens Allé'
                ),
                building_number=BuildingNumber(
                    value='15'
                ),
                city_name=CityName(
                    value='København S'
                ),
                postal_zone=PostalZone(
                    value='2300'
                ),
                country=Country(
                    identification_code=IdentificationCode(
                        value='DK'
                    )
                )
            ),
            party_tax_scheme=[
                PartyTaxScheme(
                    company_id=CompanyId(
                        value='DK18296799',
                        scheme_id='DK:SE'
                    ),
                    tax_scheme=TaxScheme(
                        id=Id(
                            value='63',
                            scheme_id='urn:oioubl:id:taxschemeid-1.1',
                            scheme_agency_id='320'
                        ),
                        name=Name(
                            value='Moms'
                        )
                    )
                ),
            ],
            party_legal_entity=[
                PartyLegalEntity(
                    registration_name=RegistrationName(
                        value='Delcomputer A/S'
                    ),
                    company_id=CompanyId(
                        value='18296799',
                        scheme_id='DK:CVR'
                    )
                ),
            ]
        )
    ),
    originator_customer_party=OriginatorCustomerParty(
        party=Party(
            endpoint_id=EndpointId(
                value='5798000416604',
                scheme_id='GLN',
                scheme_agency_id='9'
            ),
            party_identification=[
                PartyIdentification(
                    id=Id(
                        value='5798000416604',
                        scheme_id='GLN',
                        scheme_agency_id='9'
                    )
                ),
            ],
            party_name=[
                PartyName(
                    name=Name(
                        value='Gentofte Kommune'
                    )
                ),
            ],
            postal_address=PostalAddress(
                address_format_code=AddressFormatCode(
                    value='StructuredDK',
                    list_id='urn:oioubl:codelist:addressformatcode-1.1',
                    list_agency_id='320'
                ),
                street_name=StreetName(
                    value='Bernstorffsvej'
                ),
                building_number=BuildingNumber(
                    value='161'
                ),
                city_name=CityName(
                    value='Charlottenlund'
                ),
                postal_zone=PostalZone(
                    value='2920'
                ),
                country=Country(
                    identification_code=IdentificationCode(
                        value='DK'
                    )
                )
            ),
            party_tax_scheme=[
                PartyTaxScheme(
                    company_id=CompanyId(
                        value='DK12345678',
                        scheme_id='DK:SE'
                    ),
                    tax_scheme=TaxScheme(
                        id=Id(
                            value='63',
                            scheme_id='urn:oioubl:id:taxschemeid-1.1',
                            scheme_agency_id='320'
                        ),
                        name=Name(
                            value='Moms'
                        )
                    )
                ),
            ],
            party_legal_entity=[
                PartyLegalEntity(
                    registration_name=RegistrationName(
                        value='Gentofte Kommune'
                    ),
                    company_id=CompanyId(
                        value='DK12345678',
                        scheme_id='DK:CVR'
                    )
                ),
            ],
            contact=Contact(
                id=Id(
                    value='12345678'
                ),
                name=Name(
                    value='Sille Schyberg'
                )
            )
        )
    ),
    delivery=[
        Delivery(
            delivery_address=DeliveryAddress(
                address_format_code=AddressFormatCode(
                    value='StructuredDK',
                    list_id='urn:oioubl:codelist:addressformatcode-1.1',
                    list_agency_id='320'
                ),
                street_name=StreetName(
                    value='Bernstorffsvej'
                ),
                building_number=BuildingNumber(
                    value='161'
                ),
                city_name=CityName(
                    value='Charlottenlund'
                ),
                postal_zone=PostalZone(
                    value='2920'
                ),
                address_line=[
                    AddressLine(
                        line=Line(
                            value='IT-afdelingen'
                        )
                    ),
                    AddressLine(
                        line=Line(
                            value='1. sal'
                        )
                    ),
                ],
                country=Country(
                    identification_code=IdentificationCode(
                        value='DK'
                    )
                )
            ),
            requested_delivery_period=RequestedDeliveryPeriod(
                start_date=StartDate(
                    value=XmlDate(2008, 5, 6)
                ),
                start_time=StartTime(
                    value=XmlTime(9, 30, 47, 0, 0)
                ),
                end_date=EndDate(
                    value=XmlDate(2008, 5, 10)
                ),
                end_time=EndTime(
                    value=XmlTime(9, 30, 47, 0, 0)
                )
            )
        ),
    ],
    delivery_terms=DeliveryTerms(
        special_terms=[
            SpecialTerms(
                value='1% reduktion i kontraktsummen pr. dags forsinkelse jf. SKI kontrakt'
            ),
        ]
    ),
    quoted_monetary_total=QuotedMonetaryTotal(
        line_extension_amount=LineExtensionAmount(
            value=Decimal('197750.00'),
            currency_id='DKK'
        ),
        tax_exclusive_amount=TaxExclusiveAmount(
            value=Decimal('49437.50'),
            currency_id='DKK'
        ),
        tax_inclusive_amount=TaxInclusiveAmount(
            value=Decimal('247187.50'),
            currency_id='DKK'
        ),
        payable_amount=PayableAmount(
            value=Decimal('247187.50'),
            currency_id='DKK'
        )
    ),
    quotation_line=[
        QuotationLine(
            id=Id(
                value='1'
            ),
            note=[
                Note(
                    value='Computer'
                ),
            ],
            line_item=LineItem(
                id=Id(
                    value='DELL1052665'
                ),
                quantity=Quantity(
                    value=Decimal('35'),
                    unit_code='EA'
                ),
                line_extension_amount=LineExtensionAmount(
                    value=Decimal('150500.00'),
                    currency_id='DKK'
                ),
                total_tax_amount=TotalTaxAmount(
                    value=Decimal('37625.00'),
                    currency_id='DKK'
                ),
                price=Price(
                    price_amount=PriceAmount(
                        value=Decimal('4300.00'),
                        currency_id='DKK'
                    ),
                    base_quantity=BaseQuantity(
                        value=Decimal('1'),
                        unit_code='EA'
                    )
                ),
                item=Item(
                    description=[
                        Description(
                            value='Stationær computer'
                        ),
                    ],
                    name=Name(
                        value='Dell PrecisionTM  T3400'
                    )
                )
            )
        ),
        QuotationLine(
            id=Id(
                value='2'
            ),
            note=[
                Note(
                    value='Skærm'
                ),
            ],
            line_item=LineItem(
                id=Id(
                    value='DELL2363463'
                ),
                quantity=Quantity(
                    value=Decimal('35'),
                    unit_code='EA'
                ),
                line_extension_amount=LineExtensionAmount(
                    value=Decimal('43750.00'),
                    currency_id='DKK'
                ),
                total_tax_amount=TotalTaxAmount(
                    value=Decimal('10937.50'),
                    currency_id='DKK'
                ),
                price=Price(
                    price_amount=PriceAmount(
                        value=Decimal('1250.00'),
                        currency_id='DKK'
                    ),
                    base_quantity=BaseQuantity(
                        value=Decimal('1'),
                        unit_code='EA'
                    )
                ),
                item=Item(
                    description=[
                        Description(
                            value='Fladskærm'
                        ),
                    ],
                    name=Name(
                        value='FP/BL 1908WFP'
                    )
                )
            )
        ),
        QuotationLine(
            id=Id(
                value='3'
            ),
            note=[
                Note(
                    value='Mus'
                ),
            ],
            line_item=LineItem(
                id=Id(
                    value='DELL2367452'
                ),
                quantity=Quantity(
                    value=Decimal('35'),
                    unit_code='EA'
                ),
                line_extension_amount=LineExtensionAmount(
                    value=Decimal('1750.00'),
                    currency_id='DKK'
                ),
                total_tax_amount=TotalTaxAmount(
                    value=Decimal('437.50'),
                    currency_id='DKK'
                ),
                price=Price(
                    price_amount=PriceAmount(
                        value=Decimal('50.00'),
                        currency_id='DKK'
                    ),
                    base_quantity=BaseQuantity(
                        value=Decimal('1'),
                        unit_code='EA'
                    )
                ),
                item=Item(
                    description=[
                        Description(
                            value='Mus'
                        ),
                    ],
                    name=Name(
                        value='Dell Quietkey USB-tastatur, sort - Dansk (QWERTY)'
                    )
                )
            )
        ),
        QuotationLine(
            id=Id(
                value='4'
            ),
            note=[
                Note(
                    value='Tastatur'
                ),
            ],
            line_item=LineItem(
                id=Id(
                    value='DELL8436783'
                ),
                quantity=Quantity(
                    value=Decimal('35'),
                    unit_code='EA'
                ),
                line_extension_amount=LineExtensionAmount(
                    value=Decimal('1750.00'),
                    currency_id='DKK'
                ),
                total_tax_amount=TotalTaxAmount(
                    value=Decimal('437.50'),
                    currency_id='DKK'
                ),
                price=Price(
                    price_amount=PriceAmount(
                        value=Decimal('50.00'),
                        currency_id='DKK'
                    ),
                    base_quantity=BaseQuantity(
                        value=Decimal('1'),
                        unit_code='EA'
                    )
                ),
                item=Item(
                    description=[
                        Description(
                            value='Tastatur'
                        ),
                    ],
                    name=Name(
                        value='Dell Quietkey USB-tastatur, sort - Dansk (QWERTY)'
                    )
                )
            )
        ),
    ]
)
