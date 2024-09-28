from app import create_app

app = create_app()

app.secret_key = "your_secret_key"

if __name__ == "__main__":
    app.run()
