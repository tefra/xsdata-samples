from decimal import Decimal
from netex.models.access_space import AccessSpace
from netex.models.access_space_ref import AccessSpaceRef
from netex.models.access_space_type_enumeration import AccessSpaceTypeEnumeration
from netex.models.access_spaces_rel_structure import AccessSpacesRelStructure
from netex.models.all_modes_enumeration import AllModesEnumeration
from netex.models.all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from netex.models.codespace import Codespace
from netex.models.codespace_ref_structure import CodespaceRefStructure
from netex.models.codespaces_rel_structure import CodespacesRelStructure
from netex.models.compass_bearing8_enumeration import CompassBearing8Enumeration
from netex.models.connection import Connection
from netex.models.connection_end_structure import ConnectionEndStructure
from netex.models.covered_enumeration import CoveredEnumeration
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.destination_display import DestinationDisplay
from netex.models.destination_display_ref import DestinationDisplayRef
from netex.models.destination_displays_in_frame_rel_structure import DestinationDisplaysInFrameRelStructure
from netex.models.direction import Direction
from netex.models.direction_ref import DirectionRef
from netex.models.direction_type_enumeration import DirectionTypeEnumeration
from netex.models.directions_in_frame_rel_structure import DirectionsInFrameRelStructure
from netex.models.display_assignment import DisplayAssignment
from netex.models.display_assignment_type_enumeration import DisplayAssignmentTypeEnumeration
from netex.models.display_assignments_rel_structure import DisplayAssignmentsRelStructure
from netex.models.entity_in_version_structure import AvailabilityCondition
from netex.models.general_version_frame_structure import CompositeFrame
from netex.models.general_version_frame_structure import FramesRelStructure
from netex.models.journey_patterns_in_frame_rel_structure import JourneyPatternsInFrameRelStructure
from netex.models.line import Line
from netex.models.lines_in_frame_rel_structure import LinesInFrameRelStructure
from netex.models.location_structure_2 import LocationStructure2
from netex.models.logical_display import LogicalDisplay
from netex.models.logical_display_ref import LogicalDisplayRef
from netex.models.logical_displays_in_frame_rel_structure import LogicalDisplaysInFrameRelStructure
from netex.models.modification_enumeration import ModificationEnumeration
from netex.models.multilingual_string import MultilingualString
from netex.models.network_frame_topic_structure import NetworkFrameTopicStructure
from netex.models.participant_ref import ParticipantRef
from netex.models.passenger_information_equipment import PassengerInformationEquipment
from netex.models.passenger_information_equipments_in_frame_rel_structure import PassengerInformationEquipmentsInFrameRelStructure
from netex.models.passenger_stop_assignment import PassengerStopAssignment
from netex.models.points_in_journey_pattern_rel_structure import PointsInJourneyPatternRelStructure
from netex.models.pos import Pos
from netex.models.private_code_structure import PrivateCodeStructure
from netex.models.publication_delivery import PublicationDelivery
from netex.models.publication_request_structure import PublicationRequestStructure
from netex.models.quay import Quay
from netex.models.quay_ref import QuayRef
from netex.models.quay_type_enumeration import QuayTypeEnumeration
from netex.models.quays_rel_structure import QuaysRelStructure
from netex.models.resource_frame import ResourceFrame
from netex.models.responsibility_set_ref_structure import ResponsibilitySetRefStructure
from netex.models.road_address import RoadAddress
from netex.models.route_ref import RouteRef
from netex.models.scheduled_stop_point import ScheduledStopPoint
from netex.models.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.models.scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from netex.models.scheduled_stop_points_in_frame_rel_structure import ScheduledStopPointsInFrameRelStructure
from netex.models.service_frame import ServiceFrame
from netex.models.service_journey_pattern import ServiceJourneyPattern
from netex.models.service_journey_pattern_ref import ServiceJourneyPatternRef
from netex.models.simple_point_version_structure import SimplePointVersionStructure
from netex.models.site_frame import SiteFrame
from netex.models.stop_assignments_in_frame_rel_structure import StopAssignmentsInFrameRelStructure
from netex.models.stop_place import StopPlace
from netex.models.stop_place_ref import StopPlaceRef
from netex.models.stop_places_in_frame_rel_structure import StopPlacesInFrameRelStructure
from netex.models.stop_point_in_journey_pattern import StopPointInJourneyPattern
from netex.models.stop_type_enumeration import StopTypeEnumeration
from netex.models.timetable_frame_ref import TimetableFrameRef
from netex.models.timing_point_status_enumeration import TimingPointStatusEnumeration
from netex.models.transfers_in_frame_rel_structure import TransfersInFrameRelStructure
from netex.models.type_of_passenger_information_equipment import TypeOfPassengerInformationEquipment
from netex.models.type_of_passenger_information_equipment_ref import TypeOfPassengerInformationEquipmentRef
from netex.models.types_of_value_in_frame_rel_structure import TypesOfValueInFrameRelStructure
from netex.models.types_of_value_structure import TypesOfValueStructure
from netex.models.value_set import ValueSet
from netex.models.vehicle_mode import VehicleMode
from netex.models.vehicle_mode_enumeration import VehicleModeEnumeration
from netex.models.version_frame_defaults_structure import VersionFrameDefaultsStructure
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration


obj = PublicationDelivery(
    publication_timestamp=XmlDateTime(2010, 12, 17, 9, 30, 47, 0, 0),
    participant_ref=ParticipantRef(
        value='SYS001'
    ),
    publication_request=PublicationRequestStructure(
        request_timestamp=XmlDateTime(2010, 12, 17, 9, 30, 47, 0, 0),
        participant_ref=ParticipantRef(
            value='SYS002'
        ),
        topics=PublicationRequestStructure.Topics(
            network_frame_topic=[
                NetworkFrameTopicStructure(
                    choice=NetworkFrameTopicStructure.SelectionValidityConditions(
                        validity_condition=[
                            AvailabilityCondition(
                                id='hde:CAL_02',
                                version='any',
                                from_date=XmlDateTime(2010, 11, 1, 0, 0, 0, 0, 0)
                            ),
                        ]
                    ),
                    choice_1=[
                        TimetableFrameRef(
                            ref='hde:TimetableFrameTIM_23_O'
                        ),
                    ]
                ),
            ]
        )
    ),
    publication_refresh_interval=XmlDuration("P1M"),
    description=MultilingualString(
        value='Example  of simple timetable frame with two journeys and service calendar'
    ),
    data_objects=DataObjectsRelStructure(
        choice=[
            CompositeFrame(
                id='hde:CAL_02',
                version='any',
                codespaces=CodespacesRelStructure(
                    codespace_ref_or_codespace=[
                        Codespace(
                            id='mybus',
                            xmlns='mybus',
                            xmlns_url='http://www.mybuses.eu/stuff',
                            description='My buses'
                        ),
                        Codespace(
                            id='hde',
                            xmlns='hde',
                            xmlns_url='http://www.halt.de/',
                            description='Stop data  data'
                        ),
                        Codespace(
                            id='myrail',
                            xmlns='myrail',
                            xmlns_url='http://www.myrail.eu/stuff',
                            description='My rail data'
                        ),
                    ]
                ),
                frame_defaults=VersionFrameDefaultsStructure(
                    default_codespace_ref=CodespaceRefStructure(
                        ref='mybus'
                    )
                ),
                frames=FramesRelStructure(
                    common_frame=[
                        ServiceFrame(
                            id='mybus:svf_12',
                            version='any',
                            name=MultilingualString(
                                value='Logical Display assignments for Bravo '
                            ),
                            directions=DirectionsInFrameRelStructure(
                                direction=[
                                    Direction(
                                        id='mybus:DR_Westbound',
                                        version='any',
                                        name=MultilingualString(
                                            value='Westbound'
                                        )
                                    ),
                                    Direction(
                                        id='mybus:DR_Eastbound',
                                        version='any',
                                        name=MultilingualString(
                                            value='Eastbound'
                                        )
                                    ),
                                    Direction(
                                        id='mybus:DR_Southbound',
                                        version='any',
                                        name=MultilingualString(
                                            value='Southbound'
                                        )
                                    ),
                                    Direction(
                                        id='mybus:DR_Northbound',
                                        version='any',
                                        name=MultilingualString(
                                            value='Northbound'
                                        )
                                    ),
                                ]
                            ),
                            lines=LinesInFrameRelStructure(
                                line=[
                                    Line(
                                        id='mybus:LN_24',
                                        version='any',
                                        name=MultilingualString(
                                            value='Line 24 Alpha to Charley Green'
                                        ),
                                        short_name=MultilingualString(
                                            value='Line 24'
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.TRAM,
                                        public_code='24'
                                    ),
                                    Line(
                                        id='mybus:LN_46',
                                        version='any',
                                        name=MultilingualString(
                                            value='Line 46 Foxtrot to Tango'
                                        ),
                                        short_name=MultilingualString(
                                            value='Line 46'
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
                                        public_code='46'
                                    ),
                                    Line(
                                        id='mybus:LN_68',
                                        version='any',
                                        name=MultilingualString(
                                            value='Line 68 Bravo to Kilo'
                                        ),
                                        short_name=MultilingualString(
                                            value='Line 68'
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
                                        public_code='46'
                                    ),
                                ]
                            ),
                            destination_displays=DestinationDisplaysInFrameRelStructure(
                                destination_display=[
                                    DestinationDisplay(
                                        id='mybus:DST_Alpha',
                                        version='any',
                                        name=MultilingualString(
                                            value='Alpha Avenue'
                                        ),
                                        short_name=MultilingualString(
                                            value='Alpha Av'
                                        )
                                    ),
                                    DestinationDisplay(
                                        id='mybus:DST_Bravo',
                                        version='any',
                                        name=MultilingualString(
                                            value='Bravo Arch'
                                        ),
                                        short_name=MultilingualString(
                                            value='Bravo'
                                        )
                                    ),
                                    DestinationDisplay(
                                        id='mybus:DST_Charley',
                                        version='any',
                                        name=MultilingualString(
                                            value='Charley Green'
                                        ),
                                        short_name=MultilingualString(
                                            value='Charley G'
                                        )
                                    ),
                                    DestinationDisplay(
                                        id='mybus:DST_Foxtrot',
                                        version='any',
                                        name=MultilingualString(
                                            value='Foxtrot Avenue'
                                        ),
                                        short_name=MultilingualString(
                                            value='Foxtrot '
                                        )
                                    ),
                                    DestinationDisplay(
                                        id='mybus:DST_Kilo',
                                        version='any',
                                        name=MultilingualString(
                                            value='Kilo Street'
                                        ),
                                        short_name=MultilingualString(
                                            value='Kilo '
                                        )
                                    ),
                                    DestinationDisplay(
                                        id='mybus:DST_Tango',
                                        version='any',
                                        name=MultilingualString(
                                            value='Tango Green'
                                        ),
                                        short_name=MultilingualString(
                                            value='Tango G'
                                        )
                                    ),
                                ]
                            ),
                            scheduled_stop_points=ScheduledStopPointsInFrameRelStructure(
                                scheduled_stop_point=[
                                    ScheduledStopPoint(
                                        id='mybus:SSP_001',
                                        version='any',
                                        name=MultilingualString(
                                            value='Alpha & Castle'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('53.0000'),
                                            latitude=Decimal('0.1000')
                                        ),
                                        short_name=MultilingualString(
                                            value='Alpha'
                                        ),
                                        public_code=PrivateCodeStructure(
                                            value='ALPH'
                                        ),
                                        stop_type=StopTypeEnumeration.ONSTREET_TRAM,
                                        vehicle_modes=[
                                            VehicleModeEnumeration.TRAM,
                                        ]
                                    ),
                                    ScheduledStopPoint(
                                        id='mybus:SSP_002',
                                        version='any',
                                        name=MultilingualString(
                                            value='Bravo Arch ( Tram)'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('53.2000'),
                                            latitude=Decimal('0.2000')
                                        ),
                                        short_name=MultilingualString(
                                            value='Bravo Arch'
                                        ),
                                        public_code=PrivateCodeStructure(
                                            value='BRAV'
                                        ),
                                        stop_type=StopTypeEnumeration.ONSTREET_TRAM,
                                        vehicle_modes=[
                                            VehicleModeEnumeration.BUS,
                                            VehicleModeEnumeration.TRAM,
                                        ]
                                    ),
                                    ScheduledStopPoint(
                                        id='mybus:SSP_077',
                                        version='any',
                                        name=MultilingualString(
                                            value='Charley Green'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('53.3000'),
                                            latitude=Decimal('0.3000')
                                        ),
                                        short_name=MultilingualString(
                                            value='Charley'
                                        ),
                                        public_code=PrivateCodeStructure(
                                            value='CHAS'
                                        ),
                                        stop_type=StopTypeEnumeration.ONSTREET_TRAM,
                                        vehicle_modes=[
                                            VehicleModeEnumeration.TRAM,
                                        ]
                                    ),
                                    ScheduledStopPoint(
                                        id='mybus:SSP_031',
                                        version='any',
                                        name=MultilingualString(
                                            value='Foxtrot Lane'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('53.34000'),
                                            latitude=Decimal('0.34000')
                                        ),
                                        short_name=MultilingualString(
                                            value='Foxtrot Lane'
                                        ),
                                        public_code=PrivateCodeStructure(
                                            value='Foxtrot'
                                        ),
                                        stop_type=StopTypeEnumeration.ONSTREET_BUS,
                                        vehicle_modes=[
                                            VehicleModeEnumeration.BUS,
                                            VehicleModeEnumeration.TRAM,
                                        ]
                                    ),
                                    ScheduledStopPoint(
                                        id='mybus:SSP_032',
                                        version='any',
                                        name=MultilingualString(
                                            value='Bravo Arch Bus'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('53.2000'),
                                            latitude=Decimal('0.2000')
                                        ),
                                        short_name=MultilingualString(
                                            value='Bravo Arch'
                                        ),
                                        public_code=PrivateCodeStructure(
                                            value='BRAV'
                                        ),
                                        stop_type=StopTypeEnumeration.ONSTREET_BUS,
                                        vehicle_modes=[
                                            VehicleModeEnumeration.BUS,
                                        ]
                                    ),
                                    ScheduledStopPoint(
                                        id='mybus:SSP_033',
                                        version='any',
                                        name=MultilingualString(
                                            value='Tango Lane'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('53.34000'),
                                            latitude=Decimal('0.34000')
                                        ),
                                        timing_point_status=TimingPointStatusEnumeration.TIMING_POINT,
                                        short_name=MultilingualString(
                                            value='Tango Lane'
                                        ),
                                        public_code=PrivateCodeStructure(
                                            value='Tango'
                                        ),
                                        stop_type=StopTypeEnumeration.ONSTREET_BUS,
                                        vehicle_modes=[
                                            VehicleModeEnumeration.BUS,
                                        ]
                                    ),
                                    ScheduledStopPoint(
                                        id='mybus:SSP_035',
                                        version='any',
                                        name=MultilingualString(
                                            value='Juliet Park'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('53.35000'),
                                            latitude=Decimal('0.34000')
                                        ),
                                        short_name=MultilingualString(
                                            value='Juliet Lane'
                                        ),
                                        public_code=PrivateCodeStructure(
                                            value='Juliet'
                                        ),
                                        stop_type=StopTypeEnumeration.ONSTREET_BUS,
                                        vehicle_modes=[
                                            VehicleModeEnumeration.BUS,
                                        ]
                                    ),
                                    ScheduledStopPoint(
                                        id='mybus:SSP_036',
                                        version='any',
                                        name=MultilingualString(
                                            value='Kilo Street'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('53.34000'),
                                            latitude=Decimal('0.34000')
                                        ),
                                        short_name=MultilingualString(
                                            value='Kilo  Lane'
                                        ),
                                        public_code=PrivateCodeStructure(
                                            value='Kilo '
                                        ),
                                        stop_type=StopTypeEnumeration.ONSTREET_BUS,
                                        vehicle_modes=[
                                            VehicleModeEnumeration.BUS,
                                        ]
                                    ),
                                    ScheduledStopPoint(
                                        id='myrail:SSP_042',
                                        version='any',
                                        name=MultilingualString(
                                            value='Bravo Arch (Rail)'
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal('53.2000'),
                                            latitude=Decimal('0.2000')
                                        ),
                                        timing_point_status=TimingPointStatusEnumeration.TIMING_POINT,
                                        short_name=MultilingualString(
                                            value='Bravo Arch'
                                        ),
                                        public_code=PrivateCodeStructure(
                                            value='BRAV'
                                        ),
                                        stop_type=StopTypeEnumeration.RAIL_STATION,
                                        vehicle_modes=[
                                            VehicleModeEnumeration.RAIL,
                                        ]
                                    ),
                                ]
                            ),
                            connections=TransfersInFrameRelStructure(
                                transfer=[
                                    Connection(
                                        id='mybus:CX_SSP_002_to_SSP_032',
                                        version='any',
                                        name=MultilingualString(
                                            value='Bravo Arch : Tram / Bus  Connection  '
                                        ),
                                        both_ways=True,
                                        from_value=ConnectionEndStructure(
                                            transport_mode=AllModesEnumeration.TRAM,
                                            scheduled_stop_point_ref_or_vehicle_meeting_point_ref=ScheduledStopPointRefStructure(
                                                version='any',
                                                ref='mybus:SSP_002'
                                            )
                                        ),
                                        to=ConnectionEndStructure(
                                            transport_mode=AllModesEnumeration.BUS,
                                            scheduled_stop_point_ref_or_vehicle_meeting_point_ref=ScheduledStopPointRefStructure(
                                                version='any',
                                                ref='mybus:SSP_032'
                                            )
                                        )
                                    ),
                                    Connection(
                                        id='mybus:CX_SSP_002_to_SSP_042',
                                        version='any',
                                        name=MultilingualString(
                                            value='Bravo Arch : Tram / Rail  Connection  '
                                        ),
                                        both_ways=True,
                                        from_value=ConnectionEndStructure(
                                            transport_mode=AllModesEnumeration.TRAM,
                                            scheduled_stop_point_ref_or_vehicle_meeting_point_ref=ScheduledStopPointRefStructure(
                                                version='any',
                                                ref='mybus:SSP_002'
                                            )
                                        ),
                                        to=ConnectionEndStructure(
                                            transport_mode=AllModesEnumeration.RAIL,
                                            scheduled_stop_point_ref_or_vehicle_meeting_point_ref=ScheduledStopPointRefStructure(
                                                version='any',
                                                ref='myrail:SSP_042'
                                            )
                                        )
                                    ),
                                    Connection(
                                        id='mybus:CX_SSP_042_to_SSP_032',
                                        version='any',
                                        name=MultilingualString(
                                            value='Bravo Arch : Rail / bus  Connection  '
                                        ),
                                        both_ways=True,
                                        from_value=ConnectionEndStructure(
                                            transport_mode=AllModesEnumeration.RAIL,
                                            scheduled_stop_point_ref_or_vehicle_meeting_point_ref=ScheduledStopPointRefStructure(
                                                version='any',
                                                ref='myrail:SSP_042'
                                            )
                                        ),
                                        to=ConnectionEndStructure(
                                            transport_mode=AllModesEnumeration.BUS,
                                            scheduled_stop_point_ref_or_vehicle_meeting_point_ref=ScheduledStopPointRefStructure(
                                                version='any',
                                                ref='mybus:SSP_032'
                                            )
                                        )
                                    ),
                                ]
                            ),
                            stop_assignments=StopAssignmentsInFrameRelStructure(
                                stop_assignment=[
                                    PassengerStopAssignment(
                                        id='hde:psa_SSP_002_to_SP002B',
                                        version='any',
                                        description=MultilingualString(
                                            value='Assigns   Bravo tram  to physical stop - ',
                                            lang='en'
                                        ),
                                        order=1,
                                        fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=ScheduledStopPointRef(
                                            version='any',
                                            ref='mybus:SSP_002'
                                        ),
                                        taxi_rank_ref_or_stop_place_ref_or_stop_place=StopPlaceRef(
                                            version='any',
                                            ref='mybus:SP002B'
                                        )
                                    ),
                                    PassengerStopAssignment(
                                        id='hde:psa_SSP_032_to_SP002B',
                                        version='any',
                                        description=MultilingualString(
                                            value='Assigns  Bravo bus to physical stop ',
                                            lang='en'
                                        ),
                                        order=1,
                                        fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=ScheduledStopPointRef(
                                            version='any',
                                            ref='mybus:SSP_032'
                                        ),
                                        taxi_rank_ref_or_stop_place_ref_or_stop_place=StopPlaceRef(
                                            version='any',
                                            ref='mybus:SP002B'
                                        )
                                    ),
                                    PassengerStopAssignment(
                                        id='hde:psa_SSP_042_to_SP002B',
                                        version='any',
                                        description=MultilingualString(
                                            value='Assigns  Bravo  rail to physical stop ',
                                            lang='en'
                                        ),
                                        order=1,
                                        fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=ScheduledStopPointRef(
                                            version='any',
                                            ref='myrail:SSP_042'
                                        ),
                                        taxi_rank_ref_or_stop_place_ref_or_stop_place=StopPlaceRef(
                                            version='any',
                                            ref='mybus:SP002B'
                                        )
                                    ),
                                ]
                            ),
                            journey_patterns=JourneyPatternsInFrameRelStructure(
                                choice=[
                                    ServiceJourneyPattern(
                                        id='hde:jp_24o',
                                        version='any',
                                        name=MultilingualString(
                                            value='Alpha to Charley Green'
                                        ),
                                        route_ref_or_route_view=RouteRef(
                                            value='EXTERNAL',
                                            ref='mybus:RT_24o'
                                        ),
                                        direction_type=DirectionTypeEnumeration.OUTBOUND,
                                        direction_ref_or_direction_view=DirectionRef(
                                            version='any',
                                            ref='mybus:DR_Westbound'
                                        ),
                                        destination_display_ref_or_destination_display_view=DestinationDisplayRef(
                                            version='any',
                                            ref='mybus:DST_Charley'
                                        ),
                                        points_in_sequence=PointsInJourneyPatternRelStructure(
                                            point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=[
                                                StopPointInJourneyPattern(
                                                    id='hde:pijp_24o_01',
                                                    version='any',
                                                    order=1,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_001'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='hde:pijp_24o_02',
                                                    version='any',
                                                    order=2,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_002'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='hde:pijp_24o_03',
                                                    version='any',
                                                    order=3,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_077'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    ServiceJourneyPattern(
                                        id='hde:jp_24i',
                                        version='any',
                                        name=MultilingualString(
                                            value='Charley Green to Alpha'
                                        ),
                                        route_ref_or_route_view=RouteRef(
                                            value='EXTERNAL',
                                            ref='mybus:RT_24i'
                                        ),
                                        direction_type=DirectionTypeEnumeration.INBOUND,
                                        direction_ref_or_direction_view=DirectionRef(
                                            version='any',
                                            ref='mybus:DR_Eastbound'
                                        ),
                                        destination_display_ref_or_destination_display_view=DestinationDisplayRef(
                                            version='any',
                                            ref='mybus:DST_Alpha'
                                        ),
                                        points_in_sequence=PointsInJourneyPatternRelStructure(
                                            point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=[
                                                StopPointInJourneyPattern(
                                                    id='hde:jp_24i_01',
                                                    version='any',
                                                    order=1,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_077'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='hde:jp_24i_02',
                                                    version='any',
                                                    order=2,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_002'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='hde:jp_24i_03',
                                                    version='any',
                                                    order=3,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_001'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    ServiceJourneyPattern(
                                        id='hde:jp_46o',
                                        version='any',
                                        name=MultilingualString(
                                            value='Foxtrot to  Tango   '
                                        ),
                                        route_ref_or_route_view=RouteRef(
                                            value='EXTERNAL',
                                            ref='mybus:RT_46o'
                                        ),
                                        direction_type=DirectionTypeEnumeration.OUTBOUND,
                                        direction_ref_or_direction_view=DirectionRef(
                                            version='any',
                                            ref='mybus:DR_Southbound'
                                        ),
                                        destination_display_ref_or_destination_display_view=DestinationDisplayRef(
                                            version='any',
                                            ref='mybus:DST_Tango'
                                        ),
                                        points_in_sequence=PointsInJourneyPatternRelStructure(
                                            point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=[
                                                StopPointInJourneyPattern(
                                                    id='hde:pijp_46o_01',
                                                    version='any',
                                                    order=1,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_031'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='hde:pijp_46o_02',
                                                    version='any',
                                                    order=2,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_032'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='hde:pijp_46o_03',
                                                    version='any',
                                                    order=3,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_033'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    ServiceJourneyPattern(
                                        id='hde:jp_46i',
                                        version='any',
                                        name=MultilingualString(
                                            value='Tango  to  Foxtrot   '
                                        ),
                                        route_ref_or_route_view=RouteRef(
                                            value='EXTERNAL',
                                            ref='mybus:RT_46i'
                                        ),
                                        direction_type=DirectionTypeEnumeration.OUTBOUND,
                                        direction_ref_or_direction_view=DirectionRef(
                                            version='any',
                                            ref='mybus:DR_Northbound'
                                        ),
                                        destination_display_ref_or_destination_display_view=DestinationDisplayRef(
                                            version='any',
                                            ref='mybus:DST_Foxtrot'
                                        ),
                                        points_in_sequence=PointsInJourneyPatternRelStructure(
                                            point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=[
                                                StopPointInJourneyPattern(
                                                    id='hde:pijp_46i_01',
                                                    version='any',
                                                    order=1,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_033'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='hde:pijp_46i_02',
                                                    version='any',
                                                    order=2,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_032'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='hde:pijp_46i_03',
                                                    version='any',
                                                    order=3,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_031'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    ServiceJourneyPattern(
                                        id='hde:jp_68o',
                                        version='any',
                                        name=MultilingualString(
                                            value='Bravo to  Kilo   '
                                        ),
                                        route_ref_or_route_view=RouteRef(
                                            value='EXTERNAL',
                                            ref='mybus:RT_68o'
                                        ),
                                        direction_type=DirectionTypeEnumeration.OUTBOUND,
                                        direction_ref_or_direction_view=DirectionRef(
                                            version='any',
                                            ref='mybus:DR_Southbound'
                                        ),
                                        destination_display_ref_or_destination_display_view=DestinationDisplayRef(
                                            version='any',
                                            ref='mybus:DST_Tango'
                                        ),
                                        points_in_sequence=PointsInJourneyPatternRelStructure(
                                            point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=[
                                                StopPointInJourneyPattern(
                                                    id='hde:pijp_68o_01',
                                                    version='any',
                                                    order=1,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_032'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='hde:pijp_68o_02',
                                                    version='any',
                                                    order=2,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_035'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='hde:pijp_68o_03',
                                                    version='any',
                                                    order=3,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_036'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    ServiceJourneyPattern(
                                        id='hde:jp_68i',
                                        version='any',
                                        name=MultilingualString(
                                            value='Kilo to  Bravo   '
                                        ),
                                        route_ref_or_route_view=RouteRef(
                                            value='EXTERNAL',
                                            ref='mybus:RT_68i'
                                        ),
                                        direction_type=DirectionTypeEnumeration.OUTBOUND,
                                        direction_ref_or_direction_view=DirectionRef(
                                            version='any',
                                            ref='mybus:DR_Northbound'
                                        ),
                                        destination_display_ref_or_destination_display_view=DestinationDisplayRef(
                                            version='any',
                                            ref='mybus:DST_Foxtrot'
                                        ),
                                        points_in_sequence=PointsInJourneyPatternRelStructure(
                                            point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=[
                                                StopPointInJourneyPattern(
                                                    id='hde:pijp_68i_01',
                                                    version='any',
                                                    order=1,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_036'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='hde:pijp_68i_02',
                                                    version='any',
                                                    order=2,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_035'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='hde:pijp_68i_03',
                                                    version='any',
                                                    order=3,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_032'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            logical_displays=LogicalDisplaysInFrameRelStructure(
                                logical_display=[
                                    LogicalDisplay(
                                        id='mybus:LD001_TramBus_Q1_EastboundSouthbound',
                                        version='any',
                                        description=MultilingualString(
                                            value='Departures Display for use on  Bravo Bus/Tram Quay 1 Outbound'
                                        ),
                                        display_assignments=DisplayAssignmentsRelStructure(
                                            display_assignment_ref_or_display_assignment=[
                                                DisplayAssignment(
                                                    id='mybus:LD001_TramBus_Q1_EastboundSouthbound',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Assign  ScheduledStopPoint 002 (Bravo) route 24 Eastbound Departures to Display LD001 '
                                                    ),
                                                    order=1,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_002'
                                                    ),
                                                    journey_pattern_ref=ServiceJourneyPatternRef(
                                                        version='any',
                                                        ref='hde:jp_24o'
                                                    ),
                                                    display_assignment_type=DisplayAssignmentTypeEnumeration.DEPARTURES,
                                                    number_of_journeys_to_show=2,
                                                    display_priority=1
                                                ),
                                                DisplayAssignment(
                                                    id='mybus:LD001_TramBus_Q1_EastboundSouthbound',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Assign ScheduledStopPoint 032 (Bravo) route 46 Southbound Departures to Display LD001  '
                                                    ),
                                                    order=2,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_032'
                                                    ),
                                                    journey_pattern_ref=ServiceJourneyPatternRef(
                                                        version='any',
                                                        ref='hde:jp_46o'
                                                    ),
                                                    display_assignment_type=DisplayAssignmentTypeEnumeration.DEPARTURES,
                                                    number_of_journeys_to_show=2,
                                                    display_priority=1
                                                ),
                                                DisplayAssignment(
                                                    id='mybus:LD001_TramBus_Q1_EastboundSouthbound',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Assign   ScheduledStopPoint 032 (Bravo)  route 68 Eastbound Departures to Display LD001  '
                                                    ),
                                                    order=3,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_032'
                                                    ),
                                                    journey_pattern_ref=ServiceJourneyPatternRef(
                                                        version='any',
                                                        ref='hde:jp_68o'
                                                    ),
                                                    display_assignment_type=DisplayAssignmentTypeEnumeration.DEPARTURES,
                                                    number_of_journeys_to_show=2,
                                                    display_priority=1
                                                ),
                                            ]
                                        )
                                    ),
                                    LogicalDisplay(
                                        id='mybus:LD002_TramBus_Q2_WestboundNorthbound',
                                        version='any',
                                        description=MultilingualString(
                                            value='Departures Display for use on  Bravo Bus/Tram Quay 2'
                                        ),
                                        display_assignments=DisplayAssignmentsRelStructure(
                                            display_assignment_ref_or_display_assignment=[
                                                DisplayAssignment(
                                                    id='mybus:LD002_TramBus_Q2_WestboundNorthbound',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Assign ScheduledStopPoint 002 (Bravo)  LINE 24 Westbound Departures to Display LD002 '
                                                    ),
                                                    order=1,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_002'
                                                    ),
                                                    journey_pattern_ref=ServiceJourneyPatternRef(
                                                        version='any',
                                                        ref='hde:jp_24i'
                                                    ),
                                                    display_assignment_type=DisplayAssignmentTypeEnumeration.DEPARTURES,
                                                    number_of_journeys_to_show=2,
                                                    display_priority=1
                                                ),
                                                DisplayAssignment(
                                                    id='mybus:LD002_TramBus_Q2_WestboundNorthbound',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Assign ScheduledStopPoint 0032  (Bravo)  LINE 46 Northbound Departures to Display LD002 '
                                                    ),
                                                    order=2,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_032'
                                                    ),
                                                    journey_pattern_ref=ServiceJourneyPatternRef(
                                                        version='any',
                                                        ref='hde:jp_46i'
                                                    ),
                                                    display_assignment_type=DisplayAssignmentTypeEnumeration.DEPARTURES,
                                                    number_of_journeys_to_show=2,
                                                    display_priority=2
                                                ),
                                                DisplayAssignment(
                                                    id='mybus:LD002_TramBus_Q2_WestboundNorthbound',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Assign ScheduledStopPoint 0032  (Bravo)  LINE 68  Northbound  Departuresto Display LD002 - Arrivals'
                                                    ),
                                                    order=3,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_032'
                                                    ),
                                                    journey_pattern_ref=ServiceJourneyPatternRef(
                                                        version='any',
                                                        ref='hde:jp_68i'
                                                    ),
                                                    display_assignment_type=DisplayAssignmentTypeEnumeration.ARRIVALS,
                                                    number_of_journeys_to_show=3,
                                                    display_priority=3
                                                ),
                                            ]
                                        )
                                    ),
                                    LogicalDisplay(
                                        id='mybus:LD010_TicketHall_arrivals',
                                        version='any',
                                        name=MultilingualString(
                                            value='All Arrivals Display for use in Rail Ticket Hall'
                                        ),
                                        display_assignments=DisplayAssignmentsRelStructure(
                                            display_assignment_ref_or_display_assignment=[
                                                DisplayAssignment(
                                                    id='mybus:LD010_TicketHall_arrivals',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Assign ScheduledStopPoint 002 tram arrivals  all routes for Bravo to Display LD010 '
                                                    ),
                                                    order=1,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_002'
                                                    ),
                                                    vehicle_mode=VehicleMode(
                                                        value=AllModesEnumeration.TRAM
                                                    ),
                                                    display_priority=1
                                                ),
                                                DisplayAssignment(
                                                    id='mybus:LD010_TicketHall_arrivals',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Assign ScheduledStopPoint 032 bus arivals  all  routes for Bravo to Display LD010  '
                                                    ),
                                                    order=2,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_032'
                                                    ),
                                                    vehicle_mode=VehicleMode(
                                                        value=AllModesEnumeration.BUS
                                                    ),
                                                    display_assignment_type=DisplayAssignmentTypeEnumeration.ARRIVALS
                                                ),
                                                DisplayAssignment(
                                                    id='mybus:LD010_TicketHall_arrivals',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Assign ScheduledStopPoint 042 rail  arrivals all routes for Bravo to Display LD010  '
                                                    ),
                                                    order=3,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_032'
                                                    ),
                                                    vehicle_mode=VehicleMode(
                                                        value=AllModesEnumeration.RAIL
                                                    ),
                                                    display_assignment_type=DisplayAssignmentTypeEnumeration.ARRIVALS
                                                ),
                                            ]
                                        )
                                    ),
                                    LogicalDisplay(
                                        id='mybus:LD011_TicketHall_departures',
                                        version='any',
                                        description=MultilingualString(
                                            value='Departures Display in Ticket Hall'
                                        ),
                                        display_assignments=DisplayAssignmentsRelStructure(
                                            display_assignment_ref_or_display_assignment=[
                                                DisplayAssignment(
                                                    id='mybus:LD011_TicketHall_departures',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Assign ScheduledStopPoint 002 tram all routes for Bravo to Display LD011 '
                                                    ),
                                                    order=1,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_002'
                                                    ),
                                                    display_assignment_type=DisplayAssignmentTypeEnumeration.DEPARTURES
                                                ),
                                                DisplayAssignment(
                                                    id='mybus:LD011_TicketHall_departures',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Assign ScheduledStopPoint 032 bus all routes for Bravo to Display LD011 '
                                                    ),
                                                    order=2,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='mybus:SSP_032'
                                                    ),
                                                    display_assignment_type=DisplayAssignmentTypeEnumeration.DEPARTURES
                                                ),
                                                DisplayAssignment(
                                                    id='mybus:LD011_TicketHall_departures',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Assign ScheduledStopPoint 042 rail all routes for Bravo to Display LD011 '
                                                    ),
                                                    order=3,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='myrail:SSP_042'
                                                    ),
                                                    display_assignment_type=DisplayAssignmentTypeEnumeration.DEPARTURES
                                                ),
                                            ]
                                        )
                                    ),
                                    LogicalDisplay(
                                        id='mybus:LD003_Rail_Q1_all',
                                        version='any',
                                        name=MultilingualString(
                                            value='Arrivals and Departures Display for use on  on rail Platform 3'
                                        ),
                                        display_assignments=DisplayAssignmentsRelStructure(
                                            display_assignment_ref_or_display_assignment=[
                                                DisplayAssignment(
                                                    id='mybus:LD003_Rail_Q1_all',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Assign ScheduledStopPoint 042 rail  all routes for Bravo   '
                                                    ),
                                                    order=1,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='any',
                                                        ref='myrail:SSP_042'
                                                    ),
                                                    vehicle_mode=VehicleMode(
                                                        value=AllModesEnumeration.RAIL
                                                    ),
                                                    display_assignment_type=DisplayAssignmentTypeEnumeration.ALL
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            passenger_information_equipments=PassengerInformationEquipmentsInFrameRelStructure(
                                passenger_information_equipment=[
                                    PassengerInformationEquipment(
                                        id='mybus:pif_SP002B_TramBus_Q1',
                                        version='any',
                                        name=MultilingualString(
                                            value='Display on Bravo Tram bus    departures  Platform 1 '
                                        ),
                                        logical_display_ref=LogicalDisplayRef(
                                            version='any',
                                            ref='mybus:LD001_TramBus_Q1_EastboundSouthbound'
                                        ),
                                        stop_place_ref=StopPlaceRef(
                                            version='any',
                                            ref='mybus:SP002B'
                                        ),
                                        choice=QuayRef(
                                            version='any',
                                            ref='mybus:Q_SP002B_1'
                                        ),
                                        type_of_passenger_information_equipment_ref=TypeOfPassengerInformationEquipmentRef(
                                            version='any',
                                            ref='mybus:PlatDisp'
                                        )
                                    ),
                                    PassengerInformationEquipment(
                                        id='mybus:pif_SP002B_TramBus_Q2',
                                        version='any',
                                        name=MultilingualString(
                                            value='Display on Bravo   Tram bus     departures  Platform 2 '
                                        ),
                                        logical_display_ref=LogicalDisplayRef(
                                            version='any',
                                            ref='mybus:LD002_TramBus_Q2_WestboundNorthbound'
                                        ),
                                        stop_place_ref=StopPlaceRef(
                                            version='any',
                                            ref='mybus:SP002B'
                                        ),
                                        choice=QuayRef(
                                            version='any',
                                            ref='mybus:Q_SP002B_2'
                                        ),
                                        type_of_passenger_information_equipment_ref=TypeOfPassengerInformationEquipmentRef(
                                            version='any',
                                            ref='mybus:PlatDisp'
                                        )
                                    ),
                                    PassengerInformationEquipment(
                                        id='mybus:pif_SP002B_TicketHall_arrivals',
                                        version='any',
                                        name=MultilingualString(
                                            value='Display of all Arrivals all modes in Bravo  Ticket  Hall'
                                        ),
                                        logical_display_ref=LogicalDisplayRef(
                                            version='any',
                                            ref='mybus:LD010_TicketHall_arrivals'
                                        ),
                                        stop_place_ref=StopPlaceRef(
                                            version='any',
                                            ref='mybus:SP002B'
                                        ),
                                        choice=AccessSpaceRef(
                                            version='any',
                                            ref='mybus:as_SP002B_01'
                                        ),
                                        type_of_passenger_information_equipment_ref=TypeOfPassengerInformationEquipmentRef(
                                            version='any',
                                            ref='mybus:LargeBoard'
                                        )
                                    ),
                                    PassengerInformationEquipment(
                                        id='mybus:pif_SP002B_TicketHall_departures',
                                        version='any',
                                        name=MultilingualString(
                                            value='Display of all Departures all modes  in Bravo  Ticket  Hall'
                                        ),
                                        logical_display_ref=LogicalDisplayRef(
                                            version='any',
                                            ref='mybus:LD011_TicketHall_departures'
                                        ),
                                        stop_place_ref=StopPlaceRef(
                                            version='any',
                                            ref='mybus:SP002B'
                                        ),
                                        choice=AccessSpaceRef(
                                            version='any',
                                            ref='mybus:as_SP002B_01'
                                        ),
                                        type_of_passenger_information_equipment_ref=TypeOfPassengerInformationEquipmentRef(
                                            version='any',
                                            ref='mybus:LargeBoard'
                                        )
                                    ),
                                    PassengerInformationEquipment(
                                        id='mybus:pif_SP002B_Rail_01',
                                        version='any',
                                        name=MultilingualString(
                                            value='Display 1 on Bravo Rail Rail Platform 3'
                                        ),
                                        logical_display_ref=LogicalDisplayRef(
                                            version='any',
                                            ref='mybus:LD003_Rail_Q1_all'
                                        ),
                                        stop_place_ref=StopPlaceRef(
                                            version='any',
                                            ref='mybus:SP002B'
                                        ),
                                        choice=QuayRef(
                                            version='any',
                                            ref='mybus:Q_SP002B_3'
                                        ),
                                        type_of_passenger_information_equipment_ref=TypeOfPassengerInformationEquipmentRef(
                                            version='any',
                                            ref='mybus:PlatDisp'
                                        )
                                    ),
                                    PassengerInformationEquipment(
                                        id='mybus:pif_SP002B_Rail_02',
                                        version='any',
                                        name=MultilingualString(
                                            value='Display 2 on Bravo Rail Rail Platform 3'
                                        ),
                                        logical_display_ref=LogicalDisplayRef(
                                            version='any',
                                            ref='mybus:LD003_Rail_Q1_all'
                                        ),
                                        stop_place_ref=StopPlaceRef(
                                            version='any',
                                            ref='mybus:SP002B'
                                        ),
                                        choice=QuayRef(
                                            version='any',
                                            ref='mybus:Q_SP002B_3'
                                        ),
                                        type_of_passenger_information_equipment_ref=TypeOfPassengerInformationEquipmentRef(
                                            version='any',
                                            ref='mybus:PlatDisp'
                                        )
                                    ),
                                ]
                            )
                        ),
                        SiteFrame(
                            id='mybus:infraf002',
                            created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                            changed=XmlDateTime(2010, 5, 22, 10, 30, 51, 0, 0),
                            modification=ModificationEnumeration.REVISE,
                            version='024',
                            derived_from_version_ref_attribute='0023',
                            frame_defaults=VersionFrameDefaultsStructure(
                                default_responsibility_set_ref=ResponsibilitySetRefStructure(
                                    value='EXTERNAL',
                                    ref='mybus:RS_10'
                                )
                            ),
                            stop_places=StopPlacesInFrameRelStructure(
                                stop_place=[
                                    StopPlace(
                                        id='mybus:SP001A',
                                        version='any',
                                        name=MultilingualString(
                                            value='Alpha   Castle'
                                        ),
                                        short_name=MultilingualString(
                                            value='Alpha Place A '
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        524811.0,
                                                        170666.0,
                                                    ],
                                                    srs_name='UKOS'
                                                )
                                            )
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
                                        stop_place_type=StopTypeEnumeration.ONSTREET_TRAM,
                                        quays=QuaysRelStructure(
                                            taxi_stand_ref_or_quay_ref_or_quay=[
                                                Quay(
                                                    id='mybus:Q_SP001A_1',
                                                    created=XmlDateTime(2010, 4, 17, 9, 30, 47, 0, 0),
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='PlaceA'
                                                    ),
                                                    description=[
                                                        MultilingualString(
                                                            value='Stop A is termiuis serves both directions'
                                                        ),
                                                    ],
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            longitude=Decimal('-0.2071397147'),
                                                            latitude=Decimal('51.4217482061')
                                                        )
                                                    ),
                                                    covered=CoveredEnumeration.INDOORS,
                                                    label=MultilingualString(
                                                        value='Stop A'
                                                    ),
                                                    public_code='1-3454 ',
                                                    compass_octant=CompassBearing8Enumeration.S,
                                                    quay_type=QuayTypeEnumeration.TRAM_STOP
                                                ),
                                            ]
                                        )
                                    ),
                                    StopPlace(
                                        id='mybus:SP002B',
                                        version='any',
                                        name=MultilingualString(
                                            value='Bravo Road (SW19)'
                                        ),
                                        short_name=MultilingualString(
                                            value='Bravo'
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        524811.0,
                                                        170666.0,
                                                    ],
                                                    srs_name='UKOS'
                                                )
                                            )
                                        ),
                                        road_address=RoadAddress(
                                            id='mybus:RAd_SP002B_01',
                                            version='any',
                                            road_name=MultilingualString(
                                                value='Bravo Road'
                                            )
                                        ),
                                        stop_place_type=StopTypeEnumeration.TRAM_STATION,
                                        quays=QuaysRelStructure(
                                            taxi_stand_ref_or_quay_ref_or_quay=[
                                                Quay(
                                                    id='mybus:Q_SP002B_1',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Bravo, Northbound'
                                                    ),
                                                    description=[
                                                        MultilingualString(
                                                            value='Stop Ba  is paired with Stop Bb  '
                                                        ),
                                                    ],
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            longitude=Decimal('-0.2071397147'),
                                                            latitude=Decimal('51.4217482061')
                                                        )
                                                    ),
                                                    covered=CoveredEnumeration.OUTDOORS,
                                                    label=MultilingualString(
                                                        value='Stop B1'
                                                    ),
                                                    compass_octant=CompassBearing8Enumeration.S,
                                                    quay_type=QuayTypeEnumeration.TRAM_PLATFORM
                                                ),
                                                Quay(
                                                    id='mybus:Q_SP002B_2',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Bravo SOuthbound'
                                                    ),
                                                    description=[
                                                        MultilingualString(
                                                            value='Stop Ba  is paired with Stop Bb  '
                                                        ),
                                                    ],
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            longitude=Decimal('-0.2071397147'),
                                                            latitude=Decimal('51.4217482061')
                                                        )
                                                    ),
                                                    covered=CoveredEnumeration.OUTDOORS,
                                                    label=MultilingualString(
                                                        value='Stop B2'
                                                    ),
                                                    public_code='1-3457 ',
                                                    compass_octant=CompassBearing8Enumeration.N,
                                                    quay_type=QuayTypeEnumeration.TRAM_PLATFORM
                                                ),
                                                Quay(
                                                    id='mybus:Q_SP002B_3',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Bravo Rail Platform 1'
                                                    ),
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            longitude=Decimal('-0.2071397147'),
                                                            latitude=Decimal('51.4217482061')
                                                        )
                                                    ),
                                                    covered=CoveredEnumeration.INDOORS,
                                                    label=MultilingualString(
                                                        value='Platform 1'
                                                    ),
                                                    compass_octant=CompassBearing8Enumeration.N,
                                                    quay_type=QuayTypeEnumeration.RAIL_PLATFORM
                                                ),
                                            ]
                                        ),
                                        access_spaces=AccessSpacesRelStructure(
                                            access_space_ref_or_access_space=[
                                                AccessSpace(
                                                    id='mybus:as_SP002B_01',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Bravo Ticket Hall '
                                                    ),
                                                    description=[
                                                        MultilingualString(
                                                            value='Ticket Hall at Bravo'
                                                        ),
                                                    ],
                                                    covered=CoveredEnumeration.INDOORS,
                                                    access_space_type=AccessSpaceTypeEnumeration.BOOKING_HALL
                                                ),
                                            ]
                                        )
                                    ),
                                    StopPlace(
                                        id='mybus:SP003C',
                                        version='any',
                                        name=MultilingualString(
                                            value='Stop Place C'
                                        ),
                                        short_name=MultilingualString(
                                            value='Place C'
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        524811.0,
                                                        170666.0,
                                                    ],
                                                    srs_name='UKOS'
                                                )
                                            )
                                        ),
                                        road_address=RoadAddress(
                                            id='mybus:RAd_SP003C_01',
                                            version='any',
                                            road_name=MultilingualString(
                                                value='Foo Road'
                                            )
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
                                        stop_place_type=StopTypeEnumeration.ONSTREET_TRAM,
                                        quays=QuaysRelStructure(
                                            taxi_stand_ref_or_quay_ref_or_quay=[
                                                Quay(
                                                    id='mybus:Q_SP003C_1',
                                                    created=XmlDateTime(2010, 4, 17, 9, 30, 47, 0, 0),
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Place C'
                                                    ),
                                                    description=[
                                                        MultilingualString(
                                                            value='StopCa  is paired with Stop Cb  '
                                                        ),
                                                    ],
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            longitude=Decimal('-0.2071397147'),
                                                            latitude=Decimal('51.4217482061')
                                                        )
                                                    ),
                                                    covered=CoveredEnumeration.OUTDOORS,
                                                    label=MultilingualString(
                                                        value='Stop Ca'
                                                    ),
                                                    public_code='1-3454 ',
                                                    compass_octant=CompassBearing8Enumeration.NE,
                                                    quay_type=QuayTypeEnumeration.TRAM_STOP
                                                ),
                                                Quay(
                                                    id='mybus:Q_SP003C_2',
                                                    created=XmlDateTime(2010, 4, 17, 9, 30, 47, 0, 0),
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Place C'
                                                    ),
                                                    description=[
                                                        MultilingualString(
                                                            value='Stop Cb  is paired with Stop Ca '
                                                        ),
                                                    ],
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            longitude=Decimal('-0.2071397147'),
                                                            latitude=Decimal('51.4217482061')
                                                        )
                                                    ),
                                                    covered=CoveredEnumeration.OUTDOORS,
                                                    label=MultilingualString(
                                                        value='Stop Cb'
                                                    ),
                                                    public_code='1-3455 ',
                                                    compass_octant=CompassBearing8Enumeration.SE,
                                                    quay_type=QuayTypeEnumeration.TRAM_STOP
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        ResourceFrame(
                            id='tbd:SVC01',
                            version='any',
                            types_of_value=TypesOfValueInFrameRelStructure(
                                choice=[
                                    ValueSet(
                                        id='napt:PassengerInformationEquipmentTypes',
                                        version='any',
                                        name=MultilingualString(
                                            value='PASSENGER INFORMATION EQUIPMENT  Types'
                                        ),
                                        values=TypesOfValueStructure(
                                            type_of_value_or_type_of_entity=[
                                                TypeOfPassengerInformationEquipment(
                                                    id='mybus:PlatDisp',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='ON Platforom Small display '
                                                    )
                                                ),
                                                TypeOfPassengerInformationEquipment(
                                                    id='mybus:LargeBoard',
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Large Display '
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                    ]
                )
            ),
        ]
    )
)
