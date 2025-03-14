class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/genai'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    GENERATED_IMAGES_DIR = "generated_images"