# -*- mode: python -*-

block_cipher = None


a = Analysis(["D:\\SPJ\\PYTHON\\JB's", 'Projects\\Black', 'Jacks\\Backup\\Black_Jack_Ver.1.5.py'],
             pathex=["D:\\SPJ\\PYTHON\\JB's Projects\\Black Jacks\\Backup"],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='JB's',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True , icon='1.ico')
