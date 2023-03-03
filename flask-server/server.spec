# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['server.py'],
    pathex=["/home/kxsalmi/Markov-s-Letters/flask-server"],
    binaries=[],
    datas=[('templates', 'templates'),('resources/books/*.txt', 'resources/books/')],
    hiddenimports=['services.trie_service','services.markov_service','flask','pypdf2','pylint','nltk','virtualenv','pytest','python','templates',
    'jinja2', 'jinja2.ext', 'jinja2.loaders', 'flask.templating',
    'resources.books'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=True,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [('v', None, 'OPTION')],
    name='server',
    debug=True,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)