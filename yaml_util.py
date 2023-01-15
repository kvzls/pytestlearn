import os
import yaml

# path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "pytestlearn",
#                     "yamlcase/test1_data.yaml")
# print(path)


class YamlUtil:

    def read_data_test(self, yaml_name):
        f = open(os.getcwd() + "/yamlcase/" + yaml_name, encoding="utf8")
        data = yaml.load(stream=f, Loader=yaml.FullLoader)
        return data
    #
    # getdata = read_data_test()
    # print(getdata)
