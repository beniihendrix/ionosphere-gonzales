"""

This is just a rudementary serial data logger using the pyubx2 library

"""

from serial import Serial
from pyubx2 import UBXReader
from pathlib import Path
from datetime import datetime

# initalize the folder for data according to the time and day

now = datetime.now().strftime("%m%d%H%M")

dir_path = Path.home() / "Documents" / "gps" / "recordings" / now
dir_path.mkdir(parents=True, exist_ok=True)
log_file_path = dir_path / "gnss_log.ubx"

print(f"Logging to {log_file_path}")

# opening file stream to write in binary

with open(log_file_path, "wb") as f_out:
    with Serial('/dev/serial0', 115200, timeout=1) as stream:
        ubr = UBXReader(stream)     # initializing the ubx stream
        for (raw_data, parsed_data) in ubr:
            if raw_data:
                f_out.write(raw_data)
                f_out.flush()
            if parsed_data:
                print(parsed_data)
