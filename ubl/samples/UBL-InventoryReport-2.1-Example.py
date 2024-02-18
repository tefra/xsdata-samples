from decimal import Decimal
from ubl.models.common.ubl_common_aggregate_components_2_1 import BuyersItemIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import Contact
from ubl.models.common.ubl_common_aggregate_components_2_1 import Country
from ubl.models.common.ubl_common_aggregate_components_2_1 import InventoryPeriod
from ubl.models.common.ubl_common_aggregate_components_2_1 import InventoryReportLine
from ubl.models.common.ubl_common_aggregate_components_2_1 import InventoryReportingParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import Item
from ubl.models.common.ubl_common_aggregate_components_2_1 import Party
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyName
from ubl.models.common.ubl_common_aggregate_components_2_1 import PostalAddress
from ubl.models.common.ubl_common_aggregate_components_2_1 import RetailerCustomerParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import SellerSupplierParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import SellersItemIdentification
from ubl.models.common.ubl_common_basic_components_2_1 import BuildingNumber
from ubl.models.common.ubl_common_basic_components_2_1 import CityName
from ubl.models.common.ubl_common_basic_components_2_1 import CopyIndicator
from ubl.models.common.ubl_common_basic_components_2_1 import Department
from ubl.models.common.ubl_common_basic_components_2_1 import Description
from ubl.models.common.ubl_common_basic_components_2_1 import DocumentCurrencyCode
from ubl.models.common.ubl_common_basic_components_2_1 import ElectronicMail
from ubl.models.common.ubl_common_basic_components_2_1 import EndDate
from ubl.models.common.ubl_common_basic_components_2_1 import Id
from ubl.models.common.ubl_common_basic_components_2_1 import IdentificationCode
from ubl.models.common.ubl_common_basic_components_2_1 import InventoryValueAmount
from ubl.models.common.ubl_common_basic_components_2_1 import IssueDate
from ubl.models.common.ubl_common_basic_components_2_1 import Name
from ubl.models.common.ubl_common_basic_components_2_1 import Note
from ubl.models.common.ubl_common_basic_components_2_1 import PostalZone
from ubl.models.common.ubl_common_basic_components_2_1 import Quantity
from ubl.models.common.ubl_common_basic_components_2_1 import StartDate
from ubl.models.common.ubl_common_basic_components_2_1 import StartTime
from ubl.models.common.ubl_common_basic_components_2_1 import StreetName
from ubl.models.common.ubl_common_basic_components_2_1 import Telefax
from ubl.models.common.ubl_common_basic_components_2_1 import Telephone
from ubl.models.common.ubl_common_basic_components_2_1 import UblversionId
from ubl.models.maindoc.ubl_inventory_report_2_1 import InventoryReport
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlTime


obj = InventoryReport(
    ublversion_id=UblversionId(
        value='2.1'
    ),
    id=Id(
        value='CC2679'
    ),
    copy_indicator=CopyIndicator(
        value=False
    ),
    issue_date=IssueDate(
        value=XmlDate(2010, 4, 12)
    ),
    note=[
        Note(
            value='Report about the quantities on stock.'
        ),
    ],
    document_currency_code=DocumentCurrencyCode(
        value='EUR',
        list_id='ISO 4217 Alpha'
    ),
    inventory_period=InventoryPeriod(
        start_date=StartDate(
            value=XmlDate(2010, 4, 11)
        ),
        start_time=StartTime(
            value=XmlTime(14, 0, 0, 0)
        ),
        end_date=EndDate(
            value=XmlDate(2010, 4, 11)
        )
    ),
    retailer_customer_party=RetailerCustomerParty(
        party=Party(
            party_name=[
                PartyName(
                    name=Name(
                        value='Beta Shop'
                    )
                ),
            ],
            postal_address=PostalAddress(
                street_name=StreetName(
                    value='Via Emilia'
                ),
                building_number=BuildingNumber(
                    value='1'
                ),
                city_name=CityName(
                    value='Modena'
                ),
                postal_zone=PostalZone(
                    value='41121'
                ),
                country=Country(
                    identification_code=IdentificationCode(
                        value='IT'
                    ),
                    name=Name(
                        value='Italy'
                    )
                )
            ),
            contact=Contact(
                name=Name(
                    value='Mr Delta'
                ),
                telephone=Telephone(
                    value='0039 059 33000000'
                ),
                telefax=Telefax(
                    value='0039 059 33000055'
                ),
                electronic_mail=ElectronicMail(
                    value='delta@betashop.it'
                )
            )
        )
    ),
    inventory_reporting_party=InventoryReportingParty(
        party_name=[
            PartyName(
                name=Name(
                    value='Arancio Forniture spa'
                )
            ),
        ],
        postal_address=PostalAddress(
            street_name=StreetName(
                value="Via Dell'Arcoveggio"
            ),
            building_number=BuildingNumber(
                value='405'
            ),
            department=Department(
                value='Sales and Planning Department'
            ),
            city_name=CityName(
                value='Bologna'
            ),
            postal_zone=PostalZone(
                value='40129'
            ),
            country=Country(
                identification_code=IdentificationCode(
                    value='IT'
                ),
                name=Name(
                    value='Italy'
                )
            )
        ),
        contact=Contact(
            name=Name(
                value='Mr Bianchi'
            ),
            telephone=Telephone(
                value='0039 051 23000008'
            ),
            telefax=Telefax(
                value='0039 051 23000025'
            ),
            electronic_mail=ElectronicMail(
                value='bianchi@arancioforniture.it'
            )
        )
    ),
    seller_supplier_party=SellerSupplierParty(
        party=Party(
            party_name=[
                PartyName(
                    name=Name(
                        value='Arancio Forniture spa'
                    )
                ),
            ],
            postal_address=PostalAddress(
                street_name=StreetName(
                    value="Via Dell'Arcoveggio"
                ),
                building_number=BuildingNumber(
                    value='403'
                ),
                city_name=CityName(
                    value='Bologna'
                ),
                postal_zone=PostalZone(
                    value='40129'
                ),
                country=Country(
                    identification_code=IdentificationCode(
                        value='IT'
                    ),
                    name=Name(
                        value='Italy'
                    )
                )
            ),
            contact=Contact(
                name=Name(
                    value='Mr Rossi'
                ),
                telephone=Telephone(
                    value='0039 051 23000000'
                ),
                telefax=Telefax(
                    value='0039 051 23000023'
                ),
                electronic_mail=ElectronicMail(
                    value='rossi@arancioforniture.it'
                )
            )
        )
    ),
    inventory_report_line=[
        InventoryReportLine(
            id=Id(
                value='1'
            ),
            quantity=Quantity(
                value=Decimal('10'),
                unit_code='NAR'
            ),
            inventory_value_amount=InventoryValueAmount(
                value=Decimal('200'),
                currency_id='EUR'
            ),
            item=Item(
                description=[
                    Description(
                        value='shirt'
                    ),
                ],
                buyers_item_identification=BuyersItemIdentification(
                    id=Id(
                        value='SH009'
                    )
                ),
                sellers_item_identification=SellersItemIdentification(
                    id=Id(
                        value='DD88'
                    )
                )
            )
        ),
        InventoryReportLine(
            id=Id(
                value='2'
            ),
            quantity=Quantity(
                value=Decimal('15'),
                unit_code='NAR'
            ),
            inventory_value_amount=InventoryValueAmount(
                value=Decimal('750'),
                currency_id='EUR'
            ),
            item=Item(
                description=[
                    Description(
                        value='trousers'
                    ),
                ],
                buyers_item_identification=BuyersItemIdentification(
                    id=Id(
                        value='TH009'
                    )
                ),
                sellers_item_identification=SellersItemIdentification(
                    id=Id(
                        value='DA008'
                    )
                )
            )
        ),
        InventoryReportLine(
            id=Id(
                value='3'
            ),
            quantity=Quantity(
                value=Decimal('5'),
                unit_code='NAR'
            ),
            inventory_value_amount=InventoryValueAmount(
                value=Decimal('300'),
                currency_id='EUR'
            ),
            item=Item(
                description=[
                    Description(
                        value="woman's dress"
                    ),
                ],
                buyers_item_identification=BuyersItemIdentification(
                    id=Id(
                        value='DH019'
                    )
                ),
                sellers_item_identification=SellersItemIdentification(
                    id=Id(
                        value='BA058'
                    )
                )
            )
        ),
    ]
)
