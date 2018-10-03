# -*- mode: python -*-

block_cipher = None

import os
import germaniumdrivers

import germanium

def add_files(m, module_name):
    for module_path in m.__path__:
        for root, dirs, files in os.walk(module_path):
            for name in files:
                if not name.endswith('.js'):
                    continue

                full_path = os.path.join(root, name)
                #print(full_path)
                datas.append( (full_path, os.path.join(module_name + root[len(module_path):]) ) )

datas = [
    ('js/main.js', 'js'),
    (germaniumdrivers.ensure_driver('chrome'), r'germaniumdrivers/binary/chrome/linux/64'),
    (germaniumdrivers.ensure_driver('firefox'), r'germaniumdrivers/binary/firefox/linux/64'),
]

datas.append(('germaniumsb/favicon.ico', 'germaniumsb/'))

add_files(germanium, "germanium")

def add_files(m):
    for root, dirs, files in os.walk(m.__path__):
        for name in files:
            full_path = os.path.join(root, name)

a = Analysis(['germaniumsb/mainapp.py'],
             pathex=['./germaniumsb'],
             binaries=[],
             datas=datas,
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
          name='main',
          debug=False,
          strip=False,
          upx=True,
          console=True,
          icon='germaniumsb/favicon.ico',
)
