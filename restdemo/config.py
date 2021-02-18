class Config:
    # SQLALCHEMY_DATABASE_URI = "sqlite:///demo.db"
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://demo:@192.168.64.2:3306/demo'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    