from flask import Flask
def create_app():
    app = Flask(__name__)
    app.secret_key = "super-secret-key"  # You can replace this with a .env variable later

    # Import and register blueprints
    from app.routes import user
    app.register_blueprint(user.user_bp)
    @app.after_request
    def set_response_headers(response):
        """
        This function runs after a request has been handled.
        It adds headers to the response to prevent caching.
        """
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
        return response
    # ==========================================================
    
    return app
