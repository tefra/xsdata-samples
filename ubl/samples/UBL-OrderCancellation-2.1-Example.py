from ubl.models.common.ubl_common_aggregate_components_2_1 import BuyerCustomerParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import OrderReference
from ubl.models.common.ubl_common_aggregate_components_2_1 import Party
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyName
from ubl.models.common.ubl_common_aggregate_components_2_1 import SellerSupplierParty
from ubl.models.common.ubl_common_basic_components_2_1 import CancellationNote
from ubl.models.common.ubl_common_basic_components_2_1 import CustomizationId
from ubl.models.common.ubl_common_basic_components_2_1 import EndpointId
from ubl.models.common.ubl_common_basic_components_2_1 import Id
from ubl.models.common.ubl_common_basic_components_2_1 import IssueDate
from ubl.models.common.ubl_common_basic_components_2_1 import IssueTime
from ubl.models.common.ubl_common_basic_components_2_1 import Name
from ubl.models.common.ubl_common_basic_components_2_1 import ProfileId
from ubl.models.common.ubl_common_basic_components_2_1 import UblversionId
from ubl.models.maindoc.ubl_order_cancellation_2_1 import OrderCancellation
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlTime


obj = OrderCancellation(
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
    cancellation_note=[
        CancellationNote(
            value='With reference to phone call'
        ),
    ],
    order_reference=[
        OrderReference(
            id=Id(
                value='34'
            )
        ),
    ],
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
    )
)
