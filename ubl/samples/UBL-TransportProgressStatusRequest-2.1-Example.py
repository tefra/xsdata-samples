from ubl.models.common.ubl_common_aggregate_components_2_1 import Address
from ubl.models.common.ubl_common_aggregate_components_2_1 import Contact
from ubl.models.common.ubl_common_aggregate_components_2_1 import Country
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyIdentification
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyName
from ubl.models.common.ubl_common_aggregate_components_2_1 import RailTransport
from ubl.models.common.ubl_common_aggregate_components_2_1 import ReceiverParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import SenderParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import StatusLocation
from ubl.models.common.ubl_common_aggregate_components_2_1 import TransportMeans
from ubl.models.common.ubl_common_basic_components_2_1 import CityName
from ubl.models.common.ubl_common_basic_components_2_1 import ElectronicMail
from ubl.models.common.ubl_common_basic_components_2_1 import Id
from ubl.models.common.ubl_common_basic_components_2_1 import IdentificationCode
from ubl.models.common.ubl_common_basic_components_2_1 import JourneyId
from ubl.models.common.ubl_common_basic_components_2_1 import LocationTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import Name
from ubl.models.common.ubl_common_basic_components_2_1 import RegistrationNationalityId
from ubl.models.common.ubl_common_basic_components_2_1 import StreetName
from ubl.models.common.ubl_common_basic_components_2_1 import Telephone
from ubl.models.common.ubl_common_basic_components_2_1 import TrainId
from ubl.models.common.ubl_common_basic_components_2_1 import TransportMeansTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import UblversionId
from ubl.models.maindoc.ubl_transport_progress_status_request_2_1 import TransportProgressStatusRequest
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlTime


obj = TransportProgressStatusRequest(
    ublversion_id=UblversionId(
        value="2.1"
    ),
    id=Id(
        value="TPS_1"
    ),
    issue_date=XmlDate(2011, 10, 3),
    issue_time=XmlTime(14, 30, 10, 0, 60),
    sender_party=SenderParty(
        party_identification=[
            PartyIdentification(
                id=Id(
                    value="4058673827641",
                    scheme_name="GLN",
                    scheme_agency_name="GS1"
                )
            ),
        ],
        party_name=[
            PartyName(
                name=Name(
                    value="NECOSS"
                )
            ),
        ],
        contact=Contact(
            name=Name(
                value="SomeName"
            ),
            telephone=Telephone(
                value="+49450557000"
            ),
            electronic_mail=ElectronicMail(
                value="SomeName@necoss.de"
            )
        )
    ),
    receiver_party=ReceiverParty(
        party_identification=[
            PartyIdentification(
                id=Id(
                    value="4058673821325",
                    scheme_name="GLN",
                    scheme_agency_name="GS1"
                )
            ),
        ],
        party_name=[
            PartyName(
                name=Name(
                    value="ARRIVA"
                )
            ),
        ],
        contact=Contact(
            name=Name(
                value="SomeName"
            ),
            telephone=Telephone(
                value="+49450557888"
            ),
            electronic_mail=ElectronicMail(
                value="SomeName@arriva.de"
            )
        )
    ),
    transport_means=TransportMeans(
        journey_id=JourneyId(
            value="RHamBrem"
        ),
        registration_nationality_id=RegistrationNationalityId(
            value="DE"
        ),
        transport_means_type_code=TransportMeansTypeCode(
            value="230"
        ),
        rail_transport=RailTransport(
            train_id=TrainId(
                value="RID01235"
            )
        )
    ),
    status_location=[
        StatusLocation(
            location_type_code=LocationTypeCode(
                value="13"
            ),
            address=Address(
                id=Id(
                    value="4568763527610",
                    scheme_name="GLN",
                    scheme_agency_name="GS1"
                ),
                street_name=StreetName(
                    value="Ludwig-Erhard-Str. 15"
                ),
                city_name=CityName(
                    value="Bremen"
                ),
                country=Country(
                    identification_code=IdentificationCode(
                        value="DE"
                    )
                )
            )
        ),
    ]
)
