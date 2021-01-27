  
"""
This is where the application configuration is declared for Development, \
Testing and Production Environments.
"""
import os


class Config:
    """
    Base config class for the Flask App configuration
    """
    SECRET_KEY = os.getenv("SECRET_KEY", "my_very_secret_key")
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """
    Application configuration for the development environment
    """
    DEBUG = True
    ENV = "development"


class TestingConfig(Config):
    """
    Application configuration for the Testing Environment
    """
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(Config):
    """
    Application configuration for the Production environment
    """
    DEBUG = False


# This exports the Environment Configurations as classes that can then be 
# Selected when the application is being setup.
config_by_name = dict(
    development=DevelopmentConfig,
    testing=TestingConfig,
    production=ProductionConfig
)

key = Config.SECRET_KEY