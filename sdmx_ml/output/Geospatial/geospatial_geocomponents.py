from sdmx_ml.models.attribute_2 import Attribute2
from sdmx_ml.models.attribute_list import AttributeList
from sdmx_ml.models.attribute_relationship_type import AttributeRelationshipType
from sdmx_ml.models.concept_scheme_type import ConceptSchemeType
from sdmx_ml.models.concept_schemes_type import ConceptSchemesType
from sdmx_ml.models.data_structure_components import DataStructureComponents
from sdmx_ml.models.data_structure_type import DataStructureType
from sdmx_ml.models.data_structures_type import DataStructuresType
from sdmx_ml.models.data_type import DataType
from sdmx_ml.models.description import Description
from sdmx_ml.models.dimension import Dimension
from sdmx_ml.models.dimension_list import DimensionList
from sdmx_ml.models.item_type import Concept
from sdmx_ml.models.measure import Measure
from sdmx_ml.models.measure_list import MeasureList
from sdmx_ml.models.name import Name
from sdmx_ml.models.optional_local_dimension_reference_type import OptionalLocalDimensionReferenceType
from sdmx_ml.models.party_type import PartyType
from sdmx_ml.models.representation_type import RepresentationType
from sdmx_ml.models.sender_type import SenderType
from sdmx_ml.models.structure import Structure
from sdmx_ml.models.structure_header_type import StructureHeaderType
from sdmx_ml.models.structures_type import StructuresType
from sdmx_ml.models.text_format_type import TextFormatType
from sdmx_ml.models.time_dimension import TimeDimension
from sdmx_ml.models.time_dimension_representation_type import TimeDimensionRepresentationType
from xsdata.models.datatype import XmlDateTime


obj = Structure(
    header=StructureHeaderType(
        id='IREF002364',
        prepared=XmlDateTime(2021, 3, 10, 18, 17, 16, 0, 0),
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
        concept_schemes=ConceptSchemesType(
            concept_scheme=[
                ConceptSchemeType(
                    id='CS_EXAMPLE',
                    urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.ConceptScheme=EXAMPLE:CS_EXAMPLE(1.0)',
                    name=[
                        Name(
                            value='Example concepts'
                        ),
                    ],
                    description=[
                        Description(
                            value='Example concepts'
                        ),
                    ],
                    version='1.0',
                    agency_id='EXAMPLE',
                    choice=[
                        Concept(
                            id='ACTIVITY',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=EXAMPLE:CS_EXAMPLE(1.0).ACTIVITY',
                            name=[
                                Name(
                                    value='Labour force activity'
                                ),
                            ]
                        ),
                        Concept(
                            id='INDICATOR',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=EXAMPLE:CS_EXAMPLE(1.0).INDICATOR',
                            name=[
                                Name(
                                    value='Labour force indicator'
                                ),
                            ]
                        ),
                        Concept(
                            id='AREA',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=EXAMPLE:CS_EXAMPLE(1.0).AREA',
                            name=[
                                Name(
                                    value='Geographical area'
                                ),
                            ]
                        ),
                    ]
                ),
            ]
        ),
        data_structures=DataStructuresType(
            data_structure=[
                DataStructureType(
                    id='DSD_GEO_EXAMPLE',
                    urn='urn:sdmx:org.sdmx.infomodel.datastructure.DataStructure=EXAMPLE:DSD_GEO_EXAMPLE(1.0)',
                    name=[
                        Name(
                            value='Geographic coordinates example'
                        ),
                    ],
                    version='1.0',
                    agency_id='EXAMPLE',
                    metadata_structure_components_or_data_structure_components=DataStructureComponents(
                        dimension_list=DimensionList(
                            urn='urn:sdmx:org.sdmx.infomodel.datastructure.DimensionDescriptor=EXAMPLE:DSD_GEO_EXAMPLE(1.0).DimensionDescriptor',
                            dimension=[
                                Dimension(
                                    id='INDICATOR',
                                    urn='urn:sdmx:org.sdmx.infomodel.datastructure.Dimension=EXAMPLE:DSD_GEO_EXAMPLE(1.0).INDICATOR',
                                    concept_identity='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=EXAMPLE:CS_EXAMPLE(1.0).INDICATOR',
                                    local_representation=RepresentationType(
                                        text_format_or_enumeration_or_enumeration_format=[
                                            'urn:sdmx:org.sdmx.infomodel.codelist.Codelist=EXAMPLE:CL_INDICATOR(1.0)',
                                        ]
                                    ),
                                    position=1
                                ),
                            ],
                            time_dimension=TimeDimension(
                                urn='urn:sdmx:org.sdmx.infomodel.datastructure.TimeDimension=EXAMPLE:DSD_GEO_EXAMPLE(1.0).TIME_PERIOD',
                                concept_identity='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=SDMX:CROSS_DOMAIN_CONCEPTS(1.0).TIME_PERIOD',
                                local_representation=TimeDimensionRepresentationType(
                                    text_format_or_enumeration_or_enumeration_format=[
                                        TextFormatType(
                                            text_type=DataType.OBSERVATIONAL_TIME_PERIOD
                                        ),
                                    ]
                                )
                            )
                        ),
                        attribute_list=AttributeList(
                            urn='urn:sdmx:org.sdmx.infomodel.datastructure.AttributeDescriptor=EXAMPLE:DSD_GEO_EXAMPLE(1.0).AttributeDescriptor',
                            attribute_or_metadata_attribute_usage=[
                                Attribute2(
                                    id='AREA',
                                    urn='urn:sdmx:org.sdmx.infomodel.datastructure.DataAttribute=EXAMPLE:DSD_GEO_EXAMPLE(1.0).AREA',
                                    concept_identity='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=EXAMPLE:CS_EXAMPLE(1.0).AREA',
                                    local_representation=RepresentationType(
                                        text_format_or_enumeration_or_enumeration_format=[
                                            TextFormatType(
                                                text_type=DataType.GEOSPATIAL_INFORMATION,
                                                is_sequence=False
                                            ),
                                        ],
                                        min_occurs=0,
                                        max_occurs=1
                                    ),
                                    concept_role=[
                                        'urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=SDMX:SDMX_CONCEPT_ROLES(1+.0.0).GEO',
                                    ],
                                    attribute_relationship=AttributeRelationshipType(
                                        choice=[
                                            OptionalLocalDimensionReferenceType(
                                                value='INDICATOR'
                                            ),
                                        ]
                                    )
                                ),
                            ]
                        ),
                        measure_list=MeasureList(
                            urn='urn:sdmx:org.sdmx.infomodel.datastructure.MeasureDescriptor=EXAMPLE:DSD_GEO_EXAMPLE(1.0).MeasureDescriptor',
                            measure=[
                                Measure(
                                    id='OBS_VALUE',
                                    urn='urn:sdmx:org.sdmx.infomodel.datastructure.Measure=EXAMPLE:DSD_GEO_EXAMPLE(1.0).OBS_VALUE',
                                    concept_identity='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=SDMX:CROSS_DOMAIN_CONCEPTS(1.0).OBS_VALUE'
                                ),
                            ]
                        )
                    )
                ),
            ]
        )
    )
)
