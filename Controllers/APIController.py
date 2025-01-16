from flask import Blueprint, jsonify, request
from Data.DBContext.TrackRepo import TrackRepository
from Data.RepoContext.repo_context import RepoContext

api_controller = Blueprint('api_controller', __name__)

# Factory function to create repository instances
def repo_factory(session):
    return TrackRepository(session)

@api_controller.route('/api/get_version', methods=['GET'])  
def get_version():
    return jsonify({"version": "1.01"})  # Simplified response format

@api_controller.route('/api/get_tracks', methods=['GET'])  # identifies the API name such that api/get_tracks is the base URL
def get_tracks():
    page = int(request.args.get('page', 1))  # page number
    page_size = 20  # Set the number of tracks per page
    context = RepoContext(repo_factory)
    
    all_tracks = context.get_tracks_dict()  # Get all tracks as a list of dictionaries
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    paginated_tracks = all_tracks[start_index:end_index]  # Get the tracks for the requested page
    
    response = jsonify(paginated_tracks)
    response.status_code = 200
    return response

