from config.db_config import DbConfig

class DevelopmentConfig(DbConfig):
    DEBUG = True
    # 在开发环境中可以覆盖其他配置项

class ProductionConfig(DbConfig):
    # 在生产环境中可以覆盖其他配置项
    # todo 后续替换成生产环境db
    pass

class LoadConfig:
    @staticmethod
    def get_config(env):
        if env == 'development':
            return DevelopmentConfig()
        elif env == 'production':
            return ProductionConfig()
        else:
            raise ValueError(f"Invalid environment: {env}")


