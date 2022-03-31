from pydantic import BaseModel


class ImageBase(BaseModel):
    filename: str


class ImageCreate(ImageBase):
    pass


class ImageReturn(ImageBase):
    id: int
    product_id: int

    class Config:
        orm_mode = True


class Image(ImageReturn):
    pass
