from decimal import Decimal
from ubl.models.common.ubl_common_aggregate_components_2_1 import ActivityOriginLocation
from ubl.models.common.ubl_common_aggregate_components_2_1 import ActivityPeriod
from ubl.models.common.ubl_common_aggregate_components_2_1 import Address
from ubl.models.common.ubl_common_aggregate_components_2_1 import BuyersItemIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import Contact
from ubl.models.common.ubl_common_aggregate_components_2_1 import Country
from ubl.models.common.ubl_common_aggregate_components_2_1 import Item
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyName
from ubl.models.common.ubl_common_aggregate_components_2_1 import PostalAddress
from ubl.models.common.ubl_common_aggregate_components_2_1 import ReceiverParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import SalesItem
from ubl.models.common.ubl_common_aggregate_components_2_1 import SellersItemIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import SenderParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import SupplyChainActivityDataLine
from ubl.models.common.ubl_common_basic_components_2_1 import BuildingNumber
from ubl.models.common.ubl_common_basic_components_2_1 import CityName
from ubl.models.common.ubl_common_basic_components_2_1 import Department
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
from ubl.models.common.ubl_common_basic_components_2_1 import SupplyChainActivityTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import Telefax
from ubl.models.common.ubl_common_basic_components_2_1 import Telephone
from ubl.models.common.ubl_common_basic_components_2_1 import UblversionId
from ubl.models.maindoc.ubl_product_activity_2_1 import ProductActivity
from xsdata.models.datatype import XmlDate


obj = ProductActivity(
    ublversion_id=UblversionId(
        value="2.1"
    ),
    id=Id(
        value="ID0113"
    ),
    copy_indicator=False,
    issue_date=XmlDate(2010, 4, 8),
    note=[
        Note(
            value="Report about sales of goods in Beta Shop's shops located in Bologna."
        ),
    ],
    activity_period=ActivityPeriod(
        start_date=XmlDate(2010, 4, 7)
    ),
    sender_party=SenderParty(
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
    ),
    receiver_party=ReceiverParty(
        party_name=[
            PartyName(
                name=Name(
                    value="Arancio Forniture spa"
                )
            ),
        ],
        postal_address=PostalAddress(
            floor=Floor(
                value="5"
            ),
            room=Room(
                value="29"
            ),
            street_name=StreetName(
                value="Via Dell'Arcoveggio"
            ),
            building_number=BuildingNumber(
                value="403"
            ),
            department=Department(
                value="Marketing Office"
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
    ),
    supply_chain_activity_data_line=[
        SupplyChainActivityDataLine(
            id=Id(
                value="1"
            ),
            supply_chain_activity_type_code=SupplyChainActivityTypeCode(
                value="SALES"
            ),
            activity_origin_location=ActivityOriginLocation(
                description=[
                    Description(
                        value="Shop in the city center"
                    ),
                ],
                address=Address(
                    street_name=StreetName(
                        value="Via Rizzoli"
                    ),
                    building_number=BuildingNumber(
                        value="208"
                    ),
                    city_name=CityName(
                        value="Bologna"
                    ),
                    postal_zone=PostalZone(
                        value="40121"
                    ),
                    country=Country(
                        identification_code=IdentificationCode(
                            value="IT"
                        ),
                        name=Name(
                            value="Italy"
                        )
                    )
                )
            ),
            sales_item=[
                SalesItem(
                    quantity=Quantity(
                        value=Decimal("8"),
                        unit_code="NAR"
                    ),
                    item=Item(
                        description=[
                            Description(
                                value="shirt"
                            ),
                        ],
                        buyers_item_identification=BuyersItemIdentification(
                            id=Id(
                                value="SH009"
                            )
                        ),
                        sellers_item_identification=SellersItemIdentification(
                            id=Id(
                                value="DD88"
                            )
                        )
                    )
                ),
                SalesItem(
                    quantity=Quantity(
                        value=Decimal("3"),
                        unit_code="NAR"
                    ),
                    item=Item(
                        description=[
                            Description(
                                value="trousers"
                            ),
                        ],
                        buyers_item_identification=BuyersItemIdentification(
                            id=Id(
                                value="TH009"
                            )
                        ),
                        sellers_item_identification=SellersItemIdentification(
                            id=Id(
                                value="DA008"
                            )
                        )
                    )
                ),
            ]
        ),
    ]
)
