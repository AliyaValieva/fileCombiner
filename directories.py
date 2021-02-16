# Aliya Valieva
# avalieva

from pathlib import Path


def make_dir(user_dir_input):
    global p, fp
    if user_dir_input == 'DONE':
        raise KeyboardInterrupt

    p = Path(user_dir_input)

    if not p.exists():
        print("Such directory does not exist")
        p.mkdir()
        exit()

    files = []
    for f in p.glob('*.csv'):
        files.append(f)

    reportp = p/Path('Reports')
    if not reportp.exists():
        reportp.mkdir()
    return files

