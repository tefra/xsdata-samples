from decimal import Decimal
from ubl.models.common.ubl_common_aggregate_components_2_1 import AddressLine
from ubl.models.common.ubl_common_aggregate_components_2_1 import AnticipatedMonetaryTotal
from ubl.models.common.ubl_common_aggregate_components_2_1 import BuyerCustomerParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import BuyersItemIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import Contact
from ubl.models.common.ubl_common_aggregate_components_2_1 import Country
from ubl.models.common.ubl_common_aggregate_components_2_1 import Delivery
from ubl.models.common.ubl_common_aggregate_components_2_1 import DeliveryAddress
from ubl.models.common.ubl_common_aggregate_components_2_1 import DeliveryLocation
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
from ubl.models.common.ubl_common_basic_components_2_1 import CountrySubentityCode
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
from ubl.models.common.ubl_common_basic_components_2_1 import StartDate
from ubl.models.common.ubl_common_basic_components_2_1 import StartTime
from ubl.models.common.ubl_common_basic_components_2_1 import StreetName
from ubl.models.common.ubl_common_basic_components_2_1 import SupplierAssignedAccountId
from ubl.models.common.ubl_common_basic_components_2_1 import TaxTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import Telefax
from ubl.models.common.ubl_common_basic_components_2_1 import Telephone
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
        value='urn:oasis:names:specification:ubl:xpath:Order-2.0:samples-2.0-draft'
    ),
    profile_id=ProfileId(
        value='bpid:urn:oasis:names:draft:bpss:ubl-2-sample-international-scenario'
    ),
    id=Id(
        value='AEG012345'
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
            contact=Contact(
                name=Name(
                    value='Mr Fred Churchill'
                ),
                telephone=Telephone(
                    value='+44 127 2653214'
                ),
                telefax=Telefax(
                    value='+44 127 2653215'
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
                    value='Boston Road'
                ),
                building_name=BuildingName(
                    value='Suite M-102'
                ),
                building_number=BuildingNumber(
                    value='630'
                ),
                city_name=CityName(
                    value='Billerica'
                ),
                postal_zone=PostalZone(
                    value='01821'
                ),
                country_subentity=CountrySubentity(
                    value='Massachusetts'
                ),
                country_subentity_code=CountrySubentityCode(
                    value='MA'
                ),
                country=Country(
                    identification_code=IdentificationCode(
                        value='US'
                    )
                )
            ),
            contact=Contact(
                name=Name(
                    value='Mrs Bouquet'
                ),
                telephone=Telephone(
                    value=' +1 158 1233714'
                ),
                telefax=Telefax(
                    value='+ 1 158 1233856'
                ),
                electronic_mail=ElectronicMail(
                    value='bouquet@fpconsortial.com'
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
                    value='+ 44 127 98876545'
                ),
                telefax=Telefax(
                    value='+ 44 127 98876546'
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
                    value=XmlTime(1, 0, 0, 0, 0)
                ),
                end_date=EndDate(
                    value=XmlDate(2005, 6, 30)
                ),
                end_time=EndTime(
                    value=XmlTime(18, 0, 0, 0, 0)
                )
            )
        ),
    ],
    delivery_terms=[
        DeliveryTerms(
            id=Id(
                value='FOB Destination'
            ),
            delivery_location=DeliveryLocation(
                id=Id(
                    value='GBFXT'
                ),
                description=[
                    Description(
                        value='Felixstowe'
                    ),
                ]
            )
        ),
    ],
    transaction_conditions=TransactionConditions(
        description=[
            Description(
                value='Please advise when transport is booked.'
            ),
        ]
    ),
    anticipated_monetary_total=AnticipatedMonetaryTotal(
        line_extension_amount=LineExtensionAmount(
            value=Decimal('1000.00'),
            currency_id='USD'
        ),
        payable_amount=PayableAmount(
            value=Decimal('1000.00'),
            currency_id='USD'
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
                    value=Decimal('1000.00'),
                    currency_id='USD'
                ),
                price=Price(
                    price_amount=PriceAmount(
                        value=Decimal('10.00'),
                        currency_id='USD'
                    ),
                    base_quantity=BaseQuantity(
                        value=Decimal('1'),
                        unit_code='KGM'
                    )
                ),
                item=Item(
                    description=[
                        Description(
                            value='Beeswax'
                        ),
                    ],
                    name=Name(
                        value='Acme Beeswax'
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
