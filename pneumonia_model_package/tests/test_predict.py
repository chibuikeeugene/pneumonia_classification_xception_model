from pneumonia_model_package import predict
from pneumonia_model_package import __version__ as _version
from pneumonia_model_package.config import core



def test_prediction(img_file):
    # given
    filename = img_file
    expected_class =  'PNEUMONIA'

    # when
    pred =  predict.make_single_prediction(image_name = filename, 
                                           image_dir = core.VAL_FOLDER)
    
    # Then
    assert pred.get('image_class') is not None
    assert pred['version'] == _version
    assert pred.get('image_class')[0] == expected_class
