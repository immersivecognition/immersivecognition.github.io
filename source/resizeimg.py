from pil import Image
import os
import sys

def resize_aspect_fit(path, dest, final_size, fmt):
    dirs = os.listdir(path)
    for item in dirs:
        if item == '.DS_Store':
            continue
        if os.path.isfile(path + item):
            im = Image.open(path + item)
            f, e = os.path.splitext(path + item)
            size = im.size
            ratio = float(final_size) / min(size)
            new_image_size = tuple([int(x*ratio) for x in size])
            im = im.resize(new_image_size, Image.ANTIALIAS)
            new_im = Image.new("RGB" if fmt=='JPEG' else "RGBA", (final_size, final_size))
            new_im.paste(
                im, ((final_size-new_image_size[0])//2, (final_size-new_image_size[1])//2))

            width, height = new_im.size

            left = (width - final_size)/2
            top = (height - final_size)/2
            right = (width + final_size)/2
            bottom = (height + final_size)/2

            new_im.crop((left, top, right, bottom))

            fname, e = os.path.splitext(item)
            if fmt == 'JPEG':
                new_im.save(dest + fname + '.jpg', 'JPEG', quality=93)
            elif fmt == 'PNG':
                new_im.save(dest + fname + '.png', 'PNG')
            print(f"converted {item}")


resize_aspect_fit("content/people-images/", "app/static/people-images/", 130, 'JPEG')
resize_aspect_fit("content/project-images/", "app/static/project-images/", 100, 'PNG')