from decimal import Decimal
from ubl.models.common.ubl_common_aggregate_components_2_1 import AddressLine
from ubl.models.common.ubl_common_aggregate_components_2_1 import AnticipatedMonetaryTotal
from ubl.models.common.ubl_common_aggregate_components_2_1 import BuyerCustomerParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import BuyersItemIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import Contact
from ubl.models.common.ubl_common_aggregate_components_2_1 import Country
from ubl.models.common.ubl_common_aggregate_components_2_1 import Delivery
from ubl.models.common.ubl_common_aggregate_components_2_1 import DeliveryAddress
from ubl.models.common.ubl_common_aggregate_components_2_1 import DeliveryTerms
from ubl.models.common.ubl_common_aggregate_components_2_1 import Item
from ubl.models.common.ubl_common_aggregate_components_2_1 import LineItem
from ubl.models.common.ubl_common_aggregate_components_2_1 import OrderLine
from ubl.models.common.ubl_common_aggregate_components_2_1 import OriginatorCustomerParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import Party
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyName
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyTaxScheme
from ubl.models.common.ubl_common_aggregate_components_2_1 import PostalAddress
from ubl.models.common.ubl_common_aggregate_components_2_1 import Price
from ubl.models.common.ubl_common_aggregate_components_2_1 import RequestedDeliveryPeriod
from ubl.models.common.ubl_common_aggregate_components_2_1 import SellerSupplierParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import SellersItemIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import TaxScheme
from ubl.models.common.ubl_common_aggregate_components_2_1 import TransactionConditions
from ubl.models.common.ubl_common_basic_components_2_1 import BaseQuantity
from ubl.models.common.ubl_common_basic_components_2_1 import BuildingName
from ubl.models.common.ubl_common_basic_components_2_1 import BuildingNumber
from ubl.models.common.ubl_common_basic_components_2_1 import CityName
from ubl.models.common.ubl_common_basic_components_2_1 import CompanyId
from ubl.models.common.ubl_common_basic_components_2_1 import CopyIndicator
from ubl.models.common.ubl_common_basic_components_2_1 import CountrySubentity
from ubl.models.common.ubl_common_basic_components_2_1 import CustomerAssignedAccountId
from ubl.models.common.ubl_common_basic_components_2_1 import CustomizationId
from ubl.models.common.ubl_common_basic_components_2_1 import Description
from ubl.models.common.ubl_common_basic_components_2_1 import ElectronicMail
from ubl.models.common.ubl_common_basic_components_2_1 import EndDate
from ubl.models.common.ubl_common_basic_components_2_1 import EndTime
from ubl.models.common.ubl_common_basic_components_2_1 import ExemptionReason
from ubl.models.common.ubl_common_basic_components_2_1 import Id
from ubl.models.common.ubl_common_basic_components_2_1 import IdentificationCode
from ubl.models.common.ubl_common_basic_components_2_1 import IssueDate
from ubl.models.common.ubl_common_basic_components_2_1 import Line
from ubl.models.common.ubl_common_basic_components_2_1 import LineExtensionAmount
from ubl.models.common.ubl_common_basic_components_2_1 import LineStatusCode
from ubl.models.common.ubl_common_basic_components_2_1 import Name
from ubl.models.common.ubl_common_basic_components_2_1 import Note
from ubl.models.common.ubl_common_basic_components_2_1 import PayableAmount
from ubl.models.common.ubl_common_basic_components_2_1 import PostalZone
from ubl.models.common.ubl_common_basic_components_2_1 import PriceAmount
from ubl.models.common.ubl_common_basic_components_2_1 import ProfileId
from ubl.models.common.ubl_common_basic_components_2_1 import Quantity
from ubl.models.common.ubl_common_basic_components_2_1 import RegistrationName
from ubl.models.common.ubl_common_basic_components_2_1 import SalesOrderId
from ubl.models.common.ubl_common_basic_components_2_1 import SpecialTerms
from ubl.models.common.ubl_common_basic_components_2_1 import StartDate
from ubl.models.common.ubl_common_basic_components_2_1 import StartTime
from ubl.models.common.ubl_common_basic_components_2_1 import StreetName
from ubl.models.common.ubl_common_basic_components_2_1 import SupplierAssignedAccountId
from ubl.models.common.ubl_common_basic_components_2_1 import TaxTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import Telefax
from ubl.models.common.ubl_common_basic_components_2_1 import Telephone
from ubl.models.common.ubl_common_basic_components_2_1 import TotalTaxAmount
from ubl.models.common.ubl_common_basic_components_2_1 import UblversionId
from ubl.models.common.ubl_common_basic_components_2_1 import Uuid
from ubl.models.maindoc.ubl_order_2_1 import Order
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlTime


obj = Order(
    ublversion_id=UblversionId(
        value='2.0'
    ),
    customization_id=CustomizationId(
        value='urn:oasis:names:specification:ubl:xpath:Order-2.0:sbs-1.0-draft'
    ),
    profile_id=ProfileId(
        value='bpid:urn:oasis:names:draft:bpss:ubl-2-sbs-order-with-simple-response-draft'
    ),
    id=Id(
        value='AEG012345'
    ),
    sales_order_id=SalesOrderId(
        value='CON0095678'
    ),
    copy_indicator=CopyIndicator(
        value=False
    ),
    uuid=Uuid(
        value='6E09886B-DC6E-439F-82D1-7CCAC7F4E3B1'
    ),
    issue_date=IssueDate(
        value=XmlDate(2005, 6, 20)
    ),
    note=[
        Note(
            value='sample'
        ),
    ],
    buyer_customer_party=BuyerCustomerParty(
        customer_assigned_account_id=CustomerAssignedAccountId(
            value='XFB01'
        ),
        supplier_assigned_account_id=SupplierAssignedAccountId(
            value='GT00978567'
        ),
        party=Party(
            party_name=[
                PartyName(
                    name=Name(
                        value='IYT Corporation'
                    )
                ),
            ],
            postal_address=PostalAddress(
                street_name=StreetName(
                    value='Avon Way'
                ),
                building_name=BuildingName(
                    value='Thereabouts'
                ),
                building_number=BuildingNumber(
                    value='56A'
                ),
                city_name=CityName(
                    value='Bridgtow'
                ),
                postal_zone=PostalZone(
                    value='ZZ99 1ZZ'
                ),
                country_subentity=CountrySubentity(
                    value='Avon'
                ),
                address_line=[
                    AddressLine(
                        line=Line(
                            value='3rd Floor, Room 5'
                        )
                    ),
                ],
                country=Country(
                    identification_code=IdentificationCode(
                        value='GB'
                    )
                )
            ),
            party_tax_scheme=[
                PartyTaxScheme(
                    registration_name=RegistrationName(
                        value='Bridgtow District Council'
                    ),
                    company_id=CompanyId(
                        value='12356478'
                    ),
                    exemption_reason=[
                        ExemptionReason(
                            value='Local Authority'
                        ),
                    ],
                    tax_scheme=TaxScheme(
                        id=Id(
                            value='UK VAT'
                        ),
                        tax_type_code=TaxTypeCode(
                            value='VAT'
                        )
                    )
                ),
            ],
            contact=Contact(
                name=Name(
                    value='Mr Fred Churchill'
                ),
                telephone=Telephone(
                    value='0127 2653214'
                ),
                telefax=Telefax(
                    value='0127 2653215'
                ),
                electronic_mail=ElectronicMail(
                    value='fred@iytcorporation.gov.uk'
                )
            )
        )
    ),
    seller_supplier_party=SellerSupplierParty(
        customer_assigned_account_id=CustomerAssignedAccountId(
            value='CO001'
        ),
        party=Party(
            party_name=[
                PartyName(
                    name=Name(
                        value='Consortial'
                    )
                ),
            ],
            postal_address=PostalAddress(
                street_name=StreetName(
                    value='Busy Street'
                ),
                building_name=BuildingName(
                    value='Thereabouts'
                ),
                building_number=BuildingNumber(
                    value='56A'
                ),
                city_name=CityName(
                    value='Farthing'
                ),
                postal_zone=PostalZone(
                    value='AA99 1BB'
                ),
                country_subentity=CountrySubentity(
                    value='Heremouthshire'
                ),
                address_line=[
                    AddressLine(
                        line=Line(
                            value='The Roundabout'
                        )
                    ),
                ],
                country=Country(
                    identification_code=IdentificationCode(
                        value='GB'
                    )
                )
            ),
            party_tax_scheme=[
                PartyTaxScheme(
                    registration_name=RegistrationName(
                        value='Farthing Purchasing Consortium'
                    ),
                    company_id=CompanyId(
                        value='175 269 2355'
                    ),
                    exemption_reason=[
                        ExemptionReason(
                            value='N/A'
                        ),
                    ],
                    tax_scheme=TaxScheme(
                        id=Id(
                            value='VAT'
                        ),
                        tax_type_code=TaxTypeCode(
                            value='VAT'
                        )
                    )
                ),
            ],
            contact=Contact(
                name=Name(
                    value='Mrs Bouquet'
                ),
                telephone=Telephone(
                    value='0158 1233714'
                ),
                telefax=Telefax(
                    value='0158 1233856'
                ),
                electronic_mail=ElectronicMail(
                    value='bouquet@fpconsortial.co.uk'
                )
            )
        )
    ),
    originator_customer_party=OriginatorCustomerParty(
        party=Party(
            party_name=[
                PartyName(
                    name=Name(
                        value='The Terminus'
                    )
                ),
            ],
            postal_address=PostalAddress(
                street_name=StreetName(
                    value='Avon Way'
                ),
                building_name=BuildingName(
                    value='Thereabouts'
                ),
                building_number=BuildingNumber(
                    value='56A'
                ),
                city_name=CityName(
                    value='Bridgtow'
                ),
                postal_zone=PostalZone(
                    value='ZZ99 1ZZ'
                ),
                country_subentity=CountrySubentity(
                    value='Avon'
                ),
                address_line=[
                    AddressLine(
                        line=Line(
                            value='3rd Floor, Room 5'
                        )
                    ),
                ],
                country=Country(
                    identification_code=IdentificationCode(
                        value='GB'
                    )
                )
            ),
            party_tax_scheme=[
                PartyTaxScheme(
                    registration_name=RegistrationName(
                        value='Bridgtow District Council'
                    ),
                    company_id=CompanyId(
                        value='12356478'
                    ),
                    exemption_reason=[
                        ExemptionReason(
                            value='Local Authority'
                        ),
                    ],
                    tax_scheme=TaxScheme(
                        id=Id(
                            value='UK VAT'
                        ),
                        tax_type_code=TaxTypeCode(
                            value='VAT'
                        )
                    )
                ),
            ],
            contact=Contact(
                name=Name(
                    value='S Massiah'
                ),
                telephone=Telephone(
                    value='0127 98876545'
                ),
                telefax=Telefax(
                    value='0127 98876546'
                ),
                electronic_mail=ElectronicMail(
                    value='smassiah@the-email.co.uk'
                )
            )
        )
    ),
    delivery=[
        Delivery(
            delivery_address=DeliveryAddress(
                street_name=StreetName(
                    value='Avon Way'
                ),
                building_name=BuildingName(
                    value='Thereabouts'
                ),
                building_number=BuildingNumber(
                    value='56A'
                ),
                city_name=CityName(
                    value='Bridgtow'
                ),
                postal_zone=PostalZone(
                    value='ZZ99 1ZZ'
                ),
                country_subentity=CountrySubentity(
                    value='Avon'
                ),
                address_line=[
                    AddressLine(
                        line=Line(
                            value='3rd Floor, Room 5'
                        )
                    ),
                ],
                country=Country(
                    identification_code=IdentificationCode(
                        value='GB'
                    )
                )
            ),
            requested_delivery_period=RequestedDeliveryPeriod(
                start_date=StartDate(
                    value=XmlDate(2005, 6, 29)
                ),
                start_time=StartTime(
                    value=XmlTime(9, 30, 47, 0, 0)
                ),
                end_date=EndDate(
                    value=XmlDate(2005, 6, 29)
                ),
                end_time=EndTime(
                    value=XmlTime(9, 30, 47, 0, 0)
                )
            )
        ),
    ],
    delivery_terms=[
        DeliveryTerms(
            special_terms=[
                SpecialTerms(
                    value='1% deduction for late delivery as per contract'
                ),
            ]
        ),
    ],
    transaction_conditions=TransactionConditions(
        description=[
            Description(
                value='order response required; payment is by BACS or by cheque'
            ),
        ]
    ),
    anticipated_monetary_total=AnticipatedMonetaryTotal(
        line_extension_amount=LineExtensionAmount(
            value=Decimal('100.00'),
            currency_id='GBP'
        ),
        payable_amount=PayableAmount(
            value=Decimal('100.00'),
            currency_id='GBP'
        )
    ),
    order_line=[
        OrderLine(
            note=[
                Note(
                    value='this is an illustrative order line'
                ),
            ],
            line_item=LineItem(
                id=Id(
                    value='1'
                ),
                sales_order_id=SalesOrderId(
                    value='A'
                ),
                line_status_code=LineStatusCode(
                    value='NoStatus'
                ),
                quantity=Quantity(
                    value=Decimal('100'),
                    unit_code='KGM'
                ),
                line_extension_amount=LineExtensionAmount(
                    value=Decimal('100.00'),
                    currency_id='GBP'
                ),
                total_tax_amount=TotalTaxAmount(
                    value=Decimal('17.50'),
                    currency_id='GBP'
                ),
                price=Price(
                    price_amount=PriceAmount(
                        value=Decimal('100.00'),
                        currency_id='GBP'
                    ),
                    base_quantity=BaseQuantity(
                        value=Decimal('1'),
                        unit_code='KGM'
                    )
                ),
                item=Item(
                    description=[
                        Description(
                            value='Acme beeswax'
                        ),
                    ],
                    name=Name(
                        value='beeswax'
                    ),
                    buyers_item_identification=BuyersItemIdentification(
                        id=Id(
                            value='6578489'
                        )
                    ),
                    sellers_item_identification=SellersItemIdentification(
                        id=Id(
                            value='17589683'
                        )
                    )
                )
            )
        ),
    ]
)
