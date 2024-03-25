from sdmx_ml.models.description import Description
from sdmx_ml.models.geographic_codelist_type import GeographicCodelistType
from sdmx_ml.models.geographic_codelists_type import GeographicCodelistsType
from sdmx_ml.models.item_type import GeoFeatureSetCode
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
        geographic_codelists=GeographicCodelistsType(
            geographic_codelist=[
                GeographicCodelistType(
                    id='CL_ADMIN_AREA',
                    urn='urn:sdmx:org.sdmx.infomodel.codelist.Codelist=EXAMPLE:CL_ADMIN_AREA(1.0)',
                    name=[
                        Name(
                            value='Administrative Area'
                        ),
                    ],
                    description=[
                        Description(
                            value='Example Geographic Codelist for administrative areas. The geography for each area is defined by a Geo Feature Set potentially consisting of any number of Features which can be areas, lines or points. The codes are used as normal in data.'
                        ),
                    ],
                    version='1.0',
                    agency_id='EXAMPLE',
                    choice=[
                        GeoFeatureSetCode(
                            id='A1',
                            urn='urn:sdmx:org.sdmx.infomodel.codelist.Code=EXAMPLE:CL_ADMIN_AREA(1.0).A1',
                            name=[
                                Name(
                                    value='Admin Area 1'
                                ),
                            ],
                            value='CRS, PRECISION: {(POLYGON Z ((X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), (X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), …), POLYGON Z ((X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), (X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), …), POLYGON Z ((X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), (X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), …), …): GEO _DESCRIPTION}, {(POLYGON Z ((X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), (X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), …), POLYGON Z ((X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), (X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), …), POLYGON Z ((X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), (X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), …), …): GEO _DESCRIPTION}, …: GEO_DESCRIPTION'
                        ),
                        GeoFeatureSetCode(
                            id='A2',
                            urn='urn:sdmx:org.sdmx.infomodel.codelist.Code=EXAMPLE:CL_ADMIN_AREA(1.0).A1',
                            name=[
                                Name(
                                    value='Admin Area 2'
                                ),
                            ],
                            value='CRS, PRECISION: {(POLYGON Z ((X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), (X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), …), POLYGON Z ((X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), (X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), …), POLYGON Z ((X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), (X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), …), …): GEO _DESCRIPTION}, {(POLYGON Z ((X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), (X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), …), POLYGON Z ((X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), (X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), …), POLYGON Z ((X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), (X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), …), …): GEO _DESCRIPTION}, …: GEO_DESCRIPTION'
                        ),
                        GeoFeatureSetCode(
                            id='A3',
                            urn='urn:sdmx:org.sdmx.infomodel.codelist.Code=EXAMPLE:CL_ADMIN_AREA(1.0).A1',
                            name=[
                                Name(
                                    value='Admin Area 3'
                                ),
                            ],
                            value='CRS, PRECISION: {(POLYGON Z ((X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), (X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), …), POLYGON Z ((X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), (X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), …), POLYGON Z ((X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), (X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), …), …): GEO _DESCRIPTION}, {(POLYGON Z ((X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), (X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), …), POLYGON Z ((X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), (X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), …), POLYGON Z ((X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), (X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), …), …): GEO _DESCRIPTION}, …: GEO_DESCRIPTION'
                        ),
                    ]
                ),
            ]
        )
    )
)
