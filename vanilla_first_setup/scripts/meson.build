pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
scriptsdir = join_paths(pkgdatadir, 'vanilla_first_setup/scripts')

sources = [
  'install-flathub.sh',
  'install-flathub-beta.sh',
  'install-nix.sh',
  'install-nvidia.sh',
  'install-microcode.sh',
]

install_data(sources, install_dir: scriptsdir)
