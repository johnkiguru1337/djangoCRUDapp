# Put this in a storage.py files in your app
from django.conf import settings
from django.core.files.storage import FileSystemStorage, get_storage_class
from django.utils.functional import LazyObject

class UploadsStorage(FileSystemStorage):
    def __init__(self, location=None, base_url=None, *args, **kwargs):
        if location is None:
            location = getattr(settings, 'UPLOADS_ROOT', None)
        super(UploadsStorage, self).__init__(location, base_url, *args, **kwargs)
        self.base_url = None  # forbid any URL generation for uploads

class ConfiguredStorage(LazyObject):
    def _setup(self):
        storage = getattr(settings, 'UPLOADS_STORAGE', None)
        klass = UploadsStorage if storage is None else get_storage_class(storage)
        self._wrapped = klass()
uploads_storage = ConfiguredStorage()