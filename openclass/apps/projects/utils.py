import os
import math
import hashlib

def get_partition_id(pk, chunk_size=1000):
    return int(math.ceil(pk/float(chunk_size)))

def safe_filename(filename):
    name, ext = os.path.splitext(filename)
    return "%s%s" % (hashlib.md5(name.encode('utf-8')).hexdigest(), ext)
