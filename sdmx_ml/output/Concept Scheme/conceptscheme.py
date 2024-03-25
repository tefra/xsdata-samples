from sdmx_ml.models.concept_scheme_type import ConceptSchemeType
from sdmx_ml.models.concept_schemes_type import ConceptSchemesType
from sdmx_ml.models.item_type import Concept
from sdmx_ml.models.name import Name
from sdmx_ml.models.party_type import PartyType
from sdmx_ml.models.sender_type import SenderType
from sdmx_ml.models.structure import Structure
from sdmx_ml.models.structure_header_type import StructureHeaderType
from sdmx_ml.models.structures_type import StructuresType
from xsdata.models.datatype import XmlDateTime


obj = Structure(
    header=StructureHeaderType(
        id='IREF407410',
        prepared=XmlDateTime(2021, 3, 8, 21, 59, 8, 0, 0),
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
                    id='ECB_CONCEPTS',
                    urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.ConceptScheme=ECB:ECB_CONCEPTS(1.0)',
                    name=[
                        Name(
                            value='ECB concepts'
                        ),
                    ],
                    version='1.0',
                    agency_id='ECB',
                    choice=[
                        Concept(
                            id='COUNT_AREA',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).COUNT_AREA',
                            name=[
                                Name(
                                    value='Counterpart area'
                                ),
                            ]
                        ),
                        Concept(
                            id='CURRENCY',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).CURRENCY',
                            name=[
                                Name(
                                    value='Currency'
                                ),
                            ]
                        ),
                        Concept(
                            id='DATA_TYPE_PDF',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).DATA_TYPE_PDF',
                            name=[
                                Name(
                                    value='Data type in the PDF context'
                                ),
                            ]
                        ),
                        Concept(
                            id='SUFFIX_QNA',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).SUFFIX_QNA',
                            name=[
                                Name(
                                    value='OECD QNA suffix'
                                ),
                            ]
                        ),
                        Concept(
                            id='ESA95TP_TRANS',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).ESA95TP_TRANS',
                            name=[
                                Name(
                                    value='Transactions and other flows'
                                ),
                            ]
                        ),
                        Concept(
                            id='TRD_PRODUCT',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).TRD_PRODUCT',
                            name=[
                                Name(
                                    value='Product breakdown -TRD context'
                                ),
                            ]
                        ),
                        Concept(
                            id='IR_TYPE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).IR_TYPE',
                            name=[
                                Name(
                                    value='Interest rate type'
                                ),
                            ]
                        ),
                        Concept(
                            id='BDS_ITEM',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).BDS_ITEM',
                            name=[
                                Name(
                                    value='Business demography item'
                                ),
                            ]
                        ),
                        Concept(
                            id='DD_SUFFIX',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).DD_SUFFIX',
                            name=[
                                Name(
                                    value='Derived data suffix'
                                ),
                            ]
                        ),
                        Concept(
                            id='SAFE_QUESTION',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).SAFE_QUESTION',
                            name=[
                                Name(
                                    value='SAFE question'
                                ),
                            ]
                        ),
                        Concept(
                            id='BANKING_IND',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).BANKING_IND',
                            name=[
                                Name(
                                    value='Banking indicator'
                                ),
                            ]
                        ),
                        Concept(
                            id='SEC_VALUATION',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).SEC_VALUATION',
                            name=[
                                Name(
                                    value='Securities valuation'
                                ),
                            ]
                        ),
                        Concept(
                            id='BKN_TYPE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).BKN_TYPE',
                            name=[
                                Name(
                                    value='Banknote or coin'
                                ),
                            ]
                        ),
                        Concept(
                            id='STS_CONCEPT',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).STS_CONCEPT',
                            name=[
                                Name(
                                    value='Concept - STS context'
                                ),
                            ]
                        ),
                        Concept(
                            id='FM_OUTS_AMOUNT',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).FM_OUTS_AMOUNT',
                            name=[
                                Name(
                                    value='Outstanding amount'
                                ),
                            ]
                        ),
                        Concept(
                            id='DD_ECON_CONCEPT',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).DD_ECON_CONCEPT',
                            name=[
                                Name(
                                    value='Derived data economic concept'
                                ),
                            ]
                        ),
                        Concept(
                            id='MATURITY_CAT',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).MATURITY_CAT',
                            name=[
                                Name(
                                    value='Maturity category'
                                ),
                            ]
                        ),
                        Concept(
                            id='OBS_STATUS',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).OBS_STATUS',
                            name=[
                                Name(
                                    value='Observation status'
                                ),
                            ]
                        ),
                        Concept(
                            id='STS_INSTITUTION',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).STS_INSTITUTION',
                            name=[
                                Name(
                                    value='Institution originating the data flow'
                                ),
                            ]
                        ),
                        Concept(
                            id='CB_VAL_METHOD',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).CB_VAL_METHOD',
                            name=[
                                Name(
                                    value='CBD valuation method'
                                ),
                            ]
                        ),
                        Concept(
                            id='DATA_TYPE_PSS',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).DATA_TYPE_PSS',
                            name=[
                                Name(
                                    value='PSS data type'
                                ),
                            ]
                        ),
                        Concept(
                            id='PROVIDER_FM',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).PROVIDER_FM',
                            name=[
                                Name(
                                    value='Financial market provider'
                                ),
                            ]
                        ),
                        Concept(
                            id='SSS_INFO_TYPE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).SSS_INFO_TYPE',
                            name=[
                                Name(
                                    value='Information type in securities settlement, clearing, trading context'
                                ),
                            ]
                        ),
                        Concept(
                            id='PD_ITEM',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).PD_ITEM',
                            name=[
                                Name(
                                    value='Projection database item'
                                ),
                            ]
                        ),
                        Concept(
                            id='FM_COUPON_RATE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).FM_COUPON_RATE',
                            name=[
                                Name(
                                    value='Coupon rate of the bond'
                                ),
                            ]
                        ),
                        Concept(
                            id='NON_RESID_ECON_ACT',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).NON_RESID_ECON_ACT',
                            name=[
                                Name(
                                    value='Non-resident economic activity'
                                ),
                            ]
                        ),
                        Concept(
                            id='REP_CTY',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).REP_CTY',
                            name=[
                                Name(
                                    value='Reporting country'
                                ),
                            ]
                        ),
                        Concept(
                            id='OFI_REP_SECTOR',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).OFI_REP_SECTOR',
                            name=[
                                Name(
                                    value='OFI reporting sector'
                                ),
                            ]
                        ),
                        Concept(
                            id='ESA95TP_PRICE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).ESA95TP_PRICE',
                            name=[
                                Name(
                                    value='Valuation'
                                ),
                            ]
                        ),
                        Concept(
                            id='BS_COUNT_SECTOR',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).BS_COUNT_SECTOR',
                            name=[
                                Name(
                                    value='BS counterpart sector'
                                ),
                            ]
                        ),
                        Concept(
                            id='EFFECT_DOMAIN',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).EFFECT_DOMAIN',
                            name=[
                                Name(
                                    value='Effect domain'
                                ),
                            ]
                        ),
                        Concept(
                            id='ESA95TP_CPAREA',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).ESA95TP_CPAREA',
                            name=[
                                Name(
                                    value='Counterpart area'
                                ),
                            ]
                        ),
                        Concept(
                            id='EMBARGO',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).EMBARGO',
                            name=[
                                Name(
                                    value='Embargo'
                                ),
                            ]
                        ),
                        Concept(
                            id='METHOD_PUBL',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).METHOD_PUBL',
                            name=[
                                Name(
                                    value='Methodology publication'
                                ),
                            ]
                        ),
                        Concept(
                            id='REP_DELAY',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).REP_DELAY',
                            name=[
                                Name(
                                    value='Reporting delay'
                                ),
                            ]
                        ),
                        Concept(
                            id='GOVNT_REF_SECTOR',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).GOVNT_REF_SECTOR',
                            name=[
                                Name(
                                    value='Creditor user assets sector'
                                ),
                            ]
                        ),
                        Concept(
                            id='MUFA_SOURCE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).MUFA_SOURCE',
                            name=[
                                Name(
                                    value='MUFA source'
                                ),
                            ]
                        ),
                        Concept(
                            id='AME_REFERENCE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).AME_REFERENCE',
                            name=[
                                Name(
                                    value='Ameco reference'
                                ),
                            ]
                        ),
                        Concept(
                            id='DD_TRANSF',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).DD_TRANSF',
                            name=[
                                Name(
                                    value='Derived data transformation'
                                ),
                            ]
                        ),
                        Concept(
                            id='BKN_SERIES',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).BKN_SERIES',
                            name=[
                                Name(
                                    value='Banknote/coin series'
                                ),
                            ]
                        ),
                        Concept(
                            id='WEO_ITEM',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).WEO_ITEM',
                            name=[
                                Name(
                                    value='WEO item'
                                ),
                            ]
                        ),
                        Concept(
                            id='BLS_AGG_METHOD',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).BLS_AGG_METHOD',
                            name=[
                                Name(
                                    value='BLS aggregation method'
                                ),
                            ]
                        ),
                        Concept(
                            id='ESA95TP_CONS',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).ESA95TP_CONS',
                            name=[
                                Name(
                                    value='Consolidation'
                                ),
                            ]
                        ),
                        Concept(
                            id='SOURCE_DETAIL',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).SOURCE_DETAIL',
                            name=[
                                Name(
                                    value='Source detail'
                                ),
                            ]
                        ),
                        Concept(
                            id='BOP_ITEM',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).BOP_ITEM',
                            name=[
                                Name(
                                    value='Balance of Payment item'
                                ),
                            ]
                        ),
                        Concept(
                            id='SHI_SUFFIX',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).SHI_SUFFIX',
                            name=[
                                Name(
                                    value='Series variation -SHI context'
                                ),
                            ]
                        ),
                        Concept(
                            id='SOURCE_PUBL_2',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).SOURCE_PUBL_2',
                            name=[
                                Name(
                                    value='Publication source 2'
                                ),
                            ]
                        ),
                        Concept(
                            id='FIRM_TURNOVER',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).FIRM_TURNOVER',
                            name=[
                                Name(
                                    value='Firm turnover (SAFE)'
                                ),
                            ]
                        ),
                        Concept(
                            id='IVF_REP_SECTOR',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).IVF_REP_SECTOR',
                            name=[
                                Name(
                                    value='Investment funds reporting sector'
                                ),
                            ]
                        ),
                        Concept(
                            id='TRG_ACCOUNT',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).TRG_ACCOUNT',
                            name=[
                                Name(
                                    value='Type of accounts in TARGET2'
                                ),
                            ]
                        ),
                        Concept(
                            id='COMP_METHOD',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).COMP_METHOD',
                            name=[
                                Name(
                                    value='Compiliation methodology'
                                ),
                            ]
                        ),
                        Concept(
                            id='FVC_ITEM',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).FVC_ITEM',
                            name=[
                                Name(
                                    value='Assets and liabilities item in financial vehicle corporation context'
                                ),
                            ]
                        ),
                        Concept(
                            id='OBS_VALUE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).OBS_VALUE',
                            name=[
                                Name(
                                    value='Observation value'
                                ),
                            ]
                        ),
                        Concept(
                            id='STS_SUFFIX',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).STS_SUFFIX',
                            name=[
                                Name(
                                    value='Series variation - STS context'
                                ),
                            ]
                        ),
                        Concept(
                            id='CB_EXP_TYPE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).CB_EXP_TYPE',
                            name=[
                                Name(
                                    value='CBD exposure type'
                                ),
                            ]
                        ),
                        Concept(
                            id='AREA_DEFINITION',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).AREA_DEFINITION',
                            name=[
                                Name(
                                    value='Area definition'
                                ),
                            ]
                        ),
                        Concept(
                            id='MATURITY_NOT_IRATE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).MATURITY_NOT_IRATE',
                            name=[
                                Name(
                                    value='Original maturity/Period of notice/Initial rate fixation'
                                ),
                            ]
                        ),
                        Concept(
                            id='FM_MATURITY',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).FM_MATURITY',
                            name=[
                                Name(
                                    value='Bond maturity'
                                ),
                            ]
                        ),
                        Concept(
                            id='PORTFOLIO_CAT',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).PORTFOLIO_CAT',
                            name=[
                                Name(
                                    value='Portfolio category'
                                ),
                            ]
                        ),
                        Concept(
                            id='AME_REF_AREA',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).AME_REF_AREA',
                            name=[
                                Name(
                                    value='Ameco reference area'
                                ),
                            ]
                        ),
                        Concept(
                            id='COLLECTION_DETAIL',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).COLLECTION_DETAIL',
                            name=[
                                Name(
                                    value='Collection explanation detail'
                                ),
                            ]
                        ),
                        Concept(
                            id='SOURCE_DETAIL_2',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).SOURCE_DETAIL_2',
                            name=[
                                Name(
                                    value='Source detail 2'
                                ),
                            ]
                        ),
                        Concept(
                            id='ISSUER_RBG',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).ISSUER_RBG',
                            name=[
                                Name(
                                    value='Participation of the issuer in the reporting group'
                                ),
                            ]
                        ),
                        Concept(
                            id='REPO_CPARTY',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).REPO_CPARTY',
                            name=[
                                Name(
                                    value='Repo counterparty'
                                ),
                            ]
                        ),
                        Concept(
                            id='COMPILATION',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).COMPILATION',
                            name=[
                                Name(
                                    value='Compilation'
                                ),
                            ]
                        ),
                        Concept(
                            id='METHOD_DETAIL',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).METHOD_DETAIL',
                            name=[
                                Name(
                                    value='Methodology detail'
                                ),
                            ]
                        ),
                        Concept(
                            id='MUFA_DEBT_AREA',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).MUFA_DEBT_AREA',
                            name=[
                                Name(
                                    value='MUFA debtor area'
                                ),
                            ]
                        ),
                        Concept(
                            id='ESA95TP_REGION',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).ESA95TP_REGION',
                            name=[
                                Name(
                                    value='NUTS 3 regional classification'
                                ),
                            ]
                        ),
                        Concept(
                            id='FCT_TOPIC',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).FCT_TOPIC',
                            name=[
                                Name(
                                    value='Forecast topic'
                                ),
                            ]
                        ),
                        Concept(
                            id='SUBJECT_MEI',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).SUBJECT_MEI',
                            name=[
                                Name(
                                    value='OECD MEI subject'
                                ),
                            ]
                        ),
                        Concept(
                            id='REPORTING_SECTOR',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).REPORTING_SECTOR',
                            name=[
                                Name(
                                    value='Reporting sector'
                                ),
                            ]
                        ),
                        Concept(
                            id='SAFE_ANSWER',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).SAFE_ANSWER',
                            name=[
                                Name(
                                    value='SAFE answer'
                                ),
                            ]
                        ),
                        Concept(
                            id='PD_SEAS_EX',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).PD_SEAS_EX',
                            name=[
                                Name(
                                    value='Projection database season exercise'
                                ),
                            ]
                        ),
                        Concept(
                            id='DATA_TYPE_MUFA',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).DATA_TYPE_MUFA',
                            name=[
                                Name(
                                    value='Data type - MUFAs context'
                                ),
                            ]
                        ),
                        Concept(
                            id='BLS_COUNT_DETAIL',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).BLS_COUNT_DETAIL',
                            name=[
                                Name(
                                    value='BLS counterpart motivation'
                                ),
                            ]
                        ),
                        Concept(
                            id='SEC_SUFFIX',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).SEC_SUFFIX',
                            name=[
                                Name(
                                    value='Series suffix - SEC context'
                                ),
                            ]
                        ),
                        Concept(
                            id='VIS_CTY',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).VIS_CTY',
                            name=[
                                Name(
                                    value='Vis-a-vis country'
                                ),
                            ]
                        ),
                        Concept(
                            id='SAFE_ITEM',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).SAFE_ITEM',
                            name=[
                                Name(
                                    value='SAFE question related item'
                                ),
                            ]
                        ),
                        Concept(
                            id='RT_DENOM',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).RT_DENOM',
                            name=[
                                Name(
                                    value='Real time database series denomination'
                                ),
                            ]
                        ),
                        Concept(
                            id='CONF_STATUS',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).CONF_STATUS',
                            name=[
                                Name(
                                    value='Confidentiality status'
                                ),
                            ]
                        ),
                        Concept(
                            id='DATA_TYPE_BKN',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).DATA_TYPE_BKN',
                            name=[
                                Name(
                                    value='Banknote & coin data type'
                                ),
                            ]
                        ),
                        Concept(
                            id='DATA_TYPE_LIG',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).DATA_TYPE_LIG',
                            name=[
                                Name(
                                    value='Data type - LIG context'
                                ),
                            ]
                        ),
                        Concept(
                            id='OFI_ITEM',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).OFI_ITEM',
                            name=[
                                Name(
                                    value='OFI balance sheet item'
                                ),
                            ]
                        ),
                        Concept(
                            id='REF_SECTOR',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).REF_SECTOR',
                            name=[
                                Name(
                                    value='Reference sector'
                                ),
                            ]
                        ),
                        Concept(
                            id='UNIT_INDEX_BASE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).UNIT_INDEX_BASE',
                            name=[
                                Name(
                                    value='Unit index base'
                                ),
                            ]
                        ),
                        Concept(
                            id='ESA95_SUFFIX',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).ESA95_SUFFIX',
                            name=[
                                Name(
                                    value='Series suffix - ESA95 context'
                                ),
                            ]
                        ),
                        Concept(
                            id='COUNTERPART_SECTOR',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).COUNTERPART_SECTOR',
                            name=[
                                Name(
                                    value='Counterpart sector'
                                ),
                            ]
                        ),
                        Concept(
                            id='MUFA_ITEM',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).MUFA_ITEM',
                            name=[
                                Name(
                                    value='MUFA item'
                                ),
                            ]
                        ),
                        Concept(
                            id='TRG_BAND',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).TRG_BAND',
                            name=[
                                Name(
                                    value='Value & time bands for TARGET2 operations'
                                ),
                            ]
                        ),
                        Concept(
                            id='BANKING_ITEM',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).BANKING_ITEM',
                            name=[
                                Name(
                                    value='Banking reference BS/P&L Item'
                                ),
                            ]
                        ),
                        Concept(
                            id='IN_OUT_DATA_IFI',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).IN_OUT_DATA_IFI',
                            name=[
                                Name(
                                    value='IFI input-output data'
                                ),
                            ]
                        ),
                        Concept(
                            id='OBS_COM',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).OBS_COM',
                            name=[
                                Name(
                                    value='Observation comment'
                                ),
                            ]
                        ),
                        Concept(
                            id='PSS_SYSTEM',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).PSS_SYSTEM',
                            name=[
                                Name(
                                    value='PSS entry point'
                                ),
                            ]
                        ),
                        Concept(
                            id='STOCK_FLOW',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).STOCK_FLOW',
                            name=[
                                Name(
                                    value='Stock/flow'
                                ),
                            ]
                        ),
                        Concept(
                            id='COUNT_AREA_IFS',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).COUNT_AREA_IFS',
                            name=[
                                Name(
                                    value='IFS counterpart area'
                                ),
                            ]
                        ),
                        Concept(
                            id='OPTION_TYPE_PDF',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).OPTION_TYPE_PDF',
                            name=[
                                Name(
                                    value='Option type in the PDF context'
                                ),
                            ]
                        ),
                        Concept(
                            id='PD_ORIGIN',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).PD_ORIGIN',
                            name=[
                                Name(
                                    value='Projection database data origin'
                                ),
                            ]
                        ),
                        Concept(
                            id='SAFE_DENOM',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).SAFE_DENOM',
                            name=[
                                Name(
                                    value='Denomination in SAFE context'
                                ),
                            ]
                        ),
                        Concept(
                            id='UNIT_MEASURE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).UNIT_MEASURE',
                            name=[
                                Name(
                                    value='Unit of measure'
                                ),
                            ]
                        ),
                        Concept(
                            id='ICP_SUFFIX',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).ICP_SUFFIX',
                            name=[
                                Name(
                                    value='Series variation - ICP context'
                                ),
                            ]
                        ),
                        Concept(
                            id='FM_STRIKE_PRICE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).FM_STRIKE_PRICE',
                            name=[
                                Name(
                                    value='Strike price of the options'
                                ),
                            ]
                        ),
                        Concept(
                            id='STO',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).STO',
                            name=[
                                Name(
                                    value='Stocks, Transactions, Other Flows'
                                ),
                            ]
                        ),
                        Concept(
                            id='ADJUSTMENT',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).ADJUSTMENT',
                            name=[
                                Name(
                                    value='Adjustment indicator'
                                ),
                            ]
                        ),
                        Concept(
                            id='INT_ACC_ITEM',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).INT_ACC_ITEM',
                            name=[
                                Name(
                                    value='International accounts item'
                                ),
                            ]
                        ),
                        Concept(
                            id='ADJU_DETAIL',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).ADJU_DETAIL',
                            name=[
                                Name(
                                    value='Adjustment detail'
                                ),
                            ]
                        ),
                        Concept(
                            id='UNIT_MULT',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).UNIT_MULT',
                            name=[
                                Name(
                                    value='Unit multiplier'
                                ),
                            ]
                        ),
                        Concept(
                            id='SSS_INSTRUMENT',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).SSS_INSTRUMENT',
                            name=[
                                Name(
                                    value='Instrument in securities settlement, clearing and trading context'
                                ),
                            ]
                        ),
                        Concept(
                            id='MATURITY_RES',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).MATURITY_RES',
                            name=[
                                Name(
                                    value='Residual maturity'
                                ),
                            ]
                        ),
                        Concept(
                            id='ESA95_ACCOUNT',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).ESA95_ACCOUNT',
                            name=[
                                Name(
                                    value='ESA95 account'
                                ),
                            ]
                        ),
                        Concept(
                            id='PRICE_BASE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).PRICE_BASE',
                            name=[
                                Name(
                                    value='Price base'
                                ),
                            ]
                        ),
                        Concept(
                            id='BANKING_SUFFIX',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).BANKING_SUFFIX',
                            name=[
                                Name(
                                    value='DBI suffix'
                                ),
                            ]
                        ),
                        Concept(
                            id='DATA_TYPE_IFI',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).DATA_TYPE_IFI',
                            name=[
                                Name(
                                    value='Data type - IFI context'
                                ),
                            ]
                        ),
                        Concept(
                            id='EXT_TITLE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).EXT_TITLE',
                            name=[
                                Name(
                                    value='External title'
                                ),
                            ]
                        ),
                        Concept(
                            id='VAL_ROW',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).VAL_ROW',
                            name=[
                                Name(
                                    value='Publication row value'
                                ),
                            ]
                        ),
                        Concept(
                            id='ESA95TP_BRKDWN',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).ESA95TP_BRKDWN',
                            name=[
                                Name(
                                    value='Activity/product/other brkdwns'
                                ),
                            ]
                        ),
                        Concept(
                            id='BS_REP_SECTOR',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).BS_REP_SECTOR',
                            name=[
                                Name(
                                    value='BS reference sector breakdown'
                                ),
                            ]
                        ),
                        Concept(
                            id='NOM_CURR',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).NOM_CURR',
                            name=[
                                Name(
                                    value='Nominal currency of the security'
                                ),
                            ]
                        ),
                        Concept(
                            id='FM_LOT_SIZE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).FM_LOT_SIZE',
                            name=[
                                Name(
                                    value='Lot size units'
                                ),
                            ]
                        ),
                        Concept(
                            id='VAL_REPORT',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).VAL_REPORT',
                            name=[
                                Name(
                                    value='Publication sub-report value'
                                ),
                            ]
                        ),
                        Concept(
                            id='CIBL_CATEGORY',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).CIBL_CATEGORY',
                            name=[
                                Name(
                                    value='Basis, measure'
                                ),
                            ]
                        ),
                        Concept(
                            id='HOLDER_SECTOR',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).HOLDER_SECTOR',
                            name=[
                                Name(
                                    value='Holder sector'
                                ),
                            ]
                        ),
                        Concept(
                            id='REF_PERIOD_DETAIL',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).REF_PERIOD_DETAIL',
                            name=[
                                Name(
                                    value='Reference period detail'
                                ),
                            ]
                        ),
                        Concept(
                            id='CIBL_TYPE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).CIBL_TYPE',
                            name=[
                                Name(
                                    value='Data type (vis-a-vis sector / maturity / risk transfers etc.)'
                                ),
                            ]
                        ),
                        Concept(
                            id='ESA95_UNIT',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).ESA95_UNIT',
                            name=[
                                Name(
                                    value='Series unit - ESA95 context'
                                ),
                            ]
                        ),
                        Concept(
                            id='PRICE_TYPE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).PRICE_TYPE',
                            name=[
                                Name(
                                    value='Price type'
                                ),
                            ]
                        ),
                        Concept(
                            id='TPH',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).TPH',
                            name=[
                                Name(
                                    value='Third party holdings flag'
                                ),
                            ]
                        ),
                        Concept(
                            id='ORGANISATION',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).ORGANISATION',
                            name=[
                                Name(
                                    value='Organisation'
                                ),
                            ]
                        ),
                        Concept(
                            id='ESA95_BREAKDOWN',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).ESA95_BREAKDOWN',
                            name=[
                                Name(
                                    value='ESA95 breakdown'
                                ),
                            ]
                        ),
                        Concept(
                            id='FIRM_SIZE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).FIRM_SIZE',
                            name=[
                                Name(
                                    value='Firm size (SAFE)'
                                ),
                            ]
                        ),
                        Concept(
                            id='COMPILING_ORG',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).COMPILING_ORG',
                            name=[
                                Name(
                                    value='Compiling organisation'
                                ),
                            ]
                        ),
                        Concept(
                            id='RPP_SOURCE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).RPP_SOURCE',
                            name=[
                                Name(
                                    value='Source of property price statistics'
                                ),
                            ]
                        ),
                        Concept(
                            id='FVC_REP_SECTOR',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).FVC_REP_SECTOR',
                            name=[
                                Name(
                                    value='Reporting sector in financial vehicle corporation context'
                                ),
                            ]
                        ),
                        Concept(
                            id='UNIT',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).UNIT',
                            name=[
                                Name(
                                    value='Unit'
                                ),
                            ]
                        ),
                        Concept(
                            id='MEASURE_MEI',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).MEASURE_MEI',
                            name=[
                                Name(
                                    value='OECD MEI measure'
                                ),
                            ]
                        ),
                        Concept(
                            id='REF_AREA_MEI',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).REF_AREA_MEI',
                            name=[
                                Name(
                                    value='OECD MEI & QNA reference area'
                                ),
                            ]
                        ),
                        Concept(
                            id='BANKING_REF',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).BANKING_REF',
                            name=[
                                Name(
                                    value='Banking reference institution'
                                ),
                            ]
                        ),
                        Concept(
                            id='PUBL_MU',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).PUBL_MU',
                            name=[
                                Name(
                                    value='Source publication (Euro area only)'
                                ),
                            ]
                        ),
                        Concept(
                            id='ISSUER_AREA',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).ISSUER_AREA',
                            name=[
                                Name(
                                    value='Issuer domicile country'
                                ),
                            ]
                        ),
                        Concept(
                            id='PROVIDER_FM_ID',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).PROVIDER_FM_ID',
                            name=[
                                Name(
                                    value='Financial market provider identifier'
                                ),
                            ]
                        ),
                        Concept(
                            id='TRANS_TYPE_MMSR',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).TRANS_TYPE_MMSR',
                            name=[
                                Name(
                                    value='Transaction type in the Money Market context'
                                ),
                            ]
                        ),
                        Concept(
                            id='LIG_ITEM',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).LIG_ITEM',
                            name=[
                                Name(
                                    value='Large insurance group related items'
                                ),
                            ]
                        ),
                        Concept(
                            id='TRD_FLOW',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).TRD_FLOW',
                            name=[
                                Name(
                                    value='External trade flow'
                                ),
                            ]
                        ),
                        Concept(
                            id='MARKET_ROLE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).MARKET_ROLE',
                            name=[
                                Name(
                                    value='Market role'
                                ),
                            ]
                        ),
                        Concept(
                            id='ESA95TP_SECTOR',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).ESA95TP_SECTOR',
                            name=[
                                Name(
                                    value='Reporting institutional sector'
                                ),
                            ]
                        ),
                        Concept(
                            id='PRJ_PER_HORIZON',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).PRJ_PER_HORIZON',
                            name=[
                                Name(
                                    value='Period of the projection horizon - monthly NIPE, quarterly (B)MPE'
                                ),
                            ]
                        ),
                        Concept(
                            id='COMMENT_TS',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).COMMENT_TS',
                            name=[
                                Name(
                                    value='Title complement, detailed description of the series'
                                ),
                            ]
                        ),
                        Concept(
                            id='TIME_PER_COLLECT',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).TIME_PER_COLLECT',
                            name=[
                                Name(
                                    value='Time period collection'
                                ),
                            ]
                        ),
                        Concept(
                            id='CURRENCY_P_H',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).CURRENCY_P_H',
                            name=[
                                Name(
                                    value='Currency purchase - holding'
                                ),
                            ]
                        ),
                        Concept(
                            id='MATURITY_TYPE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).MATURITY_TYPE',
                            name=[
                                Name(
                                    value='Maturity type'
                                ),
                            ]
                        ),
                        Concept(
                            id='PSS_INSTRUMENT',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).PSS_INSTRUMENT',
                            name=[
                                Name(
                                    value='PSS instrument'
                                ),
                            ]
                        ),
                        Concept(
                            id='MUFA_CRED_AREA',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).MUFA_CRED_AREA',
                            name=[
                                Name(
                                    value='MUFA creditor area'
                                ),
                            ]
                        ),
                        Concept(
                            id='UNIT_DETAIL',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).UNIT_DETAIL',
                            name=[
                                Name(
                                    value='Unit detail'
                                ),
                            ]
                        ),
                        Concept(
                            id='DATA_TYPE_DBI',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).DATA_TYPE_DBI',
                            name=[
                                Name(
                                    value='Data type - DBI context'
                                ),
                            ]
                        ),
                        Concept(
                            id='VAL_ITEM',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).VAL_ITEM',
                            name=[
                                Name(
                                    value='Publication item value'
                                ),
                            ]
                        ),
                        Concept(
                            id='EXT_UNIT_MULT',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).EXT_UNIT_MULT',
                            name=[
                                Name(
                                    value='External unit multiplier'
                                ),
                            ]
                        ),
                        Concept(
                            id='AME_AGG_METHOD',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).AME_AGG_METHOD',
                            name=[
                                Name(
                                    value='Ameco aggregation method'
                                ),
                            ]
                        ),
                        Concept(
                            id='MARKET_TRANS',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).MARKET_TRANS',
                            name=[
                                Name(
                                    value='FXS market type transaction'
                                ),
                            ]
                        ),
                        Concept(
                            id='SOURCE_PUB',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).SOURCE_PUB',
                            name=[
                                Name(
                                    value='Publication source'
                                ),
                            ]
                        ),
                        Concept(
                            id='PROPERTY_CPP',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).PROPERTY_CPP',
                            name=[
                                Name(
                                    value='Property types in CPP context'
                                ),
                            ]
                        ),
                        Concept(
                            id='PUBL_PUBLIC',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).PUBL_PUBLIC',
                            name=[
                                Name(
                                    value='Source publication (public)'
                                ),
                            ]
                        ),
                        Concept(
                            id='ICP_ITEM',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).ICP_ITEM',
                            name=[
                                Name(
                                    value='Classification - ICP context'
                                ),
                            ]
                        ),
                        Concept(
                            id='SERIES_DENOM',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).SERIES_DENOM',
                            name=[
                                Name(
                                    value='Series denominat/spec calcul'
                                ),
                            ]
                        ),
                        Concept(
                            id='AME_ITEM',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).AME_ITEM',
                            name=[
                                Name(
                                    value='Ameco item'
                                ),
                            ]
                        ),
                        Concept(
                            id='EAPLUS_FLAG',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).EAPLUS_FLAG',
                            name=[
                                Name(
                                    value='EAPlus flag'
                                ),
                            ]
                        ),
                        Concept(
                            id='INSTR_TYPE_MMSR',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).INSTR_TYPE_MMSR',
                            name=[
                                Name(
                                    value='Instrument type in the Money Market context'
                                ),
                            ]
                        ),
                        Concept(
                            id='SOURCE_DATA',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).SOURCE_DATA',
                            name=[
                                Name(
                                    value='Raw statistical data source'
                                ),
                            ]
                        ),
                        Concept(
                            id='SHI_INDICATOR',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).SHI_INDICATOR',
                            name=[
                                Name(
                                    value='Structural housing indicators'
                                ),
                            ]
                        ),
                        Concept(
                            id='ISSUER_SECTOR',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).ISSUER_SECTOR',
                            name=[
                                Name(
                                    value='Issuer ESA 2010 sector'
                                ),
                            ]
                        ),
                        Concept(
                            id='IR_FV_TYPE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).IR_FV_TYPE',
                            name=[
                                Name(
                                    value='Interest rate type (fix/var)'
                                ),
                            ]
                        ),
                        Concept(
                            id='OECD_A16_CODE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).OECD_A16_CODE',
                            name=[
                                Name(
                                    value='OECD A16 code'
                                ),
                            ]
                        ),
                        Concept(
                            id='CB_REP_FRAMEWRK',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).CB_REP_FRAMEWRK',
                            name=[
                                Name(
                                    value='CBD reporting framework'
                                ),
                            ]
                        ),
                        Concept(
                            id='WOB_TAXATION',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).WOB_TAXATION',
                            name=[
                                Name(
                                    value='Weekly oil bulletin taxation'
                                ),
                            ]
                        ),
                        Concept(
                            id='BIS_BLOCK',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).BIS_BLOCK',
                            name=[
                                Name(
                                    value='International Financial Statistics block'
                                ),
                            ]
                        ),
                        Concept(
                            id='COUNT_SECTOR',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).COUNT_SECTOR',
                            name=[
                                Name(
                                    value='Counterpart sector'
                                ),
                            ]
                        ),
                        Concept(
                            id='FLOW_STOCK_ENTRY',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).FLOW_STOCK_ENTRY',
                            name=[
                                Name(
                                    value='Flows and stocks indicator'
                                ),
                            ]
                        ),
                        Concept(
                            id='DATA_TYPE_SEC',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).DATA_TYPE_SEC',
                            name=[
                                Name(
                                    value='Securities data type'
                                ),
                            ]
                        ),
                        Concept(
                            id='BIS_TOPIC',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).BIS_TOPIC',
                            name=[
                                Name(
                                    value='BIS economic phenomenon'
                                ),
                            ]
                        ),
                        Concept(
                            id='EONIA_BANK',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).EONIA_BANK',
                            name=[
                                Name(
                                    value='EONIA bank'
                                ),
                            ]
                        ),
                        Concept(
                            id='MEASURE_QNA',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).MEASURE_QNA',
                            name=[
                                Name(
                                    value='OECD QNA measure'
                                ),
                            ]
                        ),
                        Concept(
                            id='MUFA_CRED_SECTOR',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).MUFA_CRED_SECTOR',
                            name=[
                                Name(
                                    value='MUFA creditor sector'
                                ),
                            ]
                        ),
                        Concept(
                            id='OEO_CODE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).OEO_CODE',
                            name=[
                                Name(
                                    value='OEO code'
                                ),
                            ]
                        ),
                        Concept(
                            id='PRE_BREAK_VALUE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).PRE_BREAK_VALUE',
                            name=[
                                Name(
                                    value='Pre-break value'
                                ),
                            ]
                        ),
                        Concept(
                            id='DEBT_TYPE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).DEBT_TYPE',
                            name=[
                                Name(
                                    value='Debt type'
                                ),
                            ]
                        ),
                        Concept(
                            id='RT_ECON_CONCEPT',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).RT_ECON_CONCEPT',
                            name=[
                                Name(
                                    value='Real time database item'
                                ),
                            ]
                        ),
                        Concept(
                            id='ESCB_FLAG',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).ESCB_FLAG',
                            name=[
                                Name(
                                    value='ESCB flag'
                                ),
                            ]
                        ),
                        Concept(
                            id='REF_AREA',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).REF_AREA',
                            name=[
                                Name(
                                    value='Reference area'
                                ),
                            ]
                        ),
                        Concept(
                            id='CB_REP_SECTOR',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).CB_REP_SECTOR',
                            name=[
                                Name(
                                    value='CBD reference sector breakdown'
                                ),
                            ]
                        ),
                        Concept(
                            id='ACCOUNT_ENTRY',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).ACCOUNT_ENTRY',
                            name=[
                                Name(
                                    value='Accounting entries'
                                ),
                            ]
                        ),
                        Concept(
                            id='R_L_SECTOR',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).R_L_SECTOR',
                            name=[
                                Name(
                                    value='Resource or liability sector'
                                ),
                            ]
                        ),
                        Concept(
                            id='RBG_ID',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).RBG_ID',
                            name=[
                                Name(
                                    value='Reporting group'
                                ),
                            ]
                        ),
                        Concept(
                            id='TITLE_COMPL',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).TITLE_COMPL',
                            name=[
                                Name(
                                    value='Title complement'
                                ),
                            ]
                        ),
                        Concept(
                            id='CURR_BRKDWN',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).CURR_BRKDWN',
                            name=[
                                Name(
                                    value='Currency breakdown'
                                ),
                            ]
                        ),
                        Concept(
                            id='MA_FLAG',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).MA_FLAG',
                            name=[
                                Name(
                                    value='Macro-adjustment flag'
                                ),
                            ]
                        ),
                        Concept(
                            id='FM_PUT_CALL',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).FM_PUT_CALL',
                            name=[
                                Name(
                                    value='options type'
                                ),
                            ]
                        ),
                        Concept(
                            id='FM_IDENTIFIER',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).FM_IDENTIFIER',
                            name=[
                                Name(
                                    value='Financial instrument Identifier'
                                ),
                            ]
                        ),
                        Concept(
                            id='SAFE_FILTER',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).SAFE_FILTER',
                            name=[
                                Name(
                                    value='SAFE filter - applicable answer'
                                ),
                            ]
                        ),
                        Concept(
                            id='TRG_CATEGORY',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).TRG_CATEGORY',
                            name=[
                                Name(
                                    value='Type of payments in TARGET2'
                                ),
                            ]
                        ),
                        Concept(
                            id='ICPF_ITEM',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).ICPF_ITEM',
                            name=[
                                Name(
                                    value='Insurance corporations and pension funds assets and liabilities'
                                ),
                            ]
                        ),
                        Concept(
                            id='RESID_ECON_ACT',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).RESID_ECON_ACT',
                            name=[
                                Name(
                                    value='Resident economic activity'
                                ),
                            ]
                        ),
                        Concept(
                            id='ADJUST_DETAIL',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).ADJUST_DETAIL',
                            name=[
                                Name(
                                    value='Adjustment detail'
                                ),
                            ]
                        ),
                        Concept(
                            id='VALUATION',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).VALUATION',
                            name=[
                                Name(
                                    value='Valuation'
                                ),
                            ]
                        ),
                        Concept(
                            id='COMP_APPROACH',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).COMP_APPROACH',
                            name=[
                                Name(
                                    value='Compilation approach indicator'
                                ),
                            ]
                        ),
                        Concept(
                            id='FIRM_OWNERSHIP',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).FIRM_OWNERSHIP',
                            name=[
                                Name(
                                    value='Firm other breakdowns (ownership, export) (SAFE)'
                                ),
                            ]
                        ),
                        Concept(
                            id='FM_CONTRACT_TIME',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).FM_CONTRACT_TIME',
                            name=[
                                Name(
                                    value='Contract month/expired date'
                                ),
                            ]
                        ),
                        Concept(
                            id='SUBJECT_QNA',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).SUBJECT_QNA',
                            name=[
                                Name(
                                    value='OECD QNA subject'
                                ),
                            ]
                        ),
                        Concept(
                            id='MEASURE_SNA',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).MEASURE_SNA',
                            name=[
                                Name(
                                    value='OECD SNA measure'
                                ),
                            ]
                        ),
                        Concept(
                            id='PRJ_QUARTER',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).PRJ_QUARTER',
                            name=[
                                Name(
                                    value='Quarter of the projection exercise'
                                ),
                            ]
                        ),
                        Concept(
                            id='ESA95TP_DC_AL',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).ESA95TP_DC_AL',
                            name=[
                                Name(
                                    value='Uses and resources'
                                ),
                            ]
                        ),
                        Concept(
                            id='AGG_EQUN',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).AGG_EQUN',
                            name=[
                                Name(
                                    value='Aggregation equations'
                                ),
                            ]
                        ),
                        Concept(
                            id='COLLATERAL',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).COLLATERAL',
                            name=[
                                Name(
                                    value='Collateral'
                                ),
                            ]
                        ),
                        Concept(
                            id='AME_TRANSFORMATION',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).AME_TRANSFORMATION',
                            name=[
                                Name(
                                    value='Ameco transformation'
                                ),
                            ]
                        ),
                        Concept(
                            id='BIS_SUFFIX',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).BIS_SUFFIX',
                            name=[
                                Name(
                                    value='BIS suffix'
                                ),
                            ]
                        ),
                        Concept(
                            id='COUNTERPART_AREA',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).COUNTERPART_AREA',
                            name=[
                                Name(
                                    value='Counterpart area'
                                ),
                            ]
                        ),
                        Concept(
                            id='GROUP_TYPE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).GROUP_TYPE',
                            name=[
                                Name(
                                    value='Group type'
                                ),
                            ]
                        ),
                        Concept(
                            id='DATA_TYPE_BOP',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).DATA_TYPE_BOP',
                            name=[
                                Name(
                                    value='Data type - BoP related data'
                                ),
                            ]
                        ),
                        Concept(
                            id='ESA95TP_SUFFIX',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).ESA95TP_SUFFIX',
                            name=[
                                Name(
                                    value='Reference table number'
                                ),
                            ]
                        ),
                        Concept(
                            id='ICO_PAY',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).ICO_PAY',
                            name=[
                                Name(
                                    value='Insurance corporations operations item'
                                ),
                            ]
                        ),
                        Concept(
                            id='DATA_TYPE_FM',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).DATA_TYPE_FM',
                            name=[
                                Name(
                                    value='Financial market data type'
                                ),
                            ]
                        ),
                        Concept(
                            id='DATA_TYPE_MM',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).DATA_TYPE_MM',
                            name=[
                                Name(
                                    value='Data type in money market context'
                                ),
                            ]
                        ),
                        Concept(
                            id='FREQ',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).FREQ',
                            name=[
                                Name(
                                    value='Frequency'
                                ),
                            ]
                        ),
                        Concept(
                            id='BS_NFC_ACTIVITY',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).BS_NFC_ACTIVITY',
                            name=[
                                Name(
                                    value='Activity'
                                ),
                            ]
                        ),
                        Concept(
                            id='CB_SECTOR_SIZE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).CB_SECTOR_SIZE',
                            name=[
                                Name(
                                    value='CBD reference sector size'
                                ),
                            ]
                        ),
                        Concept(
                            id='CURRENCY_DENOM',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).CURRENCY_DENOM',
                            name=[
                                Name(
                                    value='Currency denominator'
                                ),
                            ]
                        ),
                        Concept(
                            id='FCT_SOURCE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).FCT_SOURCE',
                            name=[
                                Name(
                                    value='Forecaster identifier'
                                ),
                            ]
                        ),
                        Concept(
                            id='STS_CLASS',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).STS_CLASS',
                            name=[
                                Name(
                                    value='Classification - STS context'
                                ),
                            ]
                        ),
                        Concept(
                            id='PROPERTY_SUFFIX',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).PROPERTY_SUFFIX',
                            name=[
                                Name(
                                    value='Property data series variation'
                                ),
                            ]
                        ),
                        Concept(
                            id='DISS_ORG',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).DISS_ORG',
                            name=[
                                Name(
                                    value='Data dissemination organisation'
                                ),
                            ]
                        ),
                        Concept(
                            id='FIRM_SECTOR',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).FIRM_SECTOR',
                            name=[
                                Name(
                                    value='Firm economic activity (SAFE)'
                                ),
                            ]
                        ),
                        Concept(
                            id='CCP_SYSTEM',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).CCP_SYSTEM',
                            name=[
                                Name(
                                    value='System in the central counterparty clearing context'
                                ),
                            ]
                        ),
                        Concept(
                            id='EMBARGO_DETAIL',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).EMBARGO_DETAIL',
                            name=[
                                Name(
                                    value='Embargo details'
                                ),
                            ]
                        ),
                        Concept(
                            id='BS_ITEM',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).BS_ITEM',
                            name=[
                                Name(
                                    value='Balance sheet item'
                                ),
                            ]
                        ),
                        Concept(
                            id='EONIA_ITEM',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).EONIA_ITEM',
                            name=[
                                Name(
                                    value='EONIA item'
                                ),
                            ]
                        ),
                        Concept(
                            id='DATA_TYPE_EST',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).DATA_TYPE_EST',
                            name=[
                                Name(
                                    value='Data type in the ESTER context'
                                ),
                            ]
                        ),
                        Concept(
                            id='TIME_HORIZON',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).TIME_HORIZON',
                            name=[
                                Name(
                                    value='Time horizon'
                                ),
                            ]
                        ),
                        Concept(
                            id='BREAKS',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).BREAKS',
                            name=[
                                Name(
                                    value='Breaks'
                                ),
                            ]
                        ),
                        Concept(
                            id='GOVNT_COUNT_SECTOR',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).GOVNT_COUNT_SECTOR',
                            name=[
                                Name(
                                    value='Debtor resource liabil sector'
                                ),
                            ]
                        ),
                        Concept(
                            id='SOURCE_AGENCY_2',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).SOURCE_AGENCY_2',
                            name=[
                                Name(
                                    value='Source agency 2'
                                ),
                            ]
                        ),
                        Concept(
                            id='FVC_ORI_SECTOR',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).FVC_ORI_SECTOR',
                            name=[
                                Name(
                                    value='Originator sector in financial vehicle corporation context'
                                ),
                            ]
                        ),
                        Concept(
                            id='OLV_INDICATOR',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).OLV_INDICATOR',
                            name=[
                                Name(
                                    value='Oversight Indicators'
                                ),
                            ]
                        ),
                        Concept(
                            id='CURRENCY_TRANS',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).CURRENCY_TRANS',
                            name=[
                                Name(
                                    value='Currency of transaction'
                                ),
                            ]
                        ),
                        Concept(
                            id='MFI_LIST',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).MFI_LIST',
                            name=[
                                Name(
                                    value='MFI category'
                                ),
                            ]
                        ),
                        Concept(
                            id='EXR_SUFFIX',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).EXR_SUFFIX',
                            name=[
                                Name(
                                    value='Series variation - EXR context'
                                ),
                            ]
                        ),
                        Concept(
                            id='HOLDER_AREA',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).HOLDER_AREA',
                            name=[
                                Name(
                                    value='Holder country'
                                ),
                            ]
                        ),
                        Concept(
                            id='BKN_DENOM',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).BKN_DENOM',
                            name=[
                                Name(
                                    value='BKN denomination breakdown'
                                ),
                            ]
                        ),
                        Concept(
                            id='MATURITY',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).MATURITY',
                            name=[
                                Name(
                                    value='Maturity'
                                ),
                            ]
                        ),
                        Concept(
                            id='MM_SEGMENT',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).MM_SEGMENT',
                            name=[
                                Name(
                                    value='Money market segment'
                                ),
                            ]
                        ),
                        Concept(
                            id='INSTRUMENT_FM',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).INSTRUMENT_FM',
                            name=[
                                Name(
                                    value='Financial market instrument'
                                ),
                            ]
                        ),
                        Concept(
                            id='COMMENT_OBS',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).COMMENT_OBS',
                            name=[
                                Name(
                                    value='Comments to the observation value'
                                ),
                            ]
                        ),
                        Concept(
                            id='DOM_SER_IDS',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).DOM_SER_IDS',
                            name=[
                                Name(
                                    value='Domestic series ids'
                                ),
                            ]
                        ),
                        Concept(
                            id='GOVNT_ST_SUFFIX',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).GOVNT_ST_SUFFIX',
                            name=[
                                Name(
                                    value='Series variation - GST context'
                                ),
                            ]
                        ),
                        Concept(
                            id='SEC_ITEM',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).SEC_ITEM',
                            name=[
                                Name(
                                    value='Securities item'
                                ),
                            ]
                        ),
                        Concept(
                            id='GOVNT_VALUATION',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).GOVNT_VALUATION',
                            name=[
                                Name(
                                    value='Valuation - GST context'
                                ),
                            ]
                        ),
                        Concept(
                            id='FCT_BREAKDOWN',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).FCT_BREAKDOWN',
                            name=[
                                Name(
                                    value='Forecast histograph breakdown'
                                ),
                            ]
                        ),
                        Concept(
                            id='FLOATING_RATE_BASE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).FLOATING_RATE_BASE',
                            name=[
                                Name(
                                    value='Floating rate base'
                                ),
                            ]
                        ),
                        Concept(
                            id='WOB_CONCEPT',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).WOB_CONCEPT',
                            name=[
                                Name(
                                    value='Weekly oil bulletin concept'
                                ),
                            ]
                        ),
                        Concept(
                            id='DATA_TYPE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).DATA_TYPE',
                            name=[
                                Name(
                                    value='Data type'
                                ),
                            ]
                        ),
                        Concept(
                            id='SEC_ISSUING_SECTOR',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).SEC_ISSUING_SECTOR',
                            name=[
                                Name(
                                    value='Securities issuing sector'
                                ),
                            ]
                        ),
                        Concept(
                            id='CURRENCY_S',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).CURRENCY_S',
                            name=[
                                Name(
                                    value='Currency sale'
                                ),
                            ]
                        ),
                        Concept(
                            id='IVF_ITEM',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).IVF_ITEM',
                            name=[
                                Name(
                                    value='Investment funds item'
                                ),
                            ]
                        ),
                        Concept(
                            id='NAT_TITLE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).NAT_TITLE',
                            name=[
                                Name(
                                    value='National language title'
                                ),
                            ]
                        ),
                        Concept(
                            id='BLS_ITEM',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).BLS_ITEM',
                            name=[
                                Name(
                                    value='Bank lending survey item'
                                ),
                            ]
                        ),
                        Concept(
                            id='CIBL_TABLE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).CIBL_TABLE',
                            name=[
                                Name(
                                    value='Type of reporting banks'
                                ),
                            ]
                        ),
                        Concept(
                            id='PSS_INFO_TYPE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).PSS_INFO_TYPE',
                            name=[
                                Name(
                                    value='PSS information type'
                                ),
                            ]
                        ),
                        Concept(
                            id='EXT_REF_AREA',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).EXT_REF_AREA',
                            name=[
                                Name(
                                    value='External reference area'
                                ),
                            ]
                        ),
                        Concept(
                            id='OBS_PRE_BREAK',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).OBS_PRE_BREAK',
                            name=[
                                Name(
                                    value='Pre-break observation value'
                                ),
                            ]
                        ),
                        Concept(
                            id='BOP_BASIS',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).BOP_BASIS',
                            name=[
                                Name(
                                    value='BoP data collection basis'
                                ),
                            ]
                        ),
                        Concept(
                            id='DATA_TYPE_MIR',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).DATA_TYPE_MIR',
                            name=[
                                Name(
                                    value='MFI interest rate data type'
                                ),
                            ]
                        ),
                        Concept(
                            id='MODEL_ASSUMP_ERR',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).MODEL_ASSUMP_ERR',
                            name=[
                                Name(
                                    value='Model assumption error'
                                ),
                            ]
                        ),
                        Concept(
                            id='TRD_SUFFIX',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).TRD_SUFFIX',
                            name=[
                                Name(
                                    value='Series variation -TRD context'
                                ),
                            ]
                        ),
                        Concept(
                            id='INS_BUS_TYPE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).INS_BUS_TYPE',
                            name=[
                                Name(
                                    value='Type of insurance business'
                                ),
                            ]
                        ),
                        Concept(
                            id='MUFA_VALUATION',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).MUFA_VALUATION',
                            name=[
                                Name(
                                    value='MUFAs valuation'
                                ),
                            ]
                        ),
                        Concept(
                            id='CB_PORTFOLIO',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).CB_PORTFOLIO',
                            name=[
                                Name(
                                    value='CBD portfolio'
                                ),
                            ]
                        ),
                        Concept(
                            id='OIL_PRODUCT',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).OIL_PRODUCT',
                            name=[
                                Name(
                                    value='Oil product'
                                ),
                            ]
                        ),
                        Concept(
                            id='SSS_SYSTEM',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).SSS_SYSTEM',
                            name=[
                                Name(
                                    value='System in securities settlement and clearing context'
                                ),
                            ]
                        ),
                        Concept(
                            id='METHOD_REF',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).METHOD_REF',
                            name=[
                                Name(
                                    value='Methodology reference'
                                ),
                            ]
                        ),
                        Concept(
                            id='SOURCE_AGENCY',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).SOURCE_AGENCY',
                            name=[
                                Name(
                                    value='Source agency'
                                ),
                            ]
                        ),
                        Concept(
                            id='FCT_HORIZON',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).FCT_HORIZON',
                            name=[
                                Name(
                                    value='Forecast horizon'
                                ),
                            ]
                        ),
                        Concept(
                            id='WEO_REF_AREA',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).WEO_REF_AREA',
                            name=[
                                Name(
                                    value='WEO reference area'
                                ),
                            ]
                        ),
                        Concept(
                            id='DATA_TYPE_FXS',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).DATA_TYPE_FXS',
                            name=[
                                Name(
                                    value='Data type in FXS context'
                                ),
                            ]
                        ),
                        Concept(
                            id='NA_PRICE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).NA_PRICE',
                            name=[
                                Name(
                                    value='Nat accounts price reference'
                                ),
                            ]
                        ),
                        Concept(
                            id='IFS_CODE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).IFS_CODE',
                            name=[
                                Name(
                                    value='IFS code'
                                ),
                            ]
                        ),
                        Concept(
                            id='SSI_INDICATOR',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).SSI_INDICATOR',
                            name=[
                                Name(
                                    value='Structural statist indicator'
                                ),
                            ]
                        ),
                        Concept(
                            id='PUBLICATION',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).PUBLICATION',
                            name=[
                                Name(
                                    value='ECB publication'
                                ),
                            ]
                        ),
                        Concept(
                            id='BKN_ITEM',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).BKN_ITEM',
                            name=[
                                Name(
                                    value='Banknote & coin related items'
                                ),
                            ]
                        ),
                        Concept(
                            id='OTHER_METH_EXPL',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).OTHER_METH_EXPL',
                            name=[
                                Name(
                                    value='Methodological explanation'
                                ),
                            ]
                        ),
                        Concept(
                            id='IS_IN_EADB',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).IS_IN_EADB',
                            name=[
                                Name(
                                    value='Is in EADB'
                                ),
                            ]
                        ),
                        Concept(
                            id='BS_SUFFIX',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).BS_SUFFIX',
                            name=[
                                Name(
                                    value='Balance sheet suffix'
                                ),
                            ]
                        ),
                        Concept(
                            id='TR_TYPE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).TR_TYPE',
                            name=[
                                Name(
                                    value='Transaction type'
                                ),
                            ]
                        ),
                        Concept(
                            id='ESA95TP_CPSECTOR',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).ESA95TP_CPSECTOR',
                            name=[
                                Name(
                                    value='Counterpart institution sector'
                                ),
                            ]
                        ),
                        Concept(
                            id='VAL_COLUMN',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).VAL_COLUMN',
                            name=[
                                Name(
                                    value='Publication column value'
                                ),
                            ]
                        ),
                        Concept(
                            id='PROPERTY_IND',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).PROPERTY_IND',
                            name=[
                                Name(
                                    value='Property indicator'
                                ),
                            ]
                        ),
                        Concept(
                            id='MM_BANK',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).MM_BANK',
                            name=[
                                Name(
                                    value='Money market bank'
                                ),
                            ]
                        ),
                        Concept(
                            id='MUFA_DEBT_SECTOR',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).MUFA_DEBT_SECTOR',
                            name=[
                                Name(
                                    value='MUFA debtor sector'
                                ),
                            ]
                        ),
                        Concept(
                            id='FIRM_AGE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).FIRM_AGE',
                            name=[
                                Name(
                                    value='Firm age (SAFE)'
                                ),
                            ]
                        ),
                        Concept(
                            id='DATA_COMP',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).DATA_COMP',
                            name=[
                                Name(
                                    value='Underlying compilation'
                                ),
                            ]
                        ),
                        Concept(
                            id='METHOD_AGENCY',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).METHOD_AGENCY',
                            name=[
                                Name(
                                    value='Methodology agency'
                                ),
                            ]
                        ),
                        Concept(
                            id='ESA95TP_DENOM',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).ESA95TP_DENOM',
                            name=[
                                Name(
                                    value='Denomination'
                                ),
                            ]
                        ),
                        Concept(
                            id='PUBL_ECB',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).PUBL_ECB',
                            name=[
                                Name(
                                    value='Source publication (ECB only)'
                                ),
                            ]
                        ),
                        Concept(
                            id='RPP_GEO_COV',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).RPP_GEO_COV',
                            name=[
                                Name(
                                    value='Property geographical coverage'
                                ),
                            ]
                        ),
                        Concept(
                            id='BENCHMARK_ITEM',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).BENCHMARK_ITEM',
                            name=[
                                Name(
                                    value='Benchmark item'
                                ),
                            ]
                        ),
                        Concept(
                            id='RPP_SUFFIX',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).RPP_SUFFIX',
                            name=[
                                Name(
                                    value='Series variation - RPP context'
                                ),
                            ]
                        ),
                        Concept(
                            id='AVAILABILITY',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).AVAILABILITY',
                            name=[
                                Name(
                                    value='Availability'
                                ),
                            ]
                        ),
                        Concept(
                            id='CB_ITEM',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).CB_ITEM',
                            name=[
                                Name(
                                    value='Consolidated banking data item'
                                ),
                            ]
                        ),
                        Concept(
                            id='ESA95TP_ASSET',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).ESA95TP_ASSET',
                            name=[
                                Name(
                                    value='Asset/instr classification'
                                ),
                            ]
                        ),
                        Concept(
                            id='MFI_STATUS',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).MFI_STATUS',
                            name=[
                                Name(
                                    value='MFI status'
                                ),
                            ]
                        ),
                        Concept(
                            id='CREDIT_RATING',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).CREDIT_RATING',
                            name=[
                                Name(
                                    value='Programme credit rating'
                                ),
                            ]
                        ),
                        Concept(
                            id='BLS_COUNT',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).BLS_COUNT',
                            name=[
                                Name(
                                    value='BLS contract counterpart'
                                ),
                            ]
                        ),
                        Concept(
                            id='RIR_SUFFIX',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).RIR_SUFFIX',
                            name=[
                                Name(
                                    value='Series variation - IR context'
                                ),
                            ]
                        ),
                        Concept(
                            id='IR_BUS_COV',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).IR_BUS_COV',
                            name=[
                                Name(
                                    value='IR business coverage'
                                ),
                            ]
                        ),
                        Concept(
                            id='OBS_CONF',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).OBS_CONF',
                            name=[
                                Name(
                                    value='Observation confidentiality'
                                ),
                            ]
                        ),
                        Concept(
                            id='SECURITY_TYPE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).SECURITY_TYPE',
                            name=[
                                Name(
                                    value='Security type'
                                ),
                            ]
                        ),
                        Concept(
                            id='INSTR_ASSET',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).INSTR_ASSET',
                            name=[
                                Name(
                                    value='Instrument and assets classification'
                                ),
                            ]
                        ),
                        Concept(
                            id='EXR_TYPE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).EXR_TYPE',
                            name=[
                                Name(
                                    value='Exchange rate type'
                                ),
                            ]
                        ),
                        Concept(
                            id='SURVEY_FREQ',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).SURVEY_FREQ',
                            name=[
                                Name(
                                    value='Frequency of the survey'
                                ),
                            ]
                        ),
                        Concept(
                            id='COVERAGE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).COVERAGE',
                            name=[
                                Name(
                                    value='Coverage'
                                ),
                            ]
                        ),
                        Concept(
                            id='UNIT_PRICE_BASE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).UNIT_PRICE_BASE',
                            name=[
                                Name(
                                    value='Unit price base'
                                ),
                            ]
                        ),
                        Concept(
                            id='U_A_SECTOR',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).U_A_SECTOR',
                            name=[
                                Name(
                                    value='Use or asset sector'
                                ),
                            ]
                        ),
                        Concept(
                            id='GOVNT_ITEM_ESA',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).GOVNT_ITEM_ESA',
                            name=[
                                Name(
                                    value='ESA item - GST context'
                                ),
                            ]
                        ),
                        Concept(
                            id='DECIMALS',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).DECIMALS',
                            name=[
                                Name(
                                    value='Decimals'
                                ),
                            ]
                        ),
                        Concept(
                            id='MATURITY_ORIG',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).MATURITY_ORIG',
                            name=[
                                Name(
                                    value='Original maturity'
                                ),
                            ]
                        ),
                        Concept(
                            id='MFI_LIST_IND',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).MFI_LIST_IND',
                            name=[
                                Name(
                                    value='Individual MFI list'
                                ),
                            ]
                        ),
                        Concept(
                            id='TRG_ANCILLARY',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).TRG_ANCILLARY',
                            name=[
                                Name(
                                    value='Ancillary systems settling in TARGET2'
                                ),
                            ]
                        ),
                        Concept(
                            id='CPP_METHOD',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).CPP_METHOD',
                            name=[
                                Name(
                                    value='Method in CPP context'
                                ),
                            ]
                        ),
                        Concept(
                            id='EXT_UNIT',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).EXT_UNIT',
                            name=[
                                Name(
                                    value='External unit'
                                ),
                            ]
                        ),
                        Concept(
                            id='ESA95TP_COM',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).ESA95TP_COM',
                            name=[
                                Name(
                                    value='Product breakdown'
                                ),
                            ]
                        ),
                        Concept(
                            id='COLLECTION',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).COLLECTION',
                            name=[
                                Name(
                                    value='Collection indicator'
                                ),
                            ]
                        ),
                        Concept(
                            id='RPP_DWELLING',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).RPP_DWELLING',
                            name=[
                                Name(
                                    value='Type of residential property'
                                ),
                            ]
                        ),
                        Concept(
                            id='AMOUNT_CAT',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).AMOUNT_CAT',
                            name=[
                                Name(
                                    value='Amount category'
                                ),
                            ]
                        ),
                        Concept(
                            id='BANK_SELECTION',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).BANK_SELECTION',
                            name=[
                                Name(
                                    value='Bank selection'
                                ),
                            ]
                        ),
                        Concept(
                            id='ICO_UNIT',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).ICO_UNIT',
                            name=[
                                Name(
                                    value='Insurance corporations operations unit'
                                ),
                            ]
                        ),
                        Concept(
                            id='ISSUER_IN',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).ISSUER_IN',
                            name=[
                                Name(
                                    value='Split into EMU/non-EMU issuer'
                                ),
                            ]
                        ),
                        Concept(
                            id='TITLE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).TITLE',
                            name=[
                                Name(
                                    value='Title'
                                ),
                            ]
                        ),
                        Concept(
                            id='SUBJECT_SNA',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).SUBJECT_SNA',
                            name=[
                                Name(
                                    value='OECD SNA subject'
                                ),
                            ]
                        ),
                        Concept(
                            id='FXS_OP_TYPE',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).FXS_OP_TYPE',
                            name=[
                                Name(
                                    value='Operation type in FXS context'
                                ),
                            ]
                        ),
                        Concept(
                            id='SEE_SYSTEM',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).SEE_SYSTEM',
                            name=[
                                Name(
                                    value='System in securities exchange (trading) context'
                                ),
                            ]
                        ),
                        Concept(
                            id='SECURITISATION_TYP',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).SECURITISATION_TYP',
                            name=[
                                Name(
                                    value='Asset securitisation type'
                                ),
                            ]
                        ),
                        Concept(
                            id='TIME_FORMAT',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).TIME_FORMAT',
                            name=[
                                Name(
                                    value='Time format code'
                                ),
                            ]
                        ),
                        Concept(
                            id='FUNCTIONAL_CAT',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).FUNCTIONAL_CAT',
                            name=[
                                Name(
                                    value='Functional category'
                                ),
                            ]
                        ),
                        Concept(
                            id='TRADE_WEIGHT',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).TRADE_WEIGHT',
                            name=[
                                Name(
                                    value='Weight in trade flows'
                                ),
                            ]
                        ),
                        Concept(
                            id='SUBJECT_OEO',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).SUBJECT_OEO',
                            name=[
                                Name(
                                    value='OECD Economic Outlook subject'
                                ),
                            ]
                        ),
                        Concept(
                            id='AME_UNIT',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).AME_UNIT',
                            name=[
                                Name(
                                    value='Ameco unit'
                                ),
                            ]
                        ),
                        Concept(
                            id='TIME_PERIOD',
                            urn='urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=ECB:ECB_CONCEPTS(1.0).TIME_PERIOD',
                            name=[
                                Name(
                                    value='Time period or range'
                                ),
                            ]
                        ),
                    ]
                ),
            ]
        )
    )
)
