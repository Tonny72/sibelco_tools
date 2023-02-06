import os


# opbouw van de datastore
#   path
#       +-- tag1
#           +-- log1
#               +-- yyyy_mm_tag_log.csv
#           +-- log2
#       +-- tag2
#           +-- log1
#           +-- log2

class Datastore(object):
    def __init__(self, path):
        self.path = path

    def get_log_path(self, tag, log):
        return self.path + tag + os.sep + log
