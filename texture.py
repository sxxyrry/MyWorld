from ursina import load_texture, Audio, Texture
from typing import Literal, Any, TypedDict


class Textures(TypedDict):
    '''Typeed dictionary for textures'''
    texture: Any | Texture | None
    texture_3D: Any | Texture | None
    texture_type: Literal['assets/block', 'cube']
    scale: float
    sound: list[Audio]
    type: Literal['block', 'item']

grass_texture = load_texture('/VersionAssets/block/grass.png')
grass3D_texture = load_texture('/VersionAssets/block/3Dgrass.png')
dirt_texture = load_texture('/VersionAssets/block/dirt.png')
dirt3D_texture = load_texture('/VersionAssets/block/3Ddirt.png')
stone_texture = load_texture('/VersionAssets/block/stone.png')
stone3D_texture = load_texture('/VersionAssets/block/3Dstone.png')
cobblestone_texture = load_texture('/VersionAssets/block/cobblestone.png')
cobblestone3D_texture = load_texture('/VersionAssets/block/3Dcobblestone.png')
brick_texture = load_texture('/VersionAssets/block/oak_planks.png')
brick3D_texture = load_texture('/VersionAssets/block/3Dbrick.png')
axe_texture = load_texture('/VersionAssets/item/netherite_axe.png')
pickaxe_texture = load_texture('/VersionAssets/item/netherite_pickaxe.png')
shovel_texture = load_texture('/VersionAssets/item/netherite_shovel.png')
air_texture = load_texture('/VersionAssets/block/air.png')
# brick_texture = load_texture('/VersionAssets/block/oak_planks.png')
# brick3D_texture = load_texture('/VersionAssets/block/3Dbrick.png')

textures: dict[
               str,
               Textures
               ] = {
    'GrassBlock' : {
        "texture": grass_texture,
        "texture_3D": grass3D_texture,
        "texture_type": 'assets/block',
        "scale": 0.15,
        "sound": [Audio(f'/VersionAssets/music/dig/grass{i}.wav') for i in range(1, 5)],
        "type": 'block'
    },
    'Dirt': {
        "texture": dirt_texture,
        "texture_3D": dirt3D_texture,
        "texture_type": 'cube',
        "scale": 0.3,
        "sound": [Audio(f'/VersionAssets/music/dig/gravel{i}.wav') for i in range(1, 5)],
        "type": 'block'
    },
    'Stone': {
        "texture": stone_texture,
        "texture_3D": stone3D_texture,
        "texture_type": 'cube',
        "scale": 0.3,
        "sound": [Audio(f'/VersionAssets/music/dig/stone{i}.wav') for i in range(1, 5)],
        "type": 'block'
    },
    'Cobblestone': {
        "texture": cobblestone_texture,
        "texture_3D": cobblestone3D_texture,
        "texture_type": 'cube',
        "scale": 0.3,
        "sound": [Audio(f'/VersionAssets/music/dig/stone{i}.wav') for i in range(1, 5)],
        "type": 'block'
    },
    'Brick': {
        "texture": brick_texture,
        "texture_3D": brick3D_texture,
        "texture_type": 'cube',
        "scale": 0.3,
        "sound": [Audio(f'/VersionAssets/music/dig/wood{i}.wav') for i in range(1, 5)],
        "type": 'block'
    },
    # 'Air': {
    #     "texture": air_texture,
    #     "texture_3D": air_texture,
    #     "texture_type": 'cube',
    #     "scale": 0.3,
    #     "sound": [],
    #     "type": 'block'
    # },
    # 6: {
    #     "texture": axe_texture,
    #     "texture_3D": axe_texture,
    #     "texture_type": 'cube',
    #     "scale": 0.3,
    #     "sound": [],
    #     "type": 'item'
    # },
    # 7: {
    #     "texture": pickaxe_texture,
    #     "texture_3D": pickaxe_texture,
    #     "texture_type": 'cube',
    #     "scale": 0.3,
    #     "sound": [],
    #     "type": 'item'
    # },
    # 8: {
    #     "texture": shovel_texture,
    #     "texture_3D": shovel_texture,
    #     "texture_type": 'cube',
    #     "scale": 0.3,
    #     "sound": [],
    #     "type": 'item'
    # },
}

texturesIntStrDict = {
    i + 1 : list(textures.keys())[i] for i in range(len(textures))
}

texturesStrIntDict = {
    list(textures.keys())[i] : i + 1 for i in range(len(textures))
}
