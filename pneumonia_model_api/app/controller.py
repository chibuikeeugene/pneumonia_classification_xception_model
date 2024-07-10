import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from fastapi import APIRouter, UploadFile
from loguru import logger
from pneumonia_model_package import predict as p
from werkzeug.utils import secure_filename
from app.validation import UPLOAD_FOLDER, allowed_img_format

#create an instance of the router
api_router = APIRouter()

@api_router.post('/predict/chest_xray_classifier')
def predict_image(file: UploadFile):
    # check for file availability
    if not file:
        return {'message': 'no upload file sent'}
    else:
        data = file.filename
    logger.success(f"{data} received successfully")

    # validate and ensure file is secured
    if data and allowed_img_format(data):
        secure_data = secure_filename(data)
    
    # save the file to a location where we can access it
    with open(os.path.join(UPLOAD_FOLDER, secure_data), 'wb') as f:
        f.write(file.file.read())
    logger.success(f"file successfully saved to destination folder: {UPLOAD_FOLDER}")

    # call the predict function
    result  = p.make_single_prediction(
        image_dir=UPLOAD_FOLDER,
        image_name=secure_data
    )

    readable_predictions = result.get('image_class')
    version = result.get('version')

    return dict([
        ('readable_prediction', readable_predictions),
        ('version', version)
    ]
    )