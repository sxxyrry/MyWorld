from PIL import Image
import os, time


SleepTime = 0.25

class GenerateMap:
    def __init__(
                 self,
                 imgSide1Path: str,
                 imgUpPath: str,
                 imgSide2Path: str,
                 imgDownPath: str,
                 imgSide3Path: str,
                 imgSide4Path: str,
                 outputImgPath: str
                ):
        if not os.path.exists('./cache'):
            os.makedirs('./cache')

        print('clean cache...')

        time.sleep(SleepTime)

        for file in os.listdir('cache'):
            os.remove(os.path.join('cache', file))

        time.sleep(SleepTime)

        print('finished')

        time.sleep(SleepTime)

        print('create transparent images...')

        time.sleep(SleepTime)

        self.GenerateTransparentImages('cache/cache1.png')

        time.sleep(SleepTime)

        print('finished')

        time.sleep(SleepTime)

        l1 = [imgSide1Path, imgSide2Path, imgSide3Path, imgSide4Path, imgUpPath, imgDownPath]
        print('rotate images...')
        for n, path in enumerate(l1):
            if path:  # 检查路径是否为空
                # print(f"Processing image: {os.path.abspath(path)}")
                self.RotateImage(path, f'cache/cache{n + 2}.png')

        time.sleep(SleepTime)

        print('finished')

        time.sleep(SleepTime)

        print('vertical concat images...') 
        self.VerticalConcatImages(
            'cache/cache2.png',
            'cache/cache3.png',
            'cache/cache4.png',
            'cache/cache5.png',
            'cache/cache8.png'
        )

        time.sleep(SleepTime)

        self.VerticalConcatImages(
            'cache/cache1.png',
            'cache/cache6.png',
            'cache/cache1.png',
            'cache/cache1.png',
            'cache/cache9.png'
        )

        time.sleep(SleepTime)

        self.VerticalConcatImages(
            'cache/cache1.png',
            'cache/cache7.png',
            'cache/cache1.png',
            'cache/cache1.png',
            'cache/cache10.png'
        )

        time.sleep(SleepTime)

        print('finished')

        time.sleep(SleepTime)
    
        print('horizontal concat images...') 
        self.HorizontalConcatImages(
            'cache/cache9.png',
            'cache/cache8.png',
            'cache/cache10.png',
            outputImgPath
        )

        time.sleep(SleepTime)

        print('finished')

        time.sleep(SleepTime)

        print('clean cache...')

        time.sleep(SleepTime)

        for file in os.listdir('cache'):
            os.remove(os.path.join('cache', file))

        time.sleep(SleepTime)

        print('finished')

        time.sleep(SleepTime)

    def GenerateTransparentImages(self, savepath: str):
        img = Image.new('RGBA', (16, 16), (0, 0, 0, 0))
        img.save(savepath)

    def RotateImage(self, path: str, savepath: str):
        # print(f"Opening image: {path}")
        img = Image.open(path)
        img = img.transpose(Image.ROTATE_270) # type: ignore
        img.save(savepath)

    def VerticalConcatImages(self, path1: str, path2: str, path3: str, path4: str, savepath: str):
        img1 = Image.open(path1)
        img2 = Image.open(path2)
        img3 = Image.open(path3)
        img4 = Image.open(path4)
        result = Image.new('RGBA', (16, 64), (255, 255, 255, 0))

        result.paste(img1, (0, 0))
        result.paste(img2, (0, 16))
        result.paste(img3, (0, 32))
        result.paste(img4, (0, 48))

        result.save(savepath)

    def HorizontalConcatImages(self, path1: str, path2: str, path3: str, savepath: str):
        img1 = Image.open(path1)
        img2 = Image.open(path2)
        img3 = Image.open(path3)
        img4 = Image.new('RGBA', (8, 16), (255, 255, 255, 0))
        result = Image.new('RGBA', (64, 64), (255, 255, 255, 0))

        result.paste(img4, (0, 0))
        result.paste(img1, (8, 0))
        result.paste(img2, (24, 0))
        result.paste(img3, (40, 0))
        result.paste(img4, (56, 0))

        result.save(savepath)

def main():
    # img = GenerateMap(
    #     '/assets/block/grass_side_carried.png',
    #     '/assets/block/dirt.png',
    #     '/assets/block/grass_side_carried.png',
    #     '/assets/block/grass_carried.png',
    #     '/assets/block/grass_side_carried.png',
    #     '/assets/block/grass_side_carried.png',
    #     '/assets/block/grass.png'
    # )
    pass

if __name__ == '__main__':
    main()
