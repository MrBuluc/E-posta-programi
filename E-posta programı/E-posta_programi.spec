# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['E-posta_programi.py'],
             pathex=['C:\\Users\\HAKKICAN\\Desktop\\Python ile Programlama Sıfırdan İleri Seviyeye Python 3\\Sifirdan-Ileri-Seviyeye-Python-Programlama-master\\PyQt5 - Arayüz Geliştirme\\homework\\E-posta programı'],
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
          [],
          exclude_binaries=True,
          name='E-posta_programi',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='E-posta_programi')
