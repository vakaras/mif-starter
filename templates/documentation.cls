<| block document_class_documentation |>
% First identify the class:

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{documentation}

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{report}}

\ProcessOptions

\LoadClass{report}

<| block document_class_documentation_chapter |>
\renewcommand{\@makechapterhead}[1]{%
  \vspace*{50\p@}%
  { \parindent \z@ \raggedright \normalfont
    \interlinepenalty\@M
    \Huge \textbf{ \thechapter.\ #1}\par
    \nobreak
    \vskip 40\p@
    }}
<| endblock |>
<| block document_class_documentation_extra |>
<| endblock |>

\endinput
<| endblock |>
