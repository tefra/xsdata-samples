from sdmx_ml.models.agency_scheme_type import AgencySchemeType
from sdmx_ml.models.agency_schemes_type import AgencySchemesType
from sdmx_ml.models.codelist_extension_type import CodelistExtensionType
from sdmx_ml.models.codelist_type import CodelistType
from sdmx_ml.models.codelists_type import CodelistsType
from sdmx_ml.models.concept_scheme_type import ConceptSchemeType
from sdmx_ml.models.concept_schemes_type import ConceptSchemesType
from sdmx_ml.models.constraint_attachment_type import ConstraintAttachmentType
from sdmx_ml.models.contact_type_1 import ContactType1
from sdmx_ml.models.cube_region_type import CubeRegionType
from sdmx_ml.models.data_constraint_type import DataConstraintType
from sdmx_ml.models.data_constraints_type import DataConstraintsType
from sdmx_ml.models.data_structure_components import DataStructureComponents
from sdmx_ml.models.data_structure_type import DataStructureType
from sdmx_ml.models.data_structures_type import DataStructuresType
from sdmx_ml.models.dataflow_type import DataflowType
from sdmx_ml.models.dataflows_type import DataflowsType
from sdmx_ml.models.description import Description
from sdmx_ml.models.dimension import Dimension
from sdmx_ml.models.dimension_list import DimensionList
from sdmx_ml.models.item_type import Agency
from sdmx_ml.models.item_type import Concept
from sdmx_ml.models.measure import Measure
from sdmx_ml.models.measure_list import MeasureList
from sdmx_ml.models.member_selection_type import MemberSelectionType
from sdmx_ml.models.name import Name
from sdmx_ml.models.party_type import PartyType
from sdmx_ml.models.representation_type import RepresentationType
from sdmx_ml.models.sender_type import SenderType
from sdmx_ml.models.simple_component_value_type import SimpleComponentValueType
from sdmx_ml.models.structure import Structure
from sdmx_ml.models.structure_header_type import StructureHeaderType
from sdmx_ml.models.structures_type import StructuresType
from sdmx_ml.models.text_type import TextType
from sdmx_ml.models.time_dimension import TimeDimension
from sdmx_ml.models.time_dimension_representation_type import TimeDimensionRepresentationType
from sdmx_ml.models.time_text_format_type import TimeTextFormatType
from xsdata.models.datatype import XmlDateTime


obj = Structure(
    header=StructureHeaderType(
        id='IREF953220',
        prepared=XmlDateTime(2021, 3, 10, 16, 55, 29, 0, 0),
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
        agency_schemes=AgencySchemesType(
            agency_scheme=[
                AgencySchemeType(
                    urn='urn:sdmx:org.sdmx.infomodel.base.AgencyScheme=SDMX:AGENCIES(1.0)',
                    name=[
                        Name(
                            value='SDMX Agency Scheme'
                        ),
                    ],
                    agency_id='SDMX',
                    choice_1=[
                        Agency(
                            id='SDMX',
                            urn='urn:sdmx:org.sdmx.infomodel.base.Agency=SDMX:AGENCIES(1.0).SDMX',
                            name=[
                                Name(
                                    value='SDMX'
                                ),
                            ],
                            description=[
                                Description(
                                    value='SDMX is an initiative to foster standards for the exchange of statistical information. It is sponsored by the Bank for International Settlements (BIS), the European Central Bank (ECB), the Statistical Office of the European Union (Eurostat), the International Monetary Fund (IMF), the Organization for Economic Co-Operation and Development (OECD), the United Nations (UN) and the World Bank.'
                                ),
                            ],
                            contact=[
                                ContactType1(
                                    name=[
                                        Name(
                                            value='SDMX Secretariat'
                                        ),
                                    ],
                                    department=[
                                        TextType(
                                            value='SDMX Secretariat'
                                        ),
                                    ],
                                    role=[
                                        TextType(
                                            value='Single entry point for external inquiries'
                                        ),
                                    ],
                                    choice=[
                                        ContactType1.Uri(
                                            value='http://sdmx.org'
                                        ),
                                        ContactType1.Email(
                                            value='secretariat@sdmx.org'
                                        ),
                                    ]
                                ),
                            ]
                        ),
                        Agency(
                            id='EXAMPLE',
                            urn='urn:sdmx:org.sdmx.infomodel.base.Agency=SDMX:AGENCIES(1.0).EXAMPLE',
                            name=[
                                Name(
                                    value='Example Agency'
                                ),
                            ]
                        ),
                    ]
                ),
            ]
        ),
        codelists=CodelistsType(
            codelist=[
                CodelistType(
                    id='CL_ACTIVITY',
                    urn='urn:sdmx:org.sdmx.infomodel.codelist.Codelist=EXAMPLE:CL_ACTIVITY(1.0)',
                    name=[
                        Name(
                            value='Activity'
                        ),
                    ],
                    description=[
                        Description(
                            value='Activity'
                        ),
                    ],
                    version='1.0',
                    agency_id='EXAMPLE',
                    codelist_extension=[
                        CodelistExtensionType(
                            codelist='urn:sdmx:org.sdmx.infomodel.codelist.Codelist=SDMX:CL_ACTIVITY_NACE2(1.0)',
                            prefix='NACE2_'
                        ),
                        CodelistExtensionType(
                            codelist='urn:sdmx:org.sdmx.infomodel.codelist.Codelist=SDMX:CL_ACTIVITY_ISIC4(1.0)',
                            prefix='ISIC4_'
                        ),
                    ]
                ),
            ]
        ),
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
                            id='TIME_PERIOD',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=EXAMPLE:CS_EXAMPLE(1.0).TIME_PERIOD',
                            name=[
                                Name(
                                    value='Time period or range'
                                ),
                            ]
                        ),
                        Concept(
                            id='OBS_VALUE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=EXAMPLE:CS_EXAMPLE(1.0).OBS_VALUE',
                            name=[
                                Name(
                                    value='Observation value'
                                ),
                            ]
                        ),
                    ]
                ),
            ]
        ),
        data_constraints=DataConstraintsType(
            data_constraint=[
                DataConstraintType(
                    id='ISIC_CONSTRAINT',
                    urn='urn:sdmx:org.sdmx.infomodel.registry.DataConstraint=EXAMPLE:ISIC_CONSTRAINT(1.0)',
                    name=[
                        Name(
                            value='ISIC Constraint'
                        ),
                    ],
                    description=[
                        Description(
                            value='ISIC Constraint'
                        ),
                    ],
                    version='1.0',
                    agency_id='EXAMPLE',
                    constraint_attachment=ConstraintAttachmentType(
                        choice=[
                            ConstraintAttachmentType.Dataflow(
                                value='urn:sdmx:org.sdmx.infomodel.datastructure.Dataflow=EXAMPLE:LABOUR_ISIC(1.0)'
                            ),
                        ]
                    ),
                    cube_region=[
                        CubeRegionType(
                            key_value=[
                                MemberSelectionType(
                                    value_or_time_range=[
                                        SimpleComponentValueType(
                                            value='ISIC4_%'
                                        ),
                                    ],
                                    id='ACTIVITY'
                                ),
                            ]
                        ),
                    ]
                ),
                DataConstraintType(
                    id='NACE_CONSTRAINT',
                    urn='urn:sdmx:org.sdmx.infomodel.registry.DataConstraint=EXAMPLE:NACE_CONSTRAINT(1.0)',
                    name=[
                        Name(
                            value='NACE Constraint'
                        ),
                    ],
                    description=[
                        Description(
                            value='NACE Constraint'
                        ),
                    ],
                    version='1.0',
                    agency_id='EXAMPLE',
                    constraint_attachment=ConstraintAttachmentType(
                        choice=[
                            ConstraintAttachmentType.Dataflow(
                                value='urn:sdmx:org.sdmx.infomodel.datastructure.Dataflow=EXAMPLE:LABOUR_NACE(1.0)'
                            ),
                        ]
                    ),
                    cube_region=[
                        CubeRegionType(
                            key_value=[
                                MemberSelectionType(
                                    value_or_time_range=[
                                        SimpleComponentValueType(
                                            value='NACE2_%'
                                        ),
                                    ],
                                    id='ACTIVITY'
                                ),
                            ]
                        ),
                    ]
                ),
            ]
        ),
        dataflows=DataflowsType(
            dataflow=[
                DataflowType(
                    id='LABOUR_ISIC',
                    urn='urn:sdmx:org.sdmx.infomodel.datastructure.Dataflow=EXAMPLE:LABOUR_ISIC(1.0)',
                    name=[
                        Name(
                            value='Labour with ISIC4 activity coding'
                        ),
                    ],
                    description=[
                        Description(
                            value='Labour with ISIC4 activity coding'
                        ),
                    ],
                    version='1.0',
                    agency_id='EXAMPLE',
                    structure='urn:sdmx:org.sdmx.infomodel.datastructure.DataStructure=EXAMPLE:LABOUR(1.0.0)'
                ),
                DataflowType(
                    id='LABOUR_NACE',
                    urn='urn:sdmx:org.sdmx.infomodel.datastructure.Dataflow=EXAMPLE:LABOUR_NACE(1.0)',
                    name=[
                        Name(
                            value='Labour with NACE2 activity coding'
                        ),
                    ],
                    description=[
                        Description(
                            value='Labour with NACE2 activity coding'
                        ),
                    ],
                    version='1.0',
                    agency_id='EXAMPLE',
                    structure='urn:sdmx:org.sdmx.infomodel.datastructure.DataStructure=EXAMPLE:LABOUR(1.0.0)'
                ),
            ]
        ),
        data_structures=DataStructuresType(
            data_structure=[
                DataStructureType(
                    id='LABOUR',
                    urn='urn:sdmx:org.sdmx.infomodel.datastructure.DataStructure=EXAMPLE:LABOUR(1.0)',
                    name=[
                        Name(
                            value='Labour'
                        ),
                    ],
                    description=[
                        Description(
                            value='Labour statistics'
                        ),
                    ],
                    version='1.0',
                    agency_id='EXAMPLE',
                    metadata_structure_components_or_data_structure_components=DataStructureComponents(
                        dimension_list=DimensionList(
                            urn='urn:sdmx:org.sdmx.infomodel.datastructure.DimensionDescriptor=EXAMPLE:LABOUR(1.0).DimensionDescriptor',
                            dimension=[
                                Dimension(
                                    id='INDICATOR',
                                    urn='urn:sdmx:org.sdmx.infomodel.datastructure.Dimension=EXAMPLE:LABOUR(1.0).INDICATOR',
                                    concept_identity='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=EXAMPLE:CS_EXAMPLE(1.0).INDICATOR',
                                    position=1
                                ),
                                Dimension(
                                    id='ACTIVITY',
                                    urn='urn:sdmx:org.sdmx.infomodel.datastructure.Dimension=EXAMPLE:LABOUR(1.0).ACTIVITY',
                                    concept_identity='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=EXAMPLE:CS_EXAMPLE(1.0).ACTIVITY',
                                    local_representation=RepresentationType(
                                        text_format_or_enumeration_or_enumeration_format=[
                                            'urn:sdmx:org.sdmx.infomodel.codelist.Codelist=EXAMPLE:CL_ACTIVITY(1.0)',
                                        ]
                                    ),
                                    position=2
                                ),
                            ],
                            time_dimension=TimeDimension(
                                urn='urn:sdmx:org.sdmx.infomodel.datastructure.TimeDimension=EXAMPLE:LABOUR(1.0).TIME_PERIOD',
                                concept_identity='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=EXAMPLE:CS_EXAMPLE(1.0).TIME_PERIOD',
                                local_representation=TimeDimensionRepresentationType(
                                    text_format=TimeTextFormatType(

                                    )
                                )
                            )
                        ),
                        measure_list=MeasureList(
                            urn='urn:sdmx:org.sdmx.infomodel.datastructure.MeasureDescriptor=EXAMPLE:LABOUR(1.0).MeasureDescriptor',
                            measure=[
                                Measure(
                                    id='OBS_VALUE',
                                    urn='urn:sdmx:org.sdmx.infomodel.datastructure.Measure=EXAMPLE:LABOUR(1.0).OBS_VALUE',
                                    concept_identity='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=EXAMPLE:CS_EXAMPLE(1.0).OBS_VALUE'
                                ),
                            ]
                        )
                    )
                ),
            ]
        )
    )
)
