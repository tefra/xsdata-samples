from decimal import Decimal
from ubl.models.common.ubl_common_aggregate_components_2_1 import BuyersItemIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import Consignment
from ubl.models.common.ubl_common_aggregate_components_2_1 import Contact
from ubl.models.common.ubl_common_aggregate_components_2_1 import Country
from ubl.models.common.ubl_common_aggregate_components_2_1 import Delivery
from ubl.models.common.ubl_common_aggregate_components_2_1 import DeliveryAddress
from ubl.models.common.ubl_common_aggregate_components_2_1 import Despatch
from ubl.models.common.ubl_common_aggregate_components_2_1 import DespatchAddress
from ubl.models.common.ubl_common_aggregate_components_2_1 import InstructionForReturnsLine
from ubl.models.common.ubl_common_aggregate_components_2_1 import Item
from ubl.models.common.ubl_common_aggregate_components_2_1 import ManufacturerParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import Party
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyName
from ubl.models.common.ubl_common_aggregate_components_2_1 import PostalAddress
from ubl.models.common.ubl_common_aggregate_components_2_1 import RetailerCustomerParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import SellerSupplierParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import SellersItemIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import Shipment
from ubl.models.common.ubl_common_basic_components_2_1 import BuildingNumber
from ubl.models.common.ubl_common_basic_components_2_1 import CityName
from ubl.models.common.ubl_common_basic_components_2_1 import Description
from ubl.models.common.ubl_common_basic_components_2_1 import ElectronicMail
from ubl.models.common.ubl_common_basic_components_2_1 import Id
from ubl.models.common.ubl_common_basic_components_2_1 import IdentificationCode
from ubl.models.common.ubl_common_basic_components_2_1 import Name
from ubl.models.common.ubl_common_basic_components_2_1 import Note
from ubl.models.common.ubl_common_basic_components_2_1 import PostalZone
from ubl.models.common.ubl_common_basic_components_2_1 import Quantity
from ubl.models.common.ubl_common_basic_components_2_1 import StreetName
from ubl.models.common.ubl_common_basic_components_2_1 import Telefax
from ubl.models.common.ubl_common_basic_components_2_1 import Telephone
from ubl.models.common.ubl_common_basic_components_2_1 import UblversionId
from ubl.models.maindoc.ubl_instruction_for_returns_2_1 import InstructionForReturns
from xsdata.models.datatype import XmlDate


obj = InstructionForReturns(
    ublversion_id=UblversionId(
        value='2.1'
    ),
    id=Id(
        value='AB011'
    ),
    copy_indicator=False,
    issue_date=XmlDate(2010, 4, 10),
    note=[
        Note(
            value='Instruction to return goods that are badly sent to you.'
        ),
    ],
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
    manufacturer_party=ManufacturerParty(
        party_name=[
            PartyName(
                name=Name(
                    value='AZ Outsourcing srl'
                )
            ),
        ],
        postal_address=PostalAddress(
            street_name=StreetName(
                value='Via Bolognese'
            ),
            building_number=BuildingNumber(
                value='199'
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
                value='Mr Verdi'
            ),
            telephone=Telephone(
                value='0039 051 25400000'
            ),
            telefax=Telefax(
                value='0039 051 25400023'
            ),
            electronic_mail=ElectronicMail(
                value='verdi@azoutsourcing.it'
            )
        )
    ),
    shipment=Shipment(
        id=Id(
            value='51022'
        ),
        consignment=[
            Consignment(
                id=Id(
                    value='510'
                )
            ),
        ],
        delivery=Delivery(
            delivery_address=DeliveryAddress(
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
            despatch=Despatch(
                despatch_address=DespatchAddress(
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
                )
            )
        )
    ),
    instruction_for_returns_line=[
        InstructionForReturnsLine(
            id=Id(
                value='1'
            ),
            quantity=Quantity(
                value=Decimal('20'),
                unit_code='NAR'
            ),
            item=Item(
                description=[
                    Description(
                        value='Denim Jeans Jacket'
                    ),
                ],
                name=Name(
                    value='Jeans Jacket man'
                ),
                buyers_item_identification=BuyersItemIdentification(
                    id=Id(
                        value='AA109'
                    )
                ),
                sellers_item_identification=SellersItemIdentification(
                    id=Id(
                        value='YX401'
                    )
                )
            )
        ),
        InstructionForReturnsLine(
            id=Id(
                value='2'
            ),
            quantity=Quantity(
                value=Decimal('5'),
                unit_code='NAR'
            ),
            item=Item(
                description=[
                    Description(
                        value='Leather Jacket'
                    ),
                ],
                name=Name(
                    value='Leather Jacket man'
                ),
                buyers_item_identification=BuyersItemIdentification(
                    id=Id(
                        value='AA128'
                    )
                ),
                sellers_item_identification=SellersItemIdentification(
                    id=Id(
                        value='YX233'
                    )
                )
            )
        ),
    ]
)
