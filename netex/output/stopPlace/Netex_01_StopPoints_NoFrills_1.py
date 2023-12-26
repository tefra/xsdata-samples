from decimal import Decimal
from netex.models.codespace import Codespace
from netex.models.codespace_ref_structure import CodespaceRefStructure
from netex.models.codespaces_rel_structure import CodespacesRelStructure
from netex.models.data_objects_rel_structure import DataObjectsRelStructure
from netex.models.location_structure_2 import LocationStructure2
from netex.models.multilingual_string import MultilingualString
from netex.models.publication_delivery import PublicationDelivery
from netex.models.scheduled_stop_point import ScheduledStopPoint
from netex.models.scheduled_stop_points_in_frame_rel_structure import ScheduledStopPointsInFrameRelStructure
from netex.models.service_frame import ServiceFrame
from netex.models.vehicle_mode_enumeration import VehicleModeEnumeration
from netex.models.version_frame_defaults_structure import VersionFrameDefaultsStructure
from xsdata.models.datatype import XmlDateTime


obj = PublicationDelivery(
    publication_timestamp=XmlDateTime(2001, 12, 17, 9, 30, 47, 0, 0),
    participant_ref='SYS001',
    data_objects=DataObjectsRelStructure(
        choice=[
            ServiceFrame(
                id='SVF004',
                version='any',
                codespaces=CodespacesRelStructure(
                    codespace_ref_or_codespace=[
                        Codespace(
                            id='mybus',
                            xmlns='mybus',
                            xmlns_url='http://www.mybus.fr/',
                            description='My buses'
                        ),
                    ]
                ),
                frame_defaults=VersionFrameDefaultsStructure(
                    default_codespace_ref=CodespaceRefStructure(
                        ref='mybus'
                    )
                ),
                scheduled_stop_points=ScheduledStopPointsInFrameRelStructure(
                    scheduled_stop_point=[
                        ScheduledStopPoint(
                            id='SSP0042A',
                            created=XmlDateTime(2000, 12, 17, 9, 30, 47, 0, 0),
                            changed=XmlDateTime(2002, 12, 17, 9, 30, 47, 0, 0),
                            version='032',
                            name=MultilingualString(
                                value='Poste, St Jean'
                            ),
                            location=LocationStructure2(
                                longitude=Decimal('-0.2071397147'),
                                latitude=Decimal('51.4217482061')
                            ),
                            vehicle_modes=[
                                VehicleModeEnumeration.BUS,
                            ]
                        ),
                        ScheduledStopPoint(
                            id='SNCF0047',
                            created=XmlDateTime(2000, 12, 17, 11, 30, 47, 0, 0),
                            changed=XmlDateTime(2002, 12, 17, 9, 32, 47, 0, 0),
                            version='032',
                            name=MultilingualString(
                                value='Gare, St Jean'
                            ),
                            location=LocationStructure2(
                                longitude=Decimal('-0.2071397153'),
                                latitude=Decimal('51.4217482054')
                            ),
                            vehicle_modes=[
                                VehicleModeEnumeration.RAIL,
                            ]
                        ),
                    ]
                )
            ),
        ]
    )
)
