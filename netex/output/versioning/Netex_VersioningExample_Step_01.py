from netex.models.codespace import Codespace
from netex.models.codespace_ref_structure import CodespaceRefStructure
from netex.models.codespaces_rel_structure import CodespacesRelStructure
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.general_version_frame_structure import CompositeFrame
from netex.models.general_version_frame_structure import FramesRelStructure
from netex.models.multilingual_string import MultilingualString
from netex.models.network_frame_topic_structure import NetworkFrameTopicStructure
from netex.models.participant_ref import ParticipantRef
from netex.models.publication_delivery import PublicationDelivery
from netex.models.publication_request_structure import PublicationRequestStructure
from netex.models.responsibility_set_ref_structure import ResponsibilitySetRefStructure
from netex.models.scheduled_stop_point import ScheduledStopPoint
from netex.models.scheduled_stop_points_in_frame_rel_structure import ScheduledStopPointsInFrameRelStructure
from netex.models.service_frame import ServiceFrame
from netex.models.service_frame_ref import ServiceFrameRef
from netex.models.version import Version
from netex.models.version_frame_defaults_structure import VersionFrameDefaultsStructure
from netex.models.version_status_enumeration import VersionStatusEnumeration
from netex.models.version_type_enumeration import VersionTypeEnumeration
from netex.models.versions_rel_structure import VersionsRelStructure
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration


obj = PublicationDelivery(
    publication_timestamp=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
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
                        ServiceFrameRef(
                            value='REQUEST',
                            ref='mybus:ntwkf001'
                        ),
                    ]
                ),
            ]
        )
    ),
    publication_refresh_interval=XmlDuration("P7D"),
    description=MultilingualString(
        value='Netex basic Versioning Example Step 01'
    ),
    data_objects=DataObjectsRelStructure(
        choice=[
            CompositeFrame(
                id='mybus:ntwkf001',
                version='001',
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
                    ),
                    default_responsibility_set_ref=ResponsibilitySetRefStructure(
                        value='EXTERNAL',
                        ref='mybus:RS_10'
                    )
                ),
                versions=VersionsRelStructure(
                    version_ref_or_version=[
                        Version(
                            id='mybus:ntwkf001',
                            created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                            version='002',
                            status=VersionStatusEnumeration.VERSIONED,
                            description=MultilingualString(
                                value='Version 1 of Composite Frame '
                            ),
                            version_type=VersionTypeEnumeration.BASELINE
                        ),
                    ]
                ),
                frames=FramesRelStructure(
                    common_frame=[
                        ServiceFrame(
                            id='mybus:ntwkf001@service',
                            created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                            version='001',
                            responsibility_set_ref_attribute='mybus:RS_10',
                            name=MultilingualString(
                                value='My Network  (V1) '
                            ),
                            versions=VersionsRelStructure(
                                version_ref_or_version=[
                                    Version(
                                        id='mybus:ntwkf001@service',
                                        created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                        version='001',
                                        status=VersionStatusEnumeration.VERSIONED,
                                        description=MultilingualString(
                                            value='Version 1 of Service Frame '
                                        ),
                                        version_type=VersionTypeEnumeration.BASELINE
                                    ),
                                    Version(
                                        id='mybus:SSP0001A',
                                        created=XmlDateTime(2010, 5, 17, 9, 30, 47, 0, 0),
                                        version='001',
                                        status=VersionStatusEnumeration.VERSIONED,
                                        description=MultilingualString(
                                            value='Version 1 of StopPoint SSP001A '
                                        )
                                    ),
                                ]
                            ),
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
                                ]
                            )
                        ),
                    ]
                )
            ),
        ]
    )
)
