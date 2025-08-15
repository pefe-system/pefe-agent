from .consumer import Consumer
import lmdb
from ..config import *
import msgpack
import msgpack_numpy

msgpack_numpy.patch()

class PEFEConsumer(Consumer):
    def __init__(self, identity):
        super().__init__(identity)
        self.db = lmdb.open(config['self']['lmdb_path'], map_size=1024 * 1024 * 1024 * 1024) # 1 TB
    
    def handle_pe_file(self, path):
        """Returns ID and extracted features (numpy array or otherwise must be serializable)"""
        raise NotImplementedError
    
    def handle_content(self, content):
        print(f"Received content: {str(content)}")
        path = content['path']
        label = content['label']
        key, extracted_features = self.handle_pe_file(path)

        payload = {
            "lb": label,
            "ef": extracted_features
        }

        with self.db.begin(write=True) as txn:
            txn.put(key, msgpack.packb(payload, use_bin_type=True))
