from sdmx_ml.models.codelist_type import CodelistType
from sdmx_ml.models.codelists_type import CodelistsType
from sdmx_ml.models.concept_scheme_type import ConceptSchemeType
from sdmx_ml.models.concept_schemes_type import ConceptSchemesType
from sdmx_ml.models.data_structure_components import DataStructureComponents
from sdmx_ml.models.data_structure_type import DataStructureType
from sdmx_ml.models.data_structures_type import DataStructuresType
from sdmx_ml.models.dataflow_type import DataflowType
from sdmx_ml.models.dataflows_type import DataflowsType
from sdmx_ml.models.dimension import Dimension
from sdmx_ml.models.dimension_list import DimensionList
from sdmx_ml.models.from_vtl_mapping_type import FromVtlMappingType
from sdmx_ml.models.item_type import Code
from sdmx_ml.models.item_type import Concept
from sdmx_ml.models.item_type import Transformation
from sdmx_ml.models.item_type import VtlMapping
from sdmx_ml.models.item_type import VtlMappingType
from sdmx_ml.models.measure import Measure
from sdmx_ml.models.measure_list import MeasureList
from sdmx_ml.models.name import Name
from sdmx_ml.models.party_type import PartyType
from sdmx_ml.models.representation_type import RepresentationType
from sdmx_ml.models.sender_type import SenderType
from sdmx_ml.models.space_key_type import SpaceKeyType
from sdmx_ml.models.structure import Structure
from sdmx_ml.models.structure_header_type import StructureHeaderType
from sdmx_ml.models.structures_type import StructuresType
from sdmx_ml.models.time_dimension import TimeDimension
from sdmx_ml.models.time_dimension_representation_type import TimeDimensionRepresentationType
from sdmx_ml.models.time_text_format_type import TimeTextFormatType
from sdmx_ml.models.to_vtl_mapping_type import ToVtlMappingType
from sdmx_ml.models.transformation_scheme_type import TransformationSchemeType
from sdmx_ml.models.transformation_schemes_type import TransformationSchemesType
from sdmx_ml.models.vtl_mapping_scheme_type import VtlMappingSchemeType
from sdmx_ml.models.vtl_mapping_schemes_type import VtlMappingSchemesType
from xsdata.models.datatype import XmlDateTime


obj = Structure(
    header=StructureHeaderType(
        id='VTL_SAMPLE3',
        prepared=XmlDateTime(2020, 6, 5, 12, 0, 0, 0, 0),
        sender=SenderType(
            id='SDMX'
        ),
        receiver=[
            PartyType(
                id='SDMX'
            ),
        ]
    ),
    structures=StructuresType(
        codelists=CodelistsType(
            codelist=[
                CodelistType(
                    id='CL_AREA',
                    name=[
                        Name(
                            value='Area codelist'
                        ),
                    ],
                    version='1.0',
                    agency_id='SDMX',
                    choice=[
                        Code(
                            id='NA',
                            name=[
                                Name(
                                    value='North America'
                                ),
                            ]
                        ),
                        Code(
                            id='US',
                            name=[
                                Name(
                                    value='United States of America'
                                ),
                            ]
                        ),
                        Code(
                            id='MX',
                            name=[
                                Name(
                                    value='Mexico'
                                ),
                            ]
                        ),
                        Code(
                            id='CA',
                            name=[
                                Name(
                                    value='Canada'
                                ),
                            ]
                        ),
                        Code(
                            id='EU',
                            name=[
                                Name(
                                    value='European Union'
                                ),
                            ]
                        ),
                    ],
                    is_partial=True
                ),
                CodelistType(
                    id='CL_INDICATOR',
                    name=[
                        Name(
                            value='Indicators Codelist'
                        ),
                    ],
                    version='1.0',
                    agency_id='SDMX',
                    choice=[
                        Code(
                            id='GDP',
                            name=[
                                Name(
                                    value='Gross Domestic Product'
                                ),
                            ]
                        ),
                        Code(
                            id='POPULATION',
                            name=[
                                Name(
                                    value='Population'
                                ),
                            ]
                        ),
                        Code(
                            id='GDPPERCAPITA',
                            name=[
                                Name(
                                    value='Gross Domestic Product per Capita'
                                ),
                            ]
                        ),
                    ]
                ),
            ]
        ),
        concept_schemes=ConceptSchemesType(
            concept_scheme=[
                ConceptSchemeType(
                    id='CONCEPTS3',
                    name=[
                        Name(
                            value='Concepts for DSDs #2.1'
                        ),
                    ],
                    version='1.0',
                    agency_id='SDMX',
                    choice=[
                        Concept(
                            id='GEO_AREA',
                            name=[
                                Name(
                                    value='Geographical Area'
                                ),
                            ]
                        ),
                        Concept(
                            id='COUNTRY',
                            name=[
                                Name(
                                    value='Country'
                                ),
                            ]
                        ),
                        Concept(
                            id='TIME_PERIOD',
                            name=[
                                Name(
                                    value='Time Period'
                                ),
                            ]
                        ),
                        Concept(
                            id='INDICATOR',
                            name=[
                                Name(
                                    value='Measure Dimension'
                                ),
                            ]
                        ),
                        Concept(
                            id='OBS_VALUE',
                            name=[
                                Name(
                                    value='Observation Value'
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
                    id='DF31',
                    name=[
                        Name(
                            value='Dataflow #3.1'
                        ),
                    ],
                    version='1.0',
                    agency_id='SDMX',
                    structure='urn:sdmx:org.sdmx.infomodel.datastructure.DataStructure=SDMX:DS31(1.0)'
                ),
                DataflowType(
                    id='DF3R1',
                    name=[
                        Name(
                            value='Dataflow for Result #3.1'
                        ),
                    ],
                    version='1.0',
                    agency_id='SDMX',
                    structure='urn:sdmx:org.sdmx.infomodel.datastructure.DataStructure=SDMX:DS3R1(1.0)'
                ),
            ]
        ),
        data_structures=DataStructuresType(
            data_structure=[
                DataStructureType(
                    id='DS31',
                    name=[
                        Name(
                            value='Data Structure #3.1'
                        ),
                    ],
                    version='1.0',
                    agency_id='SDMX',
                    metadata_structure_components_or_data_structure_components=DataStructureComponents(
                        dimension_list=DimensionList(
                            dimension=[
                                Dimension(
                                    id='COUNTRY',
                                    concept_identity='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=SDMX:CONCEPTS3(1.0).COUNTRY',
                                    local_representation=RepresentationType(
                                        text_format_or_enumeration_or_enumeration_format=[
                                            'urn:sdmx:org.sdmx.infomodel.codelist.Codelist=SDMX:CL_AREA(1.0)',
                                        ]
                                    )
                                ),
                                Dimension(
                                    id='INDICATOR',
                                    concept_identity='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=SDMX:CONCEPTS3(1.0).INDICATOR',
                                    local_representation=RepresentationType(
                                        text_format_or_enumeration_or_enumeration_format=[
                                            'urn:sdmx:org.sdmx.infomodel.codelist.Codelist=SDMX:CL_INDICATOR(1.0)',
                                        ]
                                    )
                                ),
                            ],
                            time_dimension=TimeDimension(
                                concept_identity='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=SDMX:CONCEPTS3(1.0).TIME_PERIOD',
                                local_representation=TimeDimensionRepresentationType(
                                    text_format=TimeTextFormatType(

                                    )
                                )
                            )
                        ),
                        measure_list=MeasureList(
                            measure=[
                                Measure(
                                    id='OBS_VALUE',
                                    concept_identity='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=SDMX:CONCEPTS3(1.0).OBS_VALUE'
                                ),
                            ]
                        )
                    )
                ),
                DataStructureType(
                    id='DS3R1',
                    name=[
                        Name(
                            value='Data Structure for Results #3.1'
                        ),
                    ],
                    version='1.0',
                    agency_id='SDMX',
                    metadata_structure_components_or_data_structure_components=DataStructureComponents(
                        dimension_list=DimensionList(
                            dimension=[
                                Dimension(
                                    id='GEO_AREA',
                                    concept_identity='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=SDMX:CONCEPTS3(1.0).GEO_AREA',
                                    local_representation=RepresentationType(
                                        text_format_or_enumeration_or_enumeration_format=[
                                            'urn:sdmx:org.sdmx.infomodel.codelist.Codelist=SDMX:CL_AREA(1.0)',
                                        ]
                                    )
                                ),
                                Dimension(
                                    id='INDICATOR',
                                    concept_identity='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=SDMX:CONCEPTS3(1.0).INDICATOR',
                                    local_representation=RepresentationType(
                                        text_format_or_enumeration_or_enumeration_format=[
                                            'urn:sdmx:org.sdmx.infomodel.codelist.Codelist=SDMX:CL_INDICATOR(1.0)',
                                        ]
                                    )
                                ),
                            ],
                            time_dimension=TimeDimension(
                                concept_identity='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=SDMX:CONCEPTS3(1.0).TIME_PERIOD',
                                local_representation=TimeDimensionRepresentationType(
                                    text_format=TimeTextFormatType(

                                    )
                                )
                            )
                        ),
                        measure_list=MeasureList(
                            measure=[
                                Measure(
                                    id='OBS_VALUE',
                                    concept_identity='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=SDMX:CONCEPTS3(1.0).OBS_VALUE'
                                ),
                            ]
                        )
                    )
                ),
            ]
        ),
        transformation_schemes=TransformationSchemesType(
            transformation_scheme=[
                TransformationSchemeType(
                    id='TS3',
                    name=[
                        Name(
                            value='Transformation Scheme #3 – SDMX/VTL release sample'
                        ),
                    ],
                    version='1.0',
                    agency_id='SDMX',
                    choice=[
                        Transformation(
                            id='TS_A',
                            name=[
                                Name(
                                    value='GDP per Capita for USA'
                                ),
                            ],
                            expression="'DF31/GDP.US' / 'DF31/POPULATION.US'",
                            result='DF3R1/GDPPERCAPITA.US',
                            is_persistent=True
                        ),
                        Transformation(
                            id='TS_B',
                            name=[
                                Name(
                                    value='GDP per Capita for Canada'
                                ),
                            ],
                            expression="'DF31/GDP.CA' / 'DF31/POPULATION.CA'",
                            result='DF3R1/GDPPERCAPITA.CA',
                            is_persistent=True
                        ),
                        Transformation(
                            id='TS_C',
                            name=[
                                Name(
                                    value='Population for North America'
                                ),
                            ],
                            expression="'DF31/POPULATION.US' + 'DF31/POPULATION.CA' + 'DF31/POPULATION.MX'",
                            result='DF3R1/POPULATION.NA',
                            is_persistent=True
                        ),
                        Transformation(
                            id='TS_D',
                            name=[
                                Name(
                                    value='GDP for North America'
                                ),
                            ],
                            expression="'DF31/GDP.US' + 'DF31/GDP.CA' + 'DF31/GDP.MX'",
                            result='DF3R1/GDP.NA',
                            is_persistent=True
                        ),
                        Transformation(
                            id='TS_E',
                            name=[
                                Name(
                                    value='GDP per Capita for North America'
                                ),
                            ],
                            expression="'DF31/GDP.NA' / 'DF31/POPULATION.NA'",
                            result='DF3R1/GDPPERCAPITA.NA',
                            is_persistent=True
                        ),
                    ],
                    vtl_version='2.0',
                    vtl_mapping_scheme='urn:sdmx:org.sdmx.infomodel.transformation.VtlMappingScheme=SDMX:VTLMS3(1.0)'
                ),
            ]
        ),
        vtl_mapping_schemes=VtlMappingSchemesType(
            vtl_mapping_scheme=[
                VtlMappingSchemeType(
                    id='VTLMS3',
                    name=[
                        Name(
                            value='VTL Mapping Scheme #3'
                        ),
                    ],
                    version='1.0',
                    agency_id='SDMX',
                    choice=[
                        VtlMapping(
                            id='VTLM1',
                            name=[
                                Name(
                                    value='VTL Mapping #1'
                                ),
                            ],
                            choice_1=[
                                VtlMappingType.Dataflow(
                                    value='urn:sdmx:org.sdmx.infomodel.datastructure.Dataflow=SDMX:DF3R1(1.0)'
                                ),
                                FromVtlMappingType(
                                    from_vtl_super_space=SpaceKeyType(
                                        key=[
                                            'INDICATOR',
                                            'GEO_AREA',
                                        ]
                                    )
                                ),
                            ],
                            alias='DF3R1'
                        ),
                        VtlMapping(
                            id='VTLM2',
                            name=[
                                Name(
                                    value='VTL Mapping #2'
                                ),
                            ],
                            choice_1=[
                                VtlMappingType.Dataflow(
                                    value='urn:sdmx:org.sdmx.infomodel.datastructure.Dataflow=SDMX:D31(1.0)'
                                ),
                                ToVtlMappingType(
                                    to_vtl_sub_space=SpaceKeyType(
                                        key=[
                                            'INDICATOR',
                                            'COUNTRY',
                                        ]
                                    )
                                ),
                            ],
                            alias='DF31'
                        ),
                    ]
                ),
            ]
        )
    )
)
