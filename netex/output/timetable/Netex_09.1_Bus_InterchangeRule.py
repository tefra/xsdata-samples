from decimal import Decimal
from netex.models.all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from netex.models.alternative_texts_rel_structure import AvailabilityCondition
from netex.models.alternative_texts_rel_structure import ValidityConditionsRelStructure
from netex.models.authority import Authority
from netex.models.authority_ref import AuthorityRef
from netex.models.codespace import Codespace
from netex.models.codespace_ref_structure import CodespaceRefStructure
from netex.models.codespaces_rel_structure import CodespacesRelStructure
from netex.models.connection import Connection
from netex.models.connection_end_structure import ConnectionEndStructure
from netex.models.connection_ref_structure import ConnectionRefStructure
from netex.models.control_centre import ControlCentre
from netex.models.control_centre_ref import ControlCentreRef
from netex.models.control_centres_in_frame_rel_structure import ControlCentresInFrameRelStructure
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.direction import Direction
from netex.models.direction_ref import DirectionRef
from netex.models.directions_in_frame_rel_structure import DirectionsInFrameRelStructure
from netex.models.entities_in_version_rel_structure import CompositeFrame
from netex.models.entities_in_version_rel_structure import FramesRelStructure
from netex.models.interchange_rule import InterchangeRule
from netex.models.interchange_rule_parameter_structure import InterchangeRuleParameterStructure
from netex.models.interchange_rules_in_frame_rel_structure import InterchangeRulesInFrameRelStructure
from netex.models.line import Line
from netex.models.line_in_direction_ref import LineInDirectionRef
from netex.models.line_ref import LineRef
from netex.models.lines_in_frame_rel_structure import LinesInFrameRelStructure
from netex.models.location_structure_2 import LocationStructure2
from netex.models.multilingual_string import MultilingualString
from netex.models.network_frame_topic_structure import NetworkFrameTopicStructure
from netex.models.organisations_in_frame_rel_structure import OrganisationsInFrameRelStructure
from netex.models.publication_delivery import PublicationDelivery
from netex.models.publication_request_structure import PublicationRequestStructure
from netex.models.resource_frame import ResourceFrame
from netex.models.scheduled_stop_point import ScheduledStopPoint
from netex.models.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.models.scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from netex.models.scheduled_stop_points_in_frame_rel_structure import ScheduledStopPointsInFrameRelStructure
from netex.models.service_frame import ServiceFrame
from netex.models.stop_type_enumeration import StopTypeEnumeration
from netex.models.timetable_frame import TimetableFrame
from netex.models.timetable_frame_ref import TimetableFrameRef
from netex.models.timing_point_status_enumeration import TimingPointStatusEnumeration
from netex.models.transfer_duration_structure import TransferDurationStructure
from netex.models.transfers_in_frame_rel_structure import TransfersInFrameRelStructure
from netex.models.vehicle_mode_enumeration import VehicleModeEnumeration
from netex.models.version_frame_defaults_structure import VersionFrameDefaultsStructure
from netex.models.version_ref_structure import VersionRefStructure
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration


obj = PublicationDelivery(
    publication_timestamp=XmlDateTime(2010, 12, 17, 9, 30, 47, 0, 0),
    participant_ref="SYS001",
    publication_request=PublicationRequestStructure(
        request_timestamp=XmlDateTime(2010, 12, 17, 9, 30, 47, 0, 0),
        participant_ref="SYS002",
        topics=PublicationRequestStructure.Topics(
            network_frame_topic=[
                NetworkFrameTopicStructure(
                    choice=NetworkFrameTopicStructure.SelectionValidityConditions(
                        choice=[
                            AvailabilityCondition(
                                id="hde:CAL_02",
                                version="any",
                                from_date=XmlDateTime(2010, 11, 1, 0, 0, 0, 0, 0)
                            ),
                        ]
                    ),
                    choice_1=[
                        TimetableFrameRef(
                            value="REQUEST",
                            ref="hde:TimetableFrameTIM_23_O"
                        ),
                    ]
                ),
            ]
        )
    ),
    publication_refresh_interval=XmlDuration("P1M"),
    description=MultilingualString(
        value="Example  of simple intyerchange rulkes"
    ),
    data_objects=DataObjectsRelStructure(
        choice=[
            CompositeFrame(
                id="hde:CAL_02",
                version="2",
                codespaces=CodespacesRelStructure(
                    codespace_ref_or_codespace=[
                        Codespace(
                            id="mybus",
                            xmlns="mybus",
                            xmlns_url="http://www.mybuses.eu/stuff",
                            description="My buses"
                        ),
                        Codespace(
                            id="hde",
                            xmlns="hde",
                            xmlns_url="http://www.halt.de/",
                            description="Stop data  data"
                        ),
                    ]
                ),
                frame_defaults=VersionFrameDefaultsStructure(
                    default_codespace_ref=CodespaceRefStructure(
                        ref="mybus"
                    )
                ),
                frames=FramesRelStructure(
                    choice=[
                        ServiceFrame(
                            id="mybus:svf_12",
                            version="1",
                            name=MultilingualString(
                                value="Stops for Winter timetable for route 24 "
                            ),
                            directions=DirectionsInFrameRelStructure(
                                direction=[
                                    Direction(
                                        id="mybus:DR_hbf",
                                        version="any",
                                        name=MultilingualString(
                                            value="Main Station"
                                        ),
                                        short_name=MultilingualString(
                                            value="HBFd"
                                        )
                                    ),
                                    Direction(
                                        id="mybus:DR_Lake",
                                        version="any",
                                        name=MultilingualString(
                                            value="Lake"
                                        )
                                    ),
                                    Direction(
                                        id="mybus:DR_Forest",
                                        version="any",
                                        name=MultilingualString(
                                            value="Forest"
                                        )
                                    ),
                                    Direction(
                                        id="mybus:DR_MarketHall",
                                        version="any",
                                        name=MultilingualString(
                                            value="Market Hall"
                                        )
                                    ),
                                    Direction(
                                        id="mybus:DR_Museum",
                                        version="any",
                                        name=MultilingualString(
                                            value="Museum"
                                        )
                                    ),
                                    Direction(
                                        id="mybus:DR_Tower",
                                        version="any",
                                        name=MultilingualString(
                                            value="Tower"
                                        )
                                    ),
                                    Direction(
                                        id="mybus:DR_TownHall",
                                        version="any",
                                        name=MultilingualString(
                                            value="Town Hall"
                                        )
                                    ),
                                    Direction(
                                        id="mybus:DR_Outskirts",
                                        version="any",
                                        name=MultilingualString(
                                            value="Outskirts"
                                        )
                                    ),
                                    Direction(
                                        id="mybus:DR_Opera",
                                        version="any",
                                        name=MultilingualString(
                                            value="Opera"
                                        )
                                    ),
                                    Direction(
                                        id="mybus:DR_IndustrieparkWest",
                                        version="any",
                                        name=MultilingualString(
                                            value="Industriepark West"
                                        )
                                    ),
                                    Direction(
                                        id="mybus:DR_CarPArk",
                                        version="any",
                                        name=MultilingualString(
                                            value="Car Park"
                                        )
                                    ),
                                    Direction(
                                        id="mybus:DR_Stadium",
                                        version="any",
                                        name=MultilingualString(
                                            value="Stadium"
                                        )
                                    ),
                                    Direction(
                                        id="mybus:DR_Hospital",
                                        version="any",
                                        name=MultilingualString(
                                            value="Hospital"
                                        )
                                    ),
                                ]
                            ),
                            lines=LinesInFrameRelStructure(
                                flexible_line_or_line=[
                                    Line(
                                        id="mybus:LN_1",
                                        version="any",
                                        name=MultilingualString(
                                            value="Line 1  Lake to Forest"
                                        ),
                                        short_name=MultilingualString(
                                            value="Line 1"
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
                                        public_code="1"
                                    ),
                                    Line(
                                        id="mybus:LN_2",
                                        version="any",
                                        name=MultilingualString(
                                            value="Line 2  Market hall to Museum"
                                        ),
                                        short_name=MultilingualString(
                                            value="Line 2"
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
                                        public_code="2"
                                    ),
                                    Line(
                                        id="mybus:LN_3",
                                        version="any",
                                        name=MultilingualString(
                                            value="Line 3 Tower to Town Hall"
                                        ),
                                        short_name=MultilingualString(
                                            value="Line 3"
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
                                        public_code="3"
                                    ),
                                    Line(
                                        id="mybus:LN_4",
                                        version="any",
                                        name=MultilingualString(
                                            value="Line 4  Outskirts to Opera"
                                        ),
                                        short_name=MultilingualString(
                                            value="Line 5"
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
                                        public_code="5"
                                    ),
                                    Line(
                                        id="mybus:LN_5",
                                        version="any",
                                        name=MultilingualString(
                                            value="Line 5 IndustriePark West  to Carparkl"
                                        ),
                                        short_name=MultilingualString(
                                            value="Line 5"
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
                                        public_code="5"
                                    ),
                                    Line(
                                        id="mybus:LN_6",
                                        version="any",
                                        name=MultilingualString(
                                            value="Line 6 Stadium to Hospitall"
                                        ),
                                        short_name=MultilingualString(
                                            value="Line 6"
                                        ),
                                        transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
                                        public_code="6"
                                    ),
                                ]
                            ),
                            scheduled_stop_points=ScheduledStopPointsInFrameRelStructure(
                                scheduled_stop_point=[
                                    ScheduledStopPoint(
                                        id="mybus:SSP_025",
                                        version="any",
                                        name=MultilingualString(
                                            value="Main Station"
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal("53.0000"),
                                            latitude=Decimal("0.1000")
                                        ),
                                        timing_point_status=TimingPointStatusEnumeration.TIMING_POINT,
                                        short_name=MultilingualString(
                                            value="Main Station"
                                        ),
                                        stop_type=StopTypeEnumeration.RAIL_STATION,
                                        vehicle_modes=[
                                            VehicleModeEnumeration.RAIL,
                                            VehicleModeEnumeration.BUS,
                                            VehicleModeEnumeration.BUS,
                                        ]
                                    ),
                                    ScheduledStopPoint(
                                        id="mybus:SSP_002",
                                        version="any",
                                        name=MultilingualString(
                                            value="Bravo Street"
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal("53.2000"),
                                            latitude=Decimal("0.2000")
                                        ),
                                        timing_point_status=TimingPointStatusEnumeration.TIMING_POINT,
                                        short_name=MultilingualString(
                                            value="Bravo"
                                        ),
                                        stop_type=StopTypeEnumeration.ONSTREET_BUS,
                                        vehicle_modes=[
                                            VehicleModeEnumeration.BUS,
                                        ]
                                    ),
                                    ScheduledStopPoint(
                                        id="mybus:SSP_003",
                                        version="any",
                                        name=MultilingualString(
                                            value="Charley Crescent"
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal("53.3000"),
                                            latitude=Decimal("0.3000")
                                        ),
                                        timing_point_status=TimingPointStatusEnumeration.TIMING_POINT,
                                        short_name=MultilingualString(
                                            value="Charley"
                                        ),
                                        stop_type=StopTypeEnumeration.ONSTREET_BUS,
                                        vehicle_modes=[
                                            VehicleModeEnumeration.BUS,
                                        ]
                                    ),
                                    ScheduledStopPoint(
                                        id="mybus:SSP_011",
                                        version="any",
                                        name=MultilingualString(
                                            value="Park Lane"
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal("53.34000"),
                                            latitude=Decimal("0.34000")
                                        ),
                                        timing_point_status=TimingPointStatusEnumeration.TIMING_POINT,
                                        short_name=MultilingualString(
                                            value="Park Lane"
                                        ),
                                        stop_type=StopTypeEnumeration.ONSTREET_BUS,
                                        vehicle_modes=[
                                            VehicleModeEnumeration.BUS,
                                        ]
                                    ),
                                    ScheduledStopPoint(
                                        id="mybus:SSP_012",
                                        version="any",
                                        name=MultilingualString(
                                            value="Hospital"
                                        ),
                                        location=LocationStructure2(
                                            longitude=Decimal("53.34000"),
                                            latitude=Decimal("0.34000")
                                        ),
                                        timing_point_status=TimingPointStatusEnumeration.TIMING_POINT,
                                        short_name=MultilingualString(
                                            value="Hospital   "
                                        ),
                                        stop_type=StopTypeEnumeration.ONSTREET_BUS,
                                        vehicle_modes=[
                                            VehicleModeEnumeration.BUS,
                                        ]
                                    ),
                                ]
                            ),
                            connections=TransfersInFrameRelStructure(
                                choice=[
                                    Connection(
                                        id="mybus:CX_25",
                                        version="any",
                                        name=MultilingualString(
                                            value="Connect at Main station"
                                        ),
                                        transfer_duration=TransferDurationStructure(
                                            default_duration=XmlDuration("PT5M")
                                        ),
                                        both_ways=True,
                                        from_value=ConnectionEndStructure(
                                            transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
                                            scheduled_stop_point_ref=ScheduledStopPointRefStructure(
                                                version="any",
                                                ref="mybus:SSP_025"
                                            )
                                        ),
                                        to=ConnectionEndStructure(
                                            transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
                                            scheduled_stop_point_ref=ScheduledStopPointRefStructure(
                                                version="any",
                                                ref="mybus:SSP_025"
                                            )
                                        )
                                    ),
                                ]
                            )
                        ),
                        TimetableFrame(
                            id="hde:TIM_23_O",
                            validity_conditions_or_valid_between=[
                                ValidityConditionsRelStructure(
                                    choice=[
                                        AvailabilityCondition(
                                            id="hde:Cnd001",
                                            version="any",
                                            description=MultilingualString(
                                                value="Sept  to March"
                                            ),
                                            from_date=XmlDateTime(2010, 11, 1, 0, 0, 0, 0, 0),
                                            to_date=XmlDateTime(2011, 3, 31, 0, 0, 0, 0, 0)
                                        ),
                                    ]
                                ),
                            ],
                            version="2",
                            name=MultilingualString(
                                value="Winter timetable for route 23 outbound"
                            ),
                            baseline_version_frame_ref=VersionRefStructure(
                                name_of_ref_class="TimetableFrame",
                                ref="hde:1"
                            ),
                            interchange_rules=InterchangeRulesInFrameRelStructure(
                                interchange_rule=[
                                    InterchangeRule(
                                        id="hde:IR_25_all_f",
                                        version="any",
                                        name=MultilingualString(
                                            value="Main Station - All  inbound"
                                        ),
                                        connection_ref=ConnectionRefStructure(
                                            version="any",
                                            ref="mybus:CX_25"
                                        ),
                                        priority=5,
                                        planned=True,
                                        guaranteed=False,
                                        advertised=True,
                                        controlled=True,
                                        maximum_wait_time=XmlDuration("PT2M"),
                                        maximum_automatic_wait_time=XmlDuration("PT2M"),
                                        standard_transfer_time=XmlDuration("PT5M"),
                                        minimum_transfer_time=XmlDuration("PT3M"),
                                        maximum_transfer_time=XmlDuration("PT8M"),
                                        control_centre_ref=ControlCentreRef(
                                            version="101",
                                            ref="hde:123"
                                        ),
                                        feeder_filter=InterchangeRuleParameterStructure(
                                            transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
                                            all_lines_or_lines_in_direction_refs_or_line_in_direction_ref=[
                                                "",
                                            ],
                                            maximum_interchange_window=XmlDuration("PT5M")
                                        )
                                    ),
                                    InterchangeRule(
                                        id="hde:IR_25_LN1_f",
                                        version="any",
                                        name=MultilingualString(
                                            value="Main Station - Line 1 inbound Special rule"
                                        ),
                                        connection_ref=ConnectionRefStructure(
                                            version="any",
                                            ref="mybus:CX_25"
                                        ),
                                        priority=1,
                                        planned=True,
                                        guaranteed=True,
                                        advertised=True,
                                        controlled=True,
                                        standard_wait_time=XmlDuration("PT3M"),
                                        maximum_wait_time=XmlDuration("PT3M"),
                                        maximum_automatic_wait_time=XmlDuration("PT1M"),
                                        control_centre_ref=ControlCentreRef(
                                            version="101",
                                            ref="hde:123"
                                        ),
                                        feeder_filter=InterchangeRuleParameterStructure(
                                            transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
                                            all_lines_or_lines_in_direction_refs_or_line_in_direction_ref=[
                                                LineInDirectionRef(
                                                    flexible_line_ref_or_line_ref=LineRef(
                                                        version="any",
                                                        ref="mybus:LN_1"
                                                    ),
                                                    direction_ref=DirectionRef(
                                                        version="any",
                                                        ref="mybus:DR_hbf"
                                                    )
                                                ),
                                            ],
                                            fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref=ScheduledStopPointRef(
                                                version="any",
                                                ref="mybus:SSP_025"
                                            ),
                                            adjacent_stop_point_ref=ScheduledStopPointRefStructure(
                                                version="any",
                                                ref="mybus:SSP_003"
                                            ),
                                            end_stop_point_ref=ScheduledStopPointRefStructure(
                                                version="any",
                                                ref="mybus:SSP_002"
                                            ),
                                            maximum_interchange_window=XmlDuration("PT4M")
                                        )
                                    ),
                                    InterchangeRule(
                                        id="hde:IR_25_all_d",
                                        version="any",
                                        name=MultilingualString(
                                            value="Main Station - All lines outboundv "
                                        ),
                                        connection_ref=ConnectionRefStructure(
                                            version="any",
                                            ref="mybus:CX_25"
                                        ),
                                        priority=5,
                                        planned=True,
                                        guaranteed=False,
                                        advertised=True,
                                        controlled=True,
                                        standard_wait_time=XmlDuration("PT2M"),
                                        maximum_wait_time=XmlDuration("PT2M"),
                                        maximum_automatic_wait_time=XmlDuration("PT2M"),
                                        standard_transfer_time=XmlDuration("PT5M"),
                                        minimum_transfer_time=XmlDuration("PT3M"),
                                        maximum_transfer_time=XmlDuration("PT8M"),
                                        control_centre_ref=ControlCentreRef(
                                            version="101",
                                            ref="hde:123"
                                        ),
                                        distributor_filter=InterchangeRuleParameterStructure(
                                            transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
                                            all_lines_or_lines_in_direction_refs_or_line_in_direction_ref=[
                                                "",
                                            ],
                                            maximum_interchange_window=XmlDuration("PT5M")
                                        )
                                    ),
                                    InterchangeRule(
                                        id="hde:IR_25_LN6_d",
                                        version="any",
                                        name=MultilingualString(
                                            value="Main Station - Line 6 outbound "
                                        ),
                                        connection_ref=ConnectionRefStructure(
                                            version="any",
                                            ref="mybus:CX_25"
                                        ),
                                        priority=5,
                                        planned=True,
                                        guaranteed=True,
                                        advertised=True,
                                        controlled=True,
                                        standard_wait_time=XmlDuration("PT4M"),
                                        maximum_wait_time=XmlDuration("PT4M"),
                                        maximum_automatic_wait_time=XmlDuration("PT4M"),
                                        standard_transfer_time=XmlDuration("PT5M"),
                                        minimum_transfer_time=XmlDuration("PT3M"),
                                        maximum_transfer_time=XmlDuration("PT8M"),
                                        control_centre_ref=ControlCentreRef(
                                            version="101",
                                            ref="hde:123"
                                        ),
                                        distributor_filter=InterchangeRuleParameterStructure(
                                            transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
                                            all_lines_or_lines_in_direction_refs_or_line_in_direction_ref=[
                                                LineInDirectionRef(
                                                    flexible_line_ref_or_line_ref=LineRef(
                                                        version="any",
                                                        ref="mybus:LN_6"
                                                    ),
                                                    direction_ref=DirectionRef(
                                                        version="any",
                                                        ref="mybus:DR_Hospital"
                                                    )
                                                ),
                                            ],
                                            fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref=ScheduledStopPointRef(
                                                version="any",
                                                ref="mybus:SSP_025"
                                            ),
                                            adjacent_stop_point_ref=ScheduledStopPointRefStructure(
                                                version="any",
                                                ref="mybus:SSP_011"
                                            ),
                                            end_stop_point_ref=ScheduledStopPointRefStructure(
                                                version="any",
                                                ref="mybus:SSP_012"
                                            ),
                                            maximum_interchange_window=XmlDuration("PT5M")
                                        )
                                    ),
                                ]
                            )
                        ),
                        ResourceFrame(
                            id="hde:RS_23_O",
                            version="2",
                            name=MultilingualString(
                                value="Resoucres"
                            ),
                            baseline_version_frame_ref=VersionRefStructure(
                                name_of_ref_class="ResourceFrame",
                                ref="hde:1"
                            ),
                            organisations=OrganisationsInFrameRelStructure(
                                choice=[
                                    Authority(
                                        id="hde:TFO",
                                        version="101",
                                        name=MultilingualString(
                                            value="Mission Central"
                                        )
                                    ),
                                ]
                            ),
                            control_centres=ControlCentresInFrameRelStructure(
                                control_centre=[
                                    ControlCentre(
                                        id="hde:123",
                                        version="101",
                                        name=MultilingualString(
                                            value="Mission Central"
                                        ),
                                        choice=AuthorityRef(
                                            version="101",
                                            ref="hde:TFO"
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
