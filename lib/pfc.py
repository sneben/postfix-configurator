import os
import fnmatch

from time import time
from datetime import datetime


class Configurator(object):
    """
    Base class for the several postfix configurator types
    """

    def __init__(self):
        pass

    def process(self):
        """
        Purpose: Wrap the read and write function
        Results: Nothing
        """

        self.read_snippets()
        self.write()

    def write(self):
        """
        Purpose: Write the content list into the target file
        Results: Nothing
        """

        timestamp = time()
        date = str(datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S'))
        marker = "#POSTFIX-CONFIGURATOR: " + date

        with open(self.target_file, "w") as f:
            f.write("%s\n\n" % marker)
            for line in self.content:
                f.write("%s\n" % line)

    def read_snippets(self):
        """
        Purpose: Determine the cf files, sort their order
                 and then read their content
        Results: Set an array with the aggregated content of
                 final [main|master].cf, returns nothing
        """

        cf_files = []
        for f in fnmatch.filter(os.listdir(self.snippet_dir), "*.cf"):
            cf_files.append(f)

        content = []
        cf_files = sorted(cf_files)
        for cf_file in cf_files:
            with open(self.snippet_dir + '/' + cf_file) as f:
                content = content + [line.rstrip('\n') for line in f] + ['']

        self.content = content

    def read_target_file(self):
        """
        Purpose: Read the whole content from the file specified in target_file
                 and remove the pfc header
        Returns: Set an array with the aggregated content
                 of active [main|master].cf, returns nothing
        """

        content = []
        with open(self.target_file) as f:
            content = [line.rstrip('\n') for line in f] + ['']

        del content[0:2]
        del content[-1]
        self.active_content = content

    def diff(self):
        """
        Purpose: Builds a temporary target configuration file
                 and diffs it with the real one
        Returns: True or False
        """

        self.read_snippets()
        self.read_target_file()
        if self.active_content != self.content:
            return True
        else:
            return False
