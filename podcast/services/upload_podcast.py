import cloudinary.uploader
from devcast_backend.settings.base import CLOUDINARY_API_SECRET, CLOUDINARY_API_KEY

cloudinary.config(
    cloud_name='dafuxnger',
    api_secret=CLOUDINARY_API_SECRET,
    api_key=CLOUDINARY_API_KEY
)


class Upload:

    def upload(filename, user):
        response = cloudinary.uploader.upload_large(
            file = filename,
            folder=str(user),
            resource_type = 'video',
            cloud_name='dafuxnger',
            public_id=str(filename)
        )
        
        return response

    def delete(filename, user):
        response = cloudinary.uploader.destroy(
            resource_type='video',
            public_id=user + '/' + filename
        )

        return response
