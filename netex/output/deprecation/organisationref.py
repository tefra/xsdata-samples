from decimal import Decimal
from netex.models.all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.general_version_frame_structure import GeneralFrame
from netex.models.general_version_frame_structure import GeneralFrameMembersRelStructure
from netex.models.location_structure_2 import LocationStructure2
from netex.models.multilingual_string import MultilingualString
from netex.models.operator import Operator
from netex.models.organisation_ref import OrganisationRef
from netex.models.organisation_type_enumeration import OrganisationTypeEnumeration
from netex.models.participant_ref import ParticipantRef
from netex.models.publication_delivery import PublicationDelivery
from netex.models.simple_point_version_structure import SimplePointVersionStructure
from netex.models.stop_place import StopPlace
from netex.models.stop_type_enumeration import StopTypeEnumeration
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration


obj = PublicationDelivery(
    publication_timestamp=XmlDateTime(2015, 4, 17, 9, 30, 47, 0, 0),
    participant_ref=ParticipantRef(
        value='AURIGE001'
    ),
    publication_refresh_interval=XmlDuration("P1Y"),
    description=MultilingualString(
        value='Keeps OrganisationRef'
    ),
    data_objects=DataObjectsRelStructure(
        choice=[
            GeneralFrame(
                id='AURIGE:TypeOfFrame:NETEX_ARRET-Le-Corbusier:LOC',
                version='001',
                name=MultilingualString(
                    value='Frame NETEX_ARRET Le Corbusier'
                ),
                description=MultilingualString(
                    value="Frame NETEX_ARRET pour l'exemple d'arrêt Le Corbusier"
                ),
                members=GeneralFrameMembersRelStructure(
                    choice=[
                        StopPlace(
                            id='FR:78197:StopPlace:00001:LOC',
                            version='001',
                            name=MultilingualString(
                                value='Le Corbusier'
                            ),
                            description=[
                                MultilingualString(
                                    value='Pôle monomodal regroupant les arrêts monomodaux Le Corbusier, Lycée de Villaroy et Jules Michelet'
                                ),
                            ],
                            centroid=SimplePointVersionStructure(
                                location=LocationStructure2(
                                    longitude=Decimal('2.068554'),
                                    latitude=Decimal('48.764788'),
                                    id='AURIGE:Location:00001:LOC'
                                )
                            ),
                            cross_road=MultilingualString(
                                value="Intersection Avenue de l'Europe, Rue Eugène Violet Le Duc et Rue Le Corbusier"
                            ),
                            landmark=MultilingualString(
                                value="Lycée Villaroy et Gymnase de l'Aviation"
                            ),
                            choice=OrganisationRef(
                                version='001',
                                ref='AURIGE:Operator:768:LOC'
                            ),
                            transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
                            stop_place_type=StopTypeEnumeration.ONSTREET_BUS
                        ),
                        Operator(
                            id='AURIGE:Operator:768:LOC',
                            version='001',
                            company_number='768',
                            name=MultilingualString(
                                value='SQYBUS'
                            ),
                            organisation_type=[
                                OrganisationTypeEnumeration.OPERATOR,
                            ]
                        ),
                    ]
                )
            ),
        ]
    ),
    version='1.01'
)
