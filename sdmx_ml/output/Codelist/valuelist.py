from sdmx_ml.models.description import Description
from sdmx_ml.models.name import Name
from sdmx_ml.models.party_type import PartyType
from sdmx_ml.models.sender_type import SenderType
from sdmx_ml.models.structure import Structure
from sdmx_ml.models.structure_header_type import StructureHeaderType
from sdmx_ml.models.structures_type import StructuresType
from sdmx_ml.models.value_item_type import ValueItemType
from sdmx_ml.models.value_list_type import ValueListType
from sdmx_ml.models.value_lists_type import ValueListsType
from xsdata.models.datatype import XmlDateTime


obj = Structure(
    header=StructureHeaderType(
        id='IREF772628',
        prepared=XmlDateTime(2021, 3, 8, 17, 49, 35, 0, 0),
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
        value_lists=ValueListsType(
            value_list=[
                ValueListType(
                    id='VL_CURRENCY_SYMBOL',
                    urn='urn:sdmx:org.sdmx.infomodel.codelist.ValueList=SDMX:VL_CURRENCY_SYMBOL(1.0)',
                    name=[
                        Name(
                            value='Currency Symbol'
                        ),
                    ],
                    description=[
                        Description(
                            value='Enumerated list of currencies identified by symbol'
                        ),
                    ],
                    version='1.0',
                    agency_id='EXAMPLE',
                    value_item=[
                        ValueItemType(
                            name=[
                                Name(
                                    value='USD'
                                ),
                            ],
                            description=[
                                Description(
                                    value='US Dollar'
                                ),
                            ],
                            id='$'
                        ),
                        ValueItemType(
                            name=[
                                Name(
                                    value='GBP'
                                ),
                            ],
                            description=[
                                Description(
                                    value='UK Pound'
                                ),
                            ],
                            id='£'
                        ),
                        ValueItemType(
                            name=[
                                Name(
                                    value='EUR'
                                ),
                            ],
                            description=[
                                Description(
                                    value='Euro'
                                ),
                            ],
                            id='€'
                        ),
                        ValueItemType(
                            name=[
                                Name(
                                    value='CNY'
                                ),
                            ],
                            description=[
                                Description(
                                    value='China Yuan Renminbi'
                                ),
                            ],
                            id='¥'
                        ),
                        ValueItemType(
                            name=[
                                Name(
                                    value='IRR'
                                ),
                            ],
                            description=[
                                Description(
                                    value='Iran Rial'
                                ),
                            ],
                            id='﷼'
                        ),
                        ValueItemType(
                            name=[
                                Name(
                                    value='JPY'
                                ),
                            ],
                            description=[
                                Description(
                                    value='Japan Yen'
                                ),
                            ],
                            id='¥'
                        ),
                    ]
                ),
            ]
        )
    )
)
