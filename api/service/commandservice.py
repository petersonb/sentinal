"""
Wrapper for commands to be sent to remote machine.

Remote machine must posess the public key for this machine.

Author: PetersonB
"""
import subprocess as subp
import simplelog as logger
import sys

USERNAME = "brett"
MACHINE  = "localhost"

def _command(cmd):
    """
    All commands will run through this funciton.
    """
    cmd = "ssh {0}@{1} {2}".format(USERNAME, MACHINE, cmd)
    logger.debug(_command, cmd)
    proc = subp.Popen(cmd.split(), stdout=subp.PIPE)
    return proc.communicate()[0]

def eject():
    """
    Eject, fun to test with, wow your nontechy friends when you call
    this from your phone and your computer 'moves'.
    """
    _command("eject -T")

def shutdown(timeout=0):
    """
    Shutdown the computer

    Requires root access from user. 
    Add user to wheel group and configure sudo file to allow no passwd.
    """
    if timeout != 0:
        _command("sudo halt")
    else:
        _command("sudo shutdown -h +{0}".format(str(timeout)))

if __name__ == '__main__':
    if len(sys.argv) > 2:
        globals()[sys.argv[1]](sys.argv[2])
    else:
        globals()[sys.argv[1]]()
