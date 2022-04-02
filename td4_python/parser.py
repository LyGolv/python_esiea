from argparse import ArgumentParser

class Parser(ArgumentParser):
    def __init__(self):
        super().__init__()
            
    def add_args(self):
        self.add_argument(
            "-c",
            "--config", 
            required=True, 
            dest="config",
            help="Add config file"
        )                
        self.add_argument(
            "-l",
            "--logfile", 
            required=True,
            help="Add logs file"
        )
        self.add_argument(
            "-d",
            "--directory",
            help="Specify directory where your files are contained " 
            "(but it's necessary to use directory contained on your runtime directory)"
        )
        return self