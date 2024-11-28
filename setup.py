from setuptools import setup
from setuptools.command.install import install
import subprocess

class CustomInstall(install):
    def run(self):
        # Run the script as part of the installation
        subprocess.check_call(['bash', './build.sh'])
        super().run()

setup(
    name='streamlit-elements-fluence',
    version='0.1.7',
    cmdclass={'install': CustomInstall},
)
