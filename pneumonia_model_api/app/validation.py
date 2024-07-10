from pathlib import Path

# define the package directory
PACKAGE_ROOT = Path(__file__).resolve().parent.parent

# create an upload folder directory to store files uploaded when predict endpoint is called
UPLOAD_FOLDER = PACKAGE_ROOT / 'uploads'
UPLOAD_FOLDER.mkdir(exist_ok=True)


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_img_format(file: str):
    return '.' in file and file.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS 