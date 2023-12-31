from netex.models.alternative_texts_rel_structure import DayType
from netex.models.alternative_texts_rel_structure import DayTypesRelStructure
from netex.models.codespace import Codespace
from netex.models.codespace_ref_structure import CodespaceRefStructure
from netex.models.codespaces_rel_structure import CodespacesRelStructure
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.day_type_assignment import DayTypeAssignment
from netex.models.day_type_assignments_rel_structure import DayTypeAssignmentsRelStructure
from netex.models.day_type_ref import DayTypeRef
from netex.models.multilingual_string import MultilingualString
from netex.models.network_frame_topic_structure import NetworkFrameTopicStructure
from netex.models.publication_delivery import PublicationDelivery
from netex.models.publication_request_structure import PublicationRequestStructure
from netex.models.service_calendar import ServiceCalendar
from netex.models.service_calendar_frame import ServiceCalendarFrame
from netex.models.service_calendar_frame_ref import ServiceCalendarFrameRef
from netex.models.version_frame_defaults_structure import VersionFrameDefaultsStructure
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration


obj = PublicationDelivery(
    publication_timestamp=XmlDateTime(2001, 12, 17, 9, 30, 47, 0, 0),
    participant_ref='SYS001',
    publication_request=PublicationRequestStructure(
        request_timestamp=XmlDateTime(2001, 12, 17, 9, 30, 47, 0, 0),
        participant_ref='SYS002',
        topics=PublicationRequestStructure.Topics(
            network_frame_topic=[
                NetworkFrameTopicStructure(
                    choice='',
                    choice_1=[
                        ServiceCalendarFrameRef(
                            ref='noptis:9085002000100000'
                        ),
                    ]
                ),
            ]
        )
    ),
    publication_refresh_interval=XmlDuration("P7D"),
    description=MultilingualString(
        value='Noptis simple Simple service calendar  example'
    ),
    data_objects=DataObjectsRelStructure(
        choice=[
            ServiceCalendarFrame(
                id='noptis:9085002000100000',
                version='any',
                responsibility_set_ref_attribute='noptis:9010001000000000',
                codespaces=CodespacesRelStructure(
                    codespace_ref_or_codespace=[
                        Codespace(
                            id='noptis',
                            xmlns='noptis',
                            xmlns_url='http://www.noptis.org./noptis',
                            description='A Noptis Customer '
                        ),
                    ]
                ),
                frame_defaults=VersionFrameDefaultsStructure(
                    default_codespace_ref=CodespaceRefStructure(
                        ref='noptis'
                    )
                ),
                service_calendar=ServiceCalendar(
                    id='noptis:9085002000100000',
                    version='any',
                    responsibility_set_ref_attribute='noptis:9010001000000000',
                    name=MultilingualString(
                        value='Base'
                    ),
                    from_date=XmlDate(2007, 6, 17),
                    to_date=XmlDate(2008, 6, 14),
                    day_types=DayTypesRelStructure(
                        day_type_ref_or_day_type=[
                            DayType(
                                id='noptis:9086002000100001',
                                version='any'
                            ),
                            DayType(
                                id='noptis:9086002000100002',
                                version='any'
                            ),
                        ]
                    ),
                    day_type_assignments=DayTypeAssignmentsRelStructure(
                        day_type_assignment=[
                            DayTypeAssignment(
                                id='noptis:DayTypeAssignment:2007-06-17',
                                version='any',
                                order=1,
                                choice=XmlDate(2007, 6, 17),
                                day_type_ref=DayTypeRef(
                                    version='any',
                                    ref='noptis:9086002000100001'
                                )
                            ),
                            DayTypeAssignment(
                                id='noptis:DayTypeAssignment:2007-06-24',
                                version='any',
                                order=1,
                                choice=XmlDate(2007, 6, 24),
                                day_type_ref=DayTypeRef(
                                    version='any',
                                    ref='noptis:9086002000100001'
                                )
                            ),
                            DayTypeAssignment(
                                id='noptis:DayTypeAssignment:2007-06-18',
                                version='any',
                                order=1,
                                choice=XmlDate(2007, 6, 18),
                                day_type_ref=DayTypeRef(
                                    version='any',
                                    ref='noptis:9086002000100002'
                                )
                            ),
                            DayTypeAssignment(
                                id='noptis:DayTypeAssignment:2007-06-25',
                                version='any',
                                order=1,
                                choice=XmlDate(2007, 6, 25),
                                day_type_ref=DayTypeRef(
                                    version='any',
                                    ref='noptis:9086002000100002'
                                )
                            ),
                        ]
                    )
                )
            ),
        ]
    )
)
