from sqlalchemy.orm import Session

from src import models


def get_image(db: Session, path_id: int):
    return db.query(models.Image).filter_by(id=path_id).first()