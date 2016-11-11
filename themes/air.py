
# -*- coding: utf-8 -*-

"""
    Ex.Co. LICENSE :
        This file is part of Ex.Co..

        Ex.Co. is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 3 of the License, or
        (at your option) any later version.

        Ex.Co. is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.

        You should have received a copy of the GNU General Public License
        along with Ex.Co..  If not, see <http://www.gnu.org/licenses/>.


    PYTHON LICENSE :
        "Python" and the Python logos are trademarks or registered trademarks of the Python Software Foundation,
        used by Ex.Co. with permission from the Foundation


    Cython LICENSE:
        Cython is freely available under the open source Apache License


    PyQt4 LICENSE :
        PyQt4 is licensed under the GNU General Public License version 3
    PyQt Alternative Logo LICENSE:
        The PyQt Alternative Logo is licensed under Creative Commons CC0 1.0 Universal Public Domain Dedication


    Qt Logo LICENSE:
        The Qt logo is copyright of Digia Plc and/or its subsidiaries.
        Digia, Qt and their respective logos are trademarks of Digia Corporation in Finland and/or other countries worldwide.


    Tango Icons LICENSE:
        The Tango base icon theme is released to the Public Domain.
        The Tango base icon theme is made possible by the Tango Desktop Project.
    
    My Tango Style Icons LICENSE:
        The Tango icons I created are released under the GNU General Public License version 3.
    
    
    Eric6 LICENSE:
        Eric6 IDE is licensed under the GNU General Public License version 3


    Nuitka LICENSE:
        Nuitka is a Python compiler compatible with Ex.Co..
        Nuitka is freely available under the open source Apache License.
"""

##  FILE DESCRIPTION:
##      Air theme (Default system form color with white backgrounds and dark text)

import PyQt4.QtGui


Form = "#f0f0f0"
Cursor = PyQt4.QtGui.QColor(0x00, 0x00, 0x00)


class FoldMargin:
    ForeGround = PyQt4.QtGui.QColor(0x000000)
    BackGround = PyQt4.QtGui.QColor(0x000000)


class LineMargin:
    ForeGround = PyQt4.QtGui.QColor(0x000000)
    BackGround = PyQt4.QtGui.QColor(0xe0e0e0)


class Indication:
    Font = "#000000"
    ActiveBackGround = "#ffffff"
    ActiveBorder = "#204a87"
    PassiveBackGround = "#f0f0f0"
    PassiveBorder = "#a0a0a0"


class TextDifferColors:
    Indicator_Unique_1_Color = PyQt4.QtGui.QColor(0x72, 0x9f, 0xcf, 80)
    Indicator_Unique_2_Color = PyQt4.QtGui.QColor(0xad, 0x7f, 0xa8, 80)
    Indicator_Similar_Color = PyQt4.QtGui.QColor(0x8a, 0xe2, 0x34, 80)


class Font:
    Default = PyQt4.QtGui.QColor(0xff000000)
    
    class Repl:
        """
        THE MESSAGE COLORS ARE: 0xBBGGRR (BB-blue,GG-green,RR-red)
        """
        Error = 0x0000ff
        Warning = 0xff0000
        Success = 0x007f00
        Diff_Unique_1 = 0xcf9f72
        Diff_Unique_2 = 0xa87fad
        Diff_Similar = 0x069a4e
    
    class Ada:
        Default = ('Courier', 0xff000000, 10, None)
        Comment = ('Courier', 0xff007f00, 10, None)
        Keyword = ('Courier', 0xff00007f, 10, None)
        String = ('Courier', 0xff7f007f, 10, None)
        Procedure = ('Courier', 0xff0000ff, 10, None)
        Number = ('Courier', 0xff007f7f, 10, None)
        Type = ('Courier', 0xff00007f, 10, None)
        Package = ('Courier', 0xff7f0000, 10, None)
    
    class Nim:
        Default = ('Courier', 0xff000000, 10, None)
        Comment = ('Courier', 0xff007f00, 10, None)
        BasicKeyword = ('Courier', 0xff00007f, 10, True)
        TopKeyword = ('Courier', 0xff407fc0, 10, True)
        String = ('Courier', 0xff7f007f, 10, None)
        LongString = ('Courier', 0xff7f0000, 10, None)
        Number = ('Courier', 0xff007f7f, 10, None)
        Operator = ('Courier', 0xff7f7f7f, 10, None)
        Unsafe = ('Courier', 0xffc00000, 10, True)
        Type = ('Courier', 0xff6e6e00, 10, True)
        DocumentationComment = ('Courier', 0xff7f0a0a, 10, None)
        Definition = ('Courier', 0xff007f7f, 10, None)
        Class = ('Courier', 0xff0000ff, 10, None)
        KeywordOperator = ('Courier', 0xff963cc8, 10, None)
        CharLiteral = ('Courier', 0xff00c8ff, 10, None)
        CaseOf = ('Courier', 0xff8000ff, 10, None)
        UserKeyword = ('Courier', 0xffff8040, 10, None)
        MultilineComment = ('Courier', 0xff006c6c, 10, None)
        MultilineDocumentation = ('Courier', 0xff6e3296, 10, None)
        Pragma = ('Courier', 0xffc07f40, 10, None)
    
    class RouterOS:
        Default = ('Courier', 0xff000000, 10, True)
        Operator = ('Courier', 0xffB4B80A, 10, True)
        Comment = ('Courier', 0xff38B86B, 10, True)
        Keyword1 = ('Courier', 0xff008000, 10, True)
        Keyword2 = ('Courier', 0xffB9005C, 10, True)
        Keyword3 = ('Courier', 0xff007f7f, 10, True)
    
    class Oberon:
        Default = ('Courier', 0xff000000, 10, None)
        Comment = ('Courier', 0xff007f00, 10, None)
        Keyword = ('Courier', 0xff00007f, 10, None)
        String = ('Courier', 0xff7f007f, 10, None)
        Procedure = ('Courier', 0xff0000ff, 10, None)
        Module = ('Courier', 0xff7f0000, 10, None)
        Number = ('Courier', 0xff007f7f, 10, None)
        Type = ('Courier', 0xff00007f, 10, None)
    
    
    class AVS:
        BlockComment = ('Courier', 0xff007f00, 10, None)
        ClipProperty = ('Courier', 0xff00007f, 10, None)
        Default = ('Courier', 0xff000000, 10, None)
        Filter = ('Courier', 0xff00007f, 10, None)
        Function = ('Courier', 0xff007f7f, 10, None)
        Identifier = ('Courier', 0xff000000, 10, None)
        Keyword = ('Courier', 0xff00007f, 10, None)
        KeywordSet6 = ('Courier', 0xff8000ff, 10, None)
        LineComment = ('Courier', 0xff007f00, 10, None)
        NestedBlockComment = ('Courier', 0xff007f00, 10, None)
        Number = ('Courier', 0xff007f7f, 10, None)
        Operator = ('Courier', 0xff000000, 10, None)
        Plugin = ('Courier', 0xff0080c0, 10, None)
        String = ('Courier', 0xff7f007f, 10, None)
        TripleString = ('Courier', 0xff7f007f, 10, None)
    
    class Bash:
        Backticks = ('Courier', 0xffadad00, 10, None)
        Comment = ('Courier', 0xff007f00, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DoubleQuotedString = ('Courier', 0xff7f007f, 10, True)
        Error = ('Courier', 0xffaa0000, 10, True)
        HereDocumentDelimiter = ('Courier', 0xff000000, 10, None)
        Identifier = ('Courier', 0xff000000, 10, None)
        Keyword = ('Courier', 0xff00007f, 10, None)
        Number = ('Courier', 0xff007f7f, 10, None)
        Operator = ('Courier', 0xff000000, 10, None)
        ParameterExpansion = ('Courier', 0xff000000, 10, None)
        Scalar = ('Courier', 0xffadad00, 10, True)
        SingleQuotedHereDocument = ('Courier', 0xff7f007f, 10, None)
        SingleQuotedString = ('Courier', 0xff7f007f, 10, None)
    
    class Batch:
        Comment = ('Courier', 0xff007f00, 10, None)
        Default = ('Courier', 0xff000000, 10, None)
        ExternalCommand = ('Courier', 0xff00007f, 10, None)
        HideCommandChar = ('Courier', 0xff7f7f00, 10, None)
        Keyword = ('Courier', 0xff00007f, 10, None)
        Label = ('Courier', 0xff7f007f, 10, None)
        Operator = ('Courier', 0xff000000, 10, None)
        Variable = ('Courier', 0xff800080, 10, None)
    
    class CMake:
        BlockForeach = ('Courier', 0xff00007f, 10, None)
        BlockIf = ('Courier', 0xff00007f, 10, None)
        BlockMacro = ('Courier', 0xff00007f, 10, None)
        BlockWhile = ('Courier', 0xff00007f, 10, None)
        Comment = ('Courier', 0xff007f00, 10, None)
        Default = ('Courier', 0xff000000, 10, None)
        Function = ('Courier', 0xff00007f, 10, None)
        KeywordSet3 = ('Courier', 0xff000000, 10, None)
        Label = ('Courier', 0xffcc3300, 10, None)
        Number = ('Courier', 0xff007f7f, 10, None)
        String = ('Courier', 0xff7f007f, 10, None)
        StringLeftQuote = ('Courier', 0xff7f007f, 10, None)
        StringRightQuote = ('Courier', 0xff7f007f, 10, None)
        StringVariable = ('Courier', 0xffcc3300, 10, None)
        Variable = ('Courier', 0xff800000, 10, None)
    
    class CPP:
        Comment = ('Courier', 0xff007f00, 10, None)
        CommentDoc = ('Courier', 0xff3f703f, 10, None)
        CommentDocKeyword = ('Courier', 0xff3060a0, 10, None)
        CommentDocKeywordError = ('Courier', 0xff804020, 10, None)
        CommentLine = ('Courier', 0xff007f00, 10, None)
        CommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DoubleQuotedString = ('Courier', 0xff7f007f, 10, None)
        GlobalClass = ('Courier', 0xff000000, 10, None)
        HashQuotedString = ('Courier', 0xff007f00, 10, None)
        Identifier = ('Courier', 0xff000000, 10, None)
        InactiveComment = ('Courier', 0xff90b090, 10, None)
        InactiveCommentDoc = ('Courier', 0xffd0d0d0, 10, None)
        InactiveCommentDocKeyword = ('Courier', 0xffc0c0c0, 10, None)
        InactiveCommentDocKeywordError = ('Courier', 0xffc0c0c0, 10, None)
        InactiveCommentLine = ('Courier', 0xff90b090, 10, None)
        InactiveCommentLineDoc = ('Courier', 0xffc0c0c0, 10, None)
        InactiveDefault = ('Courier', 0xffc0c0c0, 10, None)
        InactiveDoubleQuotedString = ('Courier', 0xffb090b0, 10, None)
        InactiveGlobalClass = ('Courier', 0xffb0b0b0, 10, None)
        InactiveHashQuotedString = ('Courier', 0xff000000, 10, None)
        InactiveIdentifier = ('Courier', 0xffb0b0b0, 10, None)
        InactiveKeyword = ('Courier', 0xff9090b0, 10, None)
        InactiveKeywordSet2 = ('Courier', 0xffc0c0c0, 10, None)
        InactiveNumber = ('Courier', 0xff90b090, 10, None)
        InactiveOperator = ('Courier', 0xffb0b0b0, 10, None)
        InactivePreProcessor = ('Courier', 0xffb0b090, 10, None)
        InactivePreProcessorComment = ('Courier', 0xff000000, 10, None)
        InactivePreProcessorCommentLineDoc = ('Courier', 0xffc0c0c0, 10, None)
        InactiveRawString = ('Courier', 0xff000000, 10, None)
        InactiveRegex = ('Courier', 0xff7faf7f, 10, None)
        InactiveSingleQuotedString = ('Courier', 0xffb090b0, 10, None)
        InactiveTripleQuotedVerbatimString = ('Courier', 0xff000000, 10, None)
        InactiveUUID = ('Courier', 0xffc0c0c0, 10, None)
        InactiveUnclosedString = ('Courier', 0xff000000, 10, None)
        InactiveVerbatimString = ('Courier', 0xff90b090, 10, None)
        Keyword = ('Courier', 0xff00007f, 10, None)
        KeywordSet2 = ('Courier', 0xff000000, 10, None)
        Number = ('Courier', 0xff007f7f, 10, None)
        Operator = ('Courier', 0xff000000, 10, None)
        PreProcessor = ('Courier', 0xff7f7f00, 10, None)
        PreProcessorComment = ('Courier', 0xff659900, 10, None)
        PreProcessorCommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        RawString = ('Courier', 0xff7f007f, 10, None)
        Regex = ('Courier', 0xff3f7f3f, 10, None)
        SingleQuotedString = ('Courier', 0xff7f007f, 10, None)
        TripleQuotedVerbatimString = ('Courier', 0xff007f00, 10, None)
        UUID = ('Courier', 0xff000000, 10, None)
        UnclosedString = ('Courier', 0xff000000, 10, None)
        VerbatimString = ('Courier', 0xff007f00, 10, None)
    
    class CSS:
        AtRule = ('Courier', 0xff7f7f00, 10, None)
        Attribute = ('Courier', 0xff800000, 10, None)
        CSS1Property = ('Courier', 0xff0040e0, 10, None)
        CSS2Property = ('Courier', 0xff00a0e0, 10, None)
        CSS3Property = ('Courier', 0xff000000, 10, None)
        ClassSelector = ('Courier', 0xff000000, 10, None)
        Comment = ('Courier', 0xff007f00, 10, None)
        Default = ('Courier', 0xffff0080, 10, None)
        DoubleQuotedString = ('Courier', 0xff7f007f, 10, None)
        ExtendedCSSProperty = ('Courier', 0xff000000, 10, None)
        ExtendedPseudoClass = ('Courier', 0xff000000, 10, None)
        ExtendedPseudoElement = ('Courier', 0xff000000, 10, None)
        IDSelector = ('Courier', 0xff007f7f, 10, None)
        Important = ('Courier', 0xffff8000, 10, None)
        MediaRule = ('Courier', 0xff7f7f00, 10, None)
        Operator = ('Courier', 0xff000000, 10, None)
        PseudoClass = ('Courier', 0xff800000, 10, None)
        PseudoElement = ('Courier', 0xff000000, 10, None)
        SingleQuotedString = ('Courier', 0xff7f007f, 10, None)
        Tag = ('Courier', 0xff00007f, 10, None)
        UnknownProperty = ('Courier', 0xffff0000, 10, None)
        UnknownPseudoClass = ('Courier', 0xffff0000, 10, None)
        Value = ('Courier', 0xff7f007f, 10, None)
        Variable = ('Courier', 0xff000000, 10, None)
    
    class CSharp:
        Comment = ('Courier', 0xff007f00, 10, None)
        CommentDoc = ('Courier', 0xff3f703f, 10, None)
        CommentDocKeyword = ('Courier', 0xff3060a0, 10, None)
        CommentDocKeywordError = ('Courier', 0xff804020, 10, None)
        CommentLine = ('Courier', 0xff007f00, 10, None)
        CommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DoubleQuotedString = ('Courier', 0xff7f007f, 10, None)
        GlobalClass = ('Courier', 0xff000000, 10, None)
        HashQuotedString = ('Courier', 0xff007f00, 10, None)
        Identifier = ('Courier', 0xff000000, 10, None)
        InactiveComment = ('Courier', 0xff90b090, 10, None)
        InactiveCommentDoc = ('Courier', 0xffd0d0d0, 10, None)
        InactiveCommentDocKeyword = ('Courier', 0xffc0c0c0, 10, None)
        InactiveCommentDocKeywordError = ('Courier', 0xffc0c0c0, 10, None)
        InactiveCommentLine = ('Courier', 0xff90b090, 10, None)
        InactiveCommentLineDoc = ('Courier', 0xffc0c0c0, 10, None)
        InactiveDefault = ('Courier', 0xffc0c0c0, 10, None)
        InactiveDoubleQuotedString = ('Courier', 0xffb090b0, 10, None)
        InactiveGlobalClass = ('Courier', 0xffb0b0b0, 10, None)
        InactiveHashQuotedString = ('Courier', 0xff000000, 10, None)
        InactiveIdentifier = ('Courier', 0xffb0b0b0, 10, None)
        InactiveKeyword = ('Courier', 0xff9090b0, 10, None)
        InactiveKeywordSet2 = ('Courier', 0xffc0c0c0, 10, None)
        InactiveNumber = ('Courier', 0xff90b090, 10, None)
        InactiveOperator = ('Courier', 0xffb0b0b0, 10, None)
        InactivePreProcessor = ('Courier', 0xffb0b090, 10, None)
        InactivePreProcessorComment = ('Courier', 0xff000000, 10, None)
        InactivePreProcessorCommentLineDoc = ('Courier', 0xffc0c0c0, 10, None)
        InactiveRawString = ('Courier', 0xff000000, 10, None)
        InactiveRegex = ('Courier', 0xff7faf7f, 10, None)
        InactiveSingleQuotedString = ('Courier', 0xffb090b0, 10, None)
        InactiveTripleQuotedVerbatimString = ('Courier', 0xff000000, 10, None)
        InactiveUUID = ('Courier', 0xffc0c0c0, 10, None)
        InactiveUnclosedString = ('Courier', 0xff000000, 10, None)
        InactiveVerbatimString = ('Courier', 0xff90b090, 10, None)
        Keyword = ('Courier', 0xff00007f, 10, None)
        KeywordSet2 = ('Courier', 0xff000000, 10, None)
        Number = ('Courier', 0xff007f7f, 10, None)
        Operator = ('Courier', 0xff000000, 10, None)
        PreProcessor = ('Courier', 0xff7f7f00, 10, None)
        PreProcessorComment = ('Courier', 0xff659900, 10, None)
        PreProcessorCommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        RawString = ('Courier', 0xff7f007f, 10, None)
        Regex = ('Courier', 0xff3f7f3f, 10, None)
        SingleQuotedString = ('Courier', 0xff7f007f, 10, None)
        TripleQuotedVerbatimString = ('Courier', 0xff007f00, 10, None)
        UUID = ('Courier', 0xff000000, 10, None)
        UnclosedString = ('Courier', 0xff000000, 10, None)
        VerbatimString = ('Courier', 0xff007f00, 10, None)
    
    class CoffeeScript:
        BlockRegex = ('Courier', 0xff3f7f3f, 10, None)
        BlockRegexComment = ('Courier', 0xff007f00, 10, None)
        Comment = ('Courier', 0xff007f00, 10, None)
        CommentBlock = ('Courier', 0xff007f00, 10, None)
        CommentDoc = ('Courier', 0xff3f703f, 10, None)
        CommentDocKeyword = ('Courier', 0xff3060a0, 10, None)
        CommentDocKeywordError = ('Courier', 0xff804020, 10, None)
        CommentLine = ('Courier', 0xff007f00, 10, None)
        CommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DoubleQuotedString = ('Courier', 0xff7f007f, 10, None)
        GlobalClass = ('Courier', 0xff000000, 10, None)
        Identifier = ('Courier', 0xff000000, 10, None)
        Keyword = ('Courier', 0xff00007f, 10, None)
        KeywordSet2 = ('Courier', 0xff000000, 10, None)
        Number = ('Courier', 0xff007f7f, 10, None)
        Operator = ('Courier', 0xff000000, 10, None)
        PreProcessor = ('Courier', 0xff7f7f00, 10, None)
        Regex = ('Courier', 0xff3f7f3f, 10, None)
        SingleQuotedString = ('Courier', 0xff7f007f, 10, None)
        UUID = ('Courier', 0xff000000, 10, None)
        UnclosedString = ('Courier', 0xff000000, 10, None)
        VerbatimString = ('Courier', 0xff007f00, 10, None)
    
    class D:
        BackquoteString = ('Courier', 0xff000000, 10, None)
        Character = ('Courier', 0xff7f007f, 10, None)
        Comment = ('Courier', 0xff007f00, 10, None)
        CommentDoc = ('Courier', 0xff3f703f, 10, None)
        CommentDocKeyword = ('Courier', 0xff3060a0, 10, None)
        CommentDocKeywordError = ('Courier', 0xff804020, 10, None)
        CommentLine = ('Courier', 0xff007f00, 10, None)
        CommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        CommentNested = ('Courier', 0xffa0c0a0, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        Identifier = ('Courier', 0xff000000, 10, None)
        Keyword = ('Courier', 0xff00007f, 10, None)
        KeywordDoc = ('Courier', 0xff00007f, 10, None)
        KeywordSecondary = ('Courier', 0xff00007f, 10, None)
        KeywordSet5 = ('Courier', 0xff000000, 10, None)
        KeywordSet6 = ('Courier', 0xff000000, 10, None)
        KeywordSet7 = ('Courier', 0xff000000, 10, None)
        Number = ('Courier', 0xff007f7f, 10, None)
        Operator = ('Courier', 0xff000000, 10, None)
        RawString = ('Courier', 0xff000000, 10, None)
        String = ('Courier', 0xff7f007f, 10, None)
        Typedefs = ('Courier', 0xff00007f, 10, None)
        UnclosedString = ('Courier', 0xff000000, 10, None)
    
    class Diff:
        Command = ('Courier', 0xff7f7f00, 10, None)
        Comment = ('Courier', 0xff007f00, 10, None)
        Default = ('Courier', 0xff000000, 10, None)
        Header = ('Courier', 0xff7f0000, 10, None)
        LineAdded = ('Courier', 0xff00007f, 10, None)
        LineChanged = ('Courier', 0xff7f7f7f, 10, None)
        LineRemoved = ('Courier', 0xff007f7f, 10, None)
        Position = ('Courier', 0xff7f007f, 10, None)
    
    class Fortran:
        Comment = ('Courier', 0xff007f00, 10, None)
        Continuation = ('Courier', 0xff000000, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DottedOperator = ('Courier', 0xff000000, 10, None)
        DoubleQuotedString = ('Courier', 0xff7f007f, 10, None)
        ExtendedFunction = ('Courier', 0xffb04080, 10, None)
        Identifier = ('Courier', 0xff000000, 10, None)
        IntrinsicFunction = ('Courier', 0xffb00040, 10, None)
        Keyword = ('Courier', 0xff00007f, 10, None)
        Label = ('Courier', 0xffe0c0e0, 10, None)
        Number = ('Courier', 0xff007f7f, 10, None)
        Operator = ('Courier', 0xff000000, 10, None)
        PreProcessor = ('Courier', 0xff7f7f00, 10, None)
        SingleQuotedString = ('Courier', 0xff7f007f, 10, None)
        UnclosedString = ('Courier', 0xff000000, 10, None)
    
    class Fortran77:
        Comment = ('Courier', 0xff007f00, 10, None)
        Continuation = ('Courier', 0xff000000, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DottedOperator = ('Courier', 0xff000000, 10, None)
        DoubleQuotedString = ('Courier', 0xff7f007f, 10, None)
        ExtendedFunction = ('Courier', 0xffb04080, 10, None)
        Identifier = ('Courier', 0xff000000, 10, None)
        IntrinsicFunction = ('Courier', 0xffb00040, 10, None)
        Keyword = ('Courier', 0xff00007f, 10, None)
        Label = ('Courier', 0xffe0c0e0, 10, None)
        Number = ('Courier', 0xff007f7f, 10, None)
        Operator = ('Courier', 0xff000000, 10, None)
        PreProcessor = ('Courier', 0xff7f7f00, 10, None)
        SingleQuotedString = ('Courier', 0xff7f007f, 10, None)
        UnclosedString = ('Courier', 0xff000000, 10, None)
    
    class HTML:
        ASPAtStart = ('Courier', 0xff000000, 10, None)
        ASPJavaScriptComment = ('Courier', 0xff007f00, 10, None)
        ASPJavaScriptCommentDoc = ('Courier', 0xff7f7f7f, 10, None)
        ASPJavaScriptCommentLine = ('Courier', 0xff007f00, 10, None)
        ASPJavaScriptDefault = ('Courier', 0xff000000, 10, None)
        ASPJavaScriptDoubleQuotedString = ('Courier', 0xff7f007f, 10, None)
        ASPJavaScriptKeyword = ('Courier', 0xff00007f, 10, None)
        ASPJavaScriptNumber = ('Courier', 0xff007f7f, 10, None)
        ASPJavaScriptRegex = ('Courier', 0xff000000, 10, None)
        ASPJavaScriptSingleQuotedString = ('Courier', 0xff7f007f, 10, None)
        ASPJavaScriptStart = ('Courier', 0xff7f7f00, 10, None)
        ASPJavaScriptSymbol = ('Courier', 0xff000000, 10, None)
        ASPJavaScriptUnclosedString = ('Courier', 0xff000000, 10, None)
        ASPJavaScriptWord = ('Courier', 0xff000000, 10, None)
        ASPPythonClassName = ('Courier', 0xff0000ff, 10, None)
        ASPPythonComment = ('Courier', 0xff007f00, 10, None)
        ASPPythonDefault = ('Courier', 0xff808080, 10, None)
        ASPPythonDoubleQuotedString = ('Courier', 0xff7f007f, 10, None)
        ASPPythonFunctionMethodName = ('Courier', 0xff007f7f, 10, None)
        ASPPythonIdentifier = ('Courier', 0xff000000, 10, None)
        ASPPythonKeyword = ('Courier', 0xff00007f, 10, None)
        ASPPythonNumber = ('Courier', 0xff007f7f, 10, None)
        ASPPythonOperator = ('Courier', 0xff000000, 10, None)
        ASPPythonSingleQuotedString = ('Courier', 0xff7f007f, 10, None)
        ASPPythonStart = ('Courier', 0xff808080, 10, None)
        ASPPythonTripleDoubleQuotedString = ('Courier', 0xff7f0000, 10, None)
        ASPPythonTripleSingleQuotedString = ('Courier', 0xff7f0000, 10, None)
        ASPStart = ('Courier', 0xff000000, 10, None)
        ASPVBScriptComment = ('Courier', 0xff008000, 10, None)
        ASPVBScriptDefault = ('Courier', 0xff000000, 10, None)
        ASPVBScriptIdentifier = ('Courier', 0xff000080, 10, None)
        ASPVBScriptKeyword = ('Courier', 0xff000080, 10, None)
        ASPVBScriptNumber = ('Courier', 0xff008080, 10, None)
        ASPVBScriptStart = ('Courier', 0xff000000, 10, None)
        ASPVBScriptString = ('Courier', 0xff800080, 10, None)
        ASPVBScriptUnclosedString = ('Courier', 0xff000080, 10, None)
        ASPXCComment = ('Courier', 0xff000000, 10, None)
        Attribute = ('Courier', 0xff008080, 10, None)
        CDATA = ('Courier', 0xff000000, 10, None)
        Default = ('Courier', 0xff000000, 10, None)
        Entity = ('Courier', 0xff800080, 10, None)
        HTMLComment = ('Courier', 0xff808000, 10, None)
        HTMLDoubleQuotedString = ('Courier', 0xff7f007f, 10, None)
        HTMLNumber = ('Courier', 0xff007f7f, 10, None)
        HTMLSingleQuotedString = ('Courier', 0xff7f007f, 10, None)
        HTMLValue = ('Courier', 0xffff00ff, 10, None)
        JavaScriptComment = ('Courier', 0xff007f00, 10, None)
        JavaScriptCommentDoc = ('Courier', 0xff3f703f, 10, None)
        JavaScriptCommentLine = ('Courier', 0xff007f00, 10, None)
        JavaScriptDefault = ('Courier', 0xff000000, 10, None)
        JavaScriptDoubleQuotedString = ('Courier', 0xff7f007f, 10, None)
        JavaScriptKeyword = ('Courier', 0xff00007f, 10, None)
        JavaScriptNumber = ('Courier', 0xff007f7f, 10, None)
        JavaScriptRegex = ('Courier', 0xff000000, 10, None)
        JavaScriptSingleQuotedString = ('Courier', 0xff7f007f, 10, None)
        JavaScriptStart = ('Courier', 0xff7f7f00, 10, None)
        JavaScriptSymbol = ('Courier', 0xff000000, 10, None)
        JavaScriptUnclosedString = ('Courier', 0xff000000, 10, None)
        JavaScriptWord = ('Courier', 0xff000000, 10, None)
        OtherInTag = ('Courier', 0xff800080, 10, None)
        PHPComment = ('Courier', 0xff999999, 10, None)
        PHPCommentLine = ('Courier', 0xff666666, 10, None)
        PHPDefault = ('Courier', 0xff000033, 10, None)
        PHPDoubleQuotedString = ('Courier', 0xff007f00, 10, None)
        PHPDoubleQuotedVariable = ('Courier', 0xff00007f, 10, None)
        PHPKeyword = ('Courier', 0xff7f007f, 10, None)
        PHPNumber = ('Courier', 0xffcc9900, 10, None)
        PHPOperator = ('Courier', 0xff000000, 10, None)
        PHPSingleQuotedString = ('Courier', 0xff009f00, 10, None)
        PHPStart = ('Courier', 0xff0000ff, 10, None)
        PHPVariable = ('Courier', 0xff00007f, 10, None)
        PythonClassName = ('Courier', 0xff0000ff, 10, None)
        PythonComment = ('Courier', 0xff007f00, 10, None)
        PythonDefault = ('Courier', 0xff808080, 10, None)
        PythonDoubleQuotedString = ('Courier', 0xff7f007f, 10, None)
        PythonFunctionMethodName = ('Courier', 0xff007f7f, 10, None)
        PythonIdentifier = ('Courier', 0xff000000, 10, None)
        PythonKeyword = ('Courier', 0xff00007f, 10, None)
        PythonNumber = ('Courier', 0xff007f7f, 10, None)
        PythonOperator = ('Courier', 0xff000000, 10, None)
        PythonSingleQuotedString = ('Courier', 0xff7f007f, 10, None)
        PythonStart = ('Courier', 0xff808080, 10, None)
        PythonTripleDoubleQuotedString = ('Courier', 0xff7f0000, 10, None)
        PythonTripleSingleQuotedString = ('Courier', 0xff7f0000, 10, None)
        SGMLBlockDefault = ('Courier', 0xff000066, 10, None)
        SGMLCommand = ('Courier', 0xff000080, 10, None)
        SGMLComment = ('Courier', 0xff808000, 10, None)
        SGMLDefault = ('Courier', 0xff000080, 10, None)
        SGMLDoubleQuotedString = ('Courier', 0xff800000, 10, None)
        SGMLEntity = ('Courier', 0xff333333, 10, None)
        SGMLError = ('Courier', 0xff800000, 10, None)
        SGMLParameter = ('Courier', 0xff006600, 10, None)
        SGMLParameterComment = ('Courier', 0xff000000, 10, None)
        SGMLSingleQuotedString = ('Courier', 0xff993300, 10, None)
        SGMLSpecial = ('Courier', 0xff3366ff, 10, None)
        Script = ('Courier', 0xff000080, 10, None)
        Tag = ('Courier', 0xff000080, 10, None)
        UnknownAttribute = ('Courier', 0xffff0000, 10, None)
        UnknownTag = ('Courier', 0xffff0000, 10, None)
        VBScriptComment = ('Courier', 0xff008000, 10, None)
        VBScriptDefault = ('Courier', 0xff000000, 10, None)
        VBScriptIdentifier = ('Courier', 0xff000080, 10, None)
        VBScriptKeyword = ('Courier', 0xff000080, 10, None)
        VBScriptNumber = ('Courier', 0xff008080, 10, None)
        VBScriptStart = ('Courier', 0xff000000, 10, None)
        VBScriptString = ('Courier', 0xff800080, 10, None)
        VBScriptUnclosedString = ('Courier', 0xff000080, 10, None)
        XMLEnd = ('Courier', 0xff0000ff, 10, None)
        XMLStart = ('Courier', 0xff0000ff, 10, None)
        XMLTagEnd = ('Courier', 0xff000080, 10, None)
    
    class IDL:
        Comment = ('Courier', 0xff007f00, 10, None)
        CommentDoc = ('Courier', 0xff3f703f, 10, None)
        CommentDocKeyword = ('Courier', 0xff3060a0, 10, None)
        CommentDocKeywordError = ('Courier', 0xff804020, 10, None)
        CommentLine = ('Courier', 0xff007f00, 10, None)
        CommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DoubleQuotedString = ('Courier', 0xff7f007f, 10, None)
        GlobalClass = ('Courier', 0xff000000, 10, None)
        HashQuotedString = ('Courier', 0xff007f00, 10, None)
        Identifier = ('Courier', 0xff000000, 10, None)
        InactiveComment = ('Courier', 0xff90b090, 10, None)
        InactiveCommentDoc = ('Courier', 0xffd0d0d0, 10, None)
        InactiveCommentDocKeyword = ('Courier', 0xffc0c0c0, 10, None)
        InactiveCommentDocKeywordError = ('Courier', 0xffc0c0c0, 10, None)
        InactiveCommentLine = ('Courier', 0xff90b090, 10, None)
        InactiveCommentLineDoc = ('Courier', 0xffc0c0c0, 10, None)
        InactiveDefault = ('Courier', 0xffc0c0c0, 10, None)
        InactiveDoubleQuotedString = ('Courier', 0xffb090b0, 10, None)
        InactiveGlobalClass = ('Courier', 0xffb0b0b0, 10, None)
        InactiveHashQuotedString = ('Courier', 0xff000000, 10, None)
        InactiveIdentifier = ('Courier', 0xffb0b0b0, 10, None)
        InactiveKeyword = ('Courier', 0xff9090b0, 10, None)
        InactiveKeywordSet2 = ('Courier', 0xffc0c0c0, 10, None)
        InactiveNumber = ('Courier', 0xff90b090, 10, None)
        InactiveOperator = ('Courier', 0xffb0b0b0, 10, None)
        InactivePreProcessor = ('Courier', 0xffb0b090, 10, None)
        InactivePreProcessorComment = ('Courier', 0xff000000, 10, None)
        InactivePreProcessorCommentLineDoc = ('Courier', 0xffc0c0c0, 10, None)
        InactiveRawString = ('Courier', 0xff000000, 10, None)
        InactiveRegex = ('Courier', 0xff7faf7f, 10, None)
        InactiveSingleQuotedString = ('Courier', 0xffb090b0, 10, None)
        InactiveTripleQuotedVerbatimString = ('Courier', 0xff000000, 10, None)
        InactiveUUID = ('Courier', 0xffc0c0c0, 10, None)
        InactiveUnclosedString = ('Courier', 0xff000000, 10, None)
        InactiveVerbatimString = ('Courier', 0xff90b090, 10, None)
        Keyword = ('Courier', 0xff00007f, 10, None)
        KeywordSet2 = ('Courier', 0xff000000, 10, None)
        Number = ('Courier', 0xff007f7f, 10, None)
        Operator = ('Courier', 0xff000000, 10, None)
        PreProcessor = ('Courier', 0xff7f7f00, 10, None)
        PreProcessorComment = ('Courier', 0xff659900, 10, None)
        PreProcessorCommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        RawString = ('Courier', 0xff7f007f, 10, None)
        Regex = ('Courier', 0xff3f7f3f, 10, None)
        SingleQuotedString = ('Courier', 0xff7f007f, 10, None)
        TripleQuotedVerbatimString = ('Courier', 0xff007f00, 10, None)
        UUID = ('Courier', 0xff804080, 10, None)
        UnclosedString = ('Courier', 0xff000000, 10, None)
        VerbatimString = ('Courier', 0xff007f00, 10, None)
    
    class Java:
        Comment = ('Courier', 0xff007f00, 10, None)
        CommentDoc = ('Courier', 0xff3f703f, 10, None)
        CommentDocKeyword = ('Courier', 0xff3060a0, 10, None)
        CommentDocKeywordError = ('Courier', 0xff804020, 10, None)
        CommentLine = ('Courier', 0xff007f00, 10, None)
        CommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DoubleQuotedString = ('Courier', 0xff7f007f, 10, None)
        GlobalClass = ('Courier', 0xff000000, 10, None)
        HashQuotedString = ('Courier', 0xff007f00, 10, None)
        Identifier = ('Courier', 0xff000000, 10, None)
        InactiveComment = ('Courier', 0xff90b090, 10, None)
        InactiveCommentDoc = ('Courier', 0xffd0d0d0, 10, None)
        InactiveCommentDocKeyword = ('Courier', 0xffc0c0c0, 10, None)
        InactiveCommentDocKeywordError = ('Courier', 0xffc0c0c0, 10, None)
        InactiveCommentLine = ('Courier', 0xff90b090, 10, None)
        InactiveCommentLineDoc = ('Courier', 0xffc0c0c0, 10, None)
        InactiveDefault = ('Courier', 0xffc0c0c0, 10, None)
        InactiveDoubleQuotedString = ('Courier', 0xffb090b0, 10, None)
        InactiveGlobalClass = ('Courier', 0xffb0b0b0, 10, None)
        InactiveHashQuotedString = ('Courier', 0xff000000, 10, None)
        InactiveIdentifier = ('Courier', 0xffb0b0b0, 10, None)
        InactiveKeyword = ('Courier', 0xff9090b0, 10, None)
        InactiveKeywordSet2 = ('Courier', 0xffc0c0c0, 10, None)
        InactiveNumber = ('Courier', 0xff90b090, 10, None)
        InactiveOperator = ('Courier', 0xffb0b0b0, 10, None)
        InactivePreProcessor = ('Courier', 0xffb0b090, 10, None)
        InactivePreProcessorComment = ('Courier', 0xff000000, 10, None)
        InactivePreProcessorCommentLineDoc = ('Courier', 0xffc0c0c0, 10, None)
        InactiveRawString = ('Courier', 0xff000000, 10, None)
        InactiveRegex = ('Courier', 0xff7faf7f, 10, None)
        InactiveSingleQuotedString = ('Courier', 0xffb090b0, 10, None)
        InactiveTripleQuotedVerbatimString = ('Courier', 0xff000000, 10, None)
        InactiveUUID = ('Courier', 0xffc0c0c0, 10, None)
        InactiveUnclosedString = ('Courier', 0xff000000, 10, None)
        InactiveVerbatimString = ('Courier', 0xff90b090, 10, None)
        Keyword = ('Courier', 0xff00007f, 10, None)
        KeywordSet2 = ('Courier', 0xff000000, 10, None)
        Number = ('Courier', 0xff007f7f, 10, None)
        Operator = ('Courier', 0xff000000, 10, None)
        PreProcessor = ('Courier', 0xff7f7f00, 10, None)
        PreProcessorComment = ('Courier', 0xff659900, 10, None)
        PreProcessorCommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        RawString = ('Courier', 0xff7f007f, 10, None)
        Regex = ('Courier', 0xff3f7f3f, 10, None)
        SingleQuotedString = ('Courier', 0xff7f007f, 10, None)
        TripleQuotedVerbatimString = ('Courier', 0xff007f00, 10, None)
        UUID = ('Courier', 0xff000000, 10, None)
        UnclosedString = ('Courier', 0xff000000, 10, None)
        VerbatimString = ('Courier', 0xff007f00, 10, None)
    
    class JavaScript:
        Comment = ('Courier', 0xff007f00, 10, None)
        CommentDoc = ('Courier', 0xff3f703f, 10, None)
        CommentDocKeyword = ('Courier', 0xff3060a0, 10, None)
        CommentDocKeywordError = ('Courier', 0xff804020, 10, None)
        CommentLine = ('Courier', 0xff007f00, 10, None)
        CommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DoubleQuotedString = ('Courier', 0xff7f007f, 10, None)
        GlobalClass = ('Courier', 0xff000000, 10, None)
        HashQuotedString = ('Courier', 0xff007f00, 10, None)
        Identifier = ('Courier', 0xff000000, 10, None)
        InactiveComment = ('Courier', 0xff90b090, 10, None)
        InactiveCommentDoc = ('Courier', 0xffd0d0d0, 10, None)
        InactiveCommentDocKeyword = ('Courier', 0xffc0c0c0, 10, None)
        InactiveCommentDocKeywordError = ('Courier', 0xffc0c0c0, 10, None)
        InactiveCommentLine = ('Courier', 0xff90b090, 10, None)
        InactiveCommentLineDoc = ('Courier', 0xffc0c0c0, 10, None)
        InactiveDefault = ('Courier', 0xffc0c0c0, 10, None)
        InactiveDoubleQuotedString = ('Courier', 0xffb090b0, 10, None)
        InactiveGlobalClass = ('Courier', 0xffb0b0b0, 10, None)
        InactiveHashQuotedString = ('Courier', 0xff000000, 10, None)
        InactiveIdentifier = ('Courier', 0xffb0b0b0, 10, None)
        InactiveKeyword = ('Courier', 0xff9090b0, 10, None)
        InactiveKeywordSet2 = ('Courier', 0xffc0c0c0, 10, None)
        InactiveNumber = ('Courier', 0xff90b090, 10, None)
        InactiveOperator = ('Courier', 0xffb0b0b0, 10, None)
        InactivePreProcessor = ('Courier', 0xffb0b090, 10, None)
        InactivePreProcessorComment = ('Courier', 0xff000000, 10, None)
        InactivePreProcessorCommentLineDoc = ('Courier', 0xffc0c0c0, 10, None)
        InactiveRawString = ('Courier', 0xff000000, 10, None)
        InactiveRegex = ('Courier', 0xff7faf7f, 10, None)
        InactiveSingleQuotedString = ('Courier', 0xffb090b0, 10, None)
        InactiveTripleQuotedVerbatimString = ('Courier', 0xff000000, 10, None)
        InactiveUUID = ('Courier', 0xffc0c0c0, 10, None)
        InactiveUnclosedString = ('Courier', 0xff000000, 10, None)
        InactiveVerbatimString = ('Courier', 0xff90b090, 10, None)
        Keyword = ('Courier', 0xff00007f, 10, None)
        KeywordSet2 = ('Courier', 0xff000000, 10, None)
        Number = ('Courier', 0xff007f7f, 10, None)
        Operator = ('Courier', 0xff000000, 10, None)
        PreProcessor = ('Courier', 0xff7f7f00, 10, None)
        PreProcessorComment = ('Courier', 0xff659900, 10, None)
        PreProcessorCommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        RawString = ('Courier', 0xff7f007f, 10, None)
        Regex = ('Courier', 0xff3f7f3f, 10, None)
        SingleQuotedString = ('Courier', 0xff7f007f, 10, None)
        TripleQuotedVerbatimString = ('Courier', 0xff007f00, 10, None)
        UUID = ('Courier', 0xff000000, 10, None)
        UnclosedString = ('Courier', 0xff000000, 10, None)
        VerbatimString = ('Courier', 0xff007f00, 10, None)
    
    class Lua:
        BasicFunctions = ('Courier', 0xff00007f, 10, None)
        Character = ('Courier', 0xff7f007f, 10, None)
        Comment = ('Courier', 0xff007f00, 10, None)
        CoroutinesIOSystemFacilities = ('Courier', 0xff00007f, 10, None)
        Default = ('Courier', 0xff000000, 10, None)
        Identifier = ('Courier', 0xff000000, 10, None)
        Keyword = ('Courier', 0xff00007f, 10, None)
        KeywordSet5 = ('Courier', 0xff000000, 10, None)
        KeywordSet6 = ('Courier', 0xff000000, 10, None)
        KeywordSet7 = ('Courier', 0xff000000, 10, None)
        KeywordSet8 = ('Courier', 0xff000000, 10, None)
        Label = ('Courier', 0xff7f7f00, 10, None)
        LineComment = ('Courier', 0xff007f00, 10, None)
        LiteralString = ('Courier', 0xff7f007f, 10, None)
        Number = ('Courier', 0xff007f7f, 10, None)
        Operator = ('Courier', 0xff000000, 10, None)
        Preprocessor = ('Courier', 0xff7f7f00, 10, None)
        String = ('Courier', 0xff7f007f, 10, None)
        StringTableMathsFunctions = ('Courier', 0xff00007f, 10, None)
        UnclosedString = ('Courier', 0xff000000, 10, None)
    
    class Makefile:
        Comment = ('Courier', 0xff007f00, 10, None)
        Default = ('Courier', 0xff000000, 10, None)
        Error = ('Courier', 0xffffff00, 10, None)
        Operator = ('Courier', 0xff000000, 10, None)
        Preprocessor = ('Courier', 0xff7f7f00, 10, None)
        Target = ('Courier', 0xffa00000, 10, None)
        Variable = ('Courier', 0xff000080, 10, None)
    
    class Matlab:
        Command = ('Courier', 0xff7f7f00, 10, None)
        Comment = ('Courier', 0xff007f00, 10, None)
        Default = ('Courier', 0xff000000, 10, None)
        DoubleQuotedString = ('Courier', 0xff7f007f, 10, None)
        Identifier = ('Courier', 0xff000000, 10, None)
        Keyword = ('Courier', 0xff00007f, 10, None)
        Number = ('Courier', 0xff007f7f, 10, None)
        Operator = ('Courier', 0xff000000, 10, None)
        SingleQuotedString = ('Courier', 0xff7f007f, 10, None)
    
    class Octave:
        Command = ('Courier', 0xff7f7f00, 10, None)
        Comment = ('Courier', 0xff007f00, 10, None)
        Default = ('Courier', 0xff000000, 10, None)
        DoubleQuotedString = ('Courier', 0xff7f007f, 10, None)
        Identifier = ('Courier', 0xff000000, 10, None)
        Keyword = ('Courier', 0xff00007f, 10, None)
        Number = ('Courier', 0xff007f7f, 10, None)
        Operator = ('Courier', 0xff000000, 10, None)
        SingleQuotedString = ('Courier', 0xff7f007f, 10, None)
    
    class PO:
        Comment = ('Courier', 0xff007f00, 10, None)
        Default = ('Courier', 0xff000000, 10, None)
        Flags = ('Courier', 0xff000000, 10, None)
        Fuzzy = ('Courier', 0xff000000, 10, None)
        MessageContext = ('Courier', 0xff000000, 10, None)
        MessageContextText = ('Courier', 0xff000000, 10, None)
        MessageContextTextEOL = ('Courier', 0xff000000, 10, None)
        MessageId = ('Courier', 0xff000000, 10, None)
        MessageIdText = ('Courier', 0xff000000, 10, None)
        MessageIdTextEOL = ('Courier', 0xff000000, 10, None)
        MessageString = ('Courier', 0xff000000, 10, None)
        MessageStringText = ('Courier', 0xff000000, 10, None)
        MessageStringTextEOL = ('Courier', 0xff000000, 10, None)
        ProgrammerComment = ('Courier', 0xff000000, 10, None)
        Reference = ('Courier', 0xff000000, 10, None)
    
    class POV:
        BadDirective = ('Courier', 0xff804020, 10, None)
        Comment = ('Courier', 0xff007f00, 10, None)
        CommentLine = ('Courier', 0xff007f00, 10, None)
        Default = ('Courier', 0xffff0080, 10, None)
        Directive = ('Courier', 0xff7f7f00, 10, None)
        Identifier = ('Courier', 0xff000000, 10, None)
        KeywordSet6 = ('Courier', 0xff00007f, 10, None)
        KeywordSet7 = ('Courier', 0xff00007f, 10, None)
        KeywordSet8 = ('Courier', 0xff00007f, 10, None)
        Number = ('Courier', 0xff007f7f, 10, None)
        ObjectsCSGAppearance = ('Courier', 0xff00007f, 10, None)
        Operator = ('Courier', 0xff000000, 10, None)
        PredefinedFunctions = ('Courier', 0xff00007f, 10, None)
        PredefinedIdentifiers = ('Courier', 0xff00007f, 10, None)
        String = ('Courier', 0xff7f007f, 10, None)
        TypesModifiersItems = ('Courier', 0xff00007f, 10, None)
        UnclosedString = ('Courier', 0xff000000, 10, None)
    
    class Pascal:
        Asm = ('Courier', 0xff804080, 10, None)
        Character = ('Courier', 0xff7f007f, 10, None)
        Comment = ('Courier', 0xff007f00, 10, None)
        CommentLine = ('Courier', 0xff007f00, 10, None)
        CommentParenthesis = ('Courier', 0xff007f00, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        HexNumber = ('Courier', 0xff007f7f, 10, None)
        Identifier = ('Courier', 0xff000000, 10, None)
        Keyword = ('Courier', 0xff00007f, 10, None)
        Number = ('Courier', 0xff007f7f, 10, None)
        Operator = ('Courier', 0xff000000, 10, None)
        PreProcessor = ('Courier', 0xff7f7f00, 10, None)
        PreProcessorParenthesis = ('Courier', 0xff7f7f00, 10, None)
        SingleQuotedString = ('Courier', 0xff7f007f, 10, None)
        UnclosedString = ('Courier', 0xff000000, 10, None)
    
    class Perl:
        Array = ('Courier', 0xff000000, 10, None)
        BacktickHereDocument = ('Courier', 0xff7f007f, 10, None)
        BacktickHereDocumentVar = ('Courier', 0xffd00000, 10, None)
        Backticks = ('Courier', 0xffffff00, 10, None)
        BackticksVar = ('Courier', 0xffd00000, 10, None)
        Comment = ('Courier', 0xff007f00, 10, None)
        DataSection = ('Courier', 0xff600000, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DoubleQuotedHereDocument = ('Courier', 0xff7f007f, 10, None)
        DoubleQuotedHereDocumentVar = ('Courier', 0xffd00000, 10, None)
        DoubleQuotedString = ('Courier', 0xff7f007f, 10, None)
        DoubleQuotedStringVar = ('Courier', 0xffd00000, 10, None)
        Error = ('Courier', 0xffffff00, 10, None)
        FormatBody = ('Courier', 0xffc000c0, 10, None)
        FormatIdentifier = ('Courier', 0xffc000c0, 10, None)
        Hash = ('Courier', 0xff000000, 10, None)
        HereDocumentDelimiter = ('Courier', 0xff000000, 10, None)
        Identifier = ('Courier', 0xff000000, 10, None)
        Keyword = ('Courier', 0xff00007f, 10, None)
        Number = ('Courier', 0xff007f7f, 10, None)
        Operator = ('Courier', 0xff000000, 10, None)
        POD = ('Courier', 0xff004000, 10, None)
        PODVerbatim = ('Courier', 0xff004000, 10, None)
        QuotedStringQ = ('Courier', 0xff7f007f, 10, None)
        QuotedStringQQ = ('Courier', 0xff7f007f, 10, None)
        QuotedStringQQVar = ('Courier', 0xffd00000, 10, None)
        QuotedStringQR = ('Courier', 0xff000000, 10, None)
        QuotedStringQRVar = ('Courier', 0xffd00000, 10, None)
        QuotedStringQW = ('Courier', 0xff000000, 10, None)
        QuotedStringQX = ('Courier', 0xffffff00, 10, None)
        QuotedStringQXVar = ('Courier', 0xffd00000, 10, None)
        Regex = ('Courier', 0xff000000, 10, None)
        RegexVar = ('Courier', 0xffd00000, 10, None)
        Scalar = ('Courier', 0xff000000, 10, None)
        SingleQuotedHereDocument = ('Courier', 0xff7f007f, 10, None)
        SingleQuotedString = ('Courier', 0xff7f007f, 10, None)
        SubroutinePrototype = ('Courier', 0xff000000, 10, None)
        Substitution = ('Courier', 0xff000000, 10, None)
        SubstitutionVar = ('Courier', 0xffd00000, 10, None)
        SymbolTable = ('Courier', 0xff000000, 10, None)
        Translation = ('Courier', 0xff000000, 10, None)
    
    class PostScript:
        ArrayParenthesis = ('Courier', 0xff00007f, 10, None)
        BadStringCharacter = ('Courier', 0xffffff00, 10, None)
        Base85String = ('Courier', 0xff7f007f, 10, None)
        Comment = ('Courier', 0xff007f00, 10, None)
        DSCComment = ('Courier', 0xff3f703f, 10, None)
        DSCCommentValue = ('Courier', 0xff3060a0, 10, None)
        Default = ('Courier', 0xff000000, 10, None)
        DictionaryParenthesis = ('Courier', 0xff3060a0, 10, None)
        HexString = ('Courier', 0xff3f7f3f, 10, None)
        ImmediateEvalLiteral = ('Courier', 0xff7f7f00, 10, None)
        Keyword = ('Courier', 0xff00007f, 10, None)
        Literal = ('Courier', 0xff7f7f00, 10, None)
        Name = ('Courier', 0xff000000, 10, None)
        Number = ('Courier', 0xff007f7f, 10, None)
        ProcedureParenthesis = ('Courier', 0xff000000, 10, None)
        Text = ('Courier', 0xff7f007f, 10, None)
    
    class Properties:
        Assignment = ('Courier', 0xffb06000, 10, None)
        Comment = ('Courier', 0xff007f7f, 10, None)
        Default = ('Courier', 0xff000000, 10, None)
        DefaultValue = ('Courier', 0xff7f7f00, 10, None)
        Key = ('Courier', 0xff000000, 10, None)
        Section = ('Courier', 0xff7f007f, 10, None)
    
    class Python:
        ClassName = ('Courier', 0xff0000ff, 10, None)
        Comment = ('Courier', 0xff007f00, 10, None)
        CommentBlock = ('Courier', 0xff7f7f7f, 10, None)
        Decorator = ('Courier', 0xff805000, 10, None)
        Default = ('Courier', 0xff000000, 10, None)
        DoubleQuotedString = ('Courier', 0xff7f007f, 10, None)
        FunctionMethodName = ('Courier', 0xff007f7f, 10, None)
        HighlightedIdentifier = ('Courier', 0xff407090, 10, None)
        Identifier = ('Courier', 0xff000000, 10, None)
        Inconsistent = ('Courier', 0xff007f00, 10, None)
        Keyword = ('Courier', 0xff00007f, 10, None)
        NoWarning = ('Courier', 0xff808080, 10, None)
        Number = ('Courier', 0xff007f7f, 10, None)
        Operator = ('Courier', 0xff000000, 10, None)
        SingleQuotedString = ('Courier', 0xff7f007f, 10, None)
        Spaces = ('Courier', 0xff7f007f, 10, None)
        Tabs = ('Courier', 0xff7f007f, 10, None)
        TabsAfterSpaces = ('Courier', 0xff007f7f, 10, None)
        TripleDoubleQuotedString = ('Courier', 0xff7f0000, 10, None)
        TripleSingleQuotedString = ('Courier', 0xff7f0000, 10, None)
        UnclosedString = ('Courier', 0xff000000, 10, None)
    
    class Ruby:
        Backticks = ('Courier', 0xffffff00, 10, None)
        ClassName = ('Courier', 0xff0000ff, 10, None)
        ClassVariable = ('Courier', 0xff8000b0, 10, None)
        Comment = ('Courier', 0xff007f00, 10, None)
        DataSection = ('Courier', 0xff600000, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DemotedKeyword = ('Courier', 0xff00007f, 10, None)
        DoubleQuotedString = ('Courier', 0xff7f007f, 10, None)
        Error = ('Courier', 0xff000000, 10, None)
        FunctionMethodName = ('Courier', 0xff007f7f, 10, None)
        Global = ('Courier', 0xff800080, 10, None)
        HereDocument = ('Courier', 0xff7f007f, 10, None)
        HereDocumentDelimiter = ('Courier', 0xff000000, 10, None)
        Identifier = ('Courier', 0xff000000, 10, None)
        InstanceVariable = ('Courier', 0xffb00080, 10, None)
        Keyword = ('Courier', 0xff00007f, 10, None)
        ModuleName = ('Courier', 0xffa000a0, 10, None)
        Number = ('Courier', 0xff007f7f, 10, None)
        Operator = ('Courier', 0xff000000, 10, None)
        POD = ('Courier', 0xff004000, 10, None)
        PercentStringQ = ('Courier', 0xff7f007f, 10, None)
        PercentStringq = ('Courier', 0xff7f007f, 10, None)
        PercentStringr = ('Courier', 0xff000000, 10, None)
        PercentStringw = ('Courier', 0xff000000, 10, None)
        PercentStringx = ('Courier', 0xffffff00, 10, None)
        Regex = ('Courier', 0xff000000, 10, None)
        SingleQuotedString = ('Courier', 0xff7f007f, 10, None)
        Stderr = ('Courier', 0xff000000, 10, None)
        Stdin = ('Courier', 0xff000000, 10, None)
        Stdout = ('Courier', 0xff000000, 10, None)
        Symbol = ('Courier', 0xffc0a030, 10, None)
    
    class SQL:
        Comment = ('Courier', 0xff007f00, 10, None)
        CommentDoc = ('Courier', 0xff7f7f7f, 10, None)
        CommentDocKeyword = ('Courier', 0xff3060a0, 10, None)
        CommentDocKeywordError = ('Courier', 0xff804020, 10, None)
        CommentLine = ('Courier', 0xff007f00, 10, None)
        CommentLineHash = ('Courier', 0xff007f00, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DoubleQuotedString = ('Courier', 0xff7f007f, 10, None)
        Identifier = ('Courier', 0xff000000, 10, None)
        Keyword = ('Courier', 0xff00007f, 10, None)
        KeywordSet5 = ('Courier', 0xff4b0082, 10, None)
        KeywordSet6 = ('Courier', 0xffb00040, 10, None)
        KeywordSet7 = ('Courier', 0xff8b0000, 10, None)
        KeywordSet8 = ('Courier', 0xff800080, 10, None)
        Number = ('Courier', 0xff007f7f, 10, None)
        Operator = ('Courier', 0xff000000, 10, None)
        PlusComment = ('Courier', 0xff007f00, 10, None)
        PlusKeyword = ('Courier', 0xff7f7f00, 10, None)
        PlusPrompt = ('Courier', 0xff007f00, 10, None)
        QuotedIdentifier = ('Courier', 0xff000000, 10, None)
        SingleQuotedString = ('Courier', 0xff7f007f, 10, None)
    
    class Spice:
        Command = ('Courier', 0xff00007f, 10, None)
        Comment = ('Courier', 0xff007f00, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        Delimiter = ('Courier', 0xff000000, 10, None)
        Function = ('Courier', 0xff00007f, 10, None)
        Identifier = ('Courier', 0xff000000, 10, None)
        Number = ('Courier', 0xff007f7f, 10, None)
        Parameter = ('Courier', 0xff0040e0, 10, None)
        Value = ('Courier', 0xff7f007f, 10, None)
    
    class TCL:
        Comment = ('Courier', 0xff007f00, 10, None)
        CommentBlock = ('Courier', 0xff000000, 10, None)
        CommentBox = ('Courier', 0xff007f00, 10, None)
        CommentLine = ('Courier', 0xff007f00, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        ExpandKeyword = ('Courier', 0xff00007f, 10, None)
        ITCLKeyword = ('Courier', 0xff00007f, 10, None)
        Identifier = ('Courier', 0xff00007f, 10, None)
        KeywordSet6 = ('Courier', 0xff00007f, 10, None)
        KeywordSet7 = ('Courier', 0xff00007f, 10, None)
        KeywordSet8 = ('Courier', 0xff00007f, 10, None)
        KeywordSet9 = ('Courier', 0xff00007f, 10, None)
        Modifier = ('Courier', 0xff7f007f, 10, None)
        Number = ('Courier', 0xff007f7f, 10, None)
        Operator = ('Courier', 0xff000000, 10, None)
        QuotedKeyword = ('Courier', 0xff7f007f, 10, None)
        QuotedString = ('Courier', 0xff7f007f, 10, None)
        Substitution = ('Courier', 0xff7f7f00, 10, None)
        SubstitutionBrace = ('Courier', 0xff7f7f00, 10, None)
        TCLKeyword = ('Courier', 0xff00007f, 10, None)
        TkCommand = ('Courier', 0xff00007f, 10, None)
        TkKeyword = ('Courier', 0xff00007f, 10, None)
    
    class TeX:
        Command = ('Courier', 0xff007f00, 10, None)
        Default = ('Courier', 0xff3f3f3f, 10, None)
        Group = ('Courier', 0xff7f0000, 10, None)
        Special = ('Courier', 0xff007f7f, 10, None)
        Symbol = ('Courier', 0xff7f7f00, 10, None)
        Text = ('Courier', 0xff000000, 10, None)
    
    class VHDL:
        Attribute = ('Courier', 0xff804020, 10, None)
        Comment = ('Courier', 0xff007f00, 10, None)
        CommentLine = ('Courier', 0xff3f7f3f, 10, None)
        Default = ('Courier', 0xff800080, 10, None)
        Identifier = ('Courier', 0xff000000, 10, None)
        Keyword = ('Courier', 0xff00007f, 10, None)
        KeywordSet7 = ('Courier', 0xff804020, 10, None)
        Number = ('Courier', 0xff007f7f, 10, None)
        Operator = ('Courier', 0xff000000, 10, None)
        StandardFunction = ('Courier', 0xff808020, 10, None)
        StandardOperator = ('Courier', 0xff007f7f, 10, None)
        StandardPackage = ('Courier', 0xff208020, 10, None)
        StandardType = ('Courier', 0xff208080, 10, None)
        String = ('Courier', 0xff7f007f, 10, None)
        UnclosedString = ('Courier', 0xff000000, 10, None)
    
    class Verilog:
        Comment = ('Courier', 0xff007f00, 10, None)
        CommentBang = ('Courier', 0xff3f7f3f, 10, None)
        CommentLine = ('Courier', 0xff007f00, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        Identifier = ('Courier', 0xff000000, 10, None)
        Keyword = ('Courier', 0xff00007f, 10, None)
        KeywordSet2 = ('Courier', 0xff007f7f, 10, None)
        Number = ('Courier', 0xff007f7f, 10, None)
        Operator = ('Courier', 0xff007070, 10, None)
        Preprocessor = ('Courier', 0xff7f7f00, 10, None)
        String = ('Courier', 0xff7f007f, 10, None)
        SystemTask = ('Courier', 0xff804020, 10, None)
        UnclosedString = ('Courier', 0xff000000, 10, None)
        UserKeywordSet = ('Courier', 0xff2a00ff, 10, None)
    
    class XML:
        ASPAtStart = ('Courier', 0xff000000, 10, None)
        ASPJavaScriptComment = ('Courier', 0xff007f00, 10, None)
        ASPJavaScriptCommentDoc = ('Courier', 0xff7f7f7f, 10, None)
        ASPJavaScriptCommentLine = ('Courier', 0xff007f00, 10, None)
        ASPJavaScriptDefault = ('Courier', 0xff000000, 10, None)
        ASPJavaScriptDoubleQuotedString = ('Courier', 0xff7f007f, 10, None)
        ASPJavaScriptKeyword = ('Courier', 0xff00007f, 10, None)
        ASPJavaScriptNumber = ('Courier', 0xff007f7f, 10, None)
        ASPJavaScriptRegex = ('Courier', 0xff000000, 10, None)
        ASPJavaScriptSingleQuotedString = ('Courier', 0xff7f007f, 10, None)
        ASPJavaScriptStart = ('Courier', 0xff7f7f00, 10, None)
        ASPJavaScriptSymbol = ('Courier', 0xff000000, 10, None)
        ASPJavaScriptUnclosedString = ('Courier', 0xff000000, 10, None)
        ASPJavaScriptWord = ('Courier', 0xff000000, 10, None)
        ASPPythonClassName = ('Courier', 0xff0000ff, 10, None)
        ASPPythonComment = ('Courier', 0xff007f00, 10, None)
        ASPPythonDefault = ('Courier', 0xff808080, 10, None)
        ASPPythonDoubleQuotedString = ('Courier', 0xff7f007f, 10, None)
        ASPPythonFunctionMethodName = ('Courier', 0xff007f7f, 10, None)
        ASPPythonIdentifier = ('Courier', 0xff000000, 10, None)
        ASPPythonKeyword = ('Courier', 0xff00007f, 10, None)
        ASPPythonNumber = ('Courier', 0xff007f7f, 10, None)
        ASPPythonOperator = ('Courier', 0xff000000, 10, None)
        ASPPythonSingleQuotedString = ('Courier', 0xff7f007f, 10, None)
        ASPPythonStart = ('Courier', 0xff808080, 10, None)
        ASPPythonTripleDoubleQuotedString = ('Courier', 0xff7f0000, 10, None)
        ASPPythonTripleSingleQuotedString = ('Courier', 0xff7f0000, 10, None)
        ASPStart = ('Courier', 0xff000000, 10, None)
        ASPVBScriptComment = ('Courier', 0xff008000, 10, None)
        ASPVBScriptDefault = ('Courier', 0xff000000, 10, None)
        ASPVBScriptIdentifier = ('Courier', 0xff000080, 10, None)
        ASPVBScriptKeyword = ('Courier', 0xff000080, 10, None)
        ASPVBScriptNumber = ('Courier', 0xff008080, 10, None)
        ASPVBScriptStart = ('Courier', 0xff000000, 10, None)
        ASPVBScriptString = ('Courier', 0xff800080, 10, None)
        ASPVBScriptUnclosedString = ('Courier', 0xff000080, 10, None)
        ASPXCComment = ('Courier', 0xff000000, 10, None)
        Attribute = ('Courier', 0xff008080, 10, None)
        CDATA = ('Courier', 0xff800000, 10, None)
        Default = ('Courier', 0xff000000, 10, None)
        Entity = ('Courier', 0xff800080, 10, None)
        HTMLComment = ('Courier', 0xff808000, 10, None)
        HTMLDoubleQuotedString = ('Courier', 0xff7f007f, 10, None)
        HTMLNumber = ('Courier', 0xff007f7f, 10, None)
        HTMLSingleQuotedString = ('Courier', 0xff7f007f, 10, None)
        HTMLValue = ('Courier', 0xff608060, 10, None)
        JavaScriptComment = ('Courier', 0xff007f00, 10, None)
        JavaScriptCommentDoc = ('Courier', 0xff3f703f, 10, None)
        JavaScriptCommentLine = ('Courier', 0xff007f00, 10, None)
        JavaScriptDefault = ('Courier', 0xff000000, 10, None)
        JavaScriptDoubleQuotedString = ('Courier', 0xff7f007f, 10, None)
        JavaScriptKeyword = ('Courier', 0xff00007f, 10, None)
        JavaScriptNumber = ('Courier', 0xff007f7f, 10, None)
        JavaScriptRegex = ('Courier', 0xff000000, 10, None)
        JavaScriptSingleQuotedString = ('Courier', 0xff7f007f, 10, None)
        JavaScriptStart = ('Courier', 0xff7f7f00, 10, None)
        JavaScriptSymbol = ('Courier', 0xff000000, 10, None)
        JavaScriptUnclosedString = ('Courier', 0xff000000, 10, None)
        JavaScriptWord = ('Courier', 0xff000000, 10, None)
        OtherInTag = ('Courier', 0xff800080, 10, None)
        PHPComment = ('Courier', 0xff999999, 10, None)
        PHPCommentLine = ('Courier', 0xff666666, 10, None)
        PHPDefault = ('Courier', 0xff000033, 10, None)
        PHPDoubleQuotedString = ('Courier', 0xff007f00, 10, None)
        PHPDoubleQuotedVariable = ('Courier', 0xff00007f, 10, None)
        PHPKeyword = ('Courier', 0xff7f007f, 10, None)
        PHPNumber = ('Courier', 0xffcc9900, 10, None)
        PHPOperator = ('Courier', 0xff000000, 10, None)
        PHPSingleQuotedString = ('Courier', 0xff009f00, 10, None)
        PHPStart = ('Courier', 0xff800000, 10, None)
        PHPVariable = ('Courier', 0xff00007f, 10, None)
        PythonClassName = ('Courier', 0xff0000ff, 10, None)
        PythonComment = ('Courier', 0xff007f00, 10, None)
        PythonDefault = ('Courier', 0xff808080, 10, None)
        PythonDoubleQuotedString = ('Courier', 0xff7f007f, 10, None)
        PythonFunctionMethodName = ('Courier', 0xff007f7f, 10, None)
        PythonIdentifier = ('Courier', 0xff000000, 10, None)
        PythonKeyword = ('Courier', 0xff00007f, 10, None)
        PythonNumber = ('Courier', 0xff007f7f, 10, None)
        PythonOperator = ('Courier', 0xff000000, 10, None)
        PythonSingleQuotedString = ('Courier', 0xff7f007f, 10, None)
        PythonStart = ('Courier', 0xff808080, 10, None)
        PythonTripleDoubleQuotedString = ('Courier', 0xff7f0000, 10, None)
        PythonTripleSingleQuotedString = ('Courier', 0xff7f0000, 10, None)
        SGMLBlockDefault = ('Courier', 0xff000066, 10, None)
        SGMLCommand = ('Courier', 0xff000080, 10, None)
        SGMLComment = ('Courier', 0xff808000, 10, None)
        SGMLDefault = ('Courier', 0xff000080, 10, None)
        SGMLDoubleQuotedString = ('Courier', 0xff800000, 10, None)
        SGMLEntity = ('Courier', 0xff333333, 10, None)
        SGMLError = ('Courier', 0xff800000, 10, None)
        SGMLParameter = ('Courier', 0xff006600, 10, None)
        SGMLParameterComment = ('Courier', 0xff000000, 10, None)
        SGMLSingleQuotedString = ('Courier', 0xff993300, 10, None)
        SGMLSpecial = ('Courier', 0xff3366ff, 10, None)
        Script = ('Courier', 0xff000080, 10, None)
        Tag = ('Courier', 0xff000080, 10, None)
        UnknownAttribute = ('Courier', 0xff008080, 10, None)
        UnknownTag = ('Courier', 0xff000080, 10, None)
        VBScriptComment = ('Courier', 0xff008000, 10, None)
        VBScriptDefault = ('Courier', 0xff000000, 10, None)
        VBScriptIdentifier = ('Courier', 0xff000080, 10, None)
        VBScriptKeyword = ('Courier', 0xff000080, 10, None)
        VBScriptNumber = ('Courier', 0xff008080, 10, None)
        VBScriptStart = ('Courier', 0xff000000, 10, None)
        VBScriptString = ('Courier', 0xff800080, 10, None)
        VBScriptUnclosedString = ('Courier', 0xff000080, 10, None)
        XMLEnd = ('Courier', 0xff800080, 10, None)
        XMLStart = ('Courier', 0xff800080, 10, None)
        XMLTagEnd = ('Courier', 0xff000080, 10, None)
    
    class YAML:
        Comment = ('Courier', 0xff008800, 10, None)
        Default = ('Courier', 0xff000000, 10, None)
        DocumentDelimiter = ('Courier', 0xffffffff, 10, None)
        Identifier = ('Courier', 0xff000088, 10, None)
        Keyword = ('Courier', 0xff880088, 10, None)
        Number = ('Courier', 0xff880000, 10, None)
        Operator = ('Courier', 0xff000000, 10, None)
        Reference = ('Courier', 0xff008888, 10, None)
        SyntaxErrorMarker = ('Courier', 0xffffffff, 10, None)
        TextBlockMarker = ('Courier', 0xff333366, 10, None)


class Paper:
    Default = PyQt4.QtGui.QColor(0xffffffff)
    
    class Ada:
        Default = 0xffffffff
        Comment = 0xffffffff
        Keyword = 0xffffffff
        String = 0xffffffff
        Procedure = 0xffffffff
        Number = 0xffffffff
        Type = 0xffffffff
        Package = 0xffffffff
    
    class Nim:
        Default = 0xffffffff
        Comment = 0xffffffff
        BasicKeyword = 0xffffffff
        TopKeyword = 0xffffffff
        String = 0xffffffff
        LongString = 0xffffffff
        Number = 0xffffffff
        Operator = 0xffffffff
        Unsafe = 0xffffffff
        Type = 0xffffffff
        DocumentationComment = 0xffffffff
        Definition = 0xffffffff
        Class = 0xffffffff
        KeywordOperator = 0xffffffff
        CharLiteral = 0xffffffff
        CaseOf = 0xffffffff
        UserKeyword = 0xffffffff
        MultilineComment = 0xffffffff
        MultilineDocumentation = 0xffffffff
        Pragma = 0xffffffff
    
    class RouterOS:
        Default = 0xffffffff
        Operator = 0xffffffff
        Comment = 0xffffffff
        Keyword1 = 0xffffffff
        Keyword2 = 0xffffffff
        Keyword3 = 0xffffffff
    
    class Oberon:
        Default = 0xffffffff
        Comment = 0xffffffff
        Keyword = 0xffffffff
        String = 0xffffffff
        Procedure = 0xffffffff
        Module = 0xffffffff
        Number = 0xffffffff
        Type = 0xffffffff
    
    
    # Generated
    class AVS:
        Function = 0xffffffff
        KeywordSet6 = 0xffffffff
        TripleString = 0xffffffff
        LineComment = 0xffffffff
        Plugin = 0xffffffff
        String = 0xffffffff
        ClipProperty = 0xffffffff
        Default = 0xffffffff
        Operator = 0xffffffff
        Number = 0xffffffff
        Filter = 0xffffffff
        Identifier = 0xffffffff
        NestedBlockComment = 0xffffffff
        Keyword = 0xffffffff
        BlockComment = 0xffffffff
    
    class Bash:
        Error = 0xffff0000
        Backticks = 0xffa08080
        SingleQuotedHereDocument = 0xffddd0dd
        Scalar = 0xffffe0e0
        HereDocumentDelimiter = 0xffddd0dd
        Comment = 0xffffffff
        SingleQuotedString = 0xffffffff
        Default = 0xffffffff
        Operator = 0xffffffff
        ParameterExpansion = 0xffffffe0
        Number = 0xffffffff
        Identifier = 0xffffffff
        Keyword = 0xffffffff
        DoubleQuotedString = 0xffffffff
    
    class Batch:
        Label = 0xff606060
        Default = 0xffffffff
        Keyword = 0xffffffff
        ExternalCommand = 0xffffffff
        Variable = 0xffffffff
        Comment = 0xffffffff
        HideCommandChar = 0xffffffff
        Operator = 0xffffffff
    
    class CMake:
        Function = 0xffffffff
        BlockForeach = 0xffffffff
        BlockWhile = 0xffffffff
        StringLeftQuote = 0xffeeeeee
        Label = 0xffffffff
        Comment = 0xffffffff
        BlockMacro = 0xffffffff
        StringRightQuote = 0xffeeeeee
        Default = 0xffffffff
        Number = 0xffffffff
        BlockIf = 0xffffffff
        Variable = 0xffffffff
        KeywordSet3 = 0xffffffff
        String = 0xffeeeeee
        StringVariable = 0xffeeeeee
    
    class CPP:
        CommentDocKeywordError = 0xffffffff
        InactiveRegex = 0xffe0f0e0
        InactivePreProcessorComment = 0xffffffff
        UUID = 0xffffffff
        InactiveVerbatimString = 0xffe0ffe0
        SingleQuotedString = 0xffffffff
        Operator = 0xffffffff
        InactiveOperator = 0xffffffff
        InactivePreProcessor = 0xffffffff
        UnclosedString = 0xffe0c0e0
        Identifier = 0xffffffff
        InactiveRawString = 0xffffffff
        PreProcessor = 0xffffffff
        KeywordSet2 = 0xffffffff
        InactiveUnclosedString = 0xffe0c0e0
        InactiveCommentLine = 0xffffffff
        InactiveNumber = 0xffffffff
        InactivePreProcessorCommentLineDoc = 0xffffffff
        Number = 0xffffffff
        InactiveUUID = 0xffffffff
        CommentDoc = 0xffffffff
        InactiveCommentDoc = 0xffffffff
        GlobalClass = 0xffffffff
        InactiveSingleQuotedString = 0xffffffff
        HashQuotedString = 0xffe7ffd7
        VerbatimString = 0xffe0ffe0
        InactiveHashQuotedString = 0xffffffff
        Regex = 0xffe0f0e0
        InactiveGlobalClass = 0xffffffff
        InactiveIdentifier = 0xffffffff
        CommentLineDoc = 0xffffffff
        TripleQuotedVerbatimString = 0xffe0ffe0
        InactiveKeywordSet2 = 0xffffffff
        InactiveCommentDocKeyword = 0xffffffff
        Keyword = 0xffffffff
        InactiveCommentLineDoc = 0xffffffff
        InactiveDefault = 0xffffffff
        InactiveCommentDocKeywordError = 0xffffffff
        InactiveTripleQuotedVerbatimString = 0xffffffff
        CommentDocKeyword = 0xffffffff
        InactiveDoubleQuotedString = 0xffffffff
        CommentLine = 0xffffffff
        Comment = 0xffffffff
        PreProcessorComment = 0xffffffff
        InactiveComment = 0xffffffff
        RawString = 0xfffff3ff
        Default = 0xffffffff
        PreProcessorCommentLineDoc = 0xffffffff
        DoubleQuotedString = 0xffffffff
        InactiveKeyword = 0xffffffff
    
    class CSS:
        Important = 0xffffffff
        CSS3Property = 0xffffffff
        Attribute = 0xffffffff
        Comment = 0xffffffff
        SingleQuotedString = 0xffffffff
        MediaRule = 0xffffffff
        AtRule = 0xffffffff
        UnknownPseudoClass = 0xffffffff
        PseudoClass = 0xffffffff
        Tag = 0xffffffff
        CSS2Property = 0xffffffff
        CSS1Property = 0xffffffff
        IDSelector = 0xffffffff
        ExtendedCSSProperty = 0xffffffff
        Variable = 0xffffffff
        ExtendedPseudoClass = 0xffffffff
        ClassSelector = 0xffffffff
        Default = 0xffffffff
        PseudoElement = 0xffffffff
        UnknownProperty = 0xffffffff
        Value = 0xffffffff
        ExtendedPseudoElement = 0xffffffff
        DoubleQuotedString = 0xffffffff
        Operator = 0xffffffff
    
    class CSharp:
        CommentDocKeywordError = 0xffffffff
        InactiveRegex = 0xffffffff
        InactivePreProcessorComment = 0xffffffff
        UUID = 0xffffffff
        InactiveVerbatimString = 0xffffffff
        SingleQuotedString = 0xffffffff
        Operator = 0xffffffff
        InactiveOperator = 0xffffffff
        InactivePreProcessor = 0xffffffff
        UnclosedString = 0xffffffff
        Identifier = 0xffffffff
        InactiveRawString = 0xffffffff
        PreProcessor = 0xffffffff
        KeywordSet2 = 0xffffffff
        InactiveUnclosedString = 0xffffffff
        InactiveCommentLine = 0xffffffff
        InactiveNumber = 0xffffffff
        InactivePreProcessorCommentLineDoc = 0xffffffff
        Number = 0xffffffff
        InactiveUUID = 0xffffffff
        CommentDoc = 0xffffffff
        InactiveCommentDoc = 0xffffffff
        GlobalClass = 0xffffffff
        InactiveSingleQuotedString = 0xffffffff
        HashQuotedString = 0xffffffff
        VerbatimString = 0xffe0ffe0
        InactiveHashQuotedString = 0xffffffff
        Regex = 0xffffffff
        InactiveGlobalClass = 0xffffffff
        InactiveIdentifier = 0xffffffff
        CommentLineDoc = 0xffffffff
        TripleQuotedVerbatimString = 0xffffffff
        InactiveKeywordSet2 = 0xffffffff
        InactiveCommentDocKeyword = 0xffffffff
        Keyword = 0xffffffff
        InactiveCommentLineDoc = 0xffffffff
        InactiveDefault = 0xffffffff
        InactiveCommentDocKeywordError = 0xffffffff
        InactiveTripleQuotedVerbatimString = 0xffffffff
        CommentDocKeyword = 0xffffffff
        InactiveDoubleQuotedString = 0xffffffff
        CommentLine = 0xffffffff
        Comment = 0xffffffff
        PreProcessorComment = 0xffffffff
        InactiveComment = 0xffffffff
        RawString = 0xffffffff
        Default = 0xffffffff
        PreProcessorCommentLineDoc = 0xffffffff
        DoubleQuotedString = 0xffffffff
        InactiveKeyword = 0xffffffff
    
    class CoffeeScript:
        UUID = 0xffffffff
        CommentDocKeywordError = 0xffffffff
        GlobalClass = 0xffffffff
        VerbatimString = 0xffe0ffe0
        SingleQuotedString = 0xffffffff
        Operator = 0xffffffff
        Number = 0xffffffff
        Identifier = 0xffffffff
        Keyword = 0xffffffff
        UnclosedString = 0xffe0c0e0
        Regex = 0xffe0f0e0
        CommentDocKeyword = 0xffffffff
        BlockRegex = 0xffffffff
        CommentLineDoc = 0xffffffff
        PreProcessor = 0xffffffff
        CommentLine = 0xffffffff
        CommentBlock = 0xffffffff
        Comment = 0xffffffff
        KeywordSet2 = 0xffffffff
        BlockRegexComment = 0xffffffff
        Default = 0xffffffff
        DoubleQuotedString = 0xffffffff
        CommentDoc = 0xffffffff
    
    class D:
        BackquoteString = 0xffffffff
        CommentDocKeywordError = 0xffffffff
        Operator = 0xffffffff
        CommentNested = 0xffffffff
        KeywordDoc = 0xffffffff
        KeywordSet7 = 0xffffffff
        Keyword = 0xffffffff
        KeywordSecondary = 0xffffffff
        Identifier = 0xffffffff
        KeywordSet5 = 0xffffffff
        CommentDocKeyword = 0xffffffff
        KeywordSet6 = 0xffffffff
        CommentLineDoc = 0xffffffff
        CommentLine = 0xffffffff
        Comment = 0xffffffff
        Typedefs = 0xffffffff
        Character = 0xffffffff
        RawString = 0xffffffff
        Default = 0xffffffff
        Number = 0xffffffff
        UnclosedString = 0xffe0c0e0
        String = 0xffffffff
        CommentDoc = 0xffffffff
    
    class Diff:
        Header = 0xffffffff
        LineChanged = 0xffffffff
        Default = 0xffffffff
        LineRemoved = 0xffffffff
        Command = 0xffffffff
        Position = 0xffffffff
        LineAdded = 0xffffffff
        Comment = 0xffffffff
    
    class Fortran:
        Label = 0xffffffff
        Identifier = 0xffffffff
        DottedOperator = 0xffffffff
        PreProcessor = 0xffffffff
        Comment = 0xffffffff
        SingleQuotedString = 0xffffffff
        Default = 0xffffffff
        DoubleQuotedString = 0xffffffff
        ExtendedFunction = 0xffffffff
        UnclosedString = 0xffe0c0e0
        Number = 0xffffffff
        Continuation = 0xfff0e080
        IntrinsicFunction = 0xffffffff
        Keyword = 0xffffffff
        Operator = 0xffffffff
    
    class Fortran77:
        Label = 0xffffffff
        Identifier = 0xffffffff
        DottedOperator = 0xffffffff
        PreProcessor = 0xffffffff
        Comment = 0xffffffff
        SingleQuotedString = 0xffffffff
        Default = 0xffffffff
        DoubleQuotedString = 0xffffffff
        ExtendedFunction = 0xffffffff
        UnclosedString = 0xffe0c0e0
        Number = 0xffffffff
        Continuation = 0xfff0e080
        IntrinsicFunction = 0xffffffff
        Keyword = 0xffffffff
        Operator = 0xffffffff
    
    class HTML:
        HTMLValue = 0xffffefff
        PythonDefault = 0xffefffef
        Entity = 0xffffffff
        SGMLParameter = 0xffefefff
        SGMLDefault = 0xffefefff
        PHPVariable = 0xfffff8f8
        SGMLCommand = 0xffefefff
        PythonClassName = 0xffefffef
        VBScriptUnclosedString = 0xff7f7fff
        ASPJavaScriptDefault = 0xffdfdf7f
        ASPVBScriptStart = 0xffffffff
        VBScriptDefault = 0xffefefff
        PythonNumber = 0xffefffef
        PythonOperator = 0xffefffef
        ASPJavaScriptSingleQuotedString = 0xffdfdf7f
        PHPDefault = 0xfffff8f8
        XMLStart = 0xffffffff
        PythonFunctionMethodName = 0xffefffef
        ASPJavaScriptStart = 0xffffffff
        JavaScriptWord = 0xfff0f0ff
        PHPSingleQuotedString = 0xfffff8f8
        PythonTripleDoubleQuotedString = 0xffefffef
        JavaScriptComment = 0xfff0f0ff
        Default = 0xffffffff
        SGMLSingleQuotedString = 0xffefefff
        VBScriptComment = 0xffefefff
        ASPVBScriptNumber = 0xffcfcfef
        ASPJavaScriptCommentDoc = 0xffdfdf7f
        PythonIdentifier = 0xffefffef
        VBScriptKeyword = 0xffefefff
        JavaScriptDefault = 0xfff0f0ff
        PythonStart = 0xffffffff
        ASPPythonComment = 0xffcfefcf
        ASPJavaScriptWord = 0xffdfdf7f
        SGMLParameterComment = 0xffffffff
        JavaScriptSingleQuotedString = 0xfff0f0ff
        PythonSingleQuotedString = 0xffefffef
        HTMLSingleQuotedString = 0xffffffff
        ASPVBScriptString = 0xffcfcfef
        SGMLBlockDefault = 0xffcccce0
        PythonKeyword = 0xffefffef
        XMLTagEnd = 0xffffffff
        ASPVBScriptComment = 0xffcfcfef
        ASPPythonSingleQuotedString = 0xffcfefcf
        PHPDoubleQuotedVariable = 0xfffff8f8
        ASPJavaScriptComment = 0xffdfdf7f
        JavaScriptUnclosedString = 0xffbfbbb0
        JavaScriptDoubleQuotedString = 0xfff0f0ff
        UnknownAttribute = 0xffffffff
        ASPPythonOperator = 0xffcfefcf
        ASPJavaScriptSymbol = 0xffdfdf7f
        ASPPythonFunctionMethodName = 0xffcfefcf
        SGMLDoubleQuotedString = 0xffefefff
        PHPOperator = 0xfffff8f8
        JavaScriptNumber = 0xfff0f0ff
        PythonDoubleQuotedString = 0xffefffef
        ASPAtStart = 0xffffff00
        Script = 0xffffffff
        PHPCommentLine = 0xfffff8f8
        SGMLComment = 0xffefefff
        JavaScriptStart = 0xffffffff
        ASPPythonIdentifier = 0xffcfefcf
        ASPVBScriptKeyword = 0xffcfcfef
        ASPPythonTripleDoubleQuotedString = 0xffcfefcf
        ASPPythonKeyword = 0xffcfefcf
        ASPJavaScriptNumber = 0xffdfdf7f
        PHPStart = 0xffffefbf
        PythonTripleSingleQuotedString = 0xffefffef
        PHPNumber = 0xfffff8f8
        ASPPythonDefault = 0xffcfefcf
        SGMLSpecial = 0xffefefff
        OtherInTag = 0xffffffff
        JavaScriptCommentDoc = 0xfff0f0ff
        Tag = 0xffffffff
        XMLEnd = 0xffffffff
        CDATA = 0xffffdf00
        HTMLNumber = 0xffffffff
        SGMLError = 0xffff6666
        PHPKeyword = 0xfffff8f8
        ASPVBScriptUnclosedString = 0xff7f7fff
        ASPPythonNumber = 0xffcfefcf
        VBScriptString = 0xffefefff
        ASPPythonClassName = 0xffcfefcf
        ASPPythonStart = 0xffffffff
        JavaScriptRegex = 0xffffbbb0
        ASPJavaScriptUnclosedString = 0xffbfbbb0
        ASPJavaScriptCommentLine = 0xffdfdf7f
        SGMLEntity = 0xffefefff
        ASPJavaScriptDoubleQuotedString = 0xffdfdf7f
        ASPStart = 0xffffdf00
        Attribute = 0xffffffff
        ASPJavaScriptKeyword = 0xffdfdf7f
        ASPVBScriptDefault = 0xffcfcfef
        ASPVBScriptIdentifier = 0xffcfcfef
        ASPJavaScriptRegex = 0xffffbbb0
        VBScriptNumber = 0xffefefff
        HTMLDoubleQuotedString = 0xffffffff
        ASPXCComment = 0xffffffff
        VBScriptStart = 0xffffffff
        PHPDoubleQuotedString = 0xfffff8f8
        PHPComment = 0xfffff8f8
        ASPPythonTripleSingleQuotedString = 0xffcfefcf
        ASPPythonDoubleQuotedString = 0xffcfefcf
        JavaScriptKeyword = 0xfff0f0ff
        JavaScriptSymbol = 0xfff0f0ff
        VBScriptIdentifier = 0xffefefff
        HTMLComment = 0xffffffff
        UnknownTag = 0xffffffff
        JavaScriptCommentLine = 0xfff0f0ff
        PythonComment = 0xffefffef
    
    class IDL:
        CommentDocKeywordError = 0xffffffff
        InactiveRegex = 0xffe0f0e0
        InactivePreProcessorComment = 0xffffffff
        UUID = 0xffffffff
        InactiveVerbatimString = 0xffe0ffe0
        SingleQuotedString = 0xffffffff
        Operator = 0xffffffff
        InactiveOperator = 0xffffffff
        InactivePreProcessor = 0xffffffff
        UnclosedString = 0xffe0c0e0
        Identifier = 0xffffffff
        InactiveRawString = 0xffffffff
        PreProcessor = 0xffffffff
        KeywordSet2 = 0xffffffff
        InactiveUnclosedString = 0xffe0c0e0
        InactiveCommentLine = 0xffffffff
        InactiveNumber = 0xffffffff
        InactivePreProcessorCommentLineDoc = 0xffffffff
        Number = 0xffffffff
        InactiveUUID = 0xffffffff
        CommentDoc = 0xffffffff
        InactiveCommentDoc = 0xffffffff
        GlobalClass = 0xffffffff
        InactiveSingleQuotedString = 0xffffffff
        HashQuotedString = 0xffe7ffd7
        VerbatimString = 0xffe0ffe0
        InactiveHashQuotedString = 0xffffffff
        Regex = 0xffe0f0e0
        InactiveGlobalClass = 0xffffffff
        InactiveIdentifier = 0xffffffff
        CommentLineDoc = 0xffffffff
        TripleQuotedVerbatimString = 0xffe0ffe0
        InactiveKeywordSet2 = 0xffffffff
        InactiveCommentDocKeyword = 0xffffffff
        Keyword = 0xffffffff
        InactiveCommentLineDoc = 0xffffffff
        InactiveDefault = 0xffffffff
        InactiveCommentDocKeywordError = 0xffffffff
        InactiveTripleQuotedVerbatimString = 0xffffffff
        CommentDocKeyword = 0xffffffff
        InactiveDoubleQuotedString = 0xffffffff
        CommentLine = 0xffffffff
        Comment = 0xffffffff
        PreProcessorComment = 0xffffffff
        InactiveComment = 0xffffffff
        RawString = 0xfffff3ff
        Default = 0xffffffff
        PreProcessorCommentLineDoc = 0xffffffff
        DoubleQuotedString = 0xffffffff
        InactiveKeyword = 0xffffffff
    
    class Java:
        CommentDocKeywordError = 0xffffffff
        InactiveRegex = 0xffe0f0e0
        InactivePreProcessorComment = 0xffffffff
        UUID = 0xffffffff
        InactiveVerbatimString = 0xffe0ffe0
        SingleQuotedString = 0xffffffff
        Operator = 0xffffffff
        InactiveOperator = 0xffffffff
        InactivePreProcessor = 0xffffffff
        UnclosedString = 0xffe0c0e0
        Identifier = 0xffffffff
        InactiveRawString = 0xffffffff
        PreProcessor = 0xffffffff
        KeywordSet2 = 0xffffffff
        InactiveUnclosedString = 0xffe0c0e0
        InactiveCommentLine = 0xffffffff
        InactiveNumber = 0xffffffff
        InactivePreProcessorCommentLineDoc = 0xffffffff
        Number = 0xffffffff
        InactiveUUID = 0xffffffff
        CommentDoc = 0xffffffff
        InactiveCommentDoc = 0xffffffff
        GlobalClass = 0xffffffff
        InactiveSingleQuotedString = 0xffffffff
        HashQuotedString = 0xffe7ffd7
        VerbatimString = 0xffe0ffe0
        InactiveHashQuotedString = 0xffffffff
        Regex = 0xffe0f0e0
        InactiveGlobalClass = 0xffffffff
        InactiveIdentifier = 0xffffffff
        CommentLineDoc = 0xffffffff
        TripleQuotedVerbatimString = 0xffe0ffe0
        InactiveKeywordSet2 = 0xffffffff
        InactiveCommentDocKeyword = 0xffffffff
        Keyword = 0xffffffff
        InactiveCommentLineDoc = 0xffffffff
        InactiveDefault = 0xffffffff
        InactiveCommentDocKeywordError = 0xffffffff
        InactiveTripleQuotedVerbatimString = 0xffffffff
        CommentDocKeyword = 0xffffffff
        InactiveDoubleQuotedString = 0xffffffff
        CommentLine = 0xffffffff
        Comment = 0xffffffff
        PreProcessorComment = 0xffffffff
        InactiveComment = 0xffffffff
        RawString = 0xfffff3ff
        Default = 0xffffffff
        PreProcessorCommentLineDoc = 0xffffffff
        DoubleQuotedString = 0xffffffff
        InactiveKeyword = 0xffffffff
    
    class JavaScript:
        CommentDocKeywordError = 0xffffffff
        InactiveRegex = 0xffffffff
        InactivePreProcessorComment = 0xffffffff
        UUID = 0xffffffff
        InactiveVerbatimString = 0xffffffff
        SingleQuotedString = 0xffffffff
        Operator = 0xffffffff
        InactiveOperator = 0xffffffff
        InactivePreProcessor = 0xffffffff
        UnclosedString = 0xffffffff
        Identifier = 0xffffffff
        InactiveRawString = 0xffffffff
        PreProcessor = 0xffffffff
        KeywordSet2 = 0xffffffff
        InactiveUnclosedString = 0xffffffff
        InactiveCommentLine = 0xffffffff
        InactiveNumber = 0xffffffff
        InactivePreProcessorCommentLineDoc = 0xffffffff
        Number = 0xffffffff
        InactiveUUID = 0xffffffff
        CommentDoc = 0xffffffff
        InactiveCommentDoc = 0xffffffff
        GlobalClass = 0xffffffff
        InactiveSingleQuotedString = 0xffffffff
        HashQuotedString = 0xffffffff
        VerbatimString = 0xffffffff
        InactiveHashQuotedString = 0xffffffff
        Regex = 0xffe0f0ff
        InactiveGlobalClass = 0xffffffff
        InactiveIdentifier = 0xffffffff
        CommentLineDoc = 0xffffffff
        TripleQuotedVerbatimString = 0xffffffff
        InactiveKeywordSet2 = 0xffffffff
        InactiveCommentDocKeyword = 0xffffffff
        Keyword = 0xffffffff
        InactiveCommentLineDoc = 0xffffffff
        InactiveDefault = 0xffffffff
        InactiveCommentDocKeywordError = 0xffffffff
        InactiveTripleQuotedVerbatimString = 0xffffffff
        CommentDocKeyword = 0xffffffff
        InactiveDoubleQuotedString = 0xffffffff
        CommentLine = 0xffffffff
        Comment = 0xffffffff
        PreProcessorComment = 0xffffffff
        InactiveComment = 0xffffffff
        RawString = 0xffffffff
        Default = 0xffffffff
        PreProcessorCommentLineDoc = 0xffffffff
        DoubleQuotedString = 0xffffffff
        InactiveKeyword = 0xffffffff
    
    class Lua:
        Label = 0xffffffff
        Identifier = 0xffffffff
        StringTableMathsFunctions = 0xffd0d0ff
        CoroutinesIOSystemFacilities = 0xffffd0d0
        KeywordSet5 = 0xffffffff
        KeywordSet6 = 0xffffffff
        Preprocessor = 0xffffffff
        LineComment = 0xffffffff
        Comment = 0xffd0f0f0
        String = 0xffffffff
        Character = 0xffffffff
        Default = 0xffffffff
        Operator = 0xffffffff
        LiteralString = 0xffe0ffff
        Number = 0xffffffff
        KeywordSet8 = 0xffffffff
        KeywordSet7 = 0xffffffff
        BasicFunctions = 0xffd0ffd0
        Keyword = 0xffffffff
        UnclosedString = 0xffe0c0e0
    
    class Makefile:
        Default = 0xffffffff
        Operator = 0xffffffff
        Target = 0xffffffff
        Preprocessor = 0xffffffff
        Variable = 0xffffffff
        Comment = 0xffffffff
        Error = 0xffff0000
    
    class Matlab:
        SingleQuotedString = 0xffffffff
        Default = 0xffffffff
        Keyword = 0xffffffff
        Number = 0xffffffff
        Command = 0xffffffff
        Identifier = 0xffffffff
        Comment = 0xffffffff
        DoubleQuotedString = 0xffffffff
        Operator = 0xffffffff
    
    class Octave:
        SingleQuotedString = 0xffffffff
        Default = 0xffffffff
        Keyword = 0xffffffff
        Number = 0xffffffff
        Command = 0xffffffff
        Identifier = 0xffffffff
        Comment = 0xffffffff
        DoubleQuotedString = 0xffffffff
        Operator = 0xffffffff
    
    class PO:
        ProgrammerComment = 0xffffffff
        Flags = 0xffffffff
        MessageContextText = 0xffffffff
        MessageStringTextEOL = 0xffffffff
        MessageId = 0xffffffff
        MessageIdText = 0xffffffff
        Reference = 0xffffffff
        Comment = 0xffffffff
        MessageStringText = 0xffffffff
        MessageContext = 0xffffffff
        Fuzzy = 0xffffffff
        Default = 0xffffffff
        MessageString = 0xffffffff
        MessageContextTextEOL = 0xffffffff
        MessageIdTextEOL = 0xffffffff
    
    class POV:
        KeywordSet7 = 0xffd0d0d0
        KeywordSet6 = 0xffd0ffd0
        PredefinedFunctions = 0xffd0d0ff
        CommentLine = 0xffffffff
        PredefinedIdentifiers = 0xffffffff
        Comment = 0xffffffff
        Directive = 0xffffffff
        String = 0xffffffff
        BadDirective = 0xffffffff
        TypesModifiersItems = 0xffffffd0
        Default = 0xffffffff
        Operator = 0xffffffff
        Number = 0xffffffff
        KeywordSet8 = 0xffe0e0e0
        Identifier = 0xffffffff
        ObjectsCSGAppearance = 0xffffd0d0
        UnclosedString = 0xffe0c0e0
    
    class Pascal:
        PreProcessorParenthesis = 0xffffffff
        SingleQuotedString = 0xffffffff
        PreProcessor = 0xffffffff
        CommentLine = 0xffffffff
        Comment = 0xffffffff
        CommentParenthesis = 0xffffffff
        Asm = 0xffffffff
        Character = 0xffffffff
        Default = 0xffffffff
        Operator = 0xffffffff
        UnclosedString = 0xffe0c0e0
        Number = 0xffffffff
        Identifier = 0xffffffff
        Keyword = 0xffffffff
        HexNumber = 0xffffffff
    
    class Perl:
        Translation = 0xfff0e080
        BacktickHereDocument = 0xffddd0dd
        Array = 0xffffffe0
        QuotedStringQXVar = 0xffa08080
        PODVerbatim = 0xffc0ffc0
        DoubleQuotedStringVar = 0xffffffff
        Regex = 0xffa0ffa0
        HereDocumentDelimiter = 0xffddd0dd
        SubroutinePrototype = 0xffffffff
        BacktickHereDocumentVar = 0xffddd0dd
        QuotedStringQR = 0xffffffff
        SingleQuotedString = 0xffffffff
        QuotedStringQRVar = 0xffffffff
        SubstitutionVar = 0xffffffff
        Operator = 0xffffffff
        DoubleQuotedHereDocumentVar = 0xffddd0dd
        Identifier = 0xffffffff
        QuotedStringQX = 0xffffffff
        BackticksVar = 0xffa08080
        Keyword = 0xffffffff
        QuotedStringQ = 0xffffffff
        QuotedStringQQVar = 0xffffffff
        QuotedStringQQ = 0xffffffff
        POD = 0xffe0ffe0
        FormatIdentifier = 0xffffffff
        RegexVar = 0xffffffff
        Backticks = 0xffa08080
        DoubleQuotedHereDocument = 0xffddd0dd
        Scalar = 0xffffe0e0
        FormatBody = 0xfffff0ff
        Comment = 0xffffffff
        QuotedStringQW = 0xffffffff
        SymbolTable = 0xffe0e0e0
        Default = 0xffffffff
        Error = 0xffff0000
        SingleQuotedHereDocument = 0xffddd0dd
        Number = 0xffffffff
        Hash = 0xffffe0ff
        Substitution = 0xfff0e080
        DataSection = 0xfffff0d8
        DoubleQuotedString = 0xffffffff
    
    class PostScript:
        DictionaryParenthesis = 0xffffffff
        HexString = 0xffffffff
        DSCCommentValue = 0xffffffff
        ProcedureParenthesis = 0xffffffff
        Comment = 0xffffffff
        ImmediateEvalLiteral = 0xffffffff
        Name = 0xffffffff
        DSCComment = 0xffffffff
        Default = 0xffffffff
        Base85String = 0xffffffff
        Number = 0xffffffff
        ArrayParenthesis = 0xffffffff
        Literal = 0xffffffff
        BadStringCharacter = 0xffff0000
        Text = 0xffffffff
        Keyword = 0xffffffff
    
    class Properties:
        DefaultValue = 0xffffffff
        Default = 0xffffffff
        Section = 0xffe0f0f0
        Assignment = 0xffffffff
        Key = 0xffffffff
        Comment = 0xffffffff
    
    class Python:
        TripleDoubleQuotedString = 0xffffffff
        FunctionMethodName = 0xffffffff
        TabsAfterSpaces = 0xffffffff
        Tabs = 0xffffffff
        Decorator = 0xffffffff
        NoWarning = 0xffffffff
        UnclosedString = 0xffe0c0e0
        Spaces = 0xffffffff
        CommentBlock = 0xffffffff
        Comment = 0xffffffff
        TripleSingleQuotedString = 0xffffffff
        SingleQuotedString = 0xffffffff
        Inconsistent = 0xffffffff
        Default = 0xffffffff
        DoubleQuotedString = 0xffffffff
        Operator = 0xffffffff
        Number = 0xffffffff
        Identifier = 0xffffffff
        ClassName = 0xffffffff
        Keyword = 0xffffffff
        HighlightedIdentifier = 0xffffffff
    
    class Ruby:
        Symbol = 0xffffffff
        Stderr = 0xffff8080
        Global = 0xffffffff
        FunctionMethodName = 0xffffffff
        Stdin = 0xffff8080
        HereDocumentDelimiter = 0xffddd0dd
        PercentStringr = 0xffa0ffa0
        PercentStringQ = 0xffffffff
        ModuleName = 0xffffffff
        HereDocument = 0xffddd0dd
        SingleQuotedString = 0xffffffff
        PercentStringq = 0xffffffff
        Regex = 0xffa0ffa0
        Operator = 0xffffffff
        PercentStringw = 0xffffffe0
        PercentStringx = 0xffa08080
        POD = 0xffc0ffc0
        Keyword = 0xffffffff
        Stdout = 0xffff8080
        ClassVariable = 0xffffffff
        Identifier = 0xffffffff
        DemotedKeyword = 0xffffffff
        Backticks = 0xffa08080
        InstanceVariable = 0xffffffff
        Comment = 0xffffffff
        Default = 0xffffffff
        Error = 0xffff0000
        Number = 0xffffffff
        DataSection = 0xfffff0d8
        ClassName = 0xffffffff
        DoubleQuotedString = 0xffffffff
    
    class SQL:
        PlusComment = 0xffffffff
        KeywordSet7 = 0xffffffff
        PlusPrompt = 0xffe0ffe0
        CommentDocKeywordError = 0xffffffff
        CommentDocKeyword = 0xffffffff
        KeywordSet6 = 0xffffffff
        CommentLine = 0xffffffff
        Comment = 0xffffffff
        Operator = 0xffffffff
        QuotedIdentifier = 0xffffffff
        SingleQuotedString = 0xffffffff
        PlusKeyword = 0xffffffff
        Default = 0xffffffff
        DoubleQuotedString = 0xffffffff
        CommentLineHash = 0xffffffff
        KeywordSet5 = 0xffffffff
        Number = 0xffffffff
        KeywordSet8 = 0xffffffff
        Identifier = 0xffffffff
        Keyword = 0xffffffff
        CommentDoc = 0xffffffff
    
    class Spice:
        Function = 0xffffffff
        Delimiter = 0xffffffff
        Value = 0xffffffff
        Default = 0xffffffff
        Number = 0xffffffff
        Parameter = 0xffffffff
        Command = 0xffffffff
        Identifier = 0xffffffff
        Comment = 0xffffffff
    
    class TCL:
        SubstitutionBrace = 0xffffffff
        CommentBox = 0xfff0fff0
        ITCLKeyword = 0xfffff0f0
        TkKeyword = 0xffe0fff0
        Operator = 0xffffffff
        QuotedString = 0xfffff0f0
        ExpandKeyword = 0xffffff80
        KeywordSet7 = 0xffffffff
        TCLKeyword = 0xffffffff
        TkCommand = 0xffffd0d0
        Identifier = 0xffffffff
        KeywordSet6 = 0xffffffff
        CommentLine = 0xffffffff
        CommentBlock = 0xfff0fff0
        Comment = 0xfff0ffe0
        Default = 0xffffffff
        KeywordSet9 = 0xffffffff
        Modifier = 0xffffffff
        Number = 0xffffffff
        KeywordSet8 = 0xffffffff
        Substitution = 0xffeffff0
        QuotedKeyword = 0xfffff0f0
    
    class TeX:
        Symbol = 0xffffffff
        Default = 0xffffffff
        Command = 0xffffffff
        Group = 0xffffffff
        Text = 0xffffffff
        Special = 0xffffffff
    
    class VHDL:
        StandardOperator = 0xffffffff
        Attribute = 0xffffffff
        CommentLine = 0xffffffff
        Comment = 0xffffffff
        String = 0xffffffff
        Default = 0xffffffff
        Operator = 0xffffffff
        StandardPackage = 0xffffffff
        Number = 0xffffffff
        Identifier = 0xffffffff
        KeywordSet7 = 0xffffffff
        StandardFunction = 0xffffffff
        StandardType = 0xffffffff
        Keyword = 0xffffffff
        UnclosedString = 0xffe0c0e0
    
    class Verilog:
        CommentBang = 0xffe0f0ff
        UserKeywordSet = 0xffffffff
        Preprocessor = 0xffffffff
        CommentLine = 0xffffffff
        Comment = 0xffffffff
        KeywordSet2 = 0xffffffff
        Default = 0xffffffff
        Operator = 0xffffffff
        Number = 0xffffffff
        Identifier = 0xffffffff
        SystemTask = 0xffffffff
        String = 0xffffffff
        Keyword = 0xffffffff
        UnclosedString = 0xffe0c0e0
    
    class XML:
        HTMLValue = 0xffffefff
        PythonDefault = 0xffefffef
        Entity = 0xffffffff
        SGMLParameter = 0xffefefff
        SGMLDefault = 0xffefefff
        PHPVariable = 0xfffff8f8
        SGMLCommand = 0xffefefff
        PythonClassName = 0xffefffef
        VBScriptUnclosedString = 0xff7f7fff
        ASPJavaScriptDefault = 0xffdfdf7f
        ASPVBScriptStart = 0xffffffff
        VBScriptDefault = 0xffefefff
        PythonNumber = 0xffefffef
        PythonOperator = 0xffefffef
        ASPJavaScriptSingleQuotedString = 0xffdfdf7f
        PHPDefault = 0xfffff8f8
        XMLStart = 0xffffffff
        PythonFunctionMethodName = 0xffefffef
        ASPJavaScriptStart = 0xffffffff
        JavaScriptWord = 0xfff0f0ff
        PHPSingleQuotedString = 0xfffff8f8
        PythonTripleDoubleQuotedString = 0xffefffef
        JavaScriptComment = 0xfff0f0ff
        Default = 0xffffffff
        SGMLSingleQuotedString = 0xffefefff
        VBScriptComment = 0xffefefff
        ASPVBScriptNumber = 0xffcfcfef
        ASPJavaScriptCommentDoc = 0xffdfdf7f
        PythonIdentifier = 0xffefffef
        VBScriptKeyword = 0xffefefff
        JavaScriptDefault = 0xfff0f0ff
        PythonStart = 0xffffffff
        ASPPythonComment = 0xffcfefcf
        ASPJavaScriptWord = 0xffdfdf7f
        SGMLParameterComment = 0xffffffff
        JavaScriptSingleQuotedString = 0xfff0f0ff
        PythonSingleQuotedString = 0xffefffef
        HTMLSingleQuotedString = 0xffffffff
        ASPVBScriptString = 0xffcfcfef
        SGMLBlockDefault = 0xffcccce0
        PythonKeyword = 0xffefffef
        XMLTagEnd = 0xffffffff
        ASPVBScriptComment = 0xffcfcfef
        ASPPythonSingleQuotedString = 0xffcfefcf
        PHPDoubleQuotedVariable = 0xfffff8f8
        ASPJavaScriptComment = 0xffdfdf7f
        JavaScriptUnclosedString = 0xffbfbbb0
        JavaScriptDoubleQuotedString = 0xfff0f0ff
        UnknownAttribute = 0xffffffff
        ASPPythonOperator = 0xffcfefcf
        ASPJavaScriptSymbol = 0xffdfdf7f
        ASPPythonFunctionMethodName = 0xffcfefcf
        SGMLDoubleQuotedString = 0xffefefff
        PHPOperator = 0xfffff8f8
        JavaScriptNumber = 0xfff0f0ff
        PythonDoubleQuotedString = 0xffefffef
        ASPAtStart = 0xffffff00
        Script = 0xffffffff
        PHPCommentLine = 0xfffff8f8
        SGMLComment = 0xffefefff
        JavaScriptStart = 0xffffffff
        ASPPythonIdentifier = 0xffcfefcf
        ASPVBScriptKeyword = 0xffcfcfef
        ASPPythonTripleDoubleQuotedString = 0xffcfefcf
        ASPPythonKeyword = 0xffcfefcf
        ASPJavaScriptNumber = 0xffdfdf7f
        PHPStart = 0xffffefbf
        PythonTripleSingleQuotedString = 0xffefffef
        PHPNumber = 0xfffff8f8
        ASPPythonDefault = 0xffcfefcf
        SGMLSpecial = 0xffefefff
        OtherInTag = 0xffffffff
        JavaScriptCommentDoc = 0xfff0f0ff
        Tag = 0xffffffff
        XMLEnd = 0xffffffff
        CDATA = 0xfffff0f0
        HTMLNumber = 0xffffffff
        SGMLError = 0xffff6666
        PHPKeyword = 0xfffff8f8
        ASPVBScriptUnclosedString = 0xff7f7fff
        ASPPythonNumber = 0xffcfefcf
        VBScriptString = 0xffefefff
        ASPPythonClassName = 0xffcfefcf
        ASPPythonStart = 0xffffffff
        JavaScriptRegex = 0xffffbbb0
        ASPJavaScriptUnclosedString = 0xffbfbbb0
        ASPJavaScriptCommentLine = 0xffdfdf7f
        SGMLEntity = 0xffefefff
        ASPJavaScriptDoubleQuotedString = 0xffdfdf7f
        ASPStart = 0xffffdf00
        Attribute = 0xffffffff
        ASPJavaScriptKeyword = 0xffdfdf7f
        ASPVBScriptDefault = 0xffcfcfef
        ASPVBScriptIdentifier = 0xffcfcfef
        ASPJavaScriptRegex = 0xffffbbb0
        VBScriptNumber = 0xffefefff
        HTMLDoubleQuotedString = 0xffffffff
        ASPXCComment = 0xffffffff
        VBScriptStart = 0xffffffff
        PHPDoubleQuotedString = 0xfffff8f8
        PHPComment = 0xfffff8f8
        ASPPythonTripleSingleQuotedString = 0xffcfefcf
        ASPPythonDoubleQuotedString = 0xffcfefcf
        JavaScriptKeyword = 0xfff0f0ff
        JavaScriptSymbol = 0xfff0f0ff
        VBScriptIdentifier = 0xffefefff
        HTMLComment = 0xffffffff
        UnknownTag = 0xffffffff
        JavaScriptCommentLine = 0xfff0f0ff
        PythonComment = 0xffefffef
    
    class YAML:
        TextBlockMarker = 0xffffffff
        DocumentDelimiter = 0xff000088
        Operator = 0xffffffff
        Number = 0xffffffff
        Default = 0xffffffff
        Identifier = 0xffffffff
        Reference = 0xffffffff
        Comment = 0xffffffff
        Keyword = 0xffffffff
        SyntaxErrorMarker = 0xffff0000
    




