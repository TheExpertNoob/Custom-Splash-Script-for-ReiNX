# -*- mode: python -*-

block_cipher = None

added_files = [
         ( 'resources', 'resources' ),
         ]

a = Analysis(['CustomSplash.pyw'],
             pathex=['D:\\Downloads\\Custom-Splash-Script-for-ReiNX-GUI-master'],
             binaries=[],
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='CustomSplash',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='resources\\splash.ico')
