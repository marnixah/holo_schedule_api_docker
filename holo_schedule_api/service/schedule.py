class Schedule:
    """ Hololive schedule structre data
    """
    def __new__(cls, time, member, youtube_url, title):
        if not "youtube" in youtube_url:
            return None
        return super(Schedule, cls).__new__(cls)

    def __init__(self, time, member, youtube_url, title):
        self.time = time
        self.member = member
        self.youtube_url = youtube_url
        self.title = title

    def to_dict(self):
        return {
            "time": self.time,
            "member": self.member,
            "youtube_url": self.youtube_url,
            "title": self.title
        }