SECRET_KEY = "this;is;a;secret;key"

# 数据库配置信息
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'zhiliaooa_course'
USERNAME = 'root'
PASSWORD = 'Cyber670'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

# 邮箱配置
MAIL_SERVER = "smtp.qq.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "haohao_a@qq.com"
MAIL_PASSWORD = "xxxxxxxxxxxxxxxx"  # SMTP服务授权码
MAIL_DEFAULT_SENDER = "haohao_a@qq.com"
