from yaml import safe_load
from pathlib import Path

class paste_client_config():
    def __init__(self, file_path) -> None:
        if Path(file_path).is_file():
            with open(file_path, 'r') as f:
                config = safe_load(f)
                self.server_address = config['server_address']
                self.uid = config['uid']
                self.cid = config['cid']
                self.pubkey = config['pubkey']
                self.privkey = config['privkey']
        else:
            Path(file_path).parent.mkdir(parents=True, exist_ok=True)
            with open(file_path, 'w') as f:
                f.write('')
                self.server_address = ""
                self.uid = ""
                self.cid = ""
                self.pubkey = ""
                self.privkey = ""
        
