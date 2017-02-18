class VideoCacheBackend(object):
    def set(self, file):
        file.generate()

    def validate(self, file):
        self.set(file)
        print 'validate'

    def invalidate(self, file):
        file.delete()

    def clear(self, file):
        self.invalidate(file)

class CeleryVideoCacheBackend(VideoCacheBackend):
    pass

def get_videokit_cache_backend():
    return VideoCacheBackend()

