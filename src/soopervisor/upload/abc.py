"""
Expected behavior

Source folder (src/), destiny (dst/). Source contains src/file.txt

dst/ Does not exist:
    * create dst/ copy src/, result dst/file.txt

dst/ exists:
    * dst/src doesn't exist: create dst/src, copy src/, result dst/src/file.txt
    * dst/src exists: Show error
"""


class Uploader:
    """
    """
    pass
