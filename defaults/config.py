#!/usr/bin/python3
{
    # main.tex options
    'document_class': 'documentation',
    'document_class_args': '12pt, a4paper',
    'document_language': 'lithuanian',
    'use_annotation': False,
    'use_bibliography': True,
    'glossary': 'tools/examples/glossary.gls',
    'extra_packages': [],
    # style.sty options
    'font': 'Palemonas',
    'page_geometry': 'top=2.0cm, bottom=2.0cm, left=3.0cm, right=1.5cm',
    'bibliography_resources': [
        'bibliography.bib',
        ],
    # other options
    'git': [
        ('dump_log', {
            'output': 'git_log.tex',
            'format': r'format:%an & %ai & %s \\',
            'path': '../tools',
            }),
        ],
    'template_files': [
        'main.tex',
        'chapters.tex',
        'documentation.cls',
        'lithuanian.lbx',
        'title.sty',
        'global-config.tex',
        'bibliography.bib',
        'pglossary.py',
        'pglossary.sty',
        ],
    'concat_files': {
        'style.sty': [
            #'style/old.sty',
            'style/font.sty',
            'style/page.sty',
            'style/paragraph.sty',
            # TODO 'style/table.sty',
            'style/enumeration.sty',
            'style/footnotes.sty',
            'style/chapters.sty',
            'style/toc.sty',
            'style/figures.sty',
            'style/translations.sty',
            'style/bibliography.sty',
            'style/packages.sty',
            'style/math_operators.sty',
            'style/commands.sty',
            'style/theorems.sty',
            ],
        },
    }
