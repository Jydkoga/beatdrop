import Files
import File

def Initialize(api):
    api.add_route('/files', Files.Files())
    api.add_route('/file/{filename}', File.File())