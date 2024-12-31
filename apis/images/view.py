import os

from PIL import Image
from fastapi import UploadFile, File
from starlette.responses import FileResponse

from . import imageRouter
from settings.settings import UPLOAD_DIRECTORY


@imageRouter.post("/resize")
async def resize_image(w: int, h: int, file: UploadFile = File()):
    image = Image.open(file.file)
    image = image.resize((w, h))
    # 保存处理后的图片到本地
    # TODO 保存到 dfs
    image_path = os.path.join(UPLOAD_DIRECTORY, file.filename)
    image.save(image_path)
    return FileResponse(image_path)


@imageRouter.post("/compression image")
async def compression_image(size: int, file: UploadFile = File()):
    pass


@imageRouter.post("/Add watermark")
async def add_watermark(file: UploadFile = File(), mark: UploadFile = File(), mode=0):
    pass
