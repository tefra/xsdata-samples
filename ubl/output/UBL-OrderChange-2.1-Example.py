from decimal import Decimal
from ubl.models.common.ubl_common_aggregate_components_2_1 import AdditionalItemProperty
from ubl.models.common.ubl_common_aggregate_components_2_1 import BuyerCustomerParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import Delivery
from ubl.models.common.ubl_common_aggregate_components_2_1 import Item
from ubl.models.common.ubl_common_aggregate_components_2_1 import LineItem
from ubl.models.common.ubl_common_aggregate_components_2_1 import OrderLine
from ubl.models.common.ubl_common_aggregate_components_2_1 import OrderReference
from ubl.models.common.ubl_common_aggregate_components_2_1 import OriginatorParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import Party
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyName
from ubl.models.common.ubl_common_aggregate_components_2_1 import Price
from ubl.models.common.ubl_common_aggregate_components_2_1 import RequestedDeliveryPeriod
from ubl.models.common.ubl_common_aggregate_components_2_1 import SellerSupplierParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import SellersItemIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import StandardItemIdentification
from ubl.models.common.ubl_common_basic_components_2_1 import AccountingCostCode
from ubl.models.common.ubl_common_basic_components_2_1 import BaseQuantity
from ubl.models.common.ubl_common_basic_components_2_1 import CustomizationId
from ubl.models.common.ubl_common_basic_components_2_1 import Description
from ubl.models.common.ubl_common_basic_components_2_1 import EndDate
from ubl.models.common.ubl_common_basic_components_2_1 import EndpointId
from ubl.models.common.ubl_common_basic_components_2_1 import Id
from ubl.models.common.ubl_common_basic_components_2_1 import IssueDate
from ubl.models.common.ubl_common_basic_components_2_1 import IssueTime
from ubl.models.common.ubl_common_basic_components_2_1 import LineExtensionAmount
from ubl.models.common.ubl_common_basic_components_2_1 import LineStatusCode
from ubl.models.common.ubl_common_basic_components_2_1 import Name
from ubl.models.common.ubl_common_basic_components_2_1 import Note
from ubl.models.common.ubl_common_basic_components_2_1 import PartialDeliveryIndicator
from ubl.models.common.ubl_common_basic_components_2_1 import PriceAmount
from ubl.models.common.ubl_common_basic_components_2_1 import ProfileId
from ubl.models.common.ubl_common_basic_components_2_1 import Quantity
from ubl.models.common.ubl_common_basic_components_2_1 import SequenceNumberId
from ubl.models.common.ubl_common_basic_components_2_1 import StartDate
from ubl.models.common.ubl_common_basic_components_2_1 import TotalTaxAmount
from ubl.models.common.ubl_common_basic_components_2_1 import UblversionId
from ubl.models.common.ubl_common_basic_components_2_1 import Value
from ubl.models.maindoc.ubl_order_change_2_1 import OrderChange
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlTime


obj = OrderChange(
    ublversion_id=UblversionId(
        value='2.1'
    ),
    customization_id=CustomizationId(
        value='urn:www.cenbii.eu:transaction:biicoretrdmXYZ:ver1.0'
    ),
    profile_id=ProfileId(
        value='urn:www.cenbii.eu:profile:BIIXYZ:ver1.0',
        scheme_id='Profile',
        scheme_agency_id='BII'
    ),
    id=Id(
        value='7'
    ),
    issue_date=IssueDate(
        value=XmlDate(2010, 1, 21)
    ),
    issue_time=IssueTime(
        value=XmlTime(12, 30, 0, 0)
    ),
    sequence_number_id=SequenceNumberId(
        value='1'
    ),
    note=[
        Note(
            value='Information text for the whole order change'
        ),
    ],
    order_reference=OrderReference(
        id=Id(
            value='34'
        )
    ),
    buyer_customer_party=BuyerCustomerParty(
        party=Party(
            endpoint_id=EndpointId(
                value='7300072311115',
                scheme_id='GLN',
                scheme_agency_id='9'
            ),
            party_identification=[
                PartyIdentification(
                    id=Id(
                        value='7300070011115',
                        scheme_id='GLN',
                        scheme_agency_id='9'
                    )
                ),
                PartyIdentification(
                    id=Id(
                        value='PartyID123'
                    )
                ),
            ],
            party_name=[
                PartyName(
                    name=Name(
                        value='Johnssons byggvaror'
                    )
                ),
            ]
        )
    ),
    seller_supplier_party=SellerSupplierParty(
        party=Party(
            endpoint_id=EndpointId(
                value='7302347231111',
                scheme_id='GLN',
                scheme_agency_id='9'
            ),
            party_identification=[
                PartyIdentification(
                    id=Id(
                        value='SellerPartyID123'
                    )
                ),
            ],
            party_name=[
                PartyName(
                    name=Name(
                        value='Moderna Produkter AB'
                    )
                ),
            ]
        )
    ),
    order_line=[
        OrderLine(
            note=[
                Note(
                    value='Freetext note on line 1'
                ),
            ],
            line_item=LineItem(
                id=Id(
                    value='1'
                ),
                line_status_code=LineStatusCode(
                    value='Revised',
                    list_agency_id='UBL',
                    list_name='Line Status'
                ),
                quantity=Quantity(
                    value=Decimal('240'),
                    unit_code='LTR'
                ),
                line_extension_amount=LineExtensionAmount(
                    value=Decimal('12000'),
                    currency_id='SEK'
                ),
                total_tax_amount=TotalTaxAmount(
                    value=Decimal('20'),
                    currency_id='SEK'
                ),
                partial_delivery_indicator=PartialDeliveryIndicator(
                    value=False
                ),
                accounting_cost_code=AccountingCostCode(
                    value='ProjectID123'
                ),
                delivery=[
                    Delivery(
                        requested_delivery_period=RequestedDeliveryPeriod(
                            start_date=StartDate(
                                value=XmlDate(2010, 2, 10)
                            ),
                            end_date=EndDate(
                                value=XmlDate(2010, 2, 25)
                            )
                        )
                    ),
                ],
                originator_party=OriginatorParty(
                    party_identification=[
                        PartyIdentification(
                            id=Id(
                                value='EmployeeXXX',
                                scheme_id='ZZZ',
                                scheme_agency_id='ZZZ'
                            )
                        ),
                    ],
                    party_name=[
                        PartyName(
                            name=Name(
                                value='Josef K.'
                            )
                        ),
                    ]
                ),
                price=Price(
                    price_amount=PriceAmount(
                        value=Decimal('50'),
                        currency_id='SEK'
                    ),
                    base_quantity=BaseQuantity(
                        value=Decimal('1'),
                        unit_code='LTR'
                    )
                ),
                item=Item(
                    description=[
                        Description(
                            value='Red paint'
                        ),
                    ],
                    name=Name(
                        value='Falu Rödfärg'
                    ),
                    sellers_item_identification=SellersItemIdentification(
                        id=Id(
                            value='SItemNo001'
                        )
                    ),
                    standard_item_identification=StandardItemIdentification(
                        id=Id(
                            value='1234567890123',
                            scheme_id='GTIN',
                            scheme_agency_id='6'
                        )
                    ),
                    additional_item_property=[
                        AdditionalItemProperty(
                            name=Name(
                                value='Paint type'
                            ),
                            value=Value(
                                value='Acrylic'
                            )
                        ),
                        AdditionalItemProperty(
                            name=Name(
                                value='Solvant'
                            ),
                            value=Value(
                                value='Water'
                            )
                        ),
                    ]
                )
            )
        ),
    ]
)
