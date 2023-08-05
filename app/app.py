# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from config.load_config import LoadConfig

# # 创建 Flask 应用程序实例
# app = Flask(__name__)

# # 加载配置文件
# env = 'development'  # 或者从环境变量中获取
# config = LoadConfig.get_config(env)
# app.config.from_object(config)


# # 初始化数据库对象
# db = SQLAlchemy(app)

# # 导入和注册蓝图
# # from app.api.products.product_list import products_blueprint
# # from app.api.goods.goods_detail import goods_blueprint
# # from app.api.user.image_list import image_list

# # app.register_blueprint(products_blueprint, url_prefix='/products')
# # app.register_blueprint(goods_blueprint, url_prefix='/shop/goods')
# # app.register_blueprint(image_list, url_prefix='/user/wx/material')

# # 导入模型类，确保在初始化 db 对象之后导入
# from app.models.product import Product

# # 导入路由模块，确保在所有初始化之后导入
# from app import routes

# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()  # 创建数据库表
#     app.run(debug=True)
