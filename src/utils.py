def get_config():
    return {
        "app_name": "MyApp",
        "version": "1.0.0",
        "debug": False,
    }


def log_message(message):
    print(f"[LOG] {message}")


if __name__ == "__main__":
    config = get_config()
    print(config)
