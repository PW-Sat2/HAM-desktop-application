# -*- mode: python -*-

block_cipher = None

added_files = [
         ( 'clean_configs', '.'),
         ( 'grc_linux', 'grc_linux' ),
         ( 'saved_frames', 'saved_frames' ),
	 ( 'clean_configs/README.txt', 'logs' ),
         ( 'config_linux/config.py', '.' )
         ]

a = Analysis(['main.py'],
             pathex=['/home/pwsat2/GitHub/HAM-desktop-application'],
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
          name='main',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='main',
               icon='/home/pwsat2/GitHub/HAM-desktop-application/ui/img/pw-sat2-logo.ico')
