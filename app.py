from src.servers.web import WEB


if __name__ == "__main__":
    WEB.register_blueprints()
    WEB.start_app()
