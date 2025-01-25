from ursina import * # type: ignore
from ursina.prefabs.first_person_controller import FirstPersonController
from typing import Any, Literal, Never
import os, random, json
from folder import folder


block_pick = 'GrassBlock'

IsFLy = False
LastEnterSpaceTime = 0.0
gravity = 0

def input(key):
    if key == 'escape':
        quit()
def update():
    global block_pick, IsFLy, LastEnterSpaceTime
    if held_keys['1']: block_pick = texturesIntStrDict[1] # type: ignore
    if held_keys['2']: block_pick = texturesIntStrDict[2] # type: ignore
    if held_keys['3']: block_pick = texturesIntStrDict[3] # type: ignore
    if held_keys['4']: block_pick = texturesIntStrDict[4] # type: ignore
    if held_keys['5']: block_pick = texturesIntStrDict[5] # type: ignore
    # if held_keys['6']: block_pick = 'Air' # type: ignore
    # if held_keys['7']: block_pick = 'Air' # type: ignore
    # if held_keys['8']: block_pick = 'Air' # type: ignore
    # if held_keys['9']: block_pick = 'Air' # type: ignore
    if held_keys['space']: # type: ignore
        if not IsFLy:
            if LastEnterSpaceTime == 0.0:
                LastEnterSpaceTime = time.time()
                return
            # print(time.time(), LastEnterSpaceTime, time.time() - LastEnterSpaceTime, (time.time() - LastEnterSpaceTime) <= 0.25)
            if (time.time() - LastEnterSpaceTime) <= 0.25:
                LastEnterSpaceTime = time.time()
                return
            
            LastEnterSpaceTime = time.time()
            IsFLy = True
            player.gravity = 0
            player.position = Vec3(player.position.x, player.position.y+1, player.position.z)
            player.collision = True
        else:
            if (time.time() - LastEnterSpaceTime) < 0.25:
                # LastEnterSpaceTime = time.time()
                return
            
            LastEnterSpaceTime = time.time()
            IsFLy = False
            player.gravity = gravity
            player.collision = False
            # player.position = Vec3(player.position.x, player.position.y-1, player.position.z)

    if (held_keys['left mouse'] or held_keys['right mouse']): arm.active() # type: ignore
    if not (held_keys['left mouse'] or held_keys['right mouse']): arm.passaive() # type: ignore
    # if held_keys['']: block_pick =  # type: ignore

app: Ursina = Ursina() # 创建Ursina应用程序（3D应用程序）
# window.icon = None
window.exit_button.enabled = False # 将退出按钮禁用

from texture import *
# from MoLoD import LoadMods, GetModsList

# grass_img = map.GenerateMap(
#         'VersionAssets/block/grass_side_carried.png',
#         'VersionAssets/block/dirt.png',
#         'VersionAssets/block/grass_side_carried.png',
#         'VersionAssets/block/grass_carried.png',
#         'VersionAssets/block/grass_side_carried.png',
#         'VersionAssets/block/grass_side_carried.png',
#         'VersionAssets/block/grass.png'
# )

path = os.path.join(folder, './models_compressed/assets')
if not os.path.exists(path):
    os.makedirs(path)

class Block(Button):
    def __init__(self, texture: str, position: tuple[int, int, int]):
        self.texture_: int = texturesStrIntDict[texture]
        self.texture_a : str = texture
        self.texture_2 = textures[texture]['texture'] if texture in textures.keys() else dirt_texture
        if texture == 'GrassBlock':
            super().__init__(
                parent = scene,
                position = position,
                model = 'assets/block.obj', # type: ignore
                # origin_y = 0.5,
                texture = self.texture_2,
                color = hsv(0, 0, 0.9), # type: ignore
                scale = 0.5,
                heghlignt_color = hsv(0, 0, 1),
            )
        else:
            super().__init__(
                parent = scene,
                position = position,
                model = 'cube', # type: ignore
                # origin_y = 0.5,
                texture = self.texture_2,
                color = hsv(0, 0, 0.9), # type: ignore
                heghlignt_color = hsv(0, 0, 1),
            )
    
    def input(self, key):
        if self.hovered:
            if key == 'right mouse down' and block_pick <= max(list(textures.keys())):
                block = Block(texture=block_pick, position=self.position + mouse.normal)
                if textures[block.texture_a]['sound'] != []:
                    random.choice(list(textures[block.texture_a]['sound'])).play()
            if key == 'left mouse down': # type: ignore
                destroy(self)
                if textures[self.texture_a]['sound'] != []:
                    random.choice(list(textures[self.texture_a]['sound'])).play()
    
    def update(self):
        if self.hovered:
            if held_keys['left mouse']: # type: ignore
                # destroy(self)
                # random.choice(list(textures[self.texture_][4])).play()

                pass

class Goods(Entity):
    def __init__(self, texture: int, n: int):
        if type(textures[texture]) == dict: # type: ignore
            super().__init__(
                parent = camera.ui,
                model = 'cube',
                texture = textures[texture]['texture_3D'] if texture in textures.keys() else dirt3D_texture, # type: ignore
                scale = Vec3(0.08, 0.08, 0.08),
                rotation = Vec3(0, 0, 0),
                position = Vec2(-0.45085+0.011+(n-1)*0.11, -0.44),
            )
        else:
            super().__init__(
                parent = camera.ui,
                model = 'cube',
                texture = textures[texture], # type: ignore
                scale = Vec3(0.08, 0.08, 0.08),
                rotation = Vec3(0, 0, 0),
                position = Vec2(-0.45085+0.011+(n-1)*0.11, -0.44),
            )
        

class Inventory1(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'cube',
            texture = '/VersionAssets/block/inventory1.png',
            scale = Vec3(1, 22/182, 0),
            position = Vec2(0, -0.44),
        )

class Inventory2(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'cube',
            texture = '/VersionAssets/block/inventory2.png',
            scale = Vec3(22/182+0.0055, 22/182+0.0055, 0),
        )
    
    def update(self):
        self.position = Vec2(-0.45085+0.011+(texturesStrIntDict[block_pick]-1)*0.11, -0.44+0.003)

class Arm(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'assets/arm.obj',
            texture = 'assets/arm_texture.png',
            scale = 0.2,
            rotation = Vec3(155, -25, 0),
            position = Vec2(1, -0.65),
        )

    def active(self):
        self.position = Vec2(0.9, -0.6)
    
    def passaive(self):
        self.position = Vec2(1, -0.65)

class ArmGoods(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'assets/block',
            texture = grass_texture,
            scale = 0.15,
            rotation = Vec3(-20, 25, 0),
            position = Vec2(-0.75, -0.5),
        )

    def update(self):
        if block_pick <= max(list(textures.keys())):
            self.texture = textures[block_pick]['texture']
            self.model = textures[block_pick]['texture_type']
            self.scale = textures[block_pick]['scale']
        else:
            self.scale = 0
        
# class MessageBox(Entity):
#     def __init__(
#             self,
#             text: str,
#             title: str,
#             # texture,
#             scale: float = 0,
#             position: tuple[float | int, float | int] = (0, 0),
#             backgroundColor: color.Color = color.black,
#             font: str = 'OpenSans-Regular.ttf',
#             textColor: color.Color = color.white
#            ):
#         super().__init__(
#             parent = camera.ui,
#             model = 'cube',
#             color = backgroundColor,
#             scale = scale,
#             position = position,
#             textures = None
#         )
#         title = Text(
#             parent = self,
#             font = font,
#             text = title,
#             color = textColor,
#             position = (-0.5, 0.5),
#         )

#         text = Text(
#             parent = self,
#             font = font,
#             text = text,
#             color = textColor,
#             position = (-0.5, -0.5),
#         )
#         # _ = Button(
#         #     parent = self,
#         #     text = 'a',
#         #     position = (0.5, -0.5),
#         #     scale = (0.5, 0.5),
#         #     highlight_color = color.white,
#         #     # on_click = destroy(self),
#         #     origin = (0,0),
#         # )

#         # _.add_script(lambda: destroy(self))

#         pass

class XYZType(TypedDict):
    X: int
    Y: int
    Z: int

class BlockType(TypedDict):
    X: int
    Y: int
    Z: int
    From: str
    Name: str

class MapType(TypedDict):
    Min: XYZType
    Max: XYZType
    Data: list[
        BlockType
    ]

def LoadMap(json_path: str):
    with open(json_path, 'r') as f:
        data: MapType = json.load(f)

    Min = data['Min']
    Min_x = Min['X']
    Min_y = Min['Y']
    Min_z = Min['Z']
    Max = data['Max']
    Max_x = Max['X']
    Max_y = Max['Y']
    Max_z = Max['Z']
    Data = data['Data']

    for block in Data:
        x = block['X']
        y = block['Y']
        z = block['Z']

        # print(x, y, z)

        # print((Min_x, Max_x), (Min_y, Max_y), (Min_z, Max_z))

        # print((x < Min_x, x > Max_x), (y < Min_y, y > Max_y), (z < Min_z, z > Max_z))

        if ((x < Min_x) or (x > Max_x)) or ((y < Min_y) or (y > Max_y)) or ((z < Min_z) or (z > Max_z)):
            raise Exception('Block out of range')
            # continue
    
        block = Block(texture=block['Name'], position=(x, y, z))

    # for x in range(-10, 11):
    #     for z in range(-10, 11):
    #         block = Block(texture='GrassBlock', position=(x, 0, z))

# block = Block(texture=1, position=(5, 0, 6))

sky = Sky()
player = FirstPersonController()

gravity = player.gravity

# text = Text(text='泥土是空方块的占位符', origin=(0,0), position=(-0.6, 0.4), scale=2, font='assets/simkai.ttf')
inventory1 = Inventory1()
inventory2 = Inventory2()
arm = Arm()
armgoods = ArmGoods()

# MessageBox('a','a')

# print(textures)

# LoadMods()

# mlt = Text(text=f'Mod list: {'\n'.join(GetModsList())}', origin=(0,0), position=(-0.6, 0), scale=2, font='assets/simkai.ttf')

for i in list(textures.keys()):
    goods = Goods(i, texturesStrIntDict[i]) # type: ignore

def run(MapJsonPath: str):
    LoadMap(MapJsonPath)

    app.run() # 运行Ursina应用程序（3D应用程序）

if __name__ == '__main__':
    run(os.path.join(folder, './map.json'))
    pass
