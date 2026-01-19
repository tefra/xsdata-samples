from sdmx_ml.models.constraint_attachment_type import ConstraintAttachmentType
from sdmx_ml.models.member_selection_type import MemberSelectionType
from sdmx_ml.models.metadata_constraint_type import MetadataConstraintType
from sdmx_ml.models.metadata_constraints_type import MetadataConstraintsType
from sdmx_ml.models.metadata_target_region_type import MetadataTargetRegionType
from sdmx_ml.models.name import Name
from sdmx_ml.models.party_type import PartyType
from sdmx_ml.models.sender_type import SenderType
from sdmx_ml.models.simple_component_value_type import SimpleComponentValueType
from sdmx_ml.models.structure import Structure
from sdmx_ml.models.structure_header_type import StructureHeaderType
from sdmx_ml.models.structures_type import StructuresType
from xsdata.models.datatype import XmlDateTime


obj = Structure(
    header=StructureHeaderType(
        id='IREF583870',
        prepared=XmlDateTime(2024, 7, 30, 16, 53, 5, 0, 0),
        sender=SenderType(
            id='Unknown'
        ),
        receiver=[
            PartyType(
                id='not_supplied'
            ),
        ]
    ),
    structures=StructuresType(
        metadata_constraints=MetadataConstraintsType(
            metadata_constraint=[
                MetadataConstraintType(
                    id='DEMO_CONSTRAINT',
                    urn='urn:sdmx:org.sdmx.infomodel.registry.MetadataConstraint=DEMO:DEMO_CONSTRAINT(1.0)',
                    name=[
                        Name(
                            value='Allowed data constraints for the EXR dataflow.'
                        ),
                    ],
                    version='1.0',
                    agency_id='DEMO',
                    constraint_attachment=ConstraintAttachmentType(
                        choice=[
                            ConstraintAttachmentType.Metadataflow(
                                value='urn:sdmx:org.sdmx.infomodel.metadatastructure.Metadataflow=ECB:EXR(1.0)'
                            ),
                        ]
                    ),
                    metadata_target_region=[
                        MetadataTargetRegionType(
                            component=[
                                MemberSelectionType(
                                    value_or_time_range=[
                                        SimpleComponentValueType(
                                            value='Allowed_Value_1'
                                        ),
                                        SimpleComponentValueType(
                                            value='Allowed_Value_2'
                                        ),
                                        SimpleComponentValueType(
                                            value='Allowed_Value_3'
                                        ),
                                    ],
                                    id='METADATA_ATT1'
                                ),
                                MemberSelectionType(
                                    value_or_time_range=[
                                        SimpleComponentValueType(
                                            value='Allowed_SubValue_1'
                                        ),
                                    ],
                                    id='METADATA_ATT1.SUB_ATT1'
                                ),
                            ]
                        ),
                    ]
                ),
            ]
        )
    )
)
