from app import app

if __name__ == '__main__':
    with app.app_context():
        from app import db
        # todo
        # db.create_all()  # 创建数据库表
    app.run(debug=True)
