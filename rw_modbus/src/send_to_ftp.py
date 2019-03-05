# library to send to FTP

from ftplib import FTP
import logging

def ftp_connect(host, username, password, timeout):
    ftp = FTP()
    ftp.set_debuglevel(2)
    logging.info(ftp.connect(host, 21, timeout=timeout))
    logging.info(ftp.login(username, password))
    return ftp

def ftp_upload(ftp, remote_path, local_file, remote_filename):
    logging.info(ftp.cwd(remote_path))
    with open(local_file, "rb") as f:
        logging.info(ftp.storbinary('STOR '+remote_filename, f))

def ftp_logout(ftp):
    logging.info(ftp.quit())
    ftp.close()
