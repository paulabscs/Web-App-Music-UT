from flask import Flask, send_from_directory
from Controllers.Controller import setup_database
from Controllers.APIController import api_controller

def routing(app):
    """
    /* Sets up routing for the Flask application.
       Maps URLs to specific files or handlers.
    */
    """
    @app.route('/')
    def serve_index():
        """
        /* Serves the index.html file when the root URL is requested.
           Ensures the user lands on the main page.
        */
        """
        return send_from_directory('static/html', 'index.html')

    @app.route('/js/<path:filename>')
    def serve_js(filename):
        """
        /* Serves JavaScript files from the static/js directory.
           Provides client with necessary script files.
        */
        """
        return send_from_directory('static/js', filename)

    @app.route('/css/<path:filename>')
    def serve_css(filename):
        """
        /* Serves CSS files from the static/css directory.
           Delivers stylesheets to the client.
        */
        """
        return send_from_directory('static/css', filename)

def create_app():
    """
    /* Configures and runs the Flask application.
       Performs initial setup and starts the server.
    */
    """
    app = Flask(__name__)
    setup_database() 
    routing(app)  
    app.register_blueprint(api_controller)  

    app.run(debug=True, host='localhost', port=5283) 
    return app

if __name__ == '__main__':
    """
    /* Entry point for the application.
       Calls create_app to start the Flask server.
    */
    """
    create_app()
