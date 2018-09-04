# -*- mode: python -*-

block_cipher = None

added_files = [
         ( 'misc\\pyinstaller_hack', 'tk'),
         ( 'misc\\pyinstaller_hack', 'tcl')
         ]

a = Analysis(['grc_part.py'],
             pathex=['D:\\Documents\\GitHub\\HAM-desktop-application\\grc_part'],
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
          exclude_binaries=True,
          name='grc_part',
          debug=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='grc_part',
               icon='D:\\Documents\\GitHub\\HAM-desktop-application\\grc_part\\misc\\pw-sat2-logo.ico')               
