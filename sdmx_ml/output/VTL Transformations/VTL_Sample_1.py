from decimal import Decimal
from sdmx_ml.models.attribute_2 import Attribute2
from sdmx_ml.models.attribute_list import AttributeList
from sdmx_ml.models.attribute_relationship_type import AttributeRelationshipType
from sdmx_ml.models.codelist_type import CodelistType
from sdmx_ml.models.codelists_type import CodelistsType
from sdmx_ml.models.concept_scheme_type import ConceptSchemeType
from sdmx_ml.models.concept_schemes_type import ConceptSchemesType
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
from sdmx_ml.models.item_type import NamePersonalisation
from sdmx_ml.models.item_type import Ruleset
from sdmx_ml.models.item_type import Transformation
from sdmx_ml.models.item_type import VtlMapping
from sdmx_ml.models.item_type import VtlMappingType
from sdmx_ml.models.measure import Measure
from sdmx_ml.models.measure_list import MeasureList
from sdmx_ml.models.name import Name
from sdmx_ml.models.name_personalisation_scheme_type import NamePersonalisationSchemeType
from sdmx_ml.models.name_personalisation_schemes_type import NamePersonalisationSchemesType
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
from sdmx_ml.models.to_vtl_mapping_type import ToVtlMappingType
from sdmx_ml.models.transformation_scheme_type import TransformationSchemeType
from sdmx_ml.models.transformation_schemes_type import TransformationSchemesType
from sdmx_ml.models.vtl_mapping_scheme_type import VtlMappingSchemeType
from sdmx_ml.models.vtl_mapping_schemes_type import VtlMappingSchemesType
from xsdata.models.datatype import XmlDateTime


obj = Structure(
    header=StructureHeaderType(
        id='VTL_SAMPLE1',
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
                    id='CL_SECTOR',
                    name=[
                        Name(
                            value='Sector code list'
                        ),
                    ],
                    version='1.0',
                    agency_id='SDMX'
                ),
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
                    ]
                ),
            ]
        ),
        concept_schemes=ConceptSchemesType(
            concept_scheme=[
                ConceptSchemeType(
                    id='CS11',
                    name=[
                        Name(
                            value='Concepts for Measures #1.1'
                        ),
                    ],
                    version='1.0',
                    agency_id='SDMX',
                    choice=[
                        Concept(
                            id='CREDIT',
                            name=[
                                Name(
                                    value='Credit'
                                ),
                            ]
                        ),
                        Concept(
                            id='DEBIT',
                            name=[
                                Name(
                                    value='Debit'
                                ),
                            ]
                        ),
                        Concept(
                            id='BALANCE',
                            name=[
                                Name(
                                    value='Balance'
                                ),
                            ]
                        ),
                    ]
                ),
                ConceptSchemeType(
                    id='CONCEPTS',
                    name=[
                        Name(
                            value='Concepts for DSDs #1.1'
                        ),
                    ],
                    version='1.0',
                    agency_id='SDMX',
                    choice=[
                        Concept(
                            id='SECTOR',
                            name=[
                                Name(
                                    value='Sector'
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
                        Concept(
                            id='SEVERITY',
                            name=[
                                Name(
                                    value='Severity'
                                ),
                            ]
                        ),
                        Concept(
                            id='ERRORCODE',
                            name=[
                                Name(
                                    value='Error Code'
                                ),
                            ]
                        ),
                        Concept(
                            id='RULEID',
                            name=[
                                Name(
                                    value='Rule Identifier'
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
                    id='DF11',
                    name=[
                        Name(
                            value='Dataflow #1.1'
                        ),
                    ],
                    version='1.0',
                    agency_id='SDMX',
                    structure='urn:sdmx:org.sdmx.infomodel.datastructure.DataStructure=SDMX:DS11(1.0)'
                ),
                DataflowType(
                    id='DF1R1',
                    name=[
                        Name(
                            value='Dataflow for Result #1.1'
                        ),
                    ],
                    version='1.0',
                    agency_id='SDMX',
                    structure='urn:sdmx:org.sdmx.infomodel.datastructure.DataStructure=SDMX:DS1R1(1.0)'
                ),
            ]
        ),
        data_structures=DataStructuresType(
            data_structure=[
                DataStructureType(
                    id='DS11',
                    name=[
                        Name(
                            value='Data Structure #1.1'
                        ),
                    ],
                    version='1.0',
                    agency_id='SDMX',
                    metadata_structure_components_or_data_structure_components=DataStructureComponents(
                        dimension_list=DimensionList(
                            dimension=[
                                Dimension(
                                    id='SECTOR',
                                    concept_identity='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=SDMX:CONCEPTS(1.0).SECTOR',
                                    local_representation=RepresentationType(
                                        text_format_or_enumeration_or_enumeration_format=[
                                            'urn:sdmx:org.sdmx.infomodel.codelist.Codelist=SDMX:CL_SECTOR(1.0)',
                                        ]
                                    )
                                ),
                                Dimension(
                                    id='COUNTRY',
                                    concept_identity='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=SDMX:CONCEPTS(1.0).COUNTRY',
                                    local_representation=RepresentationType(
                                        text_format_or_enumeration_or_enumeration_format=[
                                            'urn:sdmx:org.sdmx.infomodel.codelist.Codelist=SDMX:CL_AREA(1.0)',
                                        ]
                                    )
                                ),
                            ],
                            time_dimension=TimeDimension(
                                concept_identity='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=SDMX:CONCEPTS(1.0).TIME_PERIOD',
                                local_representation=TimeDimensionRepresentationType(
                                    text_format_or_enumeration_or_enumeration_format=[
                                        TextFormatType(
                                            text_type=DataType.OBSERVATIONAL_TIME_PERIOD
                                        ),
                                    ]
                                )
                            )
                        ),
                        measure_list=MeasureList(
                            measure=[
                                Measure(
                                    id='OBS_VALUE',
                                    concept_identity='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=SDMX:CONCEPTS(1.0).OBS_VALUE'
                                ),
                            ]
                        )
                    )
                ),
                DataStructureType(
                    id='DS1R1',
                    name=[
                        Name(
                            value='Data Structure for Results #1.1'
                        ),
                    ],
                    version='1.0',
                    agency_id='SDMX',
                    metadata_structure_components_or_data_structure_components=DataStructureComponents(
                        dimension_list=DimensionList(
                            dimension=[
                                Dimension(
                                    id='SECTOR',
                                    concept_identity='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=SDMX:CONCEPTS(1.0).SECTOR',
                                    local_representation=RepresentationType(
                                        text_format_or_enumeration_or_enumeration_format=[
                                            'urn:sdmx:org.sdmx.infomodel.codelist.Codelist=SDMX:CL_SECTOR(1.0)',
                                        ]
                                    )
                                ),
                                Dimension(
                                    id='COUNTRY',
                                    concept_identity='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=SDMX:CONCEPTS(1.0).COUNTRY',
                                    local_representation=RepresentationType(
                                        text_format_or_enumeration_or_enumeration_format=[
                                            'urn:sdmx:org.sdmx.infomodel.codelist.Codelist=SDMX:CL_AREA(1.0)',
                                        ]
                                    )
                                ),
                                Dimension(
                                    id='RULEID',
                                    concept_identity='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=SDMX:CONCEPTS(1.0).RULEID',
                                    local_representation=RepresentationType(
                                        text_format_or_enumeration_or_enumeration_format=[
                                            TextFormatType(

                                            ),
                                        ]
                                    )
                                ),
                            ],
                            time_dimension=TimeDimension(
                                concept_identity='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=SDMX:CONCEPTS(1.0).TIME_PERIOD',
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
                            attribute_or_metadata_attribute_usage=[
                                Attribute2(
                                    id='ERRORCODE',
                                    concept_identity='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=SDMX:CONCEPTS(1.0).ERRORCODE',
                                    local_representation=RepresentationType(
                                        text_format_or_enumeration_or_enumeration_format=[
                                            TextFormatType(

                                            ),
                                        ],
                                        min_occurs=0,
                                        max_occurs=1
                                    ),
                                    attribute_relationship=AttributeRelationshipType(
                                        choice=[
                                            AttributeRelationshipType.Observation(

                                            ),
                                        ]
                                    )
                                ),
                                Attribute2(
                                    id='SEVERITY',
                                    concept_identity='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=SDMX:CONCEPTS(1.0).SEVERITY',
                                    local_representation=RepresentationType(
                                        text_format_or_enumeration_or_enumeration_format=[
                                            TextFormatType(
                                                text_type=DataType.INTEGER,
                                                min_value=Decimal('0'),
                                                max_value=Decimal('10')
                                            ),
                                        ],
                                        min_occurs=0,
                                        max_occurs=1
                                    ),
                                    attribute_relationship=AttributeRelationshipType(
                                        choice=[
                                            AttributeRelationshipType.Observation(

                                            ),
                                        ]
                                    )
                                ),
                            ]
                        ),
                        measure_list=MeasureList(
                            measure=[
                                Measure(
                                    id='OBS_VALUE',
                                    concept_identity='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=SDMX:CONCEPTS(1.0).OBS_VALUE'
                                ),
                            ]
                        )
                    )
                ),
            ]
        ),
        name_personalisation_schemes=NamePersonalisationSchemesType(
            name_personalisation_scheme=[
                NamePersonalisationSchemeType(
                    id='NPS1',
                    name=[
                        Name(
                            value='Name Peronalisation Scheme #1'
                        ),
                    ],
                    agency_id='SDMX',
                    choice=[
                        NamePersonalisation(
                            id='NP1',
                            name=[
                                Name(
                                    value='Name Personalisation #1'
                                ),
                            ],
                            vtl_default_name='ERRORLEVEL',
                            personalised_name='SEVERITY',
                            vtl_artefact='variable'
                        ),
                    ],
                    vtl_version='2.0'
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
                    id='TS1',
                    name=[
                        Name(
                            value='Transformation Scheme #1 – SDMX/VTL release sample'
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
                                    value='Checks the dataflow DF11 according to the datapoint ruleset DPR1.  DF11 is mapped from SDMX to VTL through the default basic method, therefore its structure remains the same in VTL. All the original input measures are maintained in the output (i.e. OBS_VALUE), moreover the check operation generates the additional identifier RULEID (the id of the applied validation rule of the ruleset) and the additional measures BOOL_VAR (the Boolean outcome of the check, with values TRUE or FALSE), ERRORCODE (text string), ERRORLEVEL (assumed numeric from 0 to 10). Because of the name personalisation from ERRORLEVEL to SEVERITY declared in the associated NamePersonalisationScheme, SEVERITY is assigned instead than the VTL standard nameERRORLEVEL. The resulting VTL dataset TEMP11  is not persistent and it is assumed that it does not need a mapping towards SDMX. \n          '
                                ),
                            ],
                            expression='check_datapoint (DF11, DPR1 all_measures)',
                            result='TEMP11',
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
                                    value='Filters the TEMP11 observations having SEVERITY >=5, drops the measure BOOL_VAR and calculates creates a the persistent result DF1R1. Due to the mapping method M2A from VTL to SDMX declared for DF1R1 in the associated MappingScheme, the  VTL measure OBS_VALUE is mapped to OBS_VALUE in SDMX while ERRORCODE and SEVERITY become SDMX data attribute.'
                                ),
                            ],
                            expression='TEMP11 [filter SEVERITY >= 5][drop BOOL_VAR]',
                            result='DF1R1',
                            is_persistent=True
                        ),
                    ],
                    vtl_version='2.0',
                    vtl_mapping_scheme='urn:sdmx:org.sdmx.infomodel.transformation.VtlMappingScheme=SDMX:VTLMS1(1.0)',
                    name_personalisation_scheme='urn:sdmx:org.sdmx.infomodel.transformation.NamePersonalisationScheme=SDMX:NPS1(1.0)',
                    ruleset_scheme=[
                        'urn:sdmx:org.sdmx.infomodel.transformation.RulesetScheme=SDMX:RS1(1.0)',
                    ]
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
                                    value='urn:sdmx:org.sdmx.infomodel.datastructure.Dataflow=SDMX:DF11(1.0)'
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
            ]
        )
    )
)
