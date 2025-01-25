from MoLoDAPI import textures, load_texture, Audio
_ = load_texture('/a_block.png')
textures.append({
    'texture': _,
    'texture_3D' : _,
    'texture_type': 'cube',
    'type': 'block',
    'scale': 0.15,
    'sound': [Audio(f'/VersionAssets/music/dig/grass{i}.wav') for i in range(1, 5)]
})
