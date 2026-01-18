from decimal import Decimal
from sdmx_ml.models.codelist_type import CodelistType
from sdmx_ml.models.codelists_type import CodelistsType
from sdmx_ml.models.concept_representation import ConceptRepresentation
from sdmx_ml.models.concept_scheme_type import ConceptSchemeType
from sdmx_ml.models.concept_schemes_type import ConceptSchemesType
from sdmx_ml.models.custom_type_scheme_type import CustomTypeSchemeType
from sdmx_ml.models.custom_type_schemes_type import CustomTypeSchemesType
from sdmx_ml.models.data_structure_components import DataStructureComponents
from sdmx_ml.models.data_structure_type import DataStructureType
from sdmx_ml.models.data_structures_type import DataStructuresType
from sdmx_ml.models.data_type import DataType
from sdmx_ml.models.dataflow_type import DataflowType
from sdmx_ml.models.dataflows_type import DataflowsType
from sdmx_ml.models.description import Description
from sdmx_ml.models.dimension import Dimension
from sdmx_ml.models.dimension_list import DimensionList
from sdmx_ml.models.from_vtl_mapping_type import FromVtlMappingType
from sdmx_ml.models.item_type import Code
from sdmx_ml.models.item_type import Concept
from sdmx_ml.models.item_type import CustomType
from sdmx_ml.models.item_type import Ruleset
from sdmx_ml.models.item_type import Transformation
from sdmx_ml.models.item_type import UserDefinedOperator
from sdmx_ml.models.item_type import VtlMapping
from sdmx_ml.models.item_type import VtlMappingType
from sdmx_ml.models.measure import Measure
from sdmx_ml.models.measure_list import MeasureList
from sdmx_ml.models.name import Name
from sdmx_ml.models.party_type import PartyType
from sdmx_ml.models.representation_type import RepresentationType
from sdmx_ml.models.ruleset_scheme_type import RulesetSchemeType
from sdmx_ml.models.ruleset_schemes_type import RulesetSchemesType
from sdmx_ml.models.sender_type import SenderType
from sdmx_ml.models.standard_from_vtl_mapping_method_type import StandardFromVtlMappingMethodType
from sdmx_ml.models.standard_to_vtl_mapping_method_type import StandardToVtlMappingMethodType
from sdmx_ml.models.structure import Structure
from sdmx_ml.models.structure_header_type import StructureHeaderType
from sdmx_ml.models.structures_type import StructuresType
from sdmx_ml.models.text_format_type import TextFormatType
from sdmx_ml.models.time_dimension import TimeDimension
from sdmx_ml.models.time_dimension_representation_type import TimeDimensionRepresentationType
from sdmx_ml.models.time_text_format_type import TimeTextFormatType
from sdmx_ml.models.to_vtl_mapping_type import ToVtlMappingType
from sdmx_ml.models.transformation_scheme_type import TransformationSchemeType
from sdmx_ml.models.transformation_schemes_type import TransformationSchemesType
from sdmx_ml.models.user_defined_operator_scheme_type import UserDefinedOperatorSchemeType
from sdmx_ml.models.user_defined_operator_schemes_type import UserDefinedOperatorSchemesType
from sdmx_ml.models.vtl_mapping_scheme_type import VtlMappingSchemeType
from sdmx_ml.models.vtl_mapping_schemes_type import VtlMappingSchemesType
from xsdata.models.datatype import XmlDateTime


obj = Structure(
    header=StructureHeaderType(
        id='VTL_SAMPLE2',
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
                            id='EU',
                            name=[
                                Name(
                                    value='European Union'
                                ),
                            ]
                        ),
                        Code(
                            id='BENELUX',
                            name=[
                                Name(
                                    value='The Benelux Union'
                                ),
                            ]
                        ),
                        Code(
                            id='BE',
                            name=[
                                Name(
                                    value='Belgium'
                                ),
                            ]
                        ),
                        Code(
                            id='LU',
                            name=[
                                Name(
                                    value='Luxembourg'
                                ),
                            ]
                        ),
                        Code(
                            id='NE',
                            name=[
                                Name(
                                    value='The Netherlands'
                                ),
                            ]
                        ),
                        Code(
                            id='AT',
                            name=[
                                Name(
                                    value='Austria'
                                ),
                            ]
                        ),
                        Code(
                            id='BG',
                            name=[
                                Name(
                                    value='Bulgaria'
                                ),
                            ]
                        ),
                        Code(
                            id='SE',
                            name=[
                                Name(
                                    value='Sweden'
                                ),
                            ]
                        ),
                        Code(
                            id='SI',
                            name=[
                                Name(
                                    value='Slovenia'
                                ),
                            ]
                        ),
                        Code(
                            id='SK',
                            name=[
                                Name(
                                    value='Slovakia'
                                ),
                            ]
                        ),
                    ],
                    is_partial=True
                ),
            ]
        ),
        concept_schemes=ConceptSchemesType(
            concept_scheme=[
                ConceptSchemeType(
                    id='CS21',
                    name=[
                        Name(
                            value='Concepts for Measures #2.1'
                        ),
                    ],
                    version='1.0',
                    agency_id='SDMX',
                    choice=[
                        Concept(
                            id='IMPORT',
                            name=[
                                Name(
                                    value='Import'
                                ),
                            ],
                            core_representation=ConceptRepresentation(
                                text_format_or_enumeration_or_enumeration_format=[
                                    TextFormatType(
                                        text_type=DataType.NUMERIC
                                    ),
                                ]
                            )
                        ),
                        Concept(
                            id='EXPORT',
                            name=[
                                Name(
                                    value='Export'
                                ),
                            ],
                            core_representation=ConceptRepresentation(
                                text_format_or_enumeration_or_enumeration_format=[
                                    TextFormatType(
                                        text_type=DataType.NUMERIC
                                    ),
                                ]
                            )
                        ),
                    ]
                ),
                ConceptSchemeType(
                    id='CS2R1',
                    name=[
                        Name(
                            value='Concepts for Measures in Results #2.1'
                        ),
                    ],
                    version='1.0',
                    agency_id='SDMX',
                    choice=[
                        Concept(
                            id='PERC_EU_IMPORT',
                            name=[
                                Name(
                                    value='Import for EU in percentage'
                                ),
                            ],
                            core_representation=ConceptRepresentation(
                                text_format_or_enumeration_or_enumeration_format=[
                                    TextFormatType(
                                        text_type=DataType.NUMERIC,
                                        min_value=Decimal('0'),
                                        max_value=Decimal('100')
                                    ),
                                ]
                            )
                        ),
                        Concept(
                            id='PERC_EU_EXPORT',
                            name=[
                                Name(
                                    value='Export for EU in percentage'
                                ),
                            ],
                            core_representation=ConceptRepresentation(
                                text_format_or_enumeration_or_enumeration_format=[
                                    TextFormatType(
                                        text_type=DataType.NUMERIC,
                                        min_value=Decimal('0'),
                                        max_value=Decimal('100')
                                    ),
                                ]
                            )
                        ),
                    ]
                ),
                ConceptSchemeType(
                    id='CONCEPTS2',
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
                            id='TIME_PERIOD',
                            name=[
                                Name(
                                    value='Time Period'
                                ),
                            ]
                        ),
                        Concept(
                            id='MEASURE_DIMENSION',
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
        custom_type_schemes=CustomTypeSchemesType(
            custom_type_scheme=[
                CustomTypeSchemeType(
                    id='CTS1',
                    name=[
                        Name(
                            value='Custom Type Scheme #1'
                        ),
                    ],
                    version='1.0',
                    agency_id='SDMX',
                    choice=[
                        CustomType(
                            id='NUMERIC_WITH_ZEROS',
                            name=[
                                Name(
                                    value='Custom Type sample for numbers'
                                ),
                            ],
                            vtl_scalar_type='number',
                            data_type='NUMERIC',
                            null_value='0'
                        ),
                    ],
                    vtl_version='2.0'
                ),
            ]
        ),
        dataflows=DataflowsType(
            dataflow=[
                DataflowType(
                    id='DF21',
                    name=[
                        Name(
                            value='Dataflow #2.1'
                        ),
                    ],
                    version='1.0',
                    agency_id='SDMX',
                    structure='urn:sdmx:org.sdmx.infomodel.datastructure.DataStructure=SDMX:DS21(1.0)'
                ),
                DataflowType(
                    id='DF2R1',
                    name=[
                        Name(
                            value='Dataflow for Result #2.1'
                        ),
                    ],
                    version='1.0',
                    agency_id='SDMX',
                    structure='urn:sdmx:org.sdmx.infomodel.datastructure.DataStructure=SDMX:DS21(1.0)'
                ),
            ]
        ),
        data_structures=DataStructuresType(
            data_structure=[
                DataStructureType(
                    id='DS21',
                    name=[
                        Name(
                            value='Data Structure #2.1'
                        ),
                    ],
                    version='1.0',
                    agency_id='SDMX',
                    metadata_structure_components_or_data_structure_components=DataStructureComponents(
                        dimension_list=DimensionList(
                            dimension=[
                                Dimension(
                                    id='GEO_AREA',
                                    concept_identity='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=SDMX:CONCEPTS2(1.0).GEO_AREA',
                                    local_representation=RepresentationType(
                                        text_format_or_enumeration_or_enumeration_format=[
                                            'urn:sdmx:org.sdmx.infomodel.codelist.Codelist=SDMX:CL_AREA(1.0)',
                                        ]
                                    )
                                ),
                            ],
                            time_dimension=TimeDimension(
                                concept_identity='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=SDMX:CONCEPTS2(1.0).TIME_PERIOD',
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
                                    concept_identity='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=SDMX:CONCEPTS2(1.0).OBS_VALUE'
                                ),
                            ]
                        )
                    )
                ),
                DataStructureType(
                    id='DS2R1',
                    name=[
                        Name(
                            value='Data Structure for Results #2.1'
                        ),
                    ],
                    version='1.0',
                    agency_id='SDMX',
                    metadata_structure_components_or_data_structure_components=DataStructureComponents(
                        dimension_list=DimensionList(
                            dimension=[
                                Dimension(
                                    id='GEO_AREA',
                                    concept_identity='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=SDMX:CONCEPTS2(1.0).GEO_AREA',
                                    local_representation=RepresentationType(
                                        text_format_or_enumeration_or_enumeration_format=[
                                            'urn:sdmx:org.sdmx.infomodel.codelist.Codelist=SDMX:CL_AREA(1.0)',
                                        ]
                                    )
                                ),
                                Dimension(
                                    id='MEASURE_DIMENSION',
                                    concept_identity='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=SDMX:CONCEPTS2(1.0).MEASURE_DIMENSION',
                                    local_representation=RepresentationType(
                                        text_format_or_enumeration_or_enumeration_format=[
                                            'urn:sdmx:org.sdmx.infomodel.codelist.Codelist=SDMX:CS2R1(1.0)',
                                        ]
                                    )
                                ),
                            ],
                            time_dimension=TimeDimension(
                                concept_identity='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=SDMX:CONCEPTS2(1.0).TIME_PERIOD',
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
                                    concept_identity='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=SDMX:CONCEPTS2(1.0).OBS_VALUE'
                                ),
                            ]
                        )
                    )
                ),
            ]
        ),
        ruleset_schemes=RulesetSchemesType(
            ruleset_scheme=[
                RulesetSchemeType(
                    id='RS1',
                    name=[
                        Name(
                            value='Ruleset Scheme #1'
                        ),
                    ],
                    version='1.0',
                    agency_id='SDMX',
                    choice=[
                        Ruleset(
                            id='DPR1',
                            name=[
                                Name(
                                    value='DataPoint Ruleset #1'
                                ),
                            ],
                            ruleset_definition='\n            define datapoint ruleset DPR1 ( variable INDICATOR as A, VALUE as B ) is  \n              rule1: when A = "CREDIT" or A = "DEBIT" then B >= 0 errorcode "Negative value" errorlevel 10;\n              rule2: when A = "CREDIT" or A = "DEBIT" then B < 999999999999 errorcode "Value too large" errorlevel 8\n            end datapoint ruleset\n          ',
                            ruleset_type='datapoint',
                            ruleset_scope='valuedomain'
                        ),
                        Ruleset(
                            id='HR1',
                            name=[
                                Name(
                                    value='Hierarchical Ruleset #1'
                                ),
                            ],
                            ruleset_definition="\n            define hierarchical ruleset HR1 (variable condition TIME as T rule GEO )\n              EU = AT [ T >= 1995-01-01 ]\n                + BE [ T >= 1958-01-01 ]\n                + BG [ T >= 2007-01-01 ] \t\n                + SE [ T >= 1995-01-01 ] \n                + SI [ T >= 2004-01-01 ]\n                + SK [ T >= 2004-01-01 ]; /* All EU countries would be added under the 'EU' code, but were not for keeping the samples smaller. */\n              BENELUX = BE [ T >= 1948-01-01 ]\n                + NE [ T >= 1948-01-01 ]\n                + LU [ T >= 1948-01-01 ]\n            end hierarchical ruleset\n          ",
                            ruleset_type='hierarchical',
                            ruleset_scope='valuedomain'
                        ),
                    ],
                    vtl_version='2.0',
                    vtl_mapping_scheme='urn:sdmx:org.sdmx.infomodel.transformation.VtlMappingScheme=SDMX:VTLMS1(1.0)'
                ),
            ]
        ),
        transformation_schemes=TransformationSchemesType(
            transformation_scheme=[
                TransformationSchemeType(
                    id='TS2',
                    name=[
                        Name(
                            value='Transformation Scheme #2 – SDMX/VTL release sample'
                        ),
                    ],
                    version='1.0',
                    agency_id='SDMX',
                    choice=[
                        Transformation(
                            id='TS_A',
                            name=[
                                Name(
                                    value='Transformation A'
                                ),
                            ],
                            description=[
                                Description(
                                    value='Aggregates the dataflow DF21 according to the hierarchical ruleset HR1.\n            DF21 is mapped from SDMX to VTL through the pivot mapping method, therefore the mapped VTL dataset has the components IMPORT and EXPORT instead of MEASURE_DIMENSION and OBS_VALUE. \n            Following the application of the hierarchy operator, the observation relevant to EU and BENELUX are produced.\n            The resulting VTL dataset TEMP1 is not persistent and it is assumed that it does not need a mapping towards SDMX.\n          '
                                ),
                            ],
                            expression=' hierarchy(DF21, HR1 computed)',
                            result='TEMP1',
                            is_persistent=False
                        ),
                        Transformation(
                            id='TS_B',
                            name=[
                                Name(
                                    value='Transformation B'
                                ),
                            ],
                            description=[
                                Description(
                                    value='Extracts from TEMP1 the observations having GEO_AREA="EU" and drops the GEO_AREA identifier. \n            The result TEMP2 is not persistent and it is assumed that it does not need a mapping towards SDMX.\n          '
                                ),
                            ],
                            expression='TEMP1 [sub GEO_AREA = "EU"]',
                            result='TEMP2',
                            is_persistent=False
                        ),
                        Transformation(
                            id='TS_C',
                            name=[
                                Name(
                                    value='Transformation C'
                                ),
                            ],
                            description=[
                                Description(
                                    value='Applies the "percentage" user defined operator to TEMP1 and TEMP2 to calculate the percentage of each EU country in respect to the EU and renames IMPORT to PERC_EU_IMPORT and EXPORT to PERC_EU_EXPORT. \n            According to the VTL behaviour, the result has the same identifiers as TEMP1 (GEO_AREA and TIME_PERIOD). \n            The result DF2R1 is persistent and is mapped from VTL to SDMX through the unpivot method, therefore the SDMX structure has MEASURE_DIMENSION and OBS_VALUE in place of PERC_EU_IMPORT and PERC_EU_EXPORT, which become the possible values of the MEASURE DIMENSION (i.e., concepts of relevant concept scheme).\n          '
                                ),
                            ],
                            expression='percentage ( TEMP1,  TEMP2 ) [rename IMPORT to PERC_EU_IMPORT, EXPORT to PERC_EU_EXPORT]',
                            result='DF2R1',
                            is_persistent=True
                        ),
                    ],
                    vtl_version='2.0',
                    vtl_mapping_scheme='urn:sdmx:org.sdmx.infomodel.transformation.VtlMappingScheme=SDMX:VTLMS2(1.0)',
                    custom_type_scheme='urn:sdmx:org.sdmx.infomodel.transformation.CustomTypeScheme=SDMX:CTS1(1.0)',
                    ruleset_scheme=[
                        'urn:sdmx:org.sdmx.infomodel.transformation.RulesetScheme=SDMX:RS1(1.0)',
                    ],
                    user_defined_operator_scheme=[
                        'urn:sdmx:org.sdmx.infomodel.transformation.UserDefinedOperatorScheme=SDMX:UDOS1(1.0)',
                    ]
                ),
            ]
        ),
        user_defined_operator_schemes=UserDefinedOperatorSchemesType(
            user_defined_operator_scheme=[
                UserDefinedOperatorSchemeType(
                    id='UDOS1',
                    name=[
                        Name(
                            value='User Defined Operators #1'
                        ),
                    ],
                    version='1.0',
                    agency_id='SDMX',
                    choice=[
                        UserDefinedOperator(
                            id='percentage',
                            name=[
                                Name(
                                    value='Percentage'
                                ),
                            ],
                            operator_definition='\n            define operator percentage (  DS_A  dataset { measure<number> _+ } ,\n              DS_B dataset { measure<number> _+ }  )\n              returns dataset { measure<number> _+ } is\n              DS_A  /  DS_B  *  100  \n            end operator\n          '
                        ),
                        UserDefinedOperator(
                            id='diffperc',
                            name=[
                                Name(
                                    value='Difference Percentage'
                                ),
                            ],
                            operator_definition='\n            define operator diffperc ( DS_A dataset { measure<number> _+ } ,\n              DS_B dataset { measure<number> _+ } )\n              returns dataset { measure<number> _+ } is \n              (DS_A  - DS_B) /  DS_B  *  100  \n            end operator \n          '
                        ),
                    ],
                    vtl_version='2.0'
                ),
            ]
        ),
        vtl_mapping_schemes=VtlMappingSchemesType(
            vtl_mapping_scheme=[
                VtlMappingSchemeType(
                    id='VTLMS1',
                    name=[
                        Name(
                            value='VTL Mapping Scheme #1'
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
                                    value='urn:sdmx:org.sdmx.infomodel.datastructure.Dataflow=SDMX:DF1R1(1.0)'
                                ),
                                FromVtlMappingType(
                                    method=StandardFromVtlMappingMethodType.M2_A
                                ),
                            ],
                            alias='DF1R1'
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
                                    value='urn:sdmx:org.sdmx.infomodel.datastructure.Dataflow=SDMX:D11(1.0)'
                                ),
                                ToVtlMappingType(
                                    method=StandardToVtlMappingMethodType.BASIC
                                ),
                            ],
                            alias='DF11'
                        ),
                        VtlMapping(
                            id='VTLM3',
                            name=[
                                Name(
                                    value='Variable INDICATOR mapping'
                                ),
                            ],
                            choice_1=[
                                VtlMappingType.Concept(
                                    value='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=SDMX:CONCEPTS(1.0).MEASURE_DIMENSION'
                                ),
                            ],
                            alias='INDICATOR'
                        ),
                        VtlMapping(
                            id='VTLM4',
                            name=[
                                Name(
                                    value='Variable VALUE mapping'
                                ),
                            ],
                            choice_1=[
                                VtlMappingType.Concept(
                                    value='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=SDMX:CONCEPTS(1.0).OBS_VALUE'
                                ),
                            ],
                            alias='VALUE'
                        ),
                        VtlMapping(
                            id='VTLM5',
                            name=[
                                Name(
                                    value='Variable TIME mapping'
                                ),
                            ],
                            choice_1=[
                                VtlMappingType.Concept(
                                    value='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=SDMX:CONCEPTS(1.0).TIME_PERIOD'
                                ),
                            ],
                            alias='TIME'
                        ),
                        VtlMapping(
                            id='VTLM6',
                            name=[
                                Name(
                                    value='Variable GEO mapping'
                                ),
                            ],
                            choice_1=[
                                VtlMappingType.Concept(
                                    value='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=SDMX:CONCEPTS(1.0).COUNTRY'
                                ),
                            ],
                            alias='GEO'
                        ),
                    ]
                ),
                VtlMappingSchemeType(
                    id='VTLMS2',
                    name=[
                        Name(
                            value='VTL Mapping Scheme #2'
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
                                    value='urn:sdmx:org.sdmx.infomodel.datastructure.Dataflow=SDMX:D21(1.0)'
                                ),
                                ToVtlMappingType(
                                    method=StandardToVtlMappingMethodType.PIVOT
                                ),
                            ],
                            alias='DF21'
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
                                    value='urn:sdmx:org.sdmx.infomodel.datastructure.Dataflow=SDMX:D2R1(1.0)'
                                ),
                                FromVtlMappingType(
                                    method=StandardFromVtlMappingMethodType.UNPIVOT
                                ),
                            ],
                            alias='DF2R1'
                        ),
                    ]
                ),
            ]
        )
    )
)
