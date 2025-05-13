from logging.config import fileConfig
from sqlalchemy import create_engine
from alembic import context
from app.orm import BaseORM

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = BaseORM.metadata  # Используем ваши модели

def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    url = config.get_main_option("sqlalchemy.url")
    engine = create_engine(url)
    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()