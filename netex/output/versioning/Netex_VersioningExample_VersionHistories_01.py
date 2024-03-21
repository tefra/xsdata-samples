from decimal import Decimal
from netex.models.codespace import Codespace
from netex.models.codespace_ref_structure import CodespaceRefStructure
from netex.models.codespaces_rel_structure import CodespacesRelStructure
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.day_of_week_enumeration import DayOfWeekEnumeration
from netex.models.day_type_ref import DayTypeRef
from netex.models.day_types_in_frame_rel_structure import DayTypesInFrameRelStructure
from netex.models.entity_in_version_structure import DayType
from netex.models.general_version_frame_structure import CompositeFrame
from netex.models.general_version_frame_structure import FramesRelStructure
from netex.models.holiday_type_enumeration import HolidayTypeEnumeration
from netex.models.modification_enumeration import ModificationEnumeration
from netex.models.multilingual_string import MultilingualString
from netex.models.network_filter_by_value_structure import NetworkFilterByValueStructure
from netex.models.network_frame_topic_structure import NetworkFrameTopicStructure
from netex.models.object_filter_by_value_structure import ObjectFilterByValueStructure
from netex.models.participant_ref import ParticipantRef
from netex.models.private_code import PrivateCode
from netex.models.properties_of_day_rel_structure import PropertiesOfDayRelStructure
from netex.models.property_of_day import PropertyOfDay
from netex.models.publication_delivery import PublicationDelivery
from netex.models.publication_request_structure import PublicationRequestStructure
from netex.models.scheduled_stop_point import ScheduledStopPoint
from netex.models.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.models.scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from netex.models.scheduled_stop_points_in_frame_rel_structure import ScheduledStopPointsInFrameRelStructure
from netex.models.service_calendar_frame import ServiceCalendarFrame
from netex.models.service_frame import ServiceFrame
from netex.models.service_link import ServiceLink
from netex.models.service_link_ref import ServiceLinkRef
from netex.models.service_links_in_frame_rel_structure import ServiceLinksInFrameRelStructure
from netex.models.service_pattern import ServicePattern
from netex.models.service_pattern_ref import ServicePatternRef
from netex.models.service_patterns_in_frame_rel_structure import ServicePatternsInFrameRelStructure
from netex.models.stop_point_in_journey_pattern import StopPointInJourneyPattern
from netex.models.stop_points_in_journey_pattern_rel_structure import StopPointsInJourneyPatternRelStructure
from netex.models.version_frame_defaults_structure import VersionFrameDefaultsStructure
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration


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
                            object_references=ObjectFilterByValueStructure.ObjectReferences(
                                choice=[
                                    ScheduledStopPointRef(
                                        value='REQUEST',
                                        ref='mybus:SSP0001A'
                                    ),
                                    ScheduledStopPointRef(
                                        value='REQUEST',
                                        ref='mybus:SSP0002B'
                                    ),
                                    ScheduledStopPointRef(
                                        value='REQUEST',
                                        ref='mybus:SSP0003C'
                                    ),
                                    ServiceLinkRef(
                                        value='REQUEST',
                                        ref='mybu:SL_AtoB01'
                                    ),
                                    ServiceLinkRef(
                                        value='REQUEST',
                                        ref='mybu:SL_BtoC01'
                                    ),
                                    ServiceLinkRef(
                                        value='REQUEST',
                                        ref='mybu:SL_BtoA01'
                                    ),
                                    ServicePatternRef(
                                        value='REQUEST',
                                        ref='mybus:SP_001'
                                    ),
                                    DayTypeRef(
                                        value='REQUEST',
                                        ref='mybus:DT001_MF'
                                    ),
                                ]
                            )
                        ),
                    ]
                ),
            ]
        )
    ),
    publication_refresh_interval=XmlDuration("P1Y2M3DT10H30M0S"),
    description=MultilingualString(
        value='Example of simple network, explicit request '
    ),
    data_objects=DataObjectsRelStructure(
        choice=[
            CompositeFrame(
                id='mybus:CF1',
                version='any',
                codespaces=CodespacesRelStructure(
                    codespace_ref_or_codespace=[
                        Codespace(
                            id='mybus',
                            xmlns='mybus',
                            xmlns_url='http://www.mybuses.eu/stuff',
                            description='My buses'
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
                            id='mybus:SF1',
                            version='any',
                            scheduled_stop_points=ScheduledStopPointsInFrameRelStructure(
                                scheduled_stop_point=[
                                    ScheduledStopPoint(
                                        id='mybus:SSP0001A',
                                        created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                        version='001',
                                        responsibility_set_ref_attribute='mybus:RS_10',
                                        name=MultilingualString(
                                            value='Haltstelle A'
                                        ),
                                        description=MultilingualString(
                                            value='Version one of stop A'
                                        )
                                    ),
                                    ScheduledStopPoint(
                                        id='mybus:SSP0001A',
                                        created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                        changed=XmlDateTime(2010, 5, 18, 9, 30, 47, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='002',
                                        derived_from_version_ref_attribute='001',
                                        responsibility_set_ref_attribute='mybus:RS_10',
                                        name=MultilingualString(
                                            value='Haltstelle A - Museum'
                                        ),
                                        description=MultilingualString(
                                            value='Version two of stop A. Name is Changed and code addded'
                                        ),
                                        private_code=PrivateCode(
                                            value='mycodeA'
                                        )
                                    ),
                                    ScheduledStopPoint(
                                        id='mybus:SSP0002B',
                                        created=XmlDateTime(2010, 5, 18, 9, 30, 47, 0, 0),
                                        version='001',
                                        responsibility_set_ref_attribute='mybus:RS_10',
                                        name=MultilingualString(
                                            value='Haltstelle B'
                                        ),
                                        description=MultilingualString(
                                            value='Version one of stop B'
                                        )
                                    ),
                                    ScheduledStopPoint(
                                        id='mybus:SSP0002B',
                                        created=XmlDateTime(2010, 5, 18, 9, 30, 47, 0, 0),
                                        changed=XmlDateTime(2010, 6, 18, 9, 30, 47, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='002',
                                        responsibility_set_ref_attribute='mybus:RS_10',
                                        name=MultilingualString(
                                            value='Haltstelle B'
                                        ),
                                        description=MultilingualString(
                                            value='Version two of stop B'
                                        ),
                                        private_code=PrivateCode(
                                            value='mycodeB'
                                        )
                                    ),
                                    ScheduledStopPoint(
                                        id='mybus:SSP0003C',
                                        created=XmlDateTime(2010, 5, 21, 10, 30, 51, 0, 0),
                                        version='001',
                                        responsibility_set_ref_attribute='mybus:RS_10',
                                        name=MultilingualString(
                                            value='Haltstelle C'
                                        ),
                                        description=MultilingualString(
                                            value='Version one of stop C'
                                        )
                                    ),
                                ]
                            ),
                            service_links=ServiceLinksInFrameRelStructure(
                                service_link=[
                                    ServiceLink(
                                        id='mybu:SL_AtoB01',
                                        created=XmlDateTime(2010, 5, 19, 10, 30, 47, 0, 0),
                                        version='001',
                                        responsibility_set_ref_attribute='mybus:RS_10',
                                        name=MultilingualString(
                                            value='Version one of Link from A to B'
                                        ),
                                        distance=Decimal('1.01'),
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            version='001',
                                            ref='mybus:SSP0001A'
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            version='001',
                                            ref='mybus:SSP0002B'
                                        )
                                    ),
                                    ServiceLink(
                                        id='mybu:SL_AtoB01',
                                        created=XmlDateTime(2010, 5, 19, 10, 30, 47, 0, 0),
                                        changed=XmlDateTime(2010, 5, 19, 10, 30, 47, 0, 0),
                                        modification=ModificationEnumeration.REVISE,
                                        version='002',
                                        responsibility_set_ref_attribute='mybus:RS_10',
                                        name=MultilingualString(
                                            value='Version one of Link from A to B'
                                        ),
                                        distance=Decimal('1.12'),
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            version='002',
                                            ref='mybus:SSP0001A'
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            version='002',
                                            ref='mybus:SSP0002B'
                                        )
                                    ),
                                    ServiceLink(
                                        id='mybu:SL_BtoC01',
                                        created=XmlDateTime(2010, 5, 21, 10, 30, 51, 0, 0),
                                        version='001',
                                        responsibility_set_ref_attribute='mybus:RS_10',
                                        name=MultilingualString(
                                            value='Version one of Link from B to C'
                                        ),
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            version='002',
                                            ref='mybus:SSP0002B'
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            version='001',
                                            ref='mybus:SSP0003C'
                                        )
                                    ),
                                    ServiceLink(
                                        id='mybu:SL_BtoA01',
                                        created=XmlDateTime(2010, 5, 19, 10, 30, 51, 0, 0),
                                        changed=XmlDateTime(2010, 5, 21, 10, 30, 51, 0, 0),
                                        modification=ModificationEnumeration.DELETE,
                                        version='002',
                                        responsibility_set_ref_attribute='mybus:RS_10',
                                        name=MultilingualString(
                                            value='Version two - deleteing  Link from B to A'
                                        ),
                                        from_point_ref=ScheduledStopPointRefStructure(
                                            version='002',
                                            ref='mybus:SSP0002B'
                                        ),
                                        to_point_ref=ScheduledStopPointRefStructure(
                                            version='002',
                                            ref='mybus:SSP0001A'
                                        )
                                    ),
                                ]
                            ),
                            service_patterns=ServicePatternsInFrameRelStructure(
                                service_pattern_or_journey_pattern_view=[
                                    ServicePattern(
                                        id='mybus:SP_001',
                                        created=XmlDateTime(2010, 5, 21, 10, 30, 51, 0, 0),
                                        version='001',
                                        name=MultilingualString(
                                            value='From A to C, version 1'
                                        ),
                                        points_in_sequence=StopPointsInJourneyPatternRelStructure(
                                            stop_point_in_journey_pattern=[
                                                StopPointInJourneyPattern(
                                                    id='mybus:P_001_01',
                                                    version='001',
                                                    order=1,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='002',
                                                        ref='mybus:SSP0001A'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='mybus:P_001_02',
                                                    version='001',
                                                    order=2,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='002',
                                                        ref='mybus:SSP0002B'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='mybus:P_001_03',
                                                    version='001',
                                                    order=3,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='001',
                                                        ref='mybus:SSP0003C'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                    ServicePattern(
                                        id='mybus:SP_001',
                                        created=XmlDateTime(2010, 5, 21, 10, 30, 51, 0, 0),
                                        changed=XmlDateTime(2010, 5, 22, 10, 30, 51, 0, 0),
                                        version='002',
                                        name=MultilingualString(
                                            value='From A to D, version 2'
                                        ),
                                        points_in_sequence=StopPointsInJourneyPatternRelStructure(
                                            stop_point_in_journey_pattern=[
                                                StopPointInJourneyPattern(
                                                    id='mybus:P_001_01',
                                                    version='002',
                                                    order=1,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='001',
                                                        ref='mybus:SSP0001A'
                                                    )
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='mybus:P_001_02',
                                                    version='002',
                                                    order=2,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='002',
                                                        ref='mybus:SSP0002B'
                                                    ),
                                                    for_alighting=True,
                                                    for_boarding=False
                                                ),
                                                StopPointInJourneyPattern(
                                                    id='mybus:P_001_03',
                                                    version='002',
                                                    order=3,
                                                    scheduled_stop_point_ref=ScheduledStopPointRef(
                                                        version='001',
                                                        ref='mybus:SSP0003C'
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ),
                        ServiceCalendarFrame(
                            id='mybus:SCF1',
                            version='any',
                            day_types=DayTypesInFrameRelStructure(
                                day_type=[
                                    DayType(
                                        id='mybus:DT001_MF',
                                        created=XmlDateTime(2010, 5, 18, 10, 30, 47, 0, 0),
                                        version='001',
                                        responsibility_set_ref_attribute='mybus:RS_10',
                                        name=MultilingualString(
                                            value='Monday to Friday'
                                        ),
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
