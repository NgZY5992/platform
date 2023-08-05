from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.load_config import LoadConfig

# 创建 Flask 应用程序实例
app = Flask(__name__)

# 加载配置文件
env = 'development'  # 或者从环境变量中获取
config = LoadConfig.get_config(env)
app.config.from_object(config)

# 初始化数据库对象
db = SQLAlchemy(app)

# 导入和注册蓝图
from app.routes.api.products.product import products_blueprint
from app.routes.api.images.image import image_blueprint
# from app.routes.api.goods.goods_detail import goods_blueprint
# from app.routes.api.user.image_list import image_list

app.register_blueprint(products_blueprint, url_prefix='/api/products')
app.register_blueprint(image_blueprint, url_prefix='/api/images')
# app.register_blueprint(goods_blueprint, url_prefix='/shop/goods')
# app.register_blueprint(image_list, url_prefix='/user/wx/material')

# 导入模型类，确保在初始化 db 对象之后导入
from app.models.product import Product

# 导入路由模块，确保在所有初始化之后导入
from app import routes
