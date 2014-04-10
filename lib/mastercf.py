from pfc import *


class MasterCF(Configurator):
    """
    Class for configuring the logical part of master.cf
    """

    def __init__(self):
        super(MasterCF, self).__init__()

        self.target_file = '/etc/postfix/master.cf'
        self.snippet_dir = '/etc/postfix/master.cf.d'
