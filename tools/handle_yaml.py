import yaml
import pprint


def get_yaml_data(filedir):
    resList = []
    # 从磁盘读到---内存
    fo = open(filedir, 'r', encoding="utf-8")
    # 使用yaml方法获取数据
    res = yaml.load(fo, Loader=yaml.FullLoader)
    fo.close()
    common = res[0]
    del res[0]
    for one in res:
        resList.append((one['data'], one['resp']))
    return resList


if __name__ == '__main__':
    res = get_yaml_data('../data/loginCase.yaml')
    print(res)