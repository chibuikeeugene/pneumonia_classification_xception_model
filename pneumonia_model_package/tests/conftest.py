import pytest

from pneumonia_model_package.config import core
from pneumonia_model_package.config.core import config
import os

@pytest.fixture
def img_file() -> str:
    filename = config.modelConfig.sample_test_image
    return filename