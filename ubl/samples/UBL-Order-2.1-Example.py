from decimal import Decimal
from ubl.models.common.ubl_common_aggregate_components_2_1 import AdditionalDocumentReference
from ubl.models.common.ubl_common_aggregate_components_2_1 import AdditionalItemProperty
from ubl.models.common.ubl_common_aggregate_components_2_1 import Address
from ubl.models.common.ubl_common_aggregate_components_2_1 import AllowanceCharge
from ubl.models.common.ubl_common_aggregate_components_2_1 import AnticipatedMonetaryTotal
from ubl.models.common.ubl_common_aggregate_components_2_1 import Attachment
from ubl.models.common.ubl_common_aggregate_components_2_1 import BuyerCustomerParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import Contact
from ubl.models.common.ubl_common_aggregate_components_2_1 import Contract
from ubl.models.common.ubl_common_aggregate_components_2_1 import Country
from ubl.models.common.ubl_common_aggregate_components_2_1 import Delivery
from ubl.models.common.ubl_common_aggregate_components_2_1 import DeliveryContact
from ubl.models.common.ubl_common_aggregate_components_2_1 import DeliveryLocation
from ubl.models.common.ubl_common_aggregate_components_2_1 import DeliveryParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import DeliveryTerms
from ubl.models.common.ubl_common_aggregate_components_2_1 import ExternalReference
from ubl.models.common.ubl_common_aggregate_components_2_1 import Item
from ubl.models.common.ubl_common_aggregate_components_2_1 import LineItem
from ubl.models.common.ubl_common_aggregate_components_2_1 import OrderDocumentReference
from ubl.models.common.ubl_common_aggregate_components_2_1 import OrderLine
from ubl.models.common.ubl_common_aggregate_components_2_1 import OriginatorCustomerParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import OriginatorDocumentReference
from ubl.models.common.ubl_common_aggregate_components_2_1 import OriginatorParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import Party
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyLegalEntity
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyName
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyTaxScheme
from ubl.models.common.ubl_common_aggregate_components_2_1 import Person
from ubl.models.common.ubl_common_aggregate_components_2_1 import PostalAddress
from ubl.models.common.ubl_common_aggregate_components_2_1 import Price
from ubl.models.common.ubl_common_aggregate_components_2_1 import QuotationDocumentReference
from ubl.models.common.ubl_common_aggregate_components_2_1 import RegistrationAddress
from ubl.models.common.ubl_common_aggregate_components_2_1 import RequestedDeliveryPeriod
from ubl.models.common.ubl_common_aggregate_components_2_1 import SellerSupplierParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import SellersItemIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import StandardItemIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import TaxScheme
from ubl.models.common.ubl_common_aggregate_components_2_1 import TaxTotal
from ubl.models.common.ubl_common_aggregate_components_2_1 import ValidityPeriod
from ubl.models.common.ubl_common_basic_components_2_1 import AccountingCostCode
from ubl.models.common.ubl_common_basic_components_2_1 import AdditionalStreetName
from ubl.models.common.ubl_common_basic_components_2_1 import AllowanceChargeReason
from ubl.models.common.ubl_common_basic_components_2_1 import AllowanceTotalAmount
from ubl.models.common.ubl_common_basic_components_2_1 import Amount
from ubl.models.common.ubl_common_basic_components_2_1 import BaseQuantity
from ubl.models.common.ubl_common_basic_components_2_1 import BuildingNumber
from ubl.models.common.ubl_common_basic_components_2_1 import ChargeTotalAmount
from ubl.models.common.ubl_common_basic_components_2_1 import CityName
from ubl.models.common.ubl_common_basic_components_2_1 import CompanyId
from ubl.models.common.ubl_common_basic_components_2_1 import ContractType
from ubl.models.common.ubl_common_basic_components_2_1 import CountrySubentity
from ubl.models.common.ubl_common_basic_components_2_1 import CustomizationId
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
from ubl.models.common.ubl_common_basic_components_2_1 import JobTitle
from ubl.models.common.ubl_common_basic_components_2_1 import LineExtensionAmount
from ubl.models.common.ubl_common_basic_components_2_1 import MiddleName
from ubl.models.common.ubl_common_basic_components_2_1 import Name
from ubl.models.common.ubl_common_basic_components_2_1 import Note
from ubl.models.common.ubl_common_basic_components_2_1 import PayableAmount
from ubl.models.common.ubl_common_basic_components_2_1 import PostalZone
from ubl.models.common.ubl_common_basic_components_2_1 import Postbox
from ubl.models.common.ubl_common_basic_components_2_1 import PriceAmount
from ubl.models.common.ubl_common_basic_components_2_1 import ProfileId
from ubl.models.common.ubl_common_basic_components_2_1 import Quantity
from ubl.models.common.ubl_common_basic_components_2_1 import RegistrationName
from ubl.models.common.ubl_common_basic_components_2_1 import SpecialTerms
from ubl.models.common.ubl_common_basic_components_2_1 import StreetName
from ubl.models.common.ubl_common_basic_components_2_1 import TaxAmount
from ubl.models.common.ubl_common_basic_components_2_1 import Telefax
from ubl.models.common.ubl_common_basic_components_2_1 import Telephone
from ubl.models.common.ubl_common_basic_components_2_1 import TotalTaxAmount
from ubl.models.common.ubl_common_basic_components_2_1 import UblversionId
from ubl.models.common.ubl_common_basic_components_2_1 import Uri
from ubl.models.common.ubl_common_basic_components_2_1 import Value
from ubl.models.maindoc.ubl_order_2_1 import Order
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlTime


obj = Order(
    ublversion_id=UblversionId(
        value="2.1"
    ),
    customization_id=CustomizationId(
        value="urn:www.cenbii.eu:transaction:biicoretrdm001:ver1.0"
    ),
    profile_id=ProfileId(
        value="urn:www.cenbii.eu:profile:BII01:ver1.0",
        scheme_id="Profile",
        scheme_agency_id="BII"
    ),
    id=Id(
        value="34"
    ),
    issue_date=XmlDate(2010, 1, 20),
    issue_time=XmlTime(12, 30, 0, 0),
    note=[
        Note(
            value="Information text for the whole order"
        ),
    ],
    document_currency_code=DocumentCurrencyCode(
        value="SEK"
    ),
    accounting_cost_code=AccountingCostCode(
        value="Project123"
    ),
    validity_period=[
        ValidityPeriod(
            end_date=XmlDate(2010, 1, 31)
        ),
    ],
    quotation_document_reference=QuotationDocumentReference(
        id=Id(
            value="QuoteID123"
        )
    ),
    order_document_reference=[
        OrderDocumentReference(
            id=Id(
                value="RjectedOrderID123"
            )
        ),
    ],
    originator_document_reference=OriginatorDocumentReference(
        id=Id(
            value="MAFO"
        )
    ),
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
    contract=[
        Contract(
            id=Id(
                value="34322"
            ),
            contract_type=ContractType(
                value="FrameworkAgreementID123"
            )
        ),
    ],
    buyer_customer_party=BuyerCustomerParty(
        party=Party(
            endpoint_id=EndpointId(
                value="7300072311115",
                scheme_id="GLN",
                scheme_agency_id="9"
            ),
            party_identification=[
                PartyIdentification(
                    id=Id(
                        value="7300070011115",
                        scheme_id="GLN",
                        scheme_agency_id="9"
                    )
                ),
                PartyIdentification(
                    id=Id(
                        value="PartyID123"
                    )
                ),
            ],
            party_name=[
                PartyName(
                    name=Name(
                        value="Johnssons byggvaror"
                    )
                ),
            ],
            postal_address=PostalAddress(
                id=Id(
                    value="1234567890123",
                    scheme_id="GLN",
                    scheme_agency_id="9"
                ),
                postbox=Postbox(
                    value="PoBox123"
                ),
                street_name=StreetName(
                    value="R\xe5dhusgatan"
                ),
                additional_street_name=AdditionalStreetName(
                    value="2nd floor"
                ),
                building_number=BuildingNumber(
                    value="5"
                ),
                department=Department(
                    value="Purchasing department"
                ),
                city_name=CityName(
                    value="Stockholm"
                ),
                postal_zone=PostalZone(
                    value="11000"
                ),
                country_subentity=CountrySubentity(
                    value="RegionX"
                ),
                country=Country(
                    identification_code=IdentificationCode(
                        value="SE"
                    )
                )
            ),
            party_tax_scheme=[
                PartyTaxScheme(
                    registration_name=RegistrationName(
                        value="Herra Johnssons byggvaror AS"
                    ),
                    company_id=CompanyId(
                        value="SE1234567801"
                    ),
                    registration_address=RegistrationAddress(
                        city_name=CityName(
                            value="Stockholm"
                        ),
                        country=Country(
                            identification_code=IdentificationCode(
                                value="SE"
                            )
                        )
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
                        value="Johnssons Byggvaror AB"
                    ),
                    company_id=CompanyId(
                        value="5532331183",
                        scheme_id="SE:ORGNR"
                    ),
                    registration_address=RegistrationAddress(
                        city_name=CityName(
                            value="Stockholm"
                        ),
                        country_subentity=CountrySubentity(
                            value="RegionX"
                        ),
                        country=Country(
                            identification_code=IdentificationCode(
                                value="SE"
                            )
                        )
                    )
                ),
            ],
            contact=Contact(
                telephone=Telephone(
                    value="123456"
                ),
                telefax=Telefax(
                    value="123456"
                ),
                electronic_mail=ElectronicMail(
                    value="pelle@johnsson.se"
                )
            ),
            person=[
                Person(
                    first_name=FirstName(
                        value="Pelle"
                    ),
                    family_name=FamilyName(
                        value="Svensson"
                    ),
                    middle_name=MiddleName(
                        value="X"
                    ),
                    job_title=JobTitle(
                        value="Boss"
                    )
                ),
            ]
        ),
        delivery_contact=DeliveryContact(
            name=Name(
                value="Eva Johnsson"
            ),
            telephone=Telephone(
                value="1234356"
            ),
            telefax=Telefax(
                value="123455"
            ),
            electronic_mail=ElectronicMail(
                value="eva@johnsson.se"
            )
        )
    ),
    seller_supplier_party=SellerSupplierParty(
        party=Party(
            endpoint_id=EndpointId(
                value="7302347231111",
                scheme_id="GLN",
                scheme_agency_id="9"
            ),
            party_identification=[
                PartyIdentification(
                    id=Id(
                        value="SellerPartyID123"
                    )
                ),
            ],
            party_name=[
                PartyName(
                    name=Name(
                        value="Moderna Produkter AB"
                    )
                ),
            ],
            postal_address=PostalAddress(
                id=Id(
                    value="0987654321123",
                    scheme_id="GLN",
                    scheme_agency_id="9"
                ),
                postbox=Postbox(
                    value="321"
                ),
                street_name=StreetName(
                    value="Kungsgatan"
                ),
                additional_street_name=AdditionalStreetName(
                    value="suite12"
                ),
                building_number=BuildingNumber(
                    value="22"
                ),
                department=Department(
                    value="Sales department"
                ),
                city_name=CityName(
                    value="Stockholm"
                ),
                postal_zone=PostalZone(
                    value="11000"
                ),
                country_subentity=CountrySubentity(
                    value="RegionX"
                ),
                country=Country(
                    identification_code=IdentificationCode(
                        value="SE"
                    )
                )
            ),
            party_legal_entity=[
                PartyLegalEntity(
                    registration_name=RegistrationName(
                        value="Moderna Produkter AB"
                    ),
                    company_id=CompanyId(
                        value="5532332283",
                        scheme_id="SE:ORGNR"
                    ),
                    registration_address=RegistrationAddress(
                        city_name=CityName(
                            value="Stockholm"
                        ),
                        country_subentity=CountrySubentity(
                            value="RegionX"
                        ),
                        country=Country(
                            identification_code=IdentificationCode(
                                value="SE"
                            )
                        )
                    )
                ),
            ],
            contact=Contact(
                telephone=Telephone(
                    value="34557"
                ),
                telefax=Telefax(
                    value="3456767"
                ),
                electronic_mail=ElectronicMail(
                    value="lars@moderna.se"
                )
            ),
            person=[
                Person(
                    first_name=FirstName(
                        value="Lars"
                    ),
                    family_name=FamilyName(
                        value="Petersen"
                    ),
                    middle_name=MiddleName(
                        value="M"
                    ),
                    job_title=JobTitle(
                        value="Sales manager"
                    )
                ),
            ]
        )
    ),
    originator_customer_party=OriginatorCustomerParty(
        party=Party(
            party_identification=[
                PartyIdentification(
                    id=Id(
                        value="0987678321123",
                        scheme_id="GLN",
                        scheme_agency_id="9"
                    )
                ),
            ],
            party_name=[
                PartyName(
                    name=Name(
                        value="Moderna Produkter AB"
                    )
                ),
            ],
            contact=Contact(
                telephone=Telephone(
                    value="346788"
                ),
                telefax=Telefax(
                    value="8567443"
                ),
                electronic_mail=ElectronicMail(
                    value="sven@moderna.se"
                )
            ),
            person=[
                Person(
                    first_name=FirstName(
                        value="Sven"
                    ),
                    family_name=FamilyName(
                        value="Pereson"
                    ),
                    middle_name=MiddleName(
                        value="N"
                    ),
                    job_title=JobTitle(
                        value="Stuffuser"
                    )
                ),
            ]
        )
    ),
    delivery=[
        Delivery(
            delivery_location=DeliveryLocation(
                address=Address(
                    id=Id(
                        value="1234567890123",
                        scheme_id="GLN",
                        scheme_agency_id="9"
                    ),
                    postbox=Postbox(
                        value="123"
                    ),
                    street_name=StreetName(
                        value="R\xe5dhusgatan"
                    ),
                    additional_street_name=AdditionalStreetName(
                        value="2nd floor"
                    ),
                    building_number=BuildingNumber(
                        value="5"
                    ),
                    department=Department(
                        value="Purchasing department"
                    ),
                    city_name=CityName(
                        value="Stockholm"
                    ),
                    postal_zone=PostalZone(
                        value="11000"
                    ),
                    country_subentity=CountrySubentity(
                        value="RegionX"
                    ),
                    country=Country(
                        identification_code=IdentificationCode(
                            value="SE"
                        )
                    )
                )
            ),
            requested_delivery_period=RequestedDeliveryPeriod(
                start_date=XmlDate(2010, 2, 10),
                end_date=XmlDate(2010, 2, 25)
            ),
            delivery_party=DeliveryParty(
                party_identification=[
                    PartyIdentification(
                        id=Id(
                            value="67654328394567",
                            scheme_id="GLN",
                            scheme_agency_id="9"
                        )
                    ),
                ],
                party_name=[
                    PartyName(
                        name=Name(
                            value="Swedish trucking"
                        )
                    ),
                ],
                contact=Contact(
                    name=Name(
                        value="Per"
                    ),
                    telephone=Telephone(
                        value="987098709"
                    ),
                    telefax=Telefax(
                        value="34673435"
                    ),
                    electronic_mail=ElectronicMail(
                        value="bill@svetruck.se"
                    )
                )
            )
        ),
    ],
    delivery_terms=[
        DeliveryTerms(
            id=Id(
                value="FOT",
                scheme_id="IMCOTERM",
                scheme_agency_id="6"
            ),
            special_terms=[
                SpecialTerms(
                    value="CAD"
                ),
            ],
            delivery_location=DeliveryLocation(
                id=Id(
                    value="STO"
                )
            )
        ),
    ],
    allowance_charge=[
        AllowanceCharge(
            charge_indicator=True,
            allowance_charge_reason=[
                AllowanceChargeReason(
                    value="Transport documents"
                ),
            ],
            amount=Amount(
                value=Decimal("100"),
                currency_id="SEK"
            )
        ),
        AllowanceCharge(
            charge_indicator=False,
            allowance_charge_reason=[
                AllowanceChargeReason(
                    value="Total order value discount"
                ),
            ],
            amount=Amount(
                value=Decimal("100"),
                currency_id="SEK"
            )
        ),
    ],
    tax_total=[
        TaxTotal(
            tax_amount=TaxAmount(
                value=Decimal("100"),
                currency_id="SEK"
            )
        ),
    ],
    anticipated_monetary_total=AnticipatedMonetaryTotal(
        line_extension_amount=LineExtensionAmount(
            value=Decimal("6225"),
            currency_id="SEK"
        ),
        allowance_total_amount=AllowanceTotalAmount(
            value=Decimal("100"),
            currency_id="SEK"
        ),
        charge_total_amount=ChargeTotalAmount(
            value=Decimal("100"),
            currency_id="SEK"
        ),
        payable_amount=PayableAmount(
            value=Decimal("6225"),
            currency_id="SEK"
        )
    ),
    order_line=[
        OrderLine(
            note=[
                Note(
                    value="Freetext note on line 1"
                ),
            ],
            line_item=LineItem(
                id=Id(
                    value="1"
                ),
                quantity=Quantity(
                    value=Decimal("120"),
                    unit_code="LTR"
                ),
                line_extension_amount=LineExtensionAmount(
                    value=Decimal("6000"),
                    currency_id="SEK"
                ),
                total_tax_amount=TotalTaxAmount(
                    value=Decimal("10"),
                    currency_id="SEK"
                ),
                partial_delivery_indicator=False,
                accounting_cost_code=AccountingCostCode(
                    value="ProjectID123"
                ),
                delivery=[
                    Delivery(
                        requested_delivery_period=RequestedDeliveryPeriod(
                            start_date=XmlDate(2010, 2, 10),
                            end_date=XmlDate(2010, 2, 25)
                        )
                    ),
                ],
                originator_party=OriginatorParty(
                    party_identification=[
                        PartyIdentification(
                            id=Id(
                                value="EmployeeXXX",
                                scheme_id="ZZZ",
                                scheme_agency_id="ZZZ"
                            )
                        ),
                    ],
                    party_name=[
                        PartyName(
                            name=Name(
                                value="Josef K."
                            )
                        ),
                    ]
                ),
                price=Price(
                    price_amount=PriceAmount(
                        value=Decimal("50"),
                        currency_id="SEK"
                    ),
                    base_quantity=BaseQuantity(
                        value=Decimal("1"),
                        unit_code="LTR"
                    )
                ),
                item=Item(
                    description=[
                        Description(
                            value="Red paint"
                        ),
                    ],
                    name=Name(
                        value="Falu R\xf6df\xe4rg"
                    ),
                    sellers_item_identification=SellersItemIdentification(
                        id=Id(
                            value="SItemNo001"
                        )
                    ),
                    standard_item_identification=StandardItemIdentification(
                        id=Id(
                            value="1234567890123",
                            scheme_id="GTIN",
                            scheme_agency_id="6"
                        )
                    ),
                    additional_item_property=[
                        AdditionalItemProperty(
                            name=Name(
                                value="Paint type"
                            ),
                            value=Value(
                                value="Acrylic"
                            )
                        ),
                        AdditionalItemProperty(
                            name=Name(
                                value="Solvant"
                            ),
                            value=Value(
                                value="Water"
                            )
                        ),
                    ]
                )
            )
        ),
        OrderLine(
            note=[
                Note(
                    value="Freetext note on line 2"
                ),
            ],
            line_item=LineItem(
                id=Id(
                    value="2"
                ),
                quantity=Quantity(
                    value=Decimal("15"),
                    unit_code="C62"
                ),
                line_extension_amount=LineExtensionAmount(
                    value=Decimal("225"),
                    currency_id="SEK"
                ),
                total_tax_amount=TotalTaxAmount(
                    value=Decimal("10"),
                    currency_id="SEK"
                ),
                partial_delivery_indicator=False,
                accounting_cost_code=AccountingCostCode(
                    value="ProjectID123"
                ),
                delivery=[
                    Delivery(
                        requested_delivery_period=RequestedDeliveryPeriod(
                            start_date=XmlDate(2010, 2, 10),
                            end_date=XmlDate(2010, 2, 25)
                        )
                    ),
                ],
                originator_party=OriginatorParty(
                    party_identification=[
                        PartyIdentification(
                            id=Id(
                                value="EmployeeXXX",
                                scheme_id="ZZZ",
                                scheme_agency_id="ZZZ"
                            )
                        ),
                    ],
                    party_name=[
                        PartyName(
                            name=Name(
                                value="Josef K."
                            )
                        ),
                    ]
                ),
                price=Price(
                    price_amount=PriceAmount(
                        value=Decimal("15"),
                        currency_id="SEK"
                    ),
                    base_quantity=BaseQuantity(
                        value=Decimal("1"),
                        unit_code="C62"
                    )
                ),
                item=Item(
                    description=[
                        Description(
                            value="Very good pencils for red paint."
                        ),
                    ],
                    name=Name(
                        value="Pensel 20 mm"
                    ),
                    sellers_item_identification=SellersItemIdentification(
                        id=Id(
                            value="SItemNo011"
                        )
                    ),
                    standard_item_identification=StandardItemIdentification(
                        id=Id(
                            value="123452340123",
                            scheme_id="GTIN",
                            scheme_agency_id="6"
                        )
                    ),
                    additional_item_property=[
                        AdditionalItemProperty(
                            name=Name(
                                value="Hair color"
                            ),
                            value=Value(
                                value="Black"
                            )
                        ),
                        AdditionalItemProperty(
                            name=Name(
                                value="Width"
                            ),
                            value=Value(
                                value="20mm"
                            )
                        ),
                    ]
                )
            )
        ),
    ]
)
