import re
import chardet
from pathlib import Path

# Thanks to: https://stackoverflow.com/a/45167602
def predict_encoding(file_path: Path, n_lines: int=20) -> str:
    '''Predict a file's encoding using chardet'''

    # Open the file as binary data
    with Path(file_path).open('rb') as f:
        # Join binary lines for specified number of lines
        rawdata = b''.join([f.readline() for _ in range(n_lines)])

    return chardet.detect(rawdata)['encoding']

# Enter path to file in FILE_PATH or copy file contents into STRING.
# enter path string as '<path_to_file>'; if relative path doesn't work, try absolute
FILE_PATH = ''
# enter multi-line string as """ <string across many lines> """
STRING = """{p}{col:2f63a0}STRENGTHS:{/col} {col:747ea4}Her demeanor might lead to others underestimating her, especially her weight or the force with which she can throw a punch. She might have an upper hand from that surprise.{/col}
{col:2f63a0}WEAKNESSES:{/col} {col:747ea4}Definitely doesn't have the strength or prowess for a prolonged fight.{/col}{/p}

{img:Interface\PETBATTLES\Weather-Rain:512:2}


{h2:r}{icon:ability_druid_eclipse:40}{/h2}"""

if FILE_PATH != '':
    encoding = predict_encoding(FILE_PATH)
    out = ''.join([re.sub("\{.*?\}", "", line) for line in open(FILE_PATH, 'r', encoding=encoding)])
    if STRING != '':
        raise ValueError(f"FILE_PATH was provided as {FILE_PATH}, but also received STRING. Use one or the other.")
else:
    if STRING != '':
        out = re.sub("\{.*?\}", "", STRING)
    else:
        raise ValueError(f"Neither FILE_PATH nor STRING were provided.")

print(out)
