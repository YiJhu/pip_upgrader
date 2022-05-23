import pkg_resources
from subprocess import call

print(''.join("Start Upgrade\n"))
packages = [dist.project_name for dist in pkg_resources.working_set]
call("pip install --upgrade " + ' '.join(packages), shell=True)
print(''.join("\n\nUpgrade Finish"))