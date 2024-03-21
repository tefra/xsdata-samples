from decimal import Decimal
from netex.models.access_feature_enumeration import AccessFeatureEnumeration
from netex.models.access_mode_enumeration import AccessModeEnumeration
from netex.models.access_space import AccessSpace
from netex.models.access_space_ref_structure import AccessSpaceRefStructure
from netex.models.access_space_type_enumeration import AccessSpaceTypeEnumeration
from netex.models.access_spaces_rel_structure import AccessSpacesRelStructure
from netex.models.access_summaries_rel_structure import AccessSummariesRelStructure
from netex.models.access_summary import AccessSummary
from netex.models.accessibility_assessment import AccessibilityAssessment
from netex.models.accessibility_limitation import AccessibilityLimitation
from netex.models.accessibility_limitations_rel_structure import AccessibilityLimitationsRelStructure
from netex.models.all_modes_enumeration import AllModesEnumeration
from netex.models.all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from netex.models.alternative_name import AlternativeName
from netex.models.alternative_names_rel_structure import AlternativeNamesRelStructure
from netex.models.audible_signals_available import AudibleSignalsAvailable
from netex.models.availability_condition_ref import AvailabilityConditionRef
from netex.models.check_constraint import CheckConstraint
from netex.models.check_constraint_delay import CheckConstraintDelay
from netex.models.check_constraint_delays_rel_structure import CheckConstraintDelaysRelStructure
from netex.models.check_constraints_rel_structure import CheckConstraintsRelStructure
from netex.models.check_process_type_enumeration import CheckProcessTypeEnumeration
from netex.models.codespace import Codespace
from netex.models.codespace_ref_structure import CodespaceRefStructure
from netex.models.codespaces_rel_structure import CodespacesRelStructure
from netex.models.compass_bearing16_enumeration import CompassBearing16Enumeration
from netex.models.compass_bearing8_enumeration import CompassBearing8Enumeration
from netex.models.congestion_enumeration import CongestionEnumeration
from netex.models.connection import Connection
from netex.models.connection_end_structure import ConnectionEndStructure
from netex.models.country_ref import CountryRef
from netex.models.covered_enumeration import CoveredEnumeration
from netex.models.crossing_equipment import CrossingEquipment
from netex.models.crossing_type_enumeration import CrossingTypeEnumeration
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.data_role_type_enumeration import DataRoleTypeEnumeration
from netex.models.day_of_week_enumeration import DayOfWeekEnumeration
from netex.models.day_type_ref import DayTypeRef
from netex.models.day_types_in_frame_rel_structure import DayTypesInFrameRelStructure
from netex.models.destination_display_view import DestinationDisplayView
from netex.models.destination_display_views_rel_structure import DestinationDisplayViewsRelStructure
from netex.models.direction_of_use_enumeration import DirectionOfUseEnumeration
from netex.models.entity_in_version_structure import AvailabilityCondition
from netex.models.entity_in_version_structure import DayType
from netex.models.entity_in_version_structure import DayTypesRelStructure
from netex.models.entity_in_version_structure import TimebandVersionedChildStructure
from netex.models.entity_in_version_structure import TimebandsRelStructure
from netex.models.entity_in_version_structure import ValidityConditionsRelStructure
from netex.models.entrance_enumeration import EntranceEnumeration
from netex.models.entrance_equipment import EntranceEquipment
from netex.models.entrance_ref import EntranceRef
from netex.models.entrance_ref_structure import EntranceRefStructure
from netex.models.equipment_place import EquipmentPlace
from netex.models.equipment_places_rel_structure import EquipmentPlacesRelStructure
from netex.models.equipment_position import EquipmentPosition
from netex.models.equipment_positions_rel_structure import EquipmentPositionsRelStructure
from netex.models.equipment_ref import EquipmentRef
from netex.models.equipments_rel_structure import EquipmentsRelStructure
from netex.models.escalator_free_access import EscalatorFreeAccess
from netex.models.gated_enumeration import GatedEnumeration
from netex.models.general_sign import GeneralSign
from netex.models.general_version_frame_structure import CompositeFrame
from netex.models.general_version_frame_structure import FramesRelStructure
from netex.models.gradient_enumeration import GradientEnumeration
from netex.models.holiday_type_enumeration import HolidayTypeEnumeration
from netex.models.iana_country_tld_enumeration import IanaCountryTldEnumeration
from netex.models.level import Level
from netex.models.level_ref import LevelRef
from netex.models.level_ref_structure import LevelRefStructure
from netex.models.levels_rel_structure import LevelsRelStructure
from netex.models.lift_free_access import LiftFreeAccess
from netex.models.lighting_enumeration import LightingEnumeration
from netex.models.limitation_status_enumeration import LimitationStatusEnumeration
from netex.models.location_structure_2 import LocationStructure2
from netex.models.modification_enumeration import ModificationEnumeration
from netex.models.multilingual_string import MultilingualString
from netex.models.name_type_enumeration import NameTypeEnumeration
from netex.models.navigation_path import NavigationPath
from netex.models.navigation_paths_rel_structure import NavigationPathsRelStructure
from netex.models.navigation_type_enumeration import NavigationTypeEnumeration
from netex.models.network_filter_by_value_structure import NetworkFilterByValueStructure
from netex.models.network_frame_topic_structure import NetworkFrameTopicStructure
from netex.models.operator import Operator
from netex.models.operator_ref_structure import OperatorRefStructure
from netex.models.organisation_type_enumeration import OrganisationTypeEnumeration
from netex.models.organisations_in_frame_rel_structure import OrganisationsInFrameRelStructure
from netex.models.participant_ref import ParticipantRef
from netex.models.passenger_stop_assignment import PassengerStopAssignment
from netex.models.path_direction_enumeration import PathDirectionEnumeration
from netex.models.path_heading_enumeration import PathHeadingEnumeration
from netex.models.path_link_end_structure import PathLinkEndStructure
from netex.models.path_link_in_sequence import PathLinkInSequence
from netex.models.path_link_ref import PathLinkRef
from netex.models.path_links_in_sequence_rel_structure import PathLinksInSequenceRelStructure
from netex.models.payment_method_enumeration import PaymentMethodEnumeration
from netex.models.place_equipments_rel_structure import PlaceEquipmentsRelStructure
from netex.models.place_sign import PlaceSign
from netex.models.point_ref_structure import PointRefStructure
from netex.models.pos import Pos
from netex.models.private_code_structure import PrivateCodeStructure
from netex.models.properties_of_day_rel_structure import PropertiesOfDayRelStructure
from netex.models.property_of_day import PropertyOfDay
from netex.models.publication_delivery import PublicationDelivery
from netex.models.publication_request_structure import PublicationRequestStructure
from netex.models.quay import Quay
from netex.models.quay_ref import QuayRef
from netex.models.quay_ref_structure import QuayRefStructure
from netex.models.quay_type_enumeration import QuayTypeEnumeration
from netex.models.quays_rel_structure import QuaysRelStructure
from netex.models.ramp_equipment import RampEquipment
from netex.models.resource_frame import ResourceFrame
from netex.models.responsibility_role_assignment import ResponsibilityRoleAssignment
from netex.models.responsibility_role_assignments_rel_structure import ResponsibilityRoleAssignmentsRelStructure
from netex.models.responsibility_set import ResponsibilitySet
from netex.models.responsibility_set_ref_structure import ResponsibilitySetRefStructure
from netex.models.responsibility_sets_in_frame_rel_structure import ResponsibilitySetsInFrameRelStructure
from netex.models.road_address import RoadAddress
from netex.models.scheduled_stop_point import ScheduledStopPoint
from netex.models.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.models.scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from netex.models.scheduled_stop_points_in_frame_rel_structure import ScheduledStopPointsInFrameRelStructure
from netex.models.service_calendar import ServiceCalendar
from netex.models.service_calendar_frame import ServiceCalendarFrame
from netex.models.service_frame import ServiceFrame
from netex.models.simple_point_version_structure import SimplePointVersionStructure
from netex.models.site_entrances_rel_structure import SiteEntrancesRelStructure
from netex.models.site_frame import SiteFrame
from netex.models.site_path_link import SitePathLink
from netex.models.site_path_links_rel_structure import SitePathLinksRelStructure
from netex.models.step_free_access import StepFreeAccess
from netex.models.stop_assignments_in_frame_rel_structure import StopAssignmentsInFrameRelStructure
from netex.models.stop_place import StopPlace
from netex.models.stop_place_entrance import StopPlaceEntrance
from netex.models.stop_place_entrance_ref_structure import StopPlaceEntranceRefStructure
from netex.models.stop_place_ref import StopPlaceRef
from netex.models.stop_places_in_frame_rel_structure import StopPlacesInFrameRelStructure
from netex.models.stop_type_enumeration import StopTypeEnumeration
from netex.models.ticketing_equipment import TicketingEquipment
from netex.models.ticketing_service_facility_enumeration import TicketingServiceFacilityEnumeration
from netex.models.ticketing_service_facility_list import TicketingServiceFacilityList
from netex.models.topographic_place import TopographicPlace
from netex.models.topographic_place_descriptor_versioned_child_structure import TopographicPlaceDescriptorVersionedChildStructure
from netex.models.topographic_place_ref import TopographicPlaceRef
from netex.models.topographic_place_ref_structure import TopographicPlaceRefStructure
from netex.models.topographic_place_refs_rel_structure import TopographicPlaceRefsRelStructure
from netex.models.topographic_place_type_enumeration import TopographicPlaceTypeEnumeration
from netex.models.topographic_place_view import TopographicPlaceView
from netex.models.topographic_places_in_frame_rel_structure import TopographicPlacesInFrameRelStructure
from netex.models.transfer_duration_structure import TransferDurationStructure
from netex.models.transfers_in_frame_rel_structure import TransfersInFrameRelStructure
from netex.models.transition_enumeration import TransitionEnumeration
from netex.models.vehicle_mode_enumeration import VehicleModeEnumeration
from netex.models.version_frame_defaults_structure import VersionFrameDefaultsStructure
from netex.models.visual_signs_available import VisualSignsAvailable
from netex.models.wheelchair_access import WheelchairAccess
from netex.models.zone_ref_structure import ZoneRefStructure
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration
from xsdata.models.datatype import XmlTime


obj = PublicationDelivery(
    publication_timestamp=XmlDateTime(2001, 12, 17, 9, 30, 47, 0, 0),
    participant_ref=ParticipantRef(
        value='SYS001'
    ),
    publication_request=PublicationRequestStructure(
        request_timestamp=XmlDateTime(2001, 12, 17, 9, 30, 47, 0, 0),
        participant_ref=ParticipantRef(
            value='SYS002'
        ),
        topics=PublicationRequestStructure.Topics(
            network_frame_topic=[
                NetworkFrameTopicStructure(
                    choice='',
                    choice_1=[
                        NetworkFilterByValueStructure(
                            places=NetworkFilterByValueStructure.Places(
                                choice=[
                                    TopographicPlaceRef(
                                        value='REQUEST',
                                        ref='topat:E0034695'
                                    ),
                                ]
                            )
                        ),
                    ]
                ),
            ]
        )
    ),
    publication_refresh_interval=XmlDuration("P3M"),
    description=MultilingualString(
        value='Simple Stop pair On street example'
    ),
    data_objects=DataObjectsRelStructure(
        choice=[
            CompositeFrame(
                id='zbt:CF001',
                validity_conditions_or_valid_between=[
                    ValidityConditionsRelStructure(
                        choice=[
                            AvailabilityCondition(
                                id='zbt:CF0021',
                                version='any',
                                from_date=XmlDateTime(2010, 12, 17, 9, 30, 47, 0, 0),
                                to_date=XmlDateTime(2011, 12, 17, 9, 30, 47, 0, 0)
                            ),
                        ]
                    ),
                ],
                version='1',
                codespaces=CodespacesRelStructure(
                    codespace_ref_or_codespace=[
                        Codespace(
                            id='zbt',
                            xmlns='zbt',
                            xmlns_url='http://www.zillerthalerbahn.at/',
                            description='ZillerthalerBahn namesapce'
                        ),
                        Codespace(
                            id='topat',
                            xmlns='topat',
                            xmlns_url='http://www.osos.at',
                            description='Austrian locality data'
                        ),
                    ]
                ),
                frame_defaults=VersionFrameDefaultsStructure(
                    default_codespace_ref=CodespaceRefStructure(
                        ref='zbt'
                    )
                ),
                frames=FramesRelStructure(
                    common_frame=[
                        ServiceCalendarFrame(
                            id='zbt:SFC0021',
                            version='any',
                            frame_defaults=VersionFrameDefaultsStructure(
                                default_responsibility_set_ref=ResponsibilitySetRefStructure(
                                    version='01',
                                    ref='zbt:Resp01'
                                )
                            ),
                            service_calendar=ServiceCalendar(
                                id='zbt:SFC0021',
                                version='any',
                                from_date=XmlDate(2010, 12, 17),
                                to_date=XmlDate(2011, 12, 17)
                            ),
                            day_types=DayTypesInFrameRelStructure(
                                day_type=[
                                    DayType(
                                        id='zbt:DT001Open_MF',
                                        version='any',
                                        properties=PropertiesOfDayRelStructure(
                                            property_of_day=[
                                                PropertyOfDay(
                                                    days_of_week=[
                                                        DayOfWeekEnumeration.MONDAY,
                                                        DayOfWeekEnumeration.TUESDAY,
                                                        DayOfWeekEnumeration.WEDNESDAY,
                                                        DayOfWeekEnumeration.THURSDAY,
                                                        DayOfWeekEnumeration.FRIDAY,
                                                    ],
                                                    holiday_types=[
                                                        HolidayTypeEnumeration.WORKING_DAY,
                                                    ]
                                                ),
                                            ]
                                        ),
                                        timebands=TimebandsRelStructure(
                                            timeband_ref_or_timeband=[
                                                TimebandVersionedChildStructure(
                                                    id='zbt:DT001Open_MF@TMB01',
                                                    version='any',
                                                    start_time_or_start_event=XmlTime(5, 0, 0, 0),
                                                    choice=[
                                                        XmlDuration("PT19H30M"),
                                                    ]
                                                ),
                                            ]
                                        )
                                    ),
                                    DayType(
                                        id='zbt:DT002Open_Sat',
                                        version='any',
                                        properties=PropertiesOfDayRelStructure(
                                            property_of_day=[
                                                PropertyOfDay(
                                                    days_of_week=[
                                                        DayOfWeekEnumeration.SATURDAY,
                                                    ],
                                                    holiday_types=[
                                                        HolidayTypeEnumeration.WORKING_DAY,
                                                    ]
                                                ),
                                            ]
                                        ),
                                        timebands=TimebandsRelStructure(
                                            timeband_ref_or_timeband=[
                                                TimebandVersionedChildStructure(
                                                    id='zbt:DT002Open_Sat@TMB01',
                                                    version='any',
                                                    start_time_or_start_event=XmlTime(6, 0, 0, 0),
                                                    choice=[
                                                        XmlDuration("PT18H30M"),
                                                    ]
                                                ),
                                            ]
                                        )
                                    ),
                                    DayType(
                                        id='zbt:DT003Open_Sun',
                                        version='any',
                                        properties=PropertiesOfDayRelStructure(
                                            property_of_day=[
                                                PropertyOfDay(
                                                    days_of_week=[
                                                        DayOfWeekEnumeration.SUNDAY,
                                                    ]
                                                ),
                                            ]
                                        ),
                                        timebands=TimebandsRelStructure(
                                            timeband_ref_or_timeband=[
                                                TimebandVersionedChildStructure(
                                                    id='zbt:DT003Open_Sun@TMB01',
                                                    version='any',
                                                    start_time_or_start_event=XmlTime(8, 0, 0, 0),
                                                    choice=[
                                                        XmlDuration("PT17H30M"),
                                                    ]
                                                ),
                                            ]
                                        )
                                    ),
                                    DayType(
                                        id='zbt:DT004Open_MFS',
                                        version='any',
                                        properties=PropertiesOfDayRelStructure(
                                            property_of_day=[
                                                PropertyOfDay(
                                                    days_of_week=[
                                                        DayOfWeekEnumeration.MONDAY,
                                                        DayOfWeekEnumeration.TUESDAY,
                                                        DayOfWeekEnumeration.WEDNESDAY,
                                                        DayOfWeekEnumeration.THURSDAY,
                                                        DayOfWeekEnumeration.FRIDAY,
                                                        DayOfWeekEnumeration.SATURDAY,
                                                    ],
                                                    holiday_types=[
                                                        HolidayTypeEnumeration.WORKING_DAY,
                                                    ]
                                                ),
                                            ]
                                        ),
                                        timebands=TimebandsRelStructure(
                                            timeband_ref_or_timeband=[
                                                TimebandVersionedChildStructure(
                                                    id='zbt:DT004Open_MFS',
                                                    version='any',
                                                    start_time_or_start_event=XmlTime(8, 30, 0, 0),
                                                    choice=[
                                                        XmlTime(20, 0, 0, 0),
                                                    ]
                                                ),
                                            ]
                                        )
                                    ),
                                    DayType(
                                        id='zbt:DT005Open_Sun',
                                        version='any',
                                        properties=PropertiesOfDayRelStructure(
                                            property_of_day=[
                                                PropertyOfDay(
                                                    days_of_week=[
                                                        DayOfWeekEnumeration.SUNDAY,
                                                    ]
                                                ),
                                            ]
                                        ),
                                        timebands=TimebandsRelStructure(
                                            timeband_ref_or_timeband=[
                                                TimebandVersionedChildStructure(
                                                    id='zbt:DT005Open_Sun',
                                                    version='any',
                                                    start_time_or_start_event=XmlTime(10, 30, 0, 0),
                                                    choice=[
                                                        XmlTime(18, 0, 0, 0),
                                                    ]
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        SiteFrame(
                            id='zbt:SF0023',
                            version='any',
                            frame_defaults=VersionFrameDefaultsStructure(
                                default_responsibility_set_ref=ResponsibilitySetRefStructure(
                                    version='01',
                                    ref='zbt:Resp02'
                                )
                            ),
                            content_validity_conditions=ValidityConditionsRelStructure(
                                choice=[
                                    AvailabilityCondition(
                                        id='zbt:AC_02_CC_Opening',
                                        version='01',
                                        day_types=DayTypesRelStructure(
                                            day_type_ref_or_day_type=[
                                                DayTypeRef(
                                                    version='any',
                                                    ref='zbt:DT004Open_MFS'
                                                ),
                                                DayTypeRef(
                                                    version='any',
                                                    ref='zbt:DT005Open_Sun'
                                                ),
                                            ]
                                        )
                                    ),
                                    AvailabilityCondition(
                                        id='zbt:AC_01_Main_Opening',
                                        version='01',
                                        day_types=DayTypesRelStructure(
                                            day_type_ref_or_day_type=[
                                                DayTypeRef(
                                                    version='any',
                                                    ref='zbt:DT001Open_MF'
                                                ),
                                                DayTypeRef(
                                                    version='any',
                                                    ref='zbt:DT002Open_Sat'
                                                ),
                                                DayTypeRef(
                                                    version='any',
                                                    ref='zbt:DT003Open_Sun'
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            topographic_places=TopographicPlacesInFrameRelStructure(
                                topographic_place=[
                                    TopographicPlace(
                                        id='topat:E0034695',
                                        version='01',
                                        name=MultilingualString(
                                            value='Reid Im Zillerthal'
                                        ),
                                        description=[
                                            MultilingualString(
                                                value='Reid'
                                            ),
                                        ],
                                        descriptor=TopographicPlaceDescriptorVersionedChildStructure(
                                            id='topat:E0034695',
                                            version='01',
                                            name=MultilingualString(
                                                value='Reid im Zillerthal',
                                                lang='de'
                                            ),
                                            short_name=MultilingualString(
                                                value='Reid',
                                                lang='de'
                                            ),
                                            qualify=TopographicPlaceDescriptorVersionedChildStructure.Qualify(
                                                qualifier_name=MultilingualString(
                                                    value='Tyrol'
                                                ),
                                                topographic_place_ref=TopographicPlaceRef(
                                                    version='01',
                                                    ref='topat:E0034'
                                                )
                                            )
                                        ),
                                        topographic_place_type=TopographicPlaceTypeEnumeration.VILLAGE,
                                        place_centre=False,
                                        country_ref=CountryRef(
                                            ref=IanaCountryTldEnumeration.AT
                                        ),
                                        parent_topographic_place_ref=TopographicPlaceRefStructure(
                                            version='01',
                                            ref='topat:E0034'
                                        )
                                    ),
                                    TopographicPlace(
                                        id='topat:E0034',
                                        version='01',
                                        name=MultilingualString(
                                            value='Tyrol'
                                        ),
                                        descriptor=TopographicPlaceDescriptorVersionedChildStructure(
                                            id='topat:E0034',
                                            version='01',
                                            name=MultilingualString(
                                                value='Tyrol',
                                                lang='de'
                                            )
                                        ),
                                        topographic_place_type=TopographicPlaceTypeEnumeration.PROVINCE,
                                        place_centre=False,
                                        country_ref=CountryRef(
                                            ref=IanaCountryTldEnumeration.AT
                                        )
                                    ),
                                ]
                            ),
                            stop_places=StopPlacesInFrameRelStructure(
                                stop_place=[
                                    StopPlace(
                                        id='ztb:bh0023',
                                        created=XmlDateTime(2006, 9, 11, 15, 42, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='01',
                                        name=MultilingualString(
                                            value='Bahnhof Ried'
                                        ),
                                        short_name=MultilingualString(
                                            value='Ried'
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        524811.0,
                                                        170666.0,
                                                    ],
                                                    srs_name='ATGRID'
                                                )
                                            )
                                        ),
                                        road_address=RoadAddress(
                                            id='ztb:bh0023@RdAddr_01',
                                            created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                            version='01',
                                            road_name=MultilingualString(
                                                value='Kleiried'
                                            )
                                        ),
                                        accessibility_assessment=AccessibilityAssessment(
                                            id='ztb:bh0023',
                                            version='any',
                                            mobility_impaired_access=LimitationStatusEnumeration.TRUE,
                                            limitations=AccessibilityLimitationsRelStructure(
                                                accessibility_limitation=AccessibilityLimitation(
                                                    wheelchair_access=WheelchairAccess(
                                                        value=LimitationStatusEnumeration.TRUE
                                                    ),
                                                    step_free_access=StepFreeAccess(
                                                        value=LimitationStatusEnumeration.TRUE
                                                    ),
                                                    escalator_free_access=EscalatorFreeAccess(
                                                        value=LimitationStatusEnumeration.TRUE
                                                    ),
                                                    lift_free_access=LiftFreeAccess(
                                                        value=LimitationStatusEnumeration.TRUE
                                                    ),
                                                    audible_signals_available=AudibleSignalsAvailable(

                                                    ),
                                                    visual_signs_available=VisualSignsAvailable(
                                                        value=LimitationStatusEnumeration.TRUE
                                                    )
                                                )
                                            )
                                        ),
                                        access_modes=[
                                            AccessModeEnumeration.FOOT,
                                        ],
                                        alternative_names=AlternativeNamesRelStructure(
                                            alternative_name=[
                                                AlternativeName(
                                                    id='ztb:bh0023@n01',
                                                    created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                    version='01',
                                                    type_of_name='label',
                                                    name=MultilingualString(
                                                        value='Ried im Zillertal'
                                                    ),
                                                    short_name=MultilingualString(
                                                        value='Ried',
                                                        lang='de'
                                                    ),
                                                    qualifier_name=MultilingualString(
                                                        value='Tyrol',
                                                        lang='de'
                                                    )
                                                ),
                                                AlternativeName(
                                                    id='ztb:bh0023@n02',
                                                    created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                    version='01',
                                                    lang='en',
                                                    name_type=NameTypeEnumeration.TRANSLATION,
                                                    type_of_name='label',
                                                    name=MultilingualString(
                                                        value='Rail Station Ried im Zillertal',
                                                        lang='en'
                                                    ),
                                                    qualifier_name=MultilingualString(
                                                        value='Tyrol',
                                                        lang='en'
                                                    )
                                                ),
                                            ]
                                        ),
                                        covered=CoveredEnumeration.MIXED,
                                        topographic_place_ref_or_topographic_place_view=TopographicPlaceView(
                                            topographic_place_ref=TopographicPlaceRef(
                                                version='01',
                                                ref='topat:E0034695'
                                            )
                                        ),
                                        contained_in_place_ref=TopographicPlaceRefStructure(
                                            version='01',
                                            ref='topat:E0034695'
                                        ),
                                        levels=LevelsRelStructure(
                                            level_ref_or_level=[
                                                Level(
                                                    id='ztb:bh0023@Lvl_0',
                                                    created=XmlDateTime(2010, 4, 17, 9, 30, 47, 0, 0),
                                                    version='01',
                                                    name=MultilingualString(
                                                        value='Erde '
                                                    ),
                                                    public_code='E'
                                                ),
                                            ]
                                        ),
                                        entrances=SiteEntrancesRelStructure(
                                            entrance_ref_or_parking_entrance_ref_or_entrance=[
                                                StopPlaceEntrance(
                                                    id='ztb:bh0023@A1-E1',
                                                    validity_conditions_or_valid_between=[
                                                        ValidityConditionsRelStructure(
                                                            choice=[
                                                                AvailabilityConditionRef(
                                                                    version='01',
                                                                    ref='zbt:AC_01_Main_Opening'
                                                                ),
                                                            ]
                                                        ),
                                                    ],
                                                    created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                    version='01',
                                                    name=MultilingualString(
                                                        value='Main Entrance from street'
                                                    ),
                                                    description=[
                                                        MultilingualString(
                                                            value='External Entrance to  Ticket Hall from forecourt',
                                                            lang='en'
                                                        ),
                                                    ],
                                                    parent_zone_ref=ZoneRefStructure(
                                                        version='01',
                                                        ref='ztb:bh0023@A1'
                                                    ),
                                                    level_ref=LevelRef(
                                                        version='01',
                                                        ref='ztb:bh0023@Lvl_0'
                                                    ),
                                                    place_equipments=PlaceEquipmentsRelStructure(
                                                        choice=[
                                                            RampEquipment(
                                                                id='ztb:bh0023@A1-E1@ramp',
                                                                version='any',
                                                                direction_of_use=DirectionOfUseEnumeration.BOTH,
                                                                gradient=22,
                                                                gradient_type=GradientEnumeration.STEEP,
                                                                visual_guidance_bands=True
                                                            ),
                                                            EntranceEquipment(
                                                                id='ztb:bh0023@A1-E1@entrance',
                                                                version='any',
                                                                door=True,
                                                                kept_open=True,
                                                                wheelchair_passable=True
                                                            ),
                                                        ]
                                                    ),
                                                    label=MultilingualString(
                                                        value='Eingang',
                                                        lang='de'
                                                    ),
                                                    entrance_type=EntranceEnumeration.OPEN_DOOR,
                                                    is_external=True,
                                                    is_entry=True,
                                                    is_exit=True,
                                                    width=Decimal('1.0'),
                                                    height=Decimal('2.0')
                                                ),
                                                StopPlaceEntrance(
                                                    id='ztb:bh0023@A1-E2',
                                                    validity_conditions_or_valid_between=[
                                                        ValidityConditionsRelStructure(
                                                            choice=[
                                                                AvailabilityConditionRef(
                                                                    version='01',
                                                                    ref='zbt:AC_02_CC_Opening'
                                                                ),
                                                            ]
                                                        ),
                                                    ],
                                                    created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                    version='01',
                                                    name=MultilingualString(
                                                        value='Entrance to platform 1 from Ticket hall '
                                                    ),
                                                    description=[
                                                        MultilingualString(
                                                            value=' Entrance to  Ticket Hall from platform 1',
                                                            lang='en'
                                                        ),
                                                    ],
                                                    parent_zone_ref=ZoneRefStructure(
                                                        version='01',
                                                        ref='ztb:bh0023@A1'
                                                    ),
                                                    level_ref=LevelRef(
                                                        version='01',
                                                        ref='ztb:bh0023@Lvl_0'
                                                    ),
                                                    place_equipments=PlaceEquipmentsRelStructure(
                                                        choice=[
                                                            EntranceEquipment(
                                                                id='ztb:bh0023@A1-E2',
                                                                version='any',
                                                                door=True,
                                                                kept_open=True,
                                                                wheelchair_passable=True
                                                            ),
                                                        ]
                                                    ),
                                                    label=MultilingualString(
                                                        value='Ausgang',
                                                        lang='de'
                                                    ),
                                                    entrance_type=EntranceEnumeration.OPEN_DOOR,
                                                    is_external=True,
                                                    is_entry=True,
                                                    is_exit=True,
                                                    width=Decimal('1.0'),
                                                    height=Decimal('2.0')
                                                ),
                                                StopPlaceEntrance(
                                                    id='ztb:bh0023@Rail@Q1-E1tr',
                                                    created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                    version='01',
                                                    name=MultilingualString(
                                                        value='Entrance to track  crossing from platorm  l '
                                                    ),
                                                    description=[
                                                        MultilingualString(
                                                            value='platform 1 Entrance to crossing over tracks to platform 2',
                                                            lang='en'
                                                        ),
                                                    ],
                                                    parent_zone_ref=ZoneRefStructure(
                                                        version='01',
                                                        ref='ztb:bh0023@Rail@Q1'
                                                    ),
                                                    level_ref=LevelRef(
                                                        version='01',
                                                        ref='ztb:bh0023@Lvl_0'
                                                    ),
                                                    place_equipments=PlaceEquipmentsRelStructure(
                                                        choice=[
                                                            RampEquipment(
                                                                id='ztb:bh0023@Rail@Q1-E1tr@ramp',
                                                                version='any',
                                                                direction_of_use=DirectionOfUseEnumeration.BOTH,
                                                                gradient=22,
                                                                visual_guidance_bands=True
                                                            ),
                                                            EntranceEquipment(
                                                                id='ztb:bh0023@Rail@Q1-E1tr@entrance',
                                                                version='any',
                                                                door=False,
                                                                kept_open=True,
                                                                wheelchair_passable=True
                                                            ),
                                                        ]
                                                    ),
                                                    entrance_type=EntranceEnumeration.OPENING,
                                                    is_external=True,
                                                    is_entry=True,
                                                    is_exit=True,
                                                    width=Decimal('2.0')
                                                ),
                                                StopPlaceEntrance(
                                                    id='ztb:bh0023@Rail@Q2-E1tr',
                                                    created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                    version='01',
                                                    name=MultilingualString(
                                                        value='platform 2 Entrance to track  crossing from platorm  l '
                                                    ),
                                                    description=[
                                                        MultilingualString(
                                                            value=' Entrance to crossing over tracks from platform2',
                                                            lang='en'
                                                        ),
                                                    ],
                                                    parent_zone_ref=ZoneRefStructure(
                                                        version='01',
                                                        ref='ztb:bh0023@Rail@Q2'
                                                    ),
                                                    level_ref=LevelRef(
                                                        version='01',
                                                        ref='ztb:bh0023@Lvl_0'
                                                    ),
                                                    place_equipments=PlaceEquipmentsRelStructure(
                                                        choice=[
                                                            RampEquipment(
                                                                id='ztb:bh0023@Rail@Q2-E1tr@ramp',
                                                                version='any',
                                                                direction_of_use=DirectionOfUseEnumeration.BOTH,
                                                                gradient=22,
                                                                visual_guidance_bands=True
                                                            ),
                                                        ]
                                                    ),
                                                    entrance_type=EntranceEnumeration.OPENING,
                                                    is_external=True,
                                                    is_entry=True,
                                                    is_exit=True,
                                                    width=Decimal('2.0')
                                                ),
                                            ]
                                        ),
                                        public_code='1564',
                                        transport_mode=AllVehicleModesOfTransportEnumeration.RAIL,
                                        stop_place_type=StopTypeEnumeration.RAIL_STATION,
                                        served_places=TopographicPlaceRefsRelStructure(
                                            topographic_place_ref=[
                                                TopographicPlaceRefStructure(
                                                    created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                    ref='topat:E0034695'
                                                ),
                                            ]
                                        ),
                                        quays=QuaysRelStructure(
                                            taxi_stand_ref_or_quay_ref_or_quay=[
                                                Quay(
                                                    id='ztb:bh0023@Rail@Q1',
                                                    created=XmlDateTime(2010, 4, 17, 9, 30, 47, 0, 0),
                                                    version='01',
                                                    name=MultilingualString(
                                                        value='Bahnsteig 1'
                                                    ),
                                                    description=[
                                                        MultilingualString(
                                                            value='Bahnsteig 1  adjacent to ticket hall'
                                                        ),
                                                    ],
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            pos=Pos(
                                                                value=[
                                                                    471800.0,
                                                                    115210.0,
                                                                ],
                                                                srs_name='ATGRID'
                                                            )
                                                        )
                                                    ),
                                                    covered=CoveredEnumeration.MIXED,
                                                    level_ref=LevelRef(
                                                        version='01',
                                                        ref='ztb:bh0023@Lvl_0'
                                                    ),
                                                    equipment_places=EquipmentPlacesRelStructure(
                                                        equipment_place_ref_or_equipment_place=[
                                                            EquipmentPlace(
                                                                id='ztb:bh0023@Rail@Q1@Sign1',
                                                                created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                                version='001',
                                                                equipment_positions=EquipmentPositionsRelStructure(
                                                                    equipment_position=[
                                                                        EquipmentPosition(
                                                                            id='ztb:bh0023@Rail@Q1@Sign1',
                                                                            version='any',
                                                                            choice=EquipmentRef(
                                                                                version='any',
                                                                                ref='ztb:bh0023@Rail@Q1@Sign_01'
                                                                            ),
                                                                            description=MultilingualString(
                                                                                value='Station name Sign on Platform 1,   10 metres from platform entrance'
                                                                            ),
                                                                            reference_point_ref=PointRefStructure(
                                                                                ref='tbd:bh0023@A1-E2@Sign_01'
                                                                            ),
                                                                            xoffset=Decimal('10'),
                                                                            yoffset=Decimal('1')
                                                                        ),
                                                                        EquipmentPosition(
                                                                            id='ztb:bh0023@Rail@Q1@Sign_02',
                                                                            version='any',
                                                                            choice=EquipmentRef(
                                                                                version='any',
                                                                                ref='ztb:bh0023@Rail@Q1@Sign_02'
                                                                            ),
                                                                            description=MultilingualString(
                                                                                value='ExitSigtn  on Platform 1,  5 metres from platform entrance'
                                                                            ),
                                                                            reference_point_ref=PointRefStructure(
                                                                                version='any',
                                                                                ref='tbd:bh0023@A1-E2@Sign_011'
                                                                            ),
                                                                            xoffset=Decimal('5'),
                                                                            yoffset=Decimal('0')
                                                                        ),
                                                                    ]
                                                                ),
                                                                place_equipments=EquipmentsRelStructure(
                                                                    choice=[
                                                                        PlaceSign(
                                                                            id='ztb:bh0023@Rail@Q1@Sign_01',
                                                                            version='any',
                                                                            height=Decimal('1'),
                                                                            width=Decimal('2'),
                                                                            height_from_floor=Decimal('1.5'),
                                                                            place_name=MultilingualString(
                                                                                value='Reid'
                                                                            )
                                                                        ),
                                                                        GeneralSign(
                                                                            id='ztb:bh0023@Rail@Q1@Sign_02',
                                                                            version='any',
                                                                            height=Decimal('1'),
                                                                            width=Decimal('2'),
                                                                            height_from_floor=Decimal('1.5'),
                                                                            content=MultilingualString(
                                                                                value='Ausgang'
                                                                            )
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    label=MultilingualString(
                                                        value='1'
                                                    ),
                                                    quay_type=QuayTypeEnumeration.RAIL_PLATFORM
                                                ),
                                                Quay(
                                                    id='ztb:bh0023@Rail@Q2',
                                                    created=XmlDateTime(2010, 4, 17, 9, 30, 47, 0, 0),
                                                    version='01',
                                                    name=MultilingualString(
                                                        value='Platform 2'
                                                    ),
                                                    description=[
                                                        MultilingualString(
                                                            value='Platform 2, reached by crossing tracks from platform 1'
                                                        ),
                                                    ],
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            pos=Pos(
                                                                value=[
                                                                    471801.0,
                                                                    115211.0,
                                                                ],
                                                                srs_name='ATGRID'
                                                            )
                                                        )
                                                    ),
                                                    covered=CoveredEnumeration.MIXED,
                                                    level_ref=LevelRef(
                                                        version='01',
                                                        ref='ztb:bh0023@Lvl_0'
                                                    ),
                                                    equipment_places=EquipmentPlacesRelStructure(
                                                        equipment_place_ref_or_equipment_place=[
                                                            EquipmentPlace(
                                                                id='ztb:bh0023@Rail@Q2@Sign1',
                                                                created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                                version='001',
                                                                equipment_positions=EquipmentPositionsRelStructure(
                                                                    equipment_position=[
                                                                        EquipmentPosition(
                                                                            id='ztb:bh0023@Rail@Q2@Sign1',
                                                                            version='any',
                                                                            choice=EquipmentRef(
                                                                                version='any',
                                                                                ref='ztb:bh0023@Rail@Q2@Sign1'
                                                                            ),
                                                                            description=MultilingualString(
                                                                                value='Station name Sign on Platform 1  "10 metres from platform entrance'
                                                                            ),
                                                                            reference_point_ref=PointRefStructure(
                                                                                version='any',
                                                                                ref='tbd:bh0023@Q2-E2'
                                                                            ),
                                                                            xoffset=Decimal('10'),
                                                                            yoffset=Decimal('1')
                                                                        ),
                                                                    ]
                                                                ),
                                                                place_equipments=EquipmentsRelStructure(
                                                                    choice=[
                                                                        PlaceSign(
                                                                            id='ztb:bh0023@Rail@Q2@Sign1',
                                                                            version='any',
                                                                            height=Decimal('1'),
                                                                            width=Decimal('2'),
                                                                            height_from_floor=Decimal('1.5'),
                                                                            place_name=MultilingualString(
                                                                                value='Reid'
                                                                            )
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    label=MultilingualString(
                                                        value='2'
                                                    ),
                                                    quay_type=QuayTypeEnumeration.RAIL_PLATFORM
                                                ),
                                            ]
                                        ),
                                        access_spaces=AccessSpacesRelStructure(
                                            access_space_ref_or_access_space=[
                                                AccessSpace(
                                                    id='ztb:bh0023@A1',
                                                    created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                    version='01',
                                                    name=MultilingualString(
                                                        value='Ticket Hall'
                                                    ),
                                                    description=[
                                                        MultilingualString(
                                                            value='Main Ticket hall with with Entrance from forecourt'
                                                        ),
                                                    ],
                                                    accessibility_assessment=AccessibilityAssessment(
                                                        id='ztb:bh0023@A1',
                                                        created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                        version='01',
                                                        mobility_impaired_access=LimitationStatusEnumeration.TRUE,
                                                        limitations=AccessibilityLimitationsRelStructure(
                                                            accessibility_limitation=AccessibilityLimitation(
                                                                created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                                version='01',
                                                                wheelchair_access=WheelchairAccess(
                                                                    value=LimitationStatusEnumeration.TRUE
                                                                ),
                                                                step_free_access=StepFreeAccess(
                                                                    value=LimitationStatusEnumeration.TRUE
                                                                ),
                                                                escalator_free_access=EscalatorFreeAccess(
                                                                    value=LimitationStatusEnumeration.TRUE
                                                                ),
                                                                lift_free_access=LiftFreeAccess(
                                                                    value=LimitationStatusEnumeration.TRUE
                                                                ),
                                                                audible_signals_available=AudibleSignalsAvailable(

                                                                ),
                                                                visual_signs_available=VisualSignsAvailable(
                                                                    value=LimitationStatusEnumeration.FALSE
                                                                )
                                                            )
                                                        )
                                                    ),
                                                    covered=CoveredEnumeration.INDOORS,
                                                    level_ref=LevelRef(
                                                        version='01',
                                                        ref='ztb:bh0023@Lvl_0'
                                                    ),
                                                    equipment_places=EquipmentPlacesRelStructure(
                                                        equipment_place_ref_or_equipment_place=[
                                                            EquipmentPlace(
                                                                id='ztb:bh0023@A1@EqP01',
                                                                version='any',
                                                                place_equipments=EquipmentsRelStructure(
                                                                    choice=[
                                                                        TicketingEquipment(
                                                                            id='ztb:bh0023@A1@EqP01_01',
                                                                            version='any',
                                                                            vehicle_modes=[
                                                                                AllModesEnumeration.RAIL,
                                                                            ],
                                                                            ticket_machines=True,
                                                                            ticketing_service_facility_list=TicketingServiceFacilityList(
                                                                                value=[
                                                                                    TicketingServiceFacilityEnumeration.CARD_TOP_UP,
                                                                                    TicketingServiceFacilityEnumeration.PURCHASE,
                                                                                ]
                                                                            ),
                                                                            payment_methods=[
                                                                                PaymentMethodEnumeration.CASH,
                                                                                PaymentMethodEnumeration.CREDIT_CARD,
                                                                                PaymentMethodEnumeration.DEBIT_CARD,
                                                                            ]
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    entrances=SiteEntrancesRelStructure(
                                                        entrance_ref_or_parking_entrance_ref_or_entrance=[
                                                            EntranceRef(
                                                                version='01',
                                                                ref='ztb:bh0023@A1-E1'
                                                            ),
                                                            EntranceRef(
                                                                version='01',
                                                                ref='ztb:bh0023@A1-E2'
                                                            ),
                                                        ]
                                                    ),
                                                    access_space_type=AccessSpaceTypeEnumeration.BOOKING_HALL
                                                ),
                                                AccessSpace(
                                                    id='ztb:bh0023@A2',
                                                    created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                    version='01',
                                                    name=MultilingualString(
                                                        value='Area in front  outside of station  '
                                                    ),
                                                    description=[
                                                        MultilingualString(
                                                            value='Areas in front of station'
                                                        ),
                                                    ],
                                                    accessibility_assessment=AccessibilityAssessment(
                                                        id='ztb:bh0023@A2',
                                                        created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                        version='01',
                                                        mobility_impaired_access=LimitationStatusEnumeration.TRUE,
                                                        limitations=AccessibilityLimitationsRelStructure(
                                                            accessibility_limitation=AccessibilityLimitation(
                                                                created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                                version='01',
                                                                wheelchair_access=WheelchairAccess(
                                                                    value=LimitationStatusEnumeration.TRUE
                                                                ),
                                                                step_free_access=StepFreeAccess(
                                                                    value=LimitationStatusEnumeration.TRUE
                                                                ),
                                                                escalator_free_access=EscalatorFreeAccess(
                                                                    value=LimitationStatusEnumeration.TRUE
                                                                ),
                                                                lift_free_access=LiftFreeAccess(
                                                                    value=LimitationStatusEnumeration.TRUE
                                                                )
                                                            )
                                                        )
                                                    ),
                                                    covered=CoveredEnumeration.OUTDOORS,
                                                    gated=GatedEnumeration.OPEN_AREA,
                                                    lighting=LightingEnumeration.WELL_LIT,
                                                    level_ref=LevelRef(
                                                        version='01',
                                                        ref='ztb:bh0023@Lvl_0'
                                                    ),
                                                    access_space_type=AccessSpaceTypeEnumeration.FORECOURT
                                                ),
                                                AccessSpace(
                                                    id='ztb:bh0023@AX3',
                                                    created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                    version='01',
                                                    name=MultilingualString(
                                                        value='Barrow Crossing   over tracks'
                                                    ),
                                                    description=[
                                                        MultilingualString(
                                                            value='Crossing over tracks'
                                                        ),
                                                    ],
                                                    accessibility_assessment=AccessibilityAssessment(
                                                        id='ztb:bh0023@AX3',
                                                        created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                        version='01',
                                                        mobility_impaired_access=LimitationStatusEnumeration.TRUE,
                                                        limitations=AccessibilityLimitationsRelStructure(
                                                            accessibility_limitation=AccessibilityLimitation(
                                                                created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                                version='01',
                                                                wheelchair_access=WheelchairAccess(
                                                                    value=LimitationStatusEnumeration.TRUE
                                                                ),
                                                                step_free_access=StepFreeAccess(
                                                                    value=LimitationStatusEnumeration.TRUE
                                                                ),
                                                                escalator_free_access=EscalatorFreeAccess(
                                                                    value=LimitationStatusEnumeration.TRUE
                                                                ),
                                                                lift_free_access=LiftFreeAccess(
                                                                    value=LimitationStatusEnumeration.TRUE
                                                                ),
                                                                audible_signals_available=AudibleSignalsAvailable(
                                                                    value=LimitationStatusEnumeration.UNKNOWN
                                                                ),
                                                                visual_signs_available=VisualSignsAvailable(
                                                                    value=LimitationStatusEnumeration.TRUE
                                                                )
                                                            )
                                                        )
                                                    ),
                                                    covered=CoveredEnumeration.OUTDOORS,
                                                    gated=GatedEnumeration.OPEN_AREA,
                                                    level_ref=LevelRef(
                                                        version='01',
                                                        ref='ztb:bh0023@Lvl_0'
                                                    ),
                                                    place_equipments=PlaceEquipmentsRelStructure(
                                                        choice=[
                                                            CrossingEquipment(
                                                                id='ztb:bh0023@AX3',
                                                                version='any',
                                                                name=MultilingualString(
                                                                    value='Barrow crossing'
                                                                ),
                                                                crossing_type=CrossingTypeEnumeration.BARROW_CROSSING
                                                            ),
                                                        ]
                                                    ),
                                                    entrances=SiteEntrancesRelStructure(
                                                        entrance_ref_or_parking_entrance_ref_or_entrance=[
                                                            EntranceRef(
                                                                version='01',
                                                                ref='ztb:bh0023@Rail@Q1-E1tr'
                                                            ),
                                                            EntranceRef(
                                                                version='01',
                                                                ref='ztb:bh0023@Rail@Q2-E1tr'
                                                            ),
                                                        ]
                                                    ),
                                                    access_space_type=AccessSpaceTypeEnumeration.PASSAGE
                                                ),
                                            ]
                                        ),
                                        path_links=SitePathLinksRelStructure(
                                            path_link_ref_or_site_path_link=[
                                                SitePathLink(
                                                    id='ztb:bh0023@lnk_A1-E1+Bus-Q1',
                                                    created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Main entrance to bus stop to'
                                                    ),
                                                    distance=Decimal('10'),
                                                    from_value=PathLinkEndStructure(
                                                        place_ref=AccessSpaceRefStructure(
                                                            version='01',
                                                            ref='ztb:bh0023@A1'
                                                        ),
                                                        level_ref=LevelRefStructure(
                                                            version='01',
                                                            ref='ztb:bh0023@Lvl_0'
                                                        ),
                                                        entrance_ref=EntranceRefStructure(
                                                            version='01',
                                                            ref='ztb:bh0023@A1-E1'
                                                        )
                                                    ),
                                                    to=PathLinkEndStructure(
                                                        place_ref=QuayRefStructure(
                                                            version='01',
                                                            ref='ztb:bh0024_Rail@Q1'
                                                        ),
                                                        level_ref=LevelRefStructure(
                                                            version='01',
                                                            ref='ztb:bh0023@Lvl_0'
                                                        )
                                                    ),
                                                    accessibility_assessment_ref_or_accessibility_assessment=AccessibilityAssessment(
                                                        id='ztb:bh0023@lnk_A1-E2+Bus-Q1',
                                                        created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                        version='01',
                                                        mobility_impaired_access=LimitationStatusEnumeration.TRUE,
                                                        limitations=AccessibilityLimitationsRelStructure(
                                                            accessibility_limitation=AccessibilityLimitation(
                                                                id='ztb:bh0023@lnk_A1-E2+Bus-Q1',
                                                                created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                                version='01',
                                                                wheelchair_access=WheelchairAccess(
                                                                    value=LimitationStatusEnumeration.TRUE
                                                                ),
                                                                step_free_access=StepFreeAccess(
                                                                    value=LimitationStatusEnumeration.TRUE
                                                                ),
                                                                escalator_free_access=EscalatorFreeAccess(
                                                                    value=LimitationStatusEnumeration.TRUE
                                                                ),
                                                                lift_free_access=LiftFreeAccess(
                                                                    value=LimitationStatusEnumeration.TRUE
                                                                )
                                                            )
                                                        )
                                                    ),
                                                    covered=CoveredEnumeration.OUTDOORS,
                                                    number_of_steps=0,
                                                    allowed_use=PathDirectionEnumeration.TWO_WAY,
                                                    transition=TransitionEnumeration.LEVEL,
                                                    maximum_flow_per_minute=200,
                                                    transfer_duration=TransferDurationStructure(
                                                        default_duration=XmlDuration("PT1M"),
                                                        frequent_traveller_duration=XmlDuration("PT1M"),
                                                        occasional_traveller_duration=XmlDuration("PT2M"),
                                                        mobility_restricted_traveller_duration=XmlDuration("PT3M")
                                                    ),
                                                    level_ref=LevelRef(
                                                        version='01',
                                                        ref='ztb:bh0023@Lvl_0'
                                                    )
                                                ),
                                                SitePathLink(
                                                    id='ztb:bh0023@lnk_A1-E1+A1-E2',
                                                    created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Tthrough hall to platform1 '
                                                    ),
                                                    distance=Decimal('5'),
                                                    from_value=PathLinkEndStructure(
                                                        place_ref=AccessSpaceRefStructure(
                                                            version='01',
                                                            ref='ztb:bh0023@A1'
                                                        ),
                                                        level_ref=LevelRefStructure(
                                                            version='01',
                                                            ref='ztb:bh0023@Lvl_0'
                                                        ),
                                                        entrance_ref=EntranceRefStructure(
                                                            version='01',
                                                            ref='ztb:bh0023@A1-E1'
                                                        )
                                                    ),
                                                    to=PathLinkEndStructure(
                                                        place_ref=AccessSpaceRefStructure(
                                                            version='01',
                                                            ref='ztb:bh0023@A1'
                                                        ),
                                                        level_ref=LevelRefStructure(
                                                            version='01',
                                                            ref='ztb:bh0023@Lvl_0'
                                                        ),
                                                        entrance_ref=EntranceRefStructure(
                                                            version='01',
                                                            ref='ztb:bh0023@A1-E2'
                                                        )
                                                    ),
                                                    accessibility_assessment_ref_or_accessibility_assessment=AccessibilityAssessment(
                                                        id='ztb:bh0023@lnk_A1-E1+A1-E2',
                                                        created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                        version='01',
                                                        mobility_impaired_access=LimitationStatusEnumeration.TRUE,
                                                        limitations=AccessibilityLimitationsRelStructure(
                                                            accessibility_limitation=AccessibilityLimitation(
                                                                id='ztb:bh0023@lnk_A1-E1+A1-E2',
                                                                created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                                version='01',
                                                                wheelchair_access=WheelchairAccess(
                                                                    value=LimitationStatusEnumeration.TRUE
                                                                ),
                                                                step_free_access=StepFreeAccess(
                                                                    value=LimitationStatusEnumeration.TRUE
                                                                ),
                                                                escalator_free_access=EscalatorFreeAccess(
                                                                    value=LimitationStatusEnumeration.TRUE
                                                                ),
                                                                lift_free_access=LiftFreeAccess(
                                                                    value=LimitationStatusEnumeration.TRUE
                                                                )
                                                            )
                                                        )
                                                    ),
                                                    covered=CoveredEnumeration.COVERED,
                                                    number_of_steps=0,
                                                    allowed_use=PathDirectionEnumeration.TWO_WAY,
                                                    transition=TransitionEnumeration.LEVEL,
                                                    access_feature_type=AccessFeatureEnumeration.OPEN_SPACE,
                                                    maximum_flow_per_minute=200,
                                                    transfer_duration=TransferDurationStructure(
                                                        default_duration=XmlDuration("PT1M"),
                                                        frequent_traveller_duration=XmlDuration("PT1M"),
                                                        occasional_traveller_duration=XmlDuration("PT2M"),
                                                        mobility_restricted_traveller_duration=XmlDuration("PT3M")
                                                    ),
                                                    check_constraints=CheckConstraintsRelStructure(
                                                        check_constraint_ref_or_check_constraint=[
                                                            CheckConstraint(
                                                                id='ztb:bh0023@lnk_A1-E1+A1-E2',
                                                                version='any',
                                                                check_process=CheckProcessTypeEnumeration.TICKET_PURCHASE,
                                                                congestion=CongestionEnumeration.QUEUE,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='ztb:bh0023@lnk_A1-E1+A1-E2_01',
                                                                            version='any',
                                                                            minimum_likely_delay=XmlDuration("PT5M"),
                                                                            average_delay=XmlDuration("PT2M"),
                                                                            maximum_likely_delay=XmlDuration("PT10M")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                SitePathLink(
                                                    id='ztb:bh0023@lnk_A1-E2+Rail@Q1-E1tr',
                                                    created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Along platform1 to barrow crossing entrance'
                                                    ),
                                                    distance=Decimal('5'),
                                                    from_value=PathLinkEndStructure(
                                                        place_ref=AccessSpaceRefStructure(
                                                            version='01',
                                                            ref='ztb:bh0023@A1'
                                                        ),
                                                        level_ref=LevelRefStructure(
                                                            version='01',
                                                            ref='ztb:bh0023@Lvl_0'
                                                        ),
                                                        entrance_ref=StopPlaceEntranceRefStructure(
                                                            version='01',
                                                            ref='ztb:bh0023@A1-E2'
                                                        )
                                                    ),
                                                    to=PathLinkEndStructure(
                                                        place_ref=QuayRefStructure(
                                                            version='01',
                                                            ref='ztb:bh0023@Rail@Q1'
                                                        ),
                                                        level_ref=LevelRefStructure(
                                                            version='01',
                                                            ref='ztb:bh0023@Lvl_0'
                                                        ),
                                                        entrance_ref=StopPlaceEntranceRefStructure(
                                                            version='01',
                                                            ref='ztb:bh0023@Rail@Q1-E1tr'
                                                        )
                                                    ),
                                                    accessibility_assessment_ref_or_accessibility_assessment=AccessibilityAssessment(
                                                        id='ztb:bh0023@lnk_A1-E2+Rail@Q1-E2tr',
                                                        created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                        version='01',
                                                        mobility_impaired_access=LimitationStatusEnumeration.TRUE,
                                                        limitations=AccessibilityLimitationsRelStructure(
                                                            accessibility_limitation=AccessibilityLimitation(
                                                                id='ztb:bh0023@lnk_A1-E2+Rail@Q1-E2tr',
                                                                created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                                version='01',
                                                                wheelchair_access=WheelchairAccess(
                                                                    value=LimitationStatusEnumeration.TRUE
                                                                ),
                                                                step_free_access=StepFreeAccess(
                                                                    value=LimitationStatusEnumeration.TRUE
                                                                ),
                                                                escalator_free_access=EscalatorFreeAccess(
                                                                    value=LimitationStatusEnumeration.TRUE
                                                                ),
                                                                lift_free_access=LiftFreeAccess(
                                                                    value=LimitationStatusEnumeration.TRUE
                                                                )
                                                            )
                                                        )
                                                    ),
                                                    covered=CoveredEnumeration.COVERED,
                                                    number_of_steps=0,
                                                    allowed_use=PathDirectionEnumeration.TWO_WAY,
                                                    transition=TransitionEnumeration.LEVEL,
                                                    access_feature_type=AccessFeatureEnumeration.OPEN_SPACE,
                                                    maximum_flow_per_minute=200,
                                                    transfer_duration=TransferDurationStructure(
                                                        default_duration=XmlDuration("PT1M"),
                                                        frequent_traveller_duration=XmlDuration("PT1M"),
                                                        occasional_traveller_duration=XmlDuration("PT2M"),
                                                        mobility_restricted_traveller_duration=XmlDuration("PT3M")
                                                    ),
                                                    check_constraints=CheckConstraintsRelStructure(
                                                        check_constraint_ref_or_check_constraint=[
                                                            CheckConstraint(
                                                                id='ztb:bh0023@lnk_A1-E2+Rail@Q1-E2t',
                                                                version='any',
                                                                check_process=CheckProcessTypeEnumeration.TICKET_PURCHASE,
                                                                congestion=CongestionEnumeration.QUEUE,
                                                                delays=CheckConstraintDelaysRelStructure(
                                                                    check_constraint_delay_ref_or_check_constraint_delay=[
                                                                        CheckConstraintDelay(
                                                                            id='ztb:bh0023@lnk_A1-E2+Rail@Q1-E2_01',
                                                                            version='any',
                                                                            minimum_likely_delay=XmlDuration("PT5M"),
                                                                            average_delay=XmlDuration("PT2M"),
                                                                            maximum_likely_delay=XmlDuration("PT10M")
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                SitePathLink(
                                                    id='ztb:bh0023@lnk_Rail@Q1-E1tr+Rail@Q2-E1tr',
                                                    created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                    version='any',
                                                    name=MultilingualString(
                                                        value='Crossing over tracks from platform 1 to platform 2'
                                                    ),
                                                    distance=Decimal('10'),
                                                    from_value=PathLinkEndStructure(
                                                        place_ref=QuayRefStructure(
                                                            version='01',
                                                            ref='ztb:bh0023@Rail@Q1'
                                                        ),
                                                        level_ref=LevelRefStructure(
                                                            version='01',
                                                            ref='ztb:bh0023@Lvl_0'
                                                        ),
                                                        entrance_ref=EntranceRefStructure(
                                                            version='01',
                                                            ref='ztb:bh0023@Rail@Q1-E1tr'
                                                        )
                                                    ),
                                                    to=PathLinkEndStructure(
                                                        place_ref=QuayRefStructure(
                                                            version='01',
                                                            ref='ztb:bh0023@Rail@Q1'
                                                        ),
                                                        level_ref=LevelRefStructure(
                                                            version='01',
                                                            ref='ztb:bh0023@Lvl_0'
                                                        ),
                                                        entrance_ref=EntranceRefStructure(
                                                            version='01',
                                                            ref='ztb:bh0023@Rail@Q2-E1tr'
                                                        )
                                                    ),
                                                    accessibility_assessment_ref_or_accessibility_assessment=AccessibilityAssessment(
                                                        id='ztb:bh0023@lnk_Rail@Q1-E1tr+Rail@Q2-E1tr',
                                                        created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                        version='01',
                                                        mobility_impaired_access=LimitationStatusEnumeration.TRUE,
                                                        limitations=AccessibilityLimitationsRelStructure(
                                                            accessibility_limitation=AccessibilityLimitation(
                                                                id='ztb:bh0023@lnk_Rail@Q1-E1tr+Rail@Q2-E2tr',
                                                                created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                                version='01',
                                                                wheelchair_access=WheelchairAccess(
                                                                    value=LimitationStatusEnumeration.TRUE
                                                                ),
                                                                step_free_access=StepFreeAccess(
                                                                    value=LimitationStatusEnumeration.TRUE
                                                                ),
                                                                escalator_free_access=EscalatorFreeAccess(
                                                                    value=LimitationStatusEnumeration.TRUE
                                                                ),
                                                                lift_free_access=LiftFreeAccess(
                                                                    value=LimitationStatusEnumeration.TRUE
                                                                )
                                                            )
                                                        )
                                                    ),
                                                    covered=CoveredEnumeration.COVERED,
                                                    number_of_steps=0,
                                                    allowed_use=PathDirectionEnumeration.TWO_WAY,
                                                    transition=TransitionEnumeration.LEVEL,
                                                    access_feature_type=AccessFeatureEnumeration.OPEN_SPACE,
                                                    maximum_flow_per_minute=200,
                                                    transfer_duration=TransferDurationStructure(
                                                        default_duration=XmlDuration("PT1M"),
                                                        frequent_traveller_duration=XmlDuration("PT1M"),
                                                        occasional_traveller_duration=XmlDuration("PT2M"),
                                                        mobility_restricted_traveller_duration=XmlDuration("PT3M")
                                                    ),
                                                    level_ref=LevelRef(
                                                        version='01',
                                                        ref='ztb:bh0023@Lvl_0'
                                                    )
                                                ),
                                            ]
                                        ),
                                        navigation_paths=NavigationPathsRelStructure(
                                            navigation_path_ref_or_navigation_path=[
                                                NavigationPath(
                                                    id='ztb:NP_bh0023@Bus-Q1+Rail@Q2-E2tr',
                                                    created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                    version='01',
                                                    name=MultilingualString(
                                                        value='Bus Stop 1 to Rail Tick Hall '
                                                    ),
                                                    accessibility_assessment=AccessibilityAssessment(
                                                        id='ztb:NP_bh0023@Bus-Q1+Rail@Q2-E2trr',
                                                        version='any',
                                                        mobility_impaired_access=LimitationStatusEnumeration.TRUE
                                                    ),
                                                    summaries=AccessSummariesRelStructure(
                                                        access_summary=[
                                                            AccessSummary(
                                                                id='ztb:NP_bh0023@Bus-Q1+Rail@Q2-E2tr',
                                                                version='any',
                                                                access_feature_type=AccessFeatureEnumeration.CROSSING,
                                                                count=1,
                                                                transition=TransitionEnumeration.DOWN_AND_UP
                                                            ),
                                                        ]
                                                    ),
                                                    transfer_duration=TransferDurationStructure(
                                                        default_duration=XmlDuration("PT1M"),
                                                        mobility_restricted_traveller_duration=XmlDuration("PT1M")
                                                    ),
                                                    navigation_type=NavigationTypeEnumeration.QUAY_TO_HALL,
                                                    path_links_in_sequence=PathLinksInSequenceRelStructure(
                                                        path_link_in_sequence=[
                                                            PathLinkInSequence(
                                                                id='ztb:bh0023@Bus-Q1+Rail@Q2-E2tr-01',
                                                                version='any',
                                                                description=[
                                                                    MultilingualString(
                                                                        value='Bus stop to entrance (Reverse use of Link)'
                                                                    ),
                                                                ],
                                                                order=1,
                                                                path_link_ref=PathLinkRef(
                                                                    version='any',
                                                                    ref='ztb:bh0023@lnk_A1-E1+Bus-Q1'
                                                                ),
                                                                reverse=True,
                                                                heading=PathHeadingEnumeration.LEFT,
                                                                transition=TransitionEnumeration.LEVEL
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                NavigationPath(
                                                    id='ztb:NP_bh0023@A1+Bus-Q1',
                                                    created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                    version='01',
                                                    name=MultilingualString(
                                                        value='Rail Ticket Hall to bus Stop 1'
                                                    ),
                                                    accessibility_assessment=AccessibilityAssessment(
                                                        id='ztb:NP_bh0023@A1+Bus-Q1',
                                                        version='any',
                                                        mobility_impaired_access=LimitationStatusEnumeration.TRUE
                                                    ),
                                                    summaries=AccessSummariesRelStructure(
                                                        access_summary=[
                                                            AccessSummary(
                                                                id='ztb:NP_bh0023@A1+Bus-Q1',
                                                                version='any',
                                                                access_feature_type=AccessFeatureEnumeration.CROSSING,
                                                                count=1,
                                                                transition=TransitionEnumeration.LEVEL
                                                            ),
                                                        ]
                                                    ),
                                                    transfer_duration=TransferDurationStructure(
                                                        default_duration=XmlDuration("PT1M"),
                                                        mobility_restricted_traveller_duration=XmlDuration("PT1M")
                                                    ),
                                                    navigation_type=NavigationTypeEnumeration.HALL_TO_QUAY,
                                                    path_links_in_sequence=PathLinksInSequenceRelStructure(
                                                        path_link_in_sequence=[
                                                            PathLinkInSequence(
                                                                id='ztb:NP_bh0023@A1+Bus-Q-01',
                                                                version='any',
                                                                description=[
                                                                    MultilingualString(
                                                                        value='Bus stop to entrance (Forwards use of Link)'
                                                                    ),
                                                                ],
                                                                order=1,
                                                                path_link_ref=PathLinkRef(
                                                                    version='any',
                                                                    ref='ztb:bh0023@lnk_A1-E1+Bus-Q1'
                                                                ),
                                                                reverse=False,
                                                                heading=PathHeadingEnumeration.LEFT,
                                                                transition=TransitionEnumeration.LEVEL
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                NavigationPath(
                                                    id='ztb:NP_bh0023@A1+Rail@Q1',
                                                    created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                    version='01',
                                                    name=MultilingualString(
                                                        value='Rail Ticket Hall to Platform 1'
                                                    ),
                                                    accessibility_assessment=AccessibilityAssessment(
                                                        id='ztb:NP_bh0023@A1+Rail@Q2',
                                                        version='any',
                                                        mobility_impaired_access=LimitationStatusEnumeration.TRUE
                                                    ),
                                                    transfer_duration=TransferDurationStructure(
                                                        default_duration=XmlDuration("PT1M"),
                                                        mobility_restricted_traveller_duration=XmlDuration("PT2M")
                                                    ),
                                                    navigation_type=NavigationTypeEnumeration.HALL_TO_QUAY,
                                                    path_links_in_sequence=PathLinksInSequenceRelStructure(
                                                        path_link_in_sequence=[
                                                            PathLinkInSequence(
                                                                id='ztb:NP_bh0023@A1+Rail@Q1',
                                                                version='any',
                                                                description=[
                                                                    MultilingualString(
                                                                        value='From  ticket hall to platform 1'
                                                                    ),
                                                                ],
                                                                order=1,
                                                                path_link_ref=PathLinkRef(
                                                                    version='any',
                                                                    ref='ztb:bh0023@lnk_A1-E1+A1-E2'
                                                                ),
                                                                reverse=False,
                                                                heading=PathHeadingEnumeration.FORWARD,
                                                                transition=TransitionEnumeration.LEVEL
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                NavigationPath(
                                                    id='ztb:NP_bh0023@Rail@Q1+A1',
                                                    created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                    version='01',
                                                    name=MultilingualString(
                                                        value='Platform 1 to Rail Ticket Hall'
                                                    ),
                                                    accessibility_assessment=AccessibilityAssessment(
                                                        id='ztb:NP_bh0023@Rail@Q1+A1',
                                                        version='any',
                                                        mobility_impaired_access=LimitationStatusEnumeration.TRUE
                                                    ),
                                                    transfer_duration=TransferDurationStructure(
                                                        default_duration=XmlDuration("PT1M"),
                                                        mobility_restricted_traveller_duration=XmlDuration("PT2M")
                                                    ),
                                                    navigation_type=NavigationTypeEnumeration.QUAY_TO_HALL,
                                                    path_links_in_sequence=PathLinksInSequenceRelStructure(
                                                        path_link_in_sequence=[
                                                            PathLinkInSequence(
                                                                id='ztb:NP_bh0023@Rail@Q1+A1',
                                                                version='any',
                                                                description=[
                                                                    MultilingualString(
                                                                        value='Reverse use: platform 1 to From  ticket hall '
                                                                    ),
                                                                ],
                                                                order=1,
                                                                path_link_ref=PathLinkRef(
                                                                    version='any',
                                                                    ref='ztb:bh0023@lnk_A1-E1+A1-E2'
                                                                ),
                                                                reverse=True,
                                                                heading=PathHeadingEnumeration.FORWARD,
                                                                transition=TransitionEnumeration.LEVEL
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                NavigationPath(
                                                    id='ztb:NP_bh0023@A1+Rail@Q2',
                                                    created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                    version='01',
                                                    name=MultilingualString(
                                                        value='Rail Ticket Hall to Platform 2'
                                                    ),
                                                    accessibility_assessment=AccessibilityAssessment(
                                                        id='ztb:NP_bh0023@A1+Rail@Q2-E1tr',
                                                        version='any',
                                                        mobility_impaired_access=LimitationStatusEnumeration.TRUE
                                                    ),
                                                    summaries=AccessSummariesRelStructure(
                                                        access_summary=[
                                                            AccessSummary(
                                                                id='ztb:NP_bh0023@A1+Rail@Q2-E1tr',
                                                                version='any',
                                                                access_feature_type=AccessFeatureEnumeration.CROSSING,
                                                                count=1,
                                                                transition=TransitionEnumeration.DOWN_AND_UP
                                                            ),
                                                        ]
                                                    ),
                                                    transfer_duration=TransferDurationStructure(
                                                        default_duration=XmlDuration("PT3M"),
                                                        mobility_restricted_traveller_duration=XmlDuration("PT10M")
                                                    ),
                                                    navigation_type=NavigationTypeEnumeration.HALL_TO_QUAY,
                                                    path_links_in_sequence=PathLinksInSequenceRelStructure(
                                                        path_link_in_sequence=[
                                                            PathLinkInSequence(
                                                                id='ztb:NP_bh0023@A1+Rail@Q2-02',
                                                                version='any',
                                                                description=[
                                                                    MultilingualString(
                                                                        value='Across ticket hall'
                                                                    ),
                                                                ],
                                                                order=1,
                                                                path_link_ref=PathLinkRef(
                                                                    version='any',
                                                                    ref='ztb:bh0023@lnk_A1-E1+A1-E2'
                                                                ),
                                                                reverse=False,
                                                                heading=PathHeadingEnumeration.FORWARD,
                                                                transition=TransitionEnumeration.LEVEL
                                                            ),
                                                            PathLinkInSequence(
                                                                id='ztb:NP_bh0023@A1+Rail@Q2-03',
                                                                version='any',
                                                                description=[
                                                                    MultilingualString(
                                                                        value='Along platform 1 to crossing'
                                                                    ),
                                                                ],
                                                                order=2,
                                                                path_link_ref=PathLinkRef(
                                                                    version='any',
                                                                    ref='ztb:bh0023@lnk_A1-E2+Rail@Q1-E1tr'
                                                                ),
                                                                reverse=False,
                                                                heading=PathHeadingEnumeration.RIGHT,
                                                                transition=TransitionEnumeration.LEVEL
                                                            ),
                                                            PathLinkInSequence(
                                                                id='ztb:NP_bh0023@A1+Rail@Q2-04',
                                                                version='any',
                                                                description=[
                                                                    MultilingualString(
                                                                        value='Crossing from platform 1 to platform 2'
                                                                    ),
                                                                ],
                                                                order=3,
                                                                path_link_ref=PathLinkRef(
                                                                    version='any',
                                                                    ref='ztb:bh0023@lnk_Rail@Q1-E1tr+Rail@Q2-E1tr'
                                                                ),
                                                                reverse=False,
                                                                heading=PathHeadingEnumeration.FORWARD,
                                                                transition=TransitionEnumeration.DOWN_AND_UP
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                NavigationPath(
                                                    id='ztb:NP_bh0023@Rail@Q2+A1',
                                                    created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                    version='01',
                                                    name=MultilingualString(
                                                        value='Platform 2 to Rail Ticket Hall '
                                                    ),
                                                    accessibility_assessment=AccessibilityAssessment(
                                                        id='ztb:NP_bh0023@Rail@Q2+A1',
                                                        version='any',
                                                        mobility_impaired_access=LimitationStatusEnumeration.TRUE
                                                    ),
                                                    summaries=AccessSummariesRelStructure(
                                                        access_summary=[
                                                            AccessSummary(
                                                                id='ztb:NP_bh0023@Rail@Q2+A1',
                                                                version='any',
                                                                access_feature_type=AccessFeatureEnumeration.CROSSING,
                                                                count=1,
                                                                transition=TransitionEnumeration.DOWN_AND_UP
                                                            ),
                                                        ]
                                                    ),
                                                    transfer_duration=TransferDurationStructure(
                                                        default_duration=XmlDuration("PT3M"),
                                                        mobility_restricted_traveller_duration=XmlDuration("PT10M")
                                                    ),
                                                    navigation_type=NavigationTypeEnumeration.QUAY_TO_HALL,
                                                    path_links_in_sequence=PathLinksInSequenceRelStructure(
                                                        path_link_in_sequence=[
                                                            PathLinkInSequence(
                                                                id='ztb:NP_bh0023@Rail@Q2+A1-01',
                                                                version='any',
                                                                description=[
                                                                    MultilingualString(
                                                                        value='Crossing from platform 1 to platform 2'
                                                                    ),
                                                                ],
                                                                order=1,
                                                                path_link_ref=PathLinkRef(
                                                                    version='any',
                                                                    ref='ztb:bh0023@lnk_Rail@Q1-E1tr+Rail@Q2-E1tr'
                                                                ),
                                                                reverse=True,
                                                                heading=PathHeadingEnumeration.FORWARD,
                                                                transition=TransitionEnumeration.DOWN_AND_UP
                                                            ),
                                                            PathLinkInSequence(
                                                                id='ztb:NP_bh0023@Rail@Q2+A1-02',
                                                                version='any',
                                                                description=[
                                                                    MultilingualString(
                                                                        value='Along platform 1 to crossing'
                                                                    ),
                                                                ],
                                                                order=2,
                                                                path_link_ref=PathLinkRef(
                                                                    version='any',
                                                                    ref='ztb:bh0023@lnk_A1-E2+Rail@Q1-E1tr'
                                                                ),
                                                                reverse=True,
                                                                heading=PathHeadingEnumeration.RIGHT,
                                                                transition=TransitionEnumeration.LEVEL
                                                            ),
                                                            PathLinkInSequence(
                                                                id='ztb:NP_bh0023@Rail@Q2+A1-03',
                                                                version='any',
                                                                description=[
                                                                    MultilingualString(
                                                                        value='Across ticket hall'
                                                                    ),
                                                                ],
                                                                order=3,
                                                                path_link_ref=PathLinkRef(
                                                                    version='any',
                                                                    ref='ztb:bh0023@lnk_A1-E1+A1-E2'
                                                                ),
                                                                reverse=True,
                                                                heading=PathHeadingEnumeration.FORWARD,
                                                                transition=TransitionEnumeration.LEVEL
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                NavigationPath(
                                                    id='ztb:bh0023@Rail@Q1+Rail@Q2',
                                                    created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                    version='01',
                                                    name=MultilingualString(
                                                        value='Platform1 to Platform2'
                                                    ),
                                                    accessibility_assessment=AccessibilityAssessment(
                                                        id='ztb:bh0023@Rail@Q1+Rail@Q2',
                                                        version='any',
                                                        mobility_impaired_access=LimitationStatusEnumeration.TRUE,
                                                        limitations=AccessibilityLimitationsRelStructure(
                                                            accessibility_limitation=AccessibilityLimitation(
                                                                id='ztb:bh0023@lnk_Rail@Q1+Rail@Q2',
                                                                wheelchair_access=WheelchairAccess(
                                                                    value=LimitationStatusEnumeration.TRUE
                                                                ),
                                                                step_free_access=StepFreeAccess(

                                                                ),
                                                                escalator_free_access=EscalatorFreeAccess(

                                                                ),
                                                                lift_free_access=LiftFreeAccess(

                                                                ),
                                                                audible_signals_available=AudibleSignalsAvailable(

                                                                ),
                                                                visual_signs_available=VisualSignsAvailable(

                                                                )
                                                            )
                                                        )
                                                    ),
                                                    summaries=AccessSummariesRelStructure(
                                                        access_summary=[
                                                            AccessSummary(
                                                                id='ztb:bh0023@Rail@Q1+Rail@Q2',
                                                                version='any',
                                                                access_feature_type=AccessFeatureEnumeration.CROSSING,
                                                                count=1,
                                                                transition=TransitionEnumeration.DOWN_AND_UP
                                                            ),
                                                        ]
                                                    ),
                                                    transfer_duration=TransferDurationStructure(
                                                        default_duration=XmlDuration("PT1M"),
                                                        mobility_restricted_traveller_duration=XmlDuration("PT5M")
                                                    ),
                                                    navigation_type=NavigationTypeEnumeration.QUAY_TO_QUAY,
                                                    path_links_in_sequence=PathLinksInSequenceRelStructure(
                                                        path_link_in_sequence=[
                                                            PathLinkInSequence(
                                                                id='ztb:bh0023@Rail@Q1+Rail@Q2_01',
                                                                version='any',
                                                                description=[
                                                                    MultilingualString(
                                                                        value='Crossing  from platform 1 to platform 2'
                                                                    ),
                                                                ],
                                                                order=1,
                                                                path_link_ref=PathLinkRef(
                                                                    version='any',
                                                                    ref='ztb:bh0023@lnk_Rail@Q1-E1tr+Rail@Q2-E1tr'
                                                                ),
                                                                reverse=False,
                                                                heading=PathHeadingEnumeration.FORWARD,
                                                                transition=TransitionEnumeration.DOWN_AND_UP
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                NavigationPath(
                                                    id='ztb:bh0023@Rail@Q2+Rail@Q1',
                                                    created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                    version='01',
                                                    name=MultilingualString(
                                                        value='Platform 2 to Platform1'
                                                    ),
                                                    accessibility_assessment=AccessibilityAssessment(
                                                        id='ztb:bh0023@Rail@Q2+Rail@Q1',
                                                        version='any',
                                                        mobility_impaired_access=LimitationStatusEnumeration.TRUE,
                                                        limitations=AccessibilityLimitationsRelStructure(
                                                            accessibility_limitation=AccessibilityLimitation(
                                                                id='ztb:bh0023@lnk_Rail@Q2+Rail@Q1',
                                                                wheelchair_access=WheelchairAccess(
                                                                    value=LimitationStatusEnumeration.TRUE
                                                                ),
                                                                step_free_access=StepFreeAccess(

                                                                ),
                                                                escalator_free_access=EscalatorFreeAccess(

                                                                ),
                                                                lift_free_access=LiftFreeAccess(

                                                                ),
                                                                audible_signals_available=AudibleSignalsAvailable(

                                                                ),
                                                                visual_signs_available=VisualSignsAvailable(

                                                                )
                                                            )
                                                        )
                                                    ),
                                                    summaries=AccessSummariesRelStructure(
                                                        access_summary=[
                                                            AccessSummary(
                                                                id='ztb:bh0023@Rail@Q2+Rail@Q1',
                                                                version='any',
                                                                access_feature_type=AccessFeatureEnumeration.CROSSING,
                                                                count=1,
                                                                transition=TransitionEnumeration.DOWN_AND_UP
                                                            ),
                                                        ]
                                                    ),
                                                    transfer_duration=TransferDurationStructure(
                                                        default_duration=XmlDuration("PT1M"),
                                                        mobility_restricted_traveller_duration=XmlDuration("PT5M")
                                                    ),
                                                    navigation_type=NavigationTypeEnumeration.QUAY_TO_QUAY,
                                                    path_links_in_sequence=PathLinksInSequenceRelStructure(
                                                        path_link_in_sequence=[
                                                            PathLinkInSequence(
                                                                id='ztb:bh0023@Rail@Q2+Rail@Q1_01',
                                                                version='any',
                                                                description=[
                                                                    MultilingualString(
                                                                        value='Crossing  from platform 2 to platform 1 (Reverse use of Link'
                                                                    ),
                                                                ],
                                                                order=1,
                                                                path_link_ref=PathLinkRef(
                                                                    version='any',
                                                                    ref='ztb:bh0023@lnk_Rail@Q1-E1tr+Rail@Q2-E1tr'
                                                                ),
                                                                reverse=True,
                                                                heading=PathHeadingEnumeration.FORWARD,
                                                                transition=TransitionEnumeration.DOWN_AND_UP
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    StopPlace(
                                        id='ztb:bh0024',
                                        created=XmlDateTime(2006, 9, 11, 15, 42, 0),
                                        version='01',
                                        name=MultilingualString(
                                            value='Bahnhof Ried'
                                        ),
                                        short_name=MultilingualString(
                                            value='Bahnhof'
                                        ),
                                        centroid=SimplePointVersionStructure(
                                            location=LocationStructure2(
                                                pos=Pos(
                                                    value=[
                                                        524811.0,
                                                        170666.0,
                                                    ],
                                                    srs_name='ATGRID'
                                                )
                                            )
                                        ),
                                        road_address=RoadAddress(
                                            id='zbt:LRd_Addr_02',
                                            version='any',
                                            road_name=MultilingualString(
                                                value='Kleiner Ried'
                                            )
                                        ),
                                        accessibility_assessment=AccessibilityAssessment(
                                            id='ztb:bh0024',
                                            created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                            version='01',
                                            mobility_impaired_access=LimitationStatusEnumeration.TRUE
                                        ),
                                        topographic_place_ref_or_topographic_place_view=TopographicPlaceView(
                                            topographic_place_ref=TopographicPlaceRef(
                                                version='01',
                                                ref='topat:E0034695'
                                            )
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
                                        stop_place_type=StopTypeEnumeration.ONSTREET_BUS,
                                        quays=QuaysRelStructure(
                                            taxi_stand_ref_or_quay_ref_or_quay=[
                                                Quay(
                                                    id='ztb:bh0024_Rail@Q1',
                                                    created=XmlDateTime(2010, 4, 17, 9, 30, 47, 0, 0),
                                                    version='01',
                                                    name=MultilingualString(
                                                        value='Ried, Bahnhof  Bus'
                                                    ),
                                                    description=[
                                                        MultilingualString(
                                                            value='Stop outside the station '
                                                        ),
                                                    ],
                                                    centroid=SimplePointVersionStructure(
                                                        location=LocationStructure2(
                                                            longitude=Decimal('-0.2068758371'),
                                                            latitude=Decimal('51.4207729447')
                                                        )
                                                    ),
                                                    road_address=RoadAddress(
                                                        id='ztb:Rd_Addr_03',
                                                        version='any',
                                                        road_name=MultilingualString(
                                                            value='Kleiner Ried'
                                                        ),
                                                        bearing_compass=CompassBearing16Enumeration.W
                                                    ),
                                                    accessibility_assessment=AccessibilityAssessment(
                                                        id='ztb:bh0024_Rail@Q1',
                                                        version='any',
                                                        mobility_impaired_access=LimitationStatusEnumeration.TRUE
                                                    ),
                                                    covered=CoveredEnumeration.OUTDOORS,
                                                    boarding_use=True,
                                                    alighting_use=True,
                                                    label=MultilingualString(
                                                        value='Halt A'
                                                    ),
                                                    public_code='1-2345',
                                                    destinations=DestinationDisplayViewsRelStructure(
                                                        destination_display_ref_or_destination_display_view=[
                                                            DestinationDisplayView(
                                                                name=MultilingualString(
                                                                    value='normalizedString'
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                    compass_octant=CompassBearing8Enumeration.W,
                                                    quay_type=QuayTypeEnumeration.BUS_STOP
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        ServiceFrame(
                            id='zbt:SF0023b',
                            version='any',
                            frame_defaults=VersionFrameDefaultsStructure(
                                default_responsibility_set_ref=ResponsibilitySetRefStructure(
                                    version='01',
                                    ref='zbt:Resp02'
                                )
                            ),
                            scheduled_stop_points=ScheduledStopPointsInFrameRelStructure(
                                scheduled_stop_point=[
                                    ScheduledStopPoint(
                                        id='ztb:ssa_bh0023',
                                        created=XmlDateTime(2000, 12, 17, 9, 30, 47, 0, 0),
                                        changed=XmlDateTime(2002, 12, 17, 9, 30, 47, 0, 0),
                                        version='032',
                                        name=MultilingualString(
                                            value='Bahnhof Ried',
                                            lang='de'
                                        ),
                                        vehicle_modes=[
                                            VehicleModeEnumeration.RAIL,
                                        ],
                                        for_alighting=True,
                                        for_boarding=True
                                    ),
                                    ScheduledStopPoint(
                                        id='ztb:ssa_bh0026',
                                        created=XmlDateTime(2000, 12, 17, 9, 30, 47, 0, 0),
                                        changed=XmlDateTime(2002, 12, 17, 9, 30, 47, 0, 0),
                                        version='002',
                                        name=MultilingualString(
                                            value='Bahnhof Ried Haltstelle',
                                            lang='de'
                                        ),
                                        vehicle_modes=[
                                            VehicleModeEnumeration.BUS,
                                        ],
                                        for_alighting=True,
                                        for_boarding=True
                                    ),
                                ]
                            ),
                            connections=TransfersInFrameRelStructure(
                                transfer=[
                                    Connection(
                                        id='ztb:ssa_bh0023',
                                        created=XmlDateTime(2000, 12, 17, 9, 30, 47, 0, 0),
                                        changed=XmlDateTime(2002, 12, 17, 9, 30, 47, 0, 0),
                                        version='032',
                                        name=MultilingualString(
                                            value='Bahnhof Ried Bus to Train'
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT3M")
                                        ),
                                        both_ways=True,
                                        from_value=ConnectionEndStructure(
                                            transport_mode=AllModesEnumeration.BUS,
                                            scheduled_stop_point_ref_or_vehicle_meeting_point_ref=ScheduledStopPointRefStructure(
                                                version='002',
                                                ref='ztb:ssa_bh0026'
                                            )
                                        ),
                                        to=ConnectionEndStructure(
                                            transport_mode=AllModesEnumeration.RAIL,
                                            scheduled_stop_point_ref_or_vehicle_meeting_point_ref=ScheduledStopPointRefStructure(
                                                version='032',
                                                ref='ztb:ssa_bh0023'
                                            )
                                        )
                                    ),
                                ]
                            ),
                            stop_assignments=StopAssignmentsInFrameRelStructure(
                                stop_assignment=[
                                    PassengerStopAssignment(
                                        id='ztb:psa_bh0023',
                                        version='any',
                                        description=MultilingualString(
                                            value='Rail Assignment regardless of Platform '
                                        ),
                                        order=1,
                                        fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=ScheduledStopPointRef(
                                            version='032',
                                            ref='ztb:ssa_bh0023'
                                        ),
                                        taxi_rank_ref_or_stop_place_ref_or_stop_place=StopPlaceRef(
                                            version='01',
                                            ref='ztb:bh0023'
                                        )
                                    ),
                                    PassengerStopAssignment(
                                        id='ztb:psa_bh0023@Rail@Q1',
                                        version='any',
                                        description=MultilingualString(
                                            value='Rail Assignment Platform 1'
                                        ),
                                        order=2,
                                        fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=ScheduledStopPointRef(
                                            version='032',
                                            ref='ztb:ssa_bh0023'
                                        ),
                                        taxi_rank_ref_or_stop_place_ref_or_stop_place=StopPlaceRef(
                                            version='01',
                                            ref='ztb:bh0023'
                                        ),
                                        taxi_stand_ref_or_quay_ref_or_quay=QuayRef(
                                            version='01',
                                            ref='ztb:bh0023@Rail@Q1'
                                        )
                                    ),
                                    PassengerStopAssignment(
                                        id='ztb:psa_bh0023@Rail@Q2',
                                        version='any',
                                        description=MultilingualString(
                                            value='Rail Assignment Platform 2 '
                                        ),
                                        order=3,
                                        fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=ScheduledStopPointRef(
                                            version='032',
                                            ref='ztb:ssa_bh0023'
                                        ),
                                        taxi_rank_ref_or_stop_place_ref_or_stop_place=StopPlaceRef(
                                            version='01',
                                            ref='ztb:bh0023'
                                        ),
                                        taxi_stand_ref_or_quay_ref_or_quay=QuayRef(
                                            version='01',
                                            ref='ztb:bh0023@Rail@Q2'
                                        )
                                    ),
                                ]
                            )
                        ),
                        ResourceFrame(
                            id='zbt:Resp01',
                            version='any',
                            responsibility_set_ref_attribute='zbt:Resp01',
                            responsibility_sets=ResponsibilitySetsInFrameRelStructure(
                                responsibility_set=[
                                    ResponsibilitySet(
                                        id='zbt:Resp01',
                                        created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                        changed=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='01',
                                        responsibility_set_ref_attribute='zbt:Resp01',
                                        name=MultilingualString(
                                            value='Responsibility for Stop Data'
                                        ),
                                        roles=ResponsibilityRoleAssignmentsRelStructure(
                                            responsibility_role_assignment=[
                                                ResponsibilityRoleAssignment(
                                                    id='mybus:Resp01',
                                                    created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                    version='01',
                                                    description=MultilingualString(
                                                        value='Zall Zillertal transport - Managed centrally'
                                                    ),
                                                    data_role_type=[
                                                        DataRoleTypeEnumeration.ALL,
                                                    ],
                                                    responsible_organisation_ref=OperatorRefStructure(
                                                        version='any',
                                                        ref='zbt:Org_ZTLB'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    ResponsibilitySet(
                                        id='zbt:Resp02',
                                        created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                        changed=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='01',
                                        responsibility_set_ref_attribute='zbt:Resp01',
                                        name=MultilingualString(
                                            value='Responsibility for timetables'
                                        ),
                                        roles=ResponsibilityRoleAssignmentsRelStructure(
                                            responsibility_role_assignment=[
                                                ResponsibilityRoleAssignment(
                                                    id='mybus:Resp02',
                                                    created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                                    version='01',
                                                    description=MultilingualString(
                                                        value='Zall Zillertal transport - Managed centrally'
                                                    ),
                                                    data_role_type=[
                                                        DataRoleTypeEnumeration.ALL,
                                                    ],
                                                    responsible_organisation_ref=OperatorRefStructure(
                                                        version='any',
                                                        ref='zbt:Org_ZTLB'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            organisations=OrganisationsInFrameRelStructure(
                                organisation_or_transport_organisation=[
                                    Operator(
                                        id='zbt:Org_ZTLB',
                                        version='any',
                                        public_code=PrivateCodeStructure(
                                            value='ZTB'
                                        ),
                                        name=MultilingualString(
                                            value='Zillerthalerbahn'
                                        ),
                                        short_name=MultilingualString(
                                            value='Z-Bahn '
                                        ),
                                        trading_name=MultilingualString(
                                            value='Zillerthalerbahn GMBh'
                                        ),
                                        description=MultilingualString(
                                            value='Responsible for Underground'
                                        ),
                                        organisation_type=[
                                            OrganisationTypeEnumeration.OPERATOR,
                                        ]
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
