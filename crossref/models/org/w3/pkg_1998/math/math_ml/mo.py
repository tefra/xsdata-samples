from dataclasses import dataclass, field
from typing import Dict, List, Optional, Union
from crossref.models.org.w3.pkg_1998.math.math_ml.common_pres_att_value import CommonPresAttValue
from crossref.models.org.w3.pkg_1998.math.math_ml.deprecated_token_att_fontstyle import DeprecatedTokenAttFontstyle
from crossref.models.org.w3.pkg_1998.math.math_ml.deprecated_token_att_fontweight import DeprecatedTokenAttFontweight
from crossref.models.org.w3.pkg_1998.math.math_ml.deprecated_token_att_value import DeprecatedTokenAttValue
from crossref.models.org.w3.pkg_1998.math.math_ml.malignmark import Malignmark
from crossref.models.org.w3.pkg_1998.math.math_ml.mglyph import Mglyph
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_attributes_accent import MoAttributesAccent
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_attributes_fence import MoAttributesFence
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_attributes_form import MoAttributesForm
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_attributes_indentalign import MoAttributesIndentalign
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_attributes_indentalignfirst import MoAttributesIndentalignfirst
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_attributes_indentalignlast import MoAttributesIndentalignlast
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_attributes_largeop import MoAttributesLargeop
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_attributes_linebreak import MoAttributesLinebreak
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_attributes_linebreakstyle import MoAttributesLinebreakstyle
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_attributes_movablelimits import MoAttributesMovablelimits
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_attributes_separator import MoAttributesSeparator
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_attributes_stretchy import MoAttributesStretchy
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_attributes_symmetric import MoAttributesSymmetric
from crossref.models.org.w3.pkg_1998.math.math_ml.mo_attributes_value import MoAttributesValue
from crossref.models.org.w3.pkg_1998.math.math_ml.token_att_dir import TokenAttDir
from crossref.models.org.w3.pkg_1998.math.math_ml.token_att_mathvariant import TokenAttMathvariant
from crossref.models.org.w3.pkg_1998.math.math_ml.token_att_value import TokenAttValue

__NAMESPACE__ = "http://www.w3.org/1998/Math/MathML"


@dataclass
class Mo:
    class Meta:
        name = "mo"
        namespace = "http://www.w3.org/1998/Math/MathML"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    xref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: List[str] = field(
        default_factory=list,
        metadata={
            "name": "class",
            "type": "Attribute",
            "tokens": True,
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    other: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )
    mathcolor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?)|[aA][qQ][uU][aA]|[bB][lL][aA][cC][kK]|[bB][lL][uU][eE]|[fF][uU][cC][hH][sS][iI][aA]|[gG][rR][aA][yY]|[gG][rR][eE][eE][nN]|[lL][iI][mM][eE]|[mM][aA][rR][oO][oO][nN]|[nN][aA][vV][yY]|[oO][lL][iI][vV][eE]|[pP][uU][rR][pP][lL][eE]|[rR][eE][dD]|[sS][iI][lL][vV][eE][rR]|[tT][eE][aA][lL]|[wW][hH][iI][tT][eE]|[yY][eE][lL][lL][oO][wW])\s*",
        }
    )
    mathbackground: Optional[Union[str, CommonPresAttValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?)|[aA][qQ][uU][aA]|[bB][lL][aA][cC][kK]|[bB][lL][uU][eE]|[fF][uU][cC][hH][sS][iI][aA]|[gG][rR][aA][yY]|[gG][rR][eE][eE][nN]|[lL][iI][mM][eE]|[mM][aA][rR][oO][oO][nN]|[nN][aA][vV][yY]|[oO][lL][iI][vV][eE]|[pP][uU][rR][pP][lL][eE]|[rR][eE][dD]|[sS][iI][lL][vV][eE][rR]|[tT][eE][aA][lL]|[wW][hH][iI][tT][eE]|[yY][eE][lL][lL][oO][wW])\s*",
        }
    )
    mathvariant: Optional[TokenAttMathvariant] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    mathsize: Optional[Union[str, TokenAttValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    dir: Optional[TokenAttDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    fontfamily: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    fontweight: Optional[DeprecatedTokenAttFontweight] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    fontstyle: Optional[DeprecatedTokenAttFontstyle] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    fontsize: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    color: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?)|[aA][qQ][uU][aA]|[bB][lL][aA][cC][kK]|[bB][lL][uU][eE]|[fF][uU][cC][hH][sS][iI][aA]|[gG][rR][aA][yY]|[gG][rR][eE][eE][nN]|[lL][iI][mM][eE]|[mM][aA][rR][oO][oO][nN]|[nN][aA][vV][yY]|[oO][lL][iI][vV][eE]|[pP][uU][rR][pP][lL][eE]|[rR][eE][dD]|[sS][iI][lL][vV][eE][rR]|[tT][eE][aA][lL]|[wW][hH][iI][tT][eE]|[yY][eE][lL][lL][oO][wW])\s*",
        }
    )
    background: Optional[Union[str, DeprecatedTokenAttValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?)|[aA][qQ][uU][aA]|[bB][lL][aA][cC][kK]|[bB][lL][uU][eE]|[fF][uU][cC][hH][sS][iI][aA]|[gG][rR][aA][yY]|[gG][rR][eE][eE][nN]|[lL][iI][mM][eE]|[mM][aA][rR][oO][oO][nN]|[nN][aA][vV][yY]|[oO][lL][iI][vV][eE]|[pP][uU][rR][pP][lL][eE]|[rR][eE][dD]|[sS][iI][lL][vV][eE][rR]|[tT][eE][aA][lL]|[wW][hH][iI][tT][eE]|[yY][eE][lL][lL][oO][wW])\s*",
        }
    )
    form: Optional[MoAttributesForm] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    fence: Optional[MoAttributesFence] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    separator: Optional[MoAttributesSeparator] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lspace: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    rspace: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    stretchy: Optional[MoAttributesStretchy] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    symmetric: Optional[MoAttributesSymmetric] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    maxsize: Optional[Union[str, MoAttributesValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    minsize: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    largeop: Optional[MoAttributesLargeop] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    movablelimits: Optional[MoAttributesMovablelimits] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    accent: Optional[MoAttributesAccent] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    linebreak: Optional[MoAttributesLinebreak] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lineleading: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    linebreakstyle: Optional[MoAttributesLinebreakstyle] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    linebreakmultchar: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    indentalign: Optional[MoAttributesIndentalign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    indentshift: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    indenttarget: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    indentalignfirst: Optional[MoAttributesIndentalignfirst] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    indentshiftfirst: Optional[Union[str, MoAttributesValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    indentalignlast: Optional[MoAttributesIndentalignlast] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    indentshiftlast: Optional[Union[str, MoAttributesValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "mglyph",
                    "type": Mglyph,
                },
                {
                    "name": "malignmark",
                    "type": Malignmark,
                },
            ),
        }
    )
