import subprocess

def install_packages(*package_names):
    for package_name in package_names:
        try:
            # Check if package is installed
            subprocess.check_call(['pip', 'freeze>
            print(package_name + '\033[1;31m is a>
        except subprocess.CalledProcessError:
            # If package is not installed, instal>
            subprocess.check_call(['pip', 'instal>
            print(package_name + '\033[1;31m has >

# List of packages to install
packages = ['requests', 'pyshorteners', 'instaloa>

# Install packages
install_packages(*packages)
