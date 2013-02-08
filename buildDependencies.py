from __future__ import with_statement
from optparse import OptionParser


def get_command_line_arguments():
    usage = "usage: %prog [options]"
    parser = OptionParser(usage)
    parser.add_option("--spec-file", dest="specfile", type="str")
    parser.add_option("--pyver", dest="pyver", type="choice",
            default="python25", choices=["python25", "python27"])
    return parser.parse_args()


def get_build_requires(options):
    spec_filename = options.specfile
    build_requires_list = None
    with open(spec_filename, "r") as specfile:
        for line in specfile.readlines():
            if line.startswith("BuildRequires:"):
                build_requires_list = line
                break
    if not build_requires_list:
        raise Exception("No BuildRequires found in %s" % spec_filename)
    return build_requires_list


def format_package(pyver, package):
    # get rid of whitespace around it.
    package = package.strip()
    # insert the correct python version
    package = package.replace("%{python_package}", pyver)
    # test if operator in the name.
    version = None
    for operator in [">=", "<=", "="]:
        if operator in package:
            package_version = package.split(operator)
            package = package_version[0]
            version = package_version[1]
    if version:
        return "%s-%s" % (package.strip(), version.strip())
    return package.strip()


def parse_build_requires(options, build_requires):
    # remove the BuildRequires
    build_requires = build_requires.replace("BuildRequires:", "")
    packages = build_requires.split(",")
    packages = [format_package(options.pyver, package)
            for package in packages]
    return packages


if __name__ == "__main__":
    (options, args) = get_command_line_arguments()
    build_requires = get_build_requires(options)
    packages = parse_build_requires(options, build_requires)
