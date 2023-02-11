project(
  'dict-ecdict',
  license: 'MIT',
  version: '1.0.0',
)

PKG = 'ecdict'
URL = 'https://github.com/skywind3000/ECDICT-ultimate'
ZIP = 'ecdict-ultimate-csv.zip'

tmp = custom_target('tmp',
    output: PKG + '.csv',
    command: [find_program('cli/get-@0@.sh'.format(PKG))],
    env: [
      'URL=@0@/releases/download'.format(URL),
      'VER=@0@'.format(meson.project_version()),
      'PKG=@0@'.format(PKG),
      'ZIP=@0@'.format(ZIP),
      ]
  )

txt = custom_target('txt',
    output: PKG + '.txt',
    depends: [tmp],
    command: [
      find_program('cli/gen-@0@.py'.format(PKG)),
      get_option('mini') ? '--mini' : '--no-mini',
      '-i',
      PKG + '.csv',
      '-o',
      PKG + '.txt'
      ]
  )

custom_target('dict', 
    output: [PKG + '.index', PKG + '.dict.dz'],
    depends: [txt],
    command: [
	  find_program('cli/fmt-dict.sh'),
      '--utf8',
      '--allchars',
      '-s',
      PKG.to_upper(),
      '-j'
      ],
    env: ['PKG=@0@'.format(PKG)],
    install: true,
    install_dir: get_option('datadir') / 'dictd'
  )
