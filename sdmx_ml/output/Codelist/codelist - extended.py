from sdmx_ml.models.codelist_extension_type import CodelistExtensionType
from sdmx_ml.models.codelist_type import CodelistType
from sdmx_ml.models.codelists_type import CodelistsType
from sdmx_ml.models.description import Description
from sdmx_ml.models.item_type import Code
from sdmx_ml.models.member_value_type import MemberValueType
from sdmx_ml.models.name import Name
from sdmx_ml.models.party_type import PartyType
from sdmx_ml.models.sender_type import SenderType
from sdmx_ml.models.structure import Structure
from sdmx_ml.models.structure_header_type import StructureHeaderType
from sdmx_ml.models.structures_type import StructuresType
from xsdata.models.datatype import XmlDateTime


obj = Structure(
    header=StructureHeaderType(
        id='IREF257793',
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
        codelists=CodelistsType(
            codelist=[
                CodelistType(
                    id='CL_AGE',
                    urn='urn:sdmx:org.sdmx.infomodel.codelist.Codelist=SDMX:CL_AGE(1.0)',
                    name=[
                        Name(
                            value='Age'
                        ),
                    ],
                    description=[
                        Description(
                            value='This code list provides a set of building blocks to be used for creating simple or complex code identifiers relating to the concept of "age" as defined in the Cross-Domain Concepts and the Metadata Common Vocabulary, i.e. the length of time that a person has lived or a thing has existed. This code list was formally adopted on 7 February 2014. More information about and supporting material for this code list and SDMX code lists in general (e.g. list of generic codes for expressing general concepts like "Total", "Unknown", etc.; syntaxes for the creation of further codes; general guidelines for the creation of SDMX code lists) can be found at this address: https://sdmx.org/?page_id=4345.'
                        ),
                    ],
                    version='1.0',
                    agency_id='SDMX',
                    structure_url='https://registry.sdmx.org/FusionRegistry/ws/rest/codelist/SDMX/CL_AGE/1.0',
                    choice=[
                        Code(
                            id='Y',
                            urn='urn:sdmx:org.sdmx.infomodel.codelist.Code=SDMX:CL_AGE(1.0).Y',
                            name=[
                                Name(
                                    value='Year(s)'
                                ),
                            ]
                        ),
                        Code(
                            id='M',
                            urn='urn:sdmx:org.sdmx.infomodel.codelist.Code=SDMX:CL_AGE(1.0).M',
                            name=[
                                Name(
                                    value='Month(s)'
                                ),
                            ]
                        ),
                        Code(
                            id='W',
                            urn='urn:sdmx:org.sdmx.infomodel.codelist.Code=SDMX:CL_AGE(1.0).W',
                            name=[
                                Name(
                                    value='Week(s)'
                                ),
                            ]
                        ),
                        Code(
                            id='D',
                            urn='urn:sdmx:org.sdmx.infomodel.codelist.Code=SDMX:CL_AGE(1.0).D',
                            name=[
                                Name(
                                    value='Day(s)'
                                ),
                            ]
                        ),
                        Code(
                            id='H',
                            urn='urn:sdmx:org.sdmx.infomodel.codelist.Code=SDMX:CL_AGE(1.0).H',
                            name=[
                                Name(
                                    value='Hour(s)'
                                ),
                            ]
                        ),
                    ]
                ),
                CodelistType(
                    id='CL_EXTENDED_AGE',
                    urn='urn:sdmx:org.sdmx.infomodel.codelist.Codelist=EXAMPLE:CL_EXTENDED_AGE(1.0)',
                    name=[
                        Name(
                            value='Age'
                        ),
                    ],
                    description=[
                        Description(
                            value='An extension to the SDMX:CL_AGE Codelist adding finer-grained time identifiers for short-lived events and objects. Years are irrelevant in this use case, so the "Y" code is excluded from the extended codelist.'
                        ),
                    ],
                    version='1.0',
                    agency_id='EXAMPLE',
                    choice=[
                        Code(
                            id='I',
                            urn='urn:sdmx:org.sdmx.infomodel.codelist.Code=EXAMPLE:CL_EXTENDED_AGE(1.0).I',
                            name=[
                                Name(
                                    value='Minutes(s)'
                                ),
                            ]
                        ),
                        Code(
                            id='S',
                            urn='urn:sdmx:org.sdmx.infomodel.codelist.Code=EXAMPLE:CL_EXTENDED_AGE(1.0).S',
                            name=[
                                Name(
                                    value='Seconds(s)'
                                ),
                            ]
                        ),
                    ],
                    codelist_extension=[
                        CodelistExtensionType(
                            codelist='urn:sdmx:org.sdmx.infomodel.codelist.Codelist=SDMX:CL_AGE(1.0)',
                            inclusive_code_selection_or_exclusive_code_selection=CodelistExtensionType.ExclusiveCodeSelection(
                                member_value=[
                                    MemberValueType(
                                        value='Y'
                                    ),
                                ]
                            )
                        ),
                    ]
                ),
            ]
        )
    )
)
