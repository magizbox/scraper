from os import listdir
from jinja2 import Template
from os.path import dirname, join

current_directory = dirname(__file__)
template = open(join(current_directory, "report.template")).read().decode("utf-8")
template = Template(template)
num_documents = len(listdir(join(dirname(current_directory), "data")))
content = template.render(num_documents=num_documents)
report_file = join(dirname(dirname(current_directory)), "README.md")
open(report_file, "w").write(content.encode("utf-8"))
