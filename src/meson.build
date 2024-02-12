pkgdatadir = get_option('prefix') / get_option('datadir') / meson.project_name()
moduledir = pkgdatadir / 'paperpie'
gnome = import('gnome')


blueprints = custom_target('blueprints',
  input: files(
    'ui/gtk/help-overlay.blp',
    'ui/window.blp',
    'ui/view_stack.blp',
    'ui/letters_column.blp',
    'ui/todo_page.blp',
    'ui/draft_page.blp',
    'ui/reminders_page.blp',
    'ui/inbox_page.blp',
  ),
  output: '.',
  command: [find_program('blueprint-compiler'), 'batch-compile', '@OUTPUT@', '@CURRENT_SOURCE_DIR@', '@INPUT@'],
)

gnome.compile_resources('paperpie',
  'paperpie.gresource.xml',
  gresource_bundle: true,
  dependencies: blueprints,
  install: true,
  install_dir: pkgdatadir,
)

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', get_option('prefix') / get_option('localedir'))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'paperpie.in',
  output: 'paperpie',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir'),
  install_mode: 'r-xr--r--'
)

paperpie_sources = [
  '__init__.py',
  'main.py',
  'window.py',
  'view_stack.py',
  'letters_column.py',
  'todo_page.py',
  'draft_page.py',
  'reminders_page.py',
  'inbox_page.py',
]

install_data(paperpie_sources, install_dir: moduledir)
