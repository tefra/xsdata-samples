from decimal import Decimal
from ubl.models.common.ubl_common_aggregate_components_2_1 import AddressLine
from ubl.models.common.ubl_common_aggregate_components_2_1 import BuyersItemIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import Consignment
from ubl.models.common.ubl_common_aggregate_components_2_1 import Contact
from ubl.models.common.ubl_common_aggregate_components_2_1 import Country
from ubl.models.common.ubl_common_aggregate_components_2_1 import Delivery
from ubl.models.common.ubl_common_aggregate_components_2_1 import DeliveryAddress
from ubl.models.common.ubl_common_aggregate_components_2_1 import DeliveryCustomerParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import DespatchLine
from ubl.models.common.ubl_common_aggregate_components_2_1 import DespatchSupplierParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import Item
from ubl.models.common.ubl_common_aggregate_components_2_1 import ItemInstance
from ubl.models.common.ubl_common_aggregate_components_2_1 import LotIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import OrderLineReference
from ubl.models.common.ubl_common_aggregate_components_2_1 import OrderReference
from ubl.models.common.ubl_common_aggregate_components_2_1 import Party
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyName
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyTaxScheme
from ubl.models.common.ubl_common_aggregate_components_2_1 import PostalAddress
from ubl.models.common.ubl_common_aggregate_components_2_1 import RequestedDeliveryPeriod
from ubl.models.common.ubl_common_aggregate_components_2_1 import SellersItemIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import Shipment
from ubl.models.common.ubl_common_aggregate_components_2_1 import TaxScheme
from ubl.models.common.ubl_common_basic_components_2_1 import BackorderQuantity
from ubl.models.common.ubl_common_basic_components_2_1 import BackorderReason
from ubl.models.common.ubl_common_basic_components_2_1 import BuildingName
from ubl.models.common.ubl_common_basic_components_2_1 import BuildingNumber
from ubl.models.common.ubl_common_basic_components_2_1 import CityName
from ubl.models.common.ubl_common_basic_components_2_1 import CompanyId
from ubl.models.common.ubl_common_basic_components_2_1 import CountrySubentity
from ubl.models.common.ubl_common_basic_components_2_1 import CustomerAssignedAccountId
from ubl.models.common.ubl_common_basic_components_2_1 import CustomizationId
from ubl.models.common.ubl_common_basic_components_2_1 import DeliveredQuantity
from ubl.models.common.ubl_common_basic_components_2_1 import Description
from ubl.models.common.ubl_common_basic_components_2_1 import DespatchAdviceTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import DocumentStatusCode
from ubl.models.common.ubl_common_basic_components_2_1 import ElectronicMail
from ubl.models.common.ubl_common_basic_components_2_1 import ExemptionReason
from ubl.models.common.ubl_common_basic_components_2_1 import Id
from ubl.models.common.ubl_common_basic_components_2_1 import IdentificationCode
from ubl.models.common.ubl_common_basic_components_2_1 import Line
from ubl.models.common.ubl_common_basic_components_2_1 import LineId
from ubl.models.common.ubl_common_basic_components_2_1 import LineStatusCode
from ubl.models.common.ubl_common_basic_components_2_1 import LotNumberId
from ubl.models.common.ubl_common_basic_components_2_1 import Name
from ubl.models.common.ubl_common_basic_components_2_1 import Note
from ubl.models.common.ubl_common_basic_components_2_1 import PostalZone
from ubl.models.common.ubl_common_basic_components_2_1 import ProfileId
from ubl.models.common.ubl_common_basic_components_2_1 import RegistrationName
from ubl.models.common.ubl_common_basic_components_2_1 import SalesOrderId
from ubl.models.common.ubl_common_basic_components_2_1 import SalesOrderLineId
from ubl.models.common.ubl_common_basic_components_2_1 import StreetName
from ubl.models.common.ubl_common_basic_components_2_1 import SupplierAssignedAccountId
from ubl.models.common.ubl_common_basic_components_2_1 import TaxTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import Telefax
from ubl.models.common.ubl_common_basic_components_2_1 import Telephone
from ubl.models.common.ubl_common_basic_components_2_1 import UblversionId
from ubl.models.common.ubl_common_basic_components_2_1 import Uuid
from ubl.models.maindoc.ubl_despatch_advice_2_1 import DespatchAdvice
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlTime


obj = DespatchAdvice(
    ublversion_id=UblversionId(
        value='2.0'
    ),
    customization_id=CustomizationId(
        value='urn:oasis:names:specification:ubl:xpath:DespatchAdvice-2.0:sbs-1.0-draft'
    ),
    profile_id=ProfileId(
        value='bpid:urn:oasis:names:draft:bpss:ubl-2-sbs-despatch-advice-notification-draft'
    ),
    id=Id(
        value='565899'
    ),
    copy_indicator=False,
    uuid=Uuid(
        value='88C7280E-8F10-419F-9949-8EFFFA2842B8'
    ),
    issue_date=XmlDate(2005, 6, 20),
    document_status_code=DocumentStatusCode(
        value='NoStatus'
    ),
    despatch_advice_type_code=DespatchAdviceTypeCode(
        value='delivery'
    ),
    note=[
        Note(
            value='sample'
        ),
    ],
    order_reference=[
        OrderReference(
            id=Id(
                value='AEG012345'
            ),
            sales_order_id=SalesOrderId(
                value='CON0095678'
            ),
            uuid=Uuid(
                value='6E09886B-DC6E-439F-82D1-7CCAC7F4E3B1'
            ),
            issue_date=XmlDate(2005, 6, 20)
        ),
    ],
    despatch_supplier_party=DespatchSupplierParty(
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
    delivery_customer_party=DeliveryCustomerParty(
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
    shipment=Shipment(
        id=Id(
            value='1'
        ),
        consignment=[
            Consignment(
                id=Id(
                    value='1'
                )
            ),
        ],
        delivery=Delivery(
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
                start_date=XmlDate(2005, 6, 20),
                start_time=XmlTime(10, 30, 47, 0, 0),
                end_date=XmlDate(2005, 6, 21),
                end_time=XmlTime(10, 30, 47, 0, 0)
            )
        )
    ),
    despatch_line=[
        DespatchLine(
            id=Id(
                value='1'
            ),
            note=[
                Note(
                    value='Mrs Green agreed to waive charge'
                ),
            ],
            line_status_code=LineStatusCode(
                value='NoStatus'
            ),
            delivered_quantity=DeliveredQuantity(
                value=Decimal('90'),
                unit_code='KGM'
            ),
            backorder_quantity=BackorderQuantity(
                value=Decimal('10'),
                unit_code='KGM'
            ),
            backorder_reason=[
                BackorderReason(
                    value='lack of stock as explained on telephone today'
                ),
            ],
            order_line_reference=[
                OrderLineReference(
                    line_id=LineId(
                        value='1'
                    ),
                    sales_order_line_id=SalesOrderLineId(
                        value='A'
                    ),
                    order_reference=OrderReference(
                        id=Id(
                            value='AEG012345'
                        ),
                        sales_order_id=SalesOrderId(
                            value='CON0095678'
                        ),
                        uuid=Uuid(
                            value='6E09886B-DC6E-439F-82D1-7CCAC7F4E3B1'
                        ),
                        issue_date=XmlDate(2005, 6, 20)
                    )
                ),
            ],
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
                ),
                item_instance=[
                    ItemInstance(
                        lot_identification=LotIdentification(
                            lot_number_id=LotNumberId(
                                value='546378239'
                            ),
                            expiry_date=XmlDate(2010, 1, 1)
                        )
                    ),
                ]
            )
        ),
    ]
)
