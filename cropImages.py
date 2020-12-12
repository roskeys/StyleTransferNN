from PIL import Image
import torchvision.transforms as transforms

imsize = 512
loader = transforms.Compose([transforms.CenterCrop(imsize)])


def image_loader(image_name):
    image = Image.open(image_name)
    if image.size[0] > 2 * imsize and image.size[1] > 2 * imsize:
        times = min(image.size[0], image.size[1]) / imsize
        new_size = (int(image.size[0] / times), int(image.size[1] / times))
        image = image.resize(new_size)
    image = loader(image)
    image.save(f"cropted/{image_name}_cropted.png", format='PNG')


if __name__ == '__main__':
    image_loader("test.png")
