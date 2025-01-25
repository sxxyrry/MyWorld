import os
from folder import folder
import log


MoLoD_log = log.get_log('MoLoD(ModsLoader)-莫楼得（模组加载器）')

MoLoD_log.config(level=log.DEBUG, format='{time} - {level} - {name} : {message}')

modsPath = os.path.join(folder, './mods')

modslist = []

def LoadMods():
    from texture import textures as ts, load_texture, Audio
    MoLoD_log.info(f'Loading mods from {modsPath}')
    ld = os.listdir(modsPath)
    for f in ld:
        if f.startswith('.py_forbidden') or (not f.endswith('.py')): continue
        fp = os.path.join(modsPath, f)

        MoLoD_log.info(f'Loading mods: {fp}')

        exec(f'''from mods.{f.split('.')[0]} import textures
for _ in textures:
    # print(_)
    ts.update({'{max(ts.keys()) + 1 : _}'})
    # print('a')''')
        
        modslist.append(f.split('.')[0])
        # exec(text)

    if ld == []:
        MoLoD_log.warning('No mods found')
    else:
        MoLoD_log.info('Mods loaded')
    
    # print(MoLoD_log.GetEventsList())

def GetModsList():
    return modslist
