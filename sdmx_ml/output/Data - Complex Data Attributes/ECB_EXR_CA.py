from sdmx_ml.models.action_type import ActionType
from sdmx_ml.models.comp_type import CompType
from sdmx_ml.models.data_set_type import DataSetType
from sdmx_ml.models.obs_dimensions_code_type import ObsDimensionsCodeType
from sdmx_ml.models.obs_type import ObsType
from sdmx_ml.models.party_type import PartyType
from sdmx_ml.models.payload_structure_type import PayloadStructureType
from sdmx_ml.models.sender_type import SenderType
from sdmx_ml.models.series_type import SeriesType
from sdmx_ml.models.structure_specific_data import StructureSpecificData
from sdmx_ml.models.structure_specific_data_header_type import StructureSpecificDataHeaderType
from sdmx_ml.models.structure_specific_data_structure_type import StructureSpecificDataStructureType
from sdmx_ml.models.text import Text
from sdmx_ml.models.value_type import ValueType
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlPeriod


obj = StructureSpecificData(
    header=StructureSpecificDataHeaderType(
        id='IREF411123',
        prepared=XmlDateTime(2021, 3, 8, 22, 5, 13, 0, 0),
        sender=SenderType(
            id='Unknown'
        ),
        receiver=[
            PartyType(
                id='ANONYMOUS'
            ),
        ],
        structure=[
            StructureSpecificDataStructureType(
                provision_agreement_or_structure_usage_or_structure=PayloadStructureType.StructureUsage(
                    value='urn:sdmx:org.sdmx.infomodel.datastructure.Dataflow=ECB:EXR(1.0)'
                ),
                structure_id='ECB_EXR_COMPLEX_ATTRIBUTES_1_0',
                namespace='urn:sdmx:org.sdmx.infomodel.datastructure.Dataflow=ECB:EXR(1.0):ObsLevelDim:TIME_PERIOD',
                dimension_at_observation=ObsDimensionsCodeType.TIME_PERIOD
            ),
        ],
        data_set_action=ActionType.INFORMATION,
        extracted=XmlDateTime(2021, 3, 8, 22, 5, 13),
        reporting_begin=XmlDateTime(1999, 1, 1, 0, 0, 0),
        reporting_end=XmlDateTime(2019, 1, 1, 23, 59, 59)
    ),
    data_set=[
        DataSetType(
            choice=[
                SeriesType(
                    comp=[
                        CompType(
                            value=[
                                ValueType(
                                    content=[
                                        Text(
                                            value='Some English Text'
                                        ),
                                        Text(
                                            value='Quelques textes en anglais',
                                            lang='fr'
                                        ),
                                    ]
                                ),
                                ValueType(
                                    content=[
                                        Text(
                                            value='Additional English Text where lang defaults to en'
                                        ),
                                        Text(
                                            value='Texte anglais supplémentaire',
                                            lang='fr'
                                        ),
                                    ]
                                ),
                            ],
                            id='TITLE'
                        ),
                        CompType(
                            value=[
                                ValueType(
                                    content=[
                                        '4F0',
                                    ]
                                ),
                                ValueType(
                                    content=[
                                        '4D0',
                                    ]
                                ),
                                ValueType(
                                    content=[
                                        'CZ2',
                                    ]
                                ),
                            ],
                            id='SOURCE_AGENCY'
                        ),
                        CompType(
                            value=[
                                ValueType(
                                    content=[
                                        'First publication source',
                                    ]
                                ),
                                ValueType(
                                    content=[
                                        'Second publication source',
                                    ]
                                ),
                            ],
                            id='SOURCE_PUB'
                        ),
                    ],
                    obs=[
                        ObsType(
                            comp=[
                                CompType(
                                    value=[
                                        ValueType(
                                            content=[
                                                'A',
                                            ]
                                        ),
                                        ValueType(
                                            content=[
                                                'F',
                                            ]
                                        ),
                                    ],
                                    id='OBS_STATUS'
                                ),
                            ],
                            time_period=XmlPeriod("2017"),
                            local_attributes={
                                'OBS_VALUE': '1.46472274509804',
                            }
                        ),
                        ObsType(
                            comp=[
                                CompType(
                                    value=[
                                        ValueType(
                                            content=[
                                                'J',
                                            ]
                                        ),
                                        ValueType(
                                            content=[
                                                'U',
                                            ]
                                        ),
                                        ValueType(
                                            content=[
                                                'N',
                                            ]
                                        ),
                                    ],
                                    id='OBS_STATUS'
                                ),
                            ],
                            time_period=XmlPeriod("2018"),
                            local_attributes={
                                'OBS_VALUE': '1.529364705882353',
                            }
                        ),
                        ObsType(
                            comp=[
                                CompType(
                                    value=[
                                        ValueType(
                                            content=[
                                                'A',
                                            ]
                                        ),
                                    ],
                                    id='OBS_STATUS'
                                ),
                            ],
                            time_period=XmlPeriod("2019"),
                            local_attributes={
                                'OBS_VALUE': '1.485477254901961',
                            }
                        ),
                        ObsType(
                            comp=[
                                CompType(
                                    value=[
                                        ValueType(
                                            content=[
                                                '#N/A',
                                            ]
                                        ),
                                    ],
                                    id='OBS_STATUS'
                                ),
                            ],
                            time_period=XmlPeriod("2020"),
                            local_attributes={
                                'OBS_VALUE': '1.585477254901961',
                            }
                        ),
                    ],
                    local_attributes={
                        'FREQ': 'A',
                        'CURRENCY': 'CAD',
                        'CURRENCY_DENOM': 'EUR',
                        'EXR_TYPE': 'SP00',
                        'EXR_SUFFIX': 'A',
                        'TIME_FORMAT': 'P1Y',
                        'COLLECTION': 'A',
                        'DECIMALS': '4',
                        'TITLE_COMPL': 'ECB reference exchange rate, Canadian dollar/Euro, 2:15 pm (C.E.T.)',
                        'UNIT': 'CAD',
                        'UNIT_MULT': '0',
                    }
                ),
            ],
            structure_ref='ECB_EXR_COMPLEX_ATTRIBUTES_1_0'
        ),
    ]
)
