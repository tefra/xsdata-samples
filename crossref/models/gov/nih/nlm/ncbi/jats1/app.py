from dataclasses import dataclass, field
from typing import List, Optional, Union
from crossref.models.gov.nih.nlm.ncbi.jats1.annotation import (
    Address,
    Alternatives,
    Answer,
    AnswerSet,
    Array,
    BlockAlternatives,
    BoxedText,
    ChemStructWrap,
    Code,
    DefList,
    DispFormula,
    DispFormulaGroup,
    DispQuote,
    Explanation,
    Fig,
    FigGroup,
    FnGroup,
    Glossary,
    Graphic,
    Label,
    ListType,
    Media,
    P,
    Permissions,
    Preformat,
    Question,
    QuestionWrap,
    QuestionWrapGroup,
    RefList,
    RelatedArticle,
    RelatedObject,
    Sec,
    SecMeta,
    Speech,
    Statement,
    SupplementaryMaterial,
    TableWrap,
    TableWrapGroup,
    Title,
    VerseGroup,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.tex_math import TexMath
from crossref.models.org.w3.pkg_1998.math.math_ml.math import Math
from crossref.models.xml.lang_value import LangValue

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class App:
    """<div>

    <h3>Appendix</h3> </div>
    """
    class Meta:
        name = "app"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    sec_meta: Optional[SecMeta] = field(
        default=None,
        metadata={
            "name": "sec-meta",
            "type": "Element",
        }
    )
    label: Optional[Label] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    title: List[Title] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequence": 5189,
        }
    )
    address: List[Address] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 5193,
        }
    )
    alternatives: List[Alternatives] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 5193,
        }
    )
    answer: List[Answer] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 5193,
        }
    )
    answer_set: List[AnswerSet] = field(
        default_factory=list,
        metadata={
            "name": "answer-set",
            "type": "Element",
            "sequence": 5193,
        }
    )
    array: List[Array] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 5193,
        }
    )
    block_alternatives: List[BlockAlternatives] = field(
        default_factory=list,
        metadata={
            "name": "block-alternatives",
            "type": "Element",
            "sequence": 5193,
        }
    )
    boxed_text: List[BoxedText] = field(
        default_factory=list,
        metadata={
            "name": "boxed-text",
            "type": "Element",
            "sequence": 5193,
        }
    )
    chem_struct_wrap: List[ChemStructWrap] = field(
        default_factory=list,
        metadata={
            "name": "chem-struct-wrap",
            "type": "Element",
            "sequence": 5193,
        }
    )
    code: List[Code] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 5193,
        }
    )
    explanation: List[Explanation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 5193,
        }
    )
    fig: List[Fig] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 5193,
        }
    )
    fig_group: List[FigGroup] = field(
        default_factory=list,
        metadata={
            "name": "fig-group",
            "type": "Element",
            "sequence": 5193,
        }
    )
    graphic: List[Graphic] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 5193,
        }
    )
    media: List[Media] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 5193,
        }
    )
    preformat: List[Preformat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 5193,
        }
    )
    question: List[Question] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 5193,
        }
    )
    question_wrap: List[QuestionWrap] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap",
            "type": "Element",
            "sequence": 5193,
        }
    )
    question_wrap_group: List[QuestionWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap-group",
            "type": "Element",
            "sequence": 5193,
        }
    )
    supplementary_material: List[SupplementaryMaterial] = field(
        default_factory=list,
        metadata={
            "name": "supplementary-material",
            "type": "Element",
            "sequence": 5193,
        }
    )
    table_wrap: List[TableWrap] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap",
            "type": "Element",
            "sequence": 5193,
        }
    )
    table_wrap_group: List[TableWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap-group",
            "type": "Element",
            "sequence": 5193,
        }
    )
    disp_formula: List[DispFormula] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula",
            "type": "Element",
            "sequence": 5193,
        }
    )
    disp_formula_group: List[DispFormulaGroup] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula-group",
            "type": "Element",
            "sequence": 5193,
        }
    )
    def_list: List[DefList] = field(
        default_factory=list,
        metadata={
            "name": "def-list",
            "type": "Element",
            "sequence": 5193,
        }
    )
    list_value: List[ListType] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
            "sequence": 5193,
        }
    )
    tex_math: List[TexMath] = field(
        default_factory=list,
        metadata={
            "name": "tex-math",
            "type": "Element",
            "sequence": 5193,
        }
    )
    math: List[Math] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1998/Math/MathML",
            "sequence": 5193,
        }
    )
    p: List[P] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 5193,
        }
    )
    related_article: List[RelatedArticle] = field(
        default_factory=list,
        metadata={
            "name": "related-article",
            "type": "Element",
            "sequence": 5193,
        }
    )
    related_object: List[RelatedObject] = field(
        default_factory=list,
        metadata={
            "name": "related-object",
            "type": "Element",
            "sequence": 5193,
        }
    )
    disp_quote: List[DispQuote] = field(
        default_factory=list,
        metadata={
            "name": "disp-quote",
            "type": "Element",
            "sequence": 5193,
        }
    )
    speech: List[Speech] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 5193,
        }
    )
    statement: List[Statement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 5193,
        }
    )
    verse_group: List[VerseGroup] = field(
        default_factory=list,
        metadata={
            "name": "verse-group",
            "type": "Element",
            "sequence": 5193,
        }
    )
    sec: List[Sec] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 5193,
        }
    )
    fn_group: List[FnGroup] = field(
        default_factory=list,
        metadata={
            "name": "fn-group",
            "type": "Element",
            "sequence": 5193,
        }
    )
    glossary: List[Glossary] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequence": 5193,
        }
    )
    ref_list: List[RefList] = field(
        default_factory=list,
        metadata={
            "name": "ref-list",
            "type": "Element",
            "sequence": 5193,
        }
    )
    permissions: Optional[Permissions] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
