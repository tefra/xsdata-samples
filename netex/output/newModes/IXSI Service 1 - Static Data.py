from decimal import Decimal
from netex.models.all_modes_enumeration import AllModesEnumeration
from netex.models.all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from netex.models.car_model_profile import CarModelProfile
from netex.models.car_model_profile_ref import CarModelProfileRef
from netex.models.child_seat_enumeration import ChildSeatEnumeration
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.fleet import Fleet
from netex.models.fleet_ref import FleetRef
from netex.models.fleet_refs_rel_structure import FleetRefsRelStructure
from netex.models.fuel_type_enumeration import FuelTypeEnumeration
from netex.models.general_organisation import GeneralOrganisation
from netex.models.general_version_frame_structure import CompositeFrame
from netex.models.general_version_frame_structure import FramesRelStructure
from netex.models.general_version_frame_structure import GeneralFrame
from netex.models.general_version_frame_structure import GeneralFrameMembersRelStructure
from netex.models.location_structure_2 import LocationStructure2
from netex.models.multilingual_string import MultilingualString
from netex.models.online_service import OnlineService
from netex.models.online_service_ref import OnlineServiceRef
from netex.models.online_service_refs_rel_structure import OnlineServiceRefsRelStructure
from netex.models.operator import Operator
from netex.models.operator_ref import OperatorRef
from netex.models.organisation_ref_structure import OrganisationRefStructure
from netex.models.organisation_type_enumeration import OrganisationTypeEnumeration
from netex.models.parking import Parking
from netex.models.parking_area_1 import ParkingArea1
from netex.models.parking_areas_rel_structure import ParkingAreasRelStructure
from netex.models.parking_layout_enumeration import ParkingLayoutEnumeration
from netex.models.parking_properties import ParkingProperties
from netex.models.parking_reservation_enumeration import ParkingReservationEnumeration
from netex.models.parking_type_enumeration import ParkingTypeEnumeration
from netex.models.parking_user_enumeration import ParkingUserEnumeration
from netex.models.parking_vehicle_enumeration import ParkingVehicleEnumeration
from netex.models.participant_ref import ParticipantRef
from netex.models.propulsion_type_enumeration import PropulsionTypeEnumeration
from netex.models.public_use_enumeration import PublicUseEnumeration
from netex.models.publication_delivery import PublicationDelivery
from netex.models.responsibility_role_assignment import ResponsibilityRoleAssignment
from netex.models.responsibility_role_assignments_rel_structure import ResponsibilityRoleAssignmentsRelStructure
from netex.models.responsibility_set import ResponsibilitySet
from netex.models.service_booking_arrangements_structure import ServiceBookingArrangementsStructure
from netex.models.simple_point_version_structure import SimplePointVersionStructure
from netex.models.simple_vehicle_category_enumeration import SimpleVehicleCategoryEnumeration
from netex.models.simple_vehicle_type import SimpleVehicleType
from netex.models.stakeholder_role_type_enumeration import StakeholderRoleTypeEnumeration
from netex.models.transport_type_refs_rel_structure import TransportTypeRefsRelStructure
from netex.models.transport_type_version_structure import TransportTypeVersionStructure
from netex.models.type_of_frame_ref import TypeOfFrameRef
from netex.models.vehicle import Vehicle
from netex.models.vehicle_model import VehicleModel
from netex.models.vehicle_model_ref import VehicleModelRef
from netex.models.vehicle_ref import VehicleRef
from netex.models.vehicle_sharing import VehicleSharing
from netex.models.vehicle_sharing_ref import VehicleSharingRef
from netex.models.vehicle_sharing_service import VehicleSharingService
from netex.models.vehicle_sharing_type_enumeration import VehicleSharingTypeEnumeration
from netex.models.vehicle_type_ref import VehicleTypeRef
from netex.models.vehicles_rel_structure import VehiclesRelStructure
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration


obj = PublicationDelivery(
    publication_timestamp=XmlDateTime(2019, 6, 12, 9, 30, 47, 0, 0),
    participant_ref=ParticipantRef(
        value='AURIGE001'
    ),
    data_objects=DataObjectsRelStructure(
        choice=[
            CompositeFrame(
                id='FR:CompositeFrame:myFrame01:LOC',
                created=XmlDateTime(2019, 6, 12, 9, 30, 47, 0, 0),
                version='1',
                frames=FramesRelStructure(
                    common_frame=[
                        GeneralFrame(
                            id='FR:TypeOfFrame:NETEX_PARKING-Example1:LOC',
                            version='001',
                            type_of_frame_ref=TypeOfFrameRef(
                                value='version="2.01:FR-NETEX_PARKING-1.0"',
                                ref='FR:TypeOfFrame:NETEX_PARKING'
                            ),
                            members=GeneralFrameMembersRelStructure(
                                choice=[
                                    Parking(
                                        id='GE:Parking:633:Stadtmobil',
                                        version='2',
                                        responsibility_set_ref_attribute='GE:ResponsibilitySet:0123',
                                        name=MultilingualString(
                                            value='Rosdorfer Weg 18/ Hinterhof'
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                longitude=Decimal('9.925000000'),
                                                latitude=Decimal('51.53000000')
                                            )
                                        ),
                                        parking_type=ParkingTypeEnumeration.URBAN_PARKING,
                                        parking_vehicle_types=[
                                            ParkingVehicleEnumeration.CAR,
                                        ],
                                        parking_layout=ParkingLayoutEnumeration.ROADSIDE,
                                        total_capacity=5,
                                        parking_reservation=ParkingReservationEnumeration.NO_RESERVATIONS,
                                        parking_areas=ParkingAreasRelStructure(
                                            parking_area_ref_or_parking_area=[
                                                ParkingArea1(
                                                    id='GE:ParkingArea:633-1:Stadtmobil',
                                                    version='any',
                                                    public_use=PublicUseEnumeration.AUTHORISED_PUBLIC_ONLY,
                                                    parking_properties_or_parking_properties=ParkingProperties(
                                                        id='GE:ParkingProperties:633-1:Stadtmobil',
                                                        version='any',
                                                        parking_user_types=[
                                                            ParkingUserEnumeration.VEHICLE_SHARING,
                                                        ]
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    GeneralOrganisation(
                                        id='GE:Organsation:25',
                                        version='any',
                                        name=MultilingualString(
                                            value='stadt-teil-auto Car Sharing Göttingen'
                                        ),
                                        description=MultilingualString(
                                            value='Comment here if the organisation is a customer making a private place available for carSharing, and set the OrganisationType to "other"'
                                        ),
                                        organisation_type=[
                                            OrganisationTypeEnumeration.FACILITY_OPERATOR,
                                        ]
                                    ),
                                    ResponsibilitySet(
                                        id='FR:ResponsibilitySet:0123',
                                        version='any',
                                        roles=ResponsibilityRoleAssignmentsRelStructure(
                                            responsibility_role_assignment=[
                                                ResponsibilityRoleAssignment(
                                                    id='GE:ResponsibilityRoleAssignment:01',
                                                    version='any',
                                                    stakeholder_role_type=[
                                                        StakeholderRoleTypeEnumeration.ENTITY_LEGAL_OWNERSHIP,
                                                    ],
                                                    responsible_organisation_ref=OrganisationRefStructure(
                                                        ref='GE:Organsation:25'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    Vehicle(
                                        id='GE:Vehicle:7292',
                                        version='any',
                                        name=MultilingualString(
                                            value='Renault Trafic (GÖ-D 9849)'
                                        ),
                                        registration_number='GÖ-D 9849',
                                        transport_type_ref_or_vehicle_type_ref=VehicleTypeRef(
                                            ref='GE:SimpleVehicleType:1'
                                        ),
                                        vehicle_model_ref=VehicleModelRef(
                                            ref='GE:VehicleModel:1'
                                        )
                                    ),
                                    SimpleVehicleType(
                                        id='GE:SimpleVehicleType:1',
                                        version='any',
                                        euro_class='3',
                                        propulsion_type=PropulsionTypeEnumeration.COMBUSTION,
                                        fuel_type_or_type_of_fuel=TransportTypeVersionStructure.FuelType(
                                            value=FuelTypeEnumeration.DIESEL
                                        ),
                                        maximum_range=Decimal('845'),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.SELF_DRIVE,
                                        length=Decimal('4'),
                                        width=Decimal('1.9'),
                                        height=Decimal('1.4'),
                                        vehicle_category=SimpleVehicleCategoryEnumeration.CAR
                                    ),
                                    VehicleModel(
                                        id='GE:VehicleModel:1',
                                        version='any',
                                        name=MultilingualString(
                                            value='Renault Trafic'
                                        ),
                                        vehicle_model_profile_ref=CarModelProfileRef(
                                            ref='GE:CarEquipmentProfile:1'
                                        )
                                    ),
                                    CarModelProfile(
                                        id='GE:CarEquipmentProfile:1',
                                        version='any',
                                        child_seat=ChildSeatEnumeration.SMALL_CHILD,
                                        seats=5
                                    ),
                                    Fleet(
                                        id='GE:Fleet:1',
                                        version='any',
                                        name=MultilingualString(
                                            value='Stadtmobil car fleet'
                                        ),
                                        members=VehiclesRelStructure(
                                            vehicle_ref_or_vehicle=[
                                                VehicleRef(
                                                    ref='GE:Vehicle:7292'
                                                ),
                                            ]
                                        ),
                                        transport_types=TransportTypeRefsRelStructure(
                                            transport_type_ref_or_vehicle_type_ref=[
                                                VehicleTypeRef(
                                                    ref='GE:VehicleType:1'
                                                ),
                                            ]
                                        )
                                    ),
                                    VehicleSharingService(
                                        id='GE:VehicleSharingService:1',
                                        version='any',
                                        organisation_ref_or_other_organisation_ref_or_transport_organisation_ref=OperatorRef(
                                            ref='GE:Operator:1'
                                        ),
                                        booking_required=True,
                                        registration_required=True,
                                        proposed_by_services=OnlineServiceRefsRelStructure(
                                            online_service_ref=[
                                                OnlineServiceRef(
                                                    version='any',
                                                    ref='GE:OnlineServiceRef:12'
                                                ),
                                            ]
                                        ),
                                        vehicle_sharing_ref=VehicleSharingRef(
                                            version='any',
                                            ref='GE:VehicleSharing:12'
                                        ),
                                        minimum_sharing_period=XmlDuration("PT30M"),
                                        maximum_sharing_period=XmlDuration("PT24H"),
                                        fleets=FleetRefsRelStructure(
                                            fleet_ref=[
                                                FleetRef(
                                                    version='any',
                                                    ref='GE:Fleet:1'
                                                ),
                                            ]
                                        )
                                    ),
                                    OnlineService(
                                        id='GE:OnlineServiceRef:12',
                                        version='any',
                                        name=MultilingualString(
                                            value='Stadtmobil'
                                        ),
                                        service_booking_arrangements=ServiceBookingArrangementsStructure(
                                            booking_url='https://www.stadtmobil.de/'
                                        ),
                                        log_in_required=True
                                    ),
                                    VehicleSharing(
                                        id='GE:VehicleSharing:12',
                                        version='any',
                                        name=MultilingualString(
                                            value='German vehicle sharing service'
                                        ),
                                        vehicle_sharing_type=VehicleSharingTypeEnumeration.VEHICLE_SHARING
                                    ),
                                    Operator(
                                        id='GE:Operator:1',
                                        version='any',
                                        name=MultilingualString(
                                            value='Stadtmobil'
                                        ),
                                        primary_mode=AllModesEnumeration.CAR
                                    ),
                                ]
                            )
                        ),
                    ]
                )
            ),
        ]
    ),
    version='1.2.2'
)
