#!/usr/bin/python3


import sys
import os
import functools
import subprocess


APPNAME = 'mif-starter'
VERSION = '0.1'

top = '..'                              # Project root directory.
out = 'build'                           # Build directory for tools.


def options(ctx):
    co = ctx.get_option_group('configure options')
    #co.add_option('--project-dir', action='store',
            #default=top,
            #help='Root directory of the project.')
    #co.add_option('--build-dir', action='store',
            #default=out,
            #help='Build directory of the project.')
    co.add_option('--tools-dir', action='store',
            default='tools',
            help=('Root directory of mif-starter (relative to '
                'project\'s root).'))
    co.add_option('--abs-tools-dir', action='store',
            default=os.path.join(top, 'tools'),
            help='Root directory of mif-starter')
    co.add_option('--content-dir', action='store',
            default=os.path.join(top, 'content'),
            help='Content directory.')
    co.add_option('--config-dir', action='store',
            default=os.path.join(top, 'config'),
            help='Configuration directory.')
    co.add_option('--config-file', action='store',
            default=os.path.join(top, 'config', 'config.py'),
            help='Project configuration file.')
    co.add_option('--extras-dir', action='store',
            default=os.path.join(top, 'extras'),
            help='Extra modules directory.')

    so = ctx.add_option_group('setup options')
    so.add_option("--dry-run", action="store_true",
            default=False,
            help="Print commands, but do not execute.")
    so.add_option('--python', action='store',
            default='python',
            help='Set Python interpreter to use.')


def configure(ctx):
    ctx.find_program('buildout', mandatory=False)
    ctx.find_program('git')
    ctx.find_program('virtualenv')
    ctx.find_program('python3', var='PYTHON')

    #ctx.env.PROJECT_DIR = ctx.options.project_dir
    #ctx.env.BUILD_DIR = ctx.options.build_dir
    ctx.env.TOOLS_DIR = ctx.options.tools_dir
    ctx.env.ABS_TOOLS_DIR = ctx.options.abs_tools_dir
    ctx.env.CONTENT_DIR = ctx.options.content_dir
    ctx.env.CONFIG_DIR = ctx.options.config_dir
    ctx.env.CONFIG_FILE = ctx.options.config_file
    ctx.env.EXTRAS_DIR = ctx.options.extras_dir
    ctx.find_program('xelatex', var='XELATEX')
    ctx.find_program('biber', var='BIBER')


def _render_templates(path, templates_names, context):
    """ Renders template using Jinja2 template engine.
    """
    from jinja2 import Environment, FileSystemLoader, exceptions
    env = Environment(
            block_start_string='<|',
            block_end_string='|>',
            variable_start_string='<<',
            variable_end_string='>>',
            loader=FileSystemLoader(path),
            )
    results = []
    for template_name in templates_names:
        try:
            template = env.get_template(template_name)
        except exceptions.TemplateSyntaxError as e:
            print('{0.filename} ({0.name}):{0.lineno} {0.message}'.format(
                e))
            raise
        results.append(template.render(context))
    return results


def _get_project_config(env):
    """ Returns project configuration as Python dict.
    """
    path = os.path.join(env.ABS_TOOLS_DIR, 'defaults', 'config.py')
    with open(path) as fp:
        config = eval(fp.read())
    try:
        file = open(env.CONFIG_FILE)
    except IOError:
        pass
    else:
        config.update(eval(file.read()))
    return config


def build(bld):
    path = (
            os.path.join(bld.env.CONFIG_DIR, 'templates'),
            os.path.join(top, bld.env.TOOLS_DIR, 'templates'),
            )
    templates_names = ('wscript', 'Makefile',)
    env = dict(bld.env)
    lines = []
    for key, value in env.items():
        if key != 'TOOLS_DIR' and (
                key.endswith('_DIR') or key.endswith('_FILE')):
            value = os.path.normpath(os.path.join(env['TOOLS_DIR'], value))
        lines.append('    ctx.env.{0} = \'{1}\''.format(key, value))
    env.update(_get_project_config(bld.env))
    env['configuration'] = '\n'.join(lines)
    results = _render_templates(path, templates_names, env)
    for template_name, result in zip(templates_names, results):
        with open(os.path.join(top, template_name), 'w') as outfile:
            outfile.write(result)


def _sh(cmd, dry_run=False):
    print(cmd)
    if not dry_run:
        rcode = subprocess.call(cmd, shell=True)
        if rcode > 0:
            sys.exit(rcode)


def virtualenv(ctx):
    """ Initialize virtualenv environment.
    """
    sh = functools.partial(_sh, dry_run=ctx.options.dry_run)
    sh('virtualenv --python={0} env'.format(
        ctx.options.python))
    sh('env/bin/pip install MarkupSafe Jinja2')
