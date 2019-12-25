from pathlib import Path
import os
import ftplib
import getpass

try:
    jwa_dir = Path(__file__).parent
    os.chdir(jwa_dir)
except NameError:
    jwa_dir = Path(os.getcwd())

site_dir = jwa_dir.joinpath('_site')


ftp = ftplib.FTP('ftp.cluster027.hosting.ovh.net')
ftp.login('jwaclassxd', getpass.getpass())
##
ftp.rmd('www')
ftp.mkd('www')
##


def FtpRmTree(ftp, path):
    """Recursively delete a directory tree on a remote server."""
    wd = ftp.pwd()

    try:
        names = ftp.nlst(path)
    except ftplib.all_errors as e:
        # some FTP servers complain when you try and list non-existent paths
        _log.debug('FtpRmTree: Could not remove {0}: {1}'.format(path, e))
        return

    for name in names:
        if os.path.split(name)[1] in ('.', '..'): continue

        _log.debug('FtpRmTree: Checking {0}'.format(name))

        try:
            ftp.cwd(name)  # if we can cwd to it, it's a folder
            ftp.cwd(wd)  # don't try a nuke a folder we're in
            FtpRmTree(ftp, name)
        except ftplib.all_errors:
            ftp.delete(name)

    try:
        ftp.rmd(path)
    except ftplib.all_errors as e:
        _log.debug('FtpRmTree: Could not remove {0}: {1}'.format(path, e))


for obj in sorted(site_dir.rglob('*')):
    print(obj)


    rel_path = obj.relative_to(site_dir)
    if obj.is_dir():
        print(obj)
    else:
        print("STOR", rel_path)
        ftp.storbinary('STOR ' + obj.name, open(str(obj), 'rb'))



##
ftp.quit()