from pfc import *


class MainCF(Configurator):
    """
    Class for configuring the logical part of main.cf
    """

    def __init__(self):
        super(MainCF, self).__init__()

        self.target_file = '/etc/postfix/main.cf'
        self.snippet_dir = '/etc/postfix/main.cf.d'
