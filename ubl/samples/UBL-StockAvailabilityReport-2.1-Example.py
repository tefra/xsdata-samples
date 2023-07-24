from decimal import Decimal
from ubl.models.common.ubl_common_aggregate_components_2_1 import BuyersItemIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import Contact
from ubl.models.common.ubl_common_aggregate_components_2_1 import Country
from ubl.models.common.ubl_common_aggregate_components_2_1 import InventoryPeriod
from ubl.models.common.ubl_common_aggregate_components_2_1 import InventoryReportingParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import Item
from ubl.models.common.ubl_common_aggregate_components_2_1 import Party
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyName
from ubl.models.common.ubl_common_aggregate_components_2_1 import PostalAddress
from ubl.models.common.ubl_common_aggregate_components_2_1 import RetailerCustomerParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import SellerSupplierParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import SellersItemIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import StockAvailabilityReportLine
from ubl.models.common.ubl_common_basic_components_2_1 import AvailabilityStatusCode
from ubl.models.common.ubl_common_basic_components_2_1 import BuildingNumber
from ubl.models.common.ubl_common_basic_components_2_1 import CityName
from ubl.models.common.ubl_common_basic_components_2_1 import Description
from ubl.models.common.ubl_common_basic_components_2_1 import ElectronicMail
from ubl.models.common.ubl_common_basic_components_2_1 import Floor
from ubl.models.common.ubl_common_basic_components_2_1 import Id
from ubl.models.common.ubl_common_basic_components_2_1 import IdentificationCode
from ubl.models.common.ubl_common_basic_components_2_1 import Name
from ubl.models.common.ubl_common_basic_components_2_1 import Note
from ubl.models.common.ubl_common_basic_components_2_1 import PostalZone
from ubl.models.common.ubl_common_basic_components_2_1 import Quantity
from ubl.models.common.ubl_common_basic_components_2_1 import Room
from ubl.models.common.ubl_common_basic_components_2_1 import StreetName
from ubl.models.common.ubl_common_basic_components_2_1 import Telefax
from ubl.models.common.ubl_common_basic_components_2_1 import Telephone
from ubl.models.common.ubl_common_basic_components_2_1 import UblversionId
from ubl.models.maindoc.ubl_stock_availability_report_2_1 import StockAvailabilityReport
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlTime


obj = StockAvailabilityReport(
    ublversion_id=UblversionId(
        value="2.1"
    ),
    id=Id(
        value="SA2009"
    ),
    copy_indicator=False,
    issue_date=XmlDate(2010, 4, 11),
    note=[
        Note(
            value="Report about quantities of each item which are (or will be) available"
        ),
    ],
    inventory_period=InventoryPeriod(
        start_date=XmlDate(2010, 4, 11),
        start_time=XmlTime(8, 0, 0, 0),
        end_date=XmlDate(2011, 4, 11)
    ),
    seller_supplier_party=SellerSupplierParty(
        party=Party(
            party_name=[
                PartyName(
                    name=Name(
                        value="Arancio Forniture spa"
                    )
                ),
            ],
            postal_address=PostalAddress(
                street_name=StreetName(
                    value="Via Dell'Arcoveggio"
                ),
                building_number=BuildingNumber(
                    value="403"
                ),
                city_name=CityName(
                    value="Bologna"
                ),
                postal_zone=PostalZone(
                    value="40129"
                ),
                country=Country(
                    identification_code=IdentificationCode(
                        value="IT"
                    ),
                    name=Name(
                        value="Italy"
                    )
                )
            ),
            contact=Contact(
                name=Name(
                    value="Mr Rossi"
                ),
                telephone=Telephone(
                    value="0039 051 23000000"
                ),
                telefax=Telefax(
                    value="0039 051 23000023"
                ),
                electronic_mail=ElectronicMail(
                    value="rossi@arancioforniture.it"
                )
            )
        )
    ),
    retailer_customer_party=RetailerCustomerParty(
        party=Party(
            party_name=[
                PartyName(
                    name=Name(
                        value="Beta Shop"
                    )
                ),
            ],
            postal_address=PostalAddress(
                street_name=StreetName(
                    value="Via Emilia"
                ),
                building_number=BuildingNumber(
                    value="1"
                ),
                city_name=CityName(
                    value="Modena"
                ),
                postal_zone=PostalZone(
                    value="41121"
                ),
                country=Country(
                    identification_code=IdentificationCode(
                        value="IT"
                    ),
                    name=Name(
                        value="Italy"
                    )
                )
            ),
            contact=Contact(
                name=Name(
                    value="Mr Delta"
                ),
                telephone=Telephone(
                    value="0039 059 33000000"
                ),
                telefax=Telefax(
                    value="0039 059 33000055"
                ),
                electronic_mail=ElectronicMail(
                    value="delta@betashop.it"
                )
            )
        )
    ),
    inventory_reporting_party=InventoryReportingParty(
        party_name=[
            PartyName(
                name=Name(
                    value="Beta Shop"
                )
            ),
        ],
        postal_address=PostalAddress(
            floor=Floor(
                value="2"
            ),
            room=Room(
                value="309"
            ),
            street_name=StreetName(
                value="Via Emilia"
            ),
            building_number=BuildingNumber(
                value="1"
            ),
            city_name=CityName(
                value="Modena"
            ),
            postal_zone=PostalZone(
                value="41121"
            ),
            country=Country(
                identification_code=IdentificationCode(
                    value="IT"
                ),
                name=Name(
                    value="Italy"
                )
            )
        ),
        contact=Contact(
            name=Name(
                value="Mr Gamma"
            ),
            telephone=Telephone(
                value="0039 059 33000022"
            ),
            telefax=Telefax(
                value="0039 059 33000057"
            ),
            electronic_mail=ElectronicMail(
                value="gamma@betashop.it"
            )
        )
    ),
    stock_availability_report_line=[
        StockAvailabilityReportLine(
            id=Id(
                value="1"
            ),
            quantity=Quantity(
                value=Decimal("50"),
                unit_code="NAR"
            ),
            availability_date=XmlDate(2010, 4, 20),
            availability_status_code=AvailabilityStatusCode(
                value="1",
                list_id="7011",
                list_agency_name="UN/ECE",
                list_uri="http://www.unece.org/trade/untdid/d09b/tred/tred7011.htm"
            ),
            item=Item(
                description=[
                    Description(
                        value="T-shirt"
                    ),
                ],
                buyers_item_identification=BuyersItemIdentification(
                    id=Id(
                        value="TT319"
                    )
                ),
                sellers_item_identification=SellersItemIdentification(
                    id=Id(
                        value="ZZ738"
                    )
                )
            )
        ),
        StockAvailabilityReportLine(
            id=Id(
                value="2"
            ),
            quantity=Quantity(
                value=Decimal("80"),
                unit_code="NAR"
            ),
            availability_date=XmlDate(2010, 4, 11),
            availability_status_code=AvailabilityStatusCode(
                value="2",
                list_id="7011",
                list_agency_name="UN/ECE",
                list_uri="http://www.unece.org/trade/untdid/d09b/tred/tred7011.htm"
            ),
            item=Item(
                description=[
                    Description(
                        value="jersey"
                    ),
                ],
                buyers_item_identification=BuyersItemIdentification(
                    id=Id(
                        value="TJ043"
                    )
                ),
                sellers_item_identification=SellersItemIdentification(
                    id=Id(
                        value="K0058"
                    )
                )
            )
        ),
        StockAvailabilityReportLine(
            id=Id(
                value="3"
            ),
            quantity=Quantity(
                value=Decimal("0"),
                unit_code="NAR"
            ),
            availability_status_code=AvailabilityStatusCode(
                value="8",
                list_id="7011",
                list_agency_name="UN/ECE",
                list_uri="http://www.unece.org/trade/untdid/d09b/tred/tred7011.htm"
            ),
            item=Item(
                description=[
                    Description(
                        value="skirt"
                    ),
                ],
                buyers_item_identification=BuyersItemIdentification(
                    id=Id(
                        value="TS893"
                    )
                ),
                sellers_item_identification=SellersItemIdentification(
                    id=Id(
                        value="PK009"
                    )
                )
            )
        ),
    ]
)
