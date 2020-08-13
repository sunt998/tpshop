import yaml
def yml_data_with_file(file_name,key):
    with open("./data/"+file_name+".yml",'r',encoding='utf-8') as f:
       data_list=[]
       for data in yaml.load(f)[key].values():
           #print(data)
           data_list.append(data)
           # print(data_list)
           # print('**************')

       return data_list

if __name__ == '__main__':
    data_list=yml_data_with_file("login_data",'test_login')
    print(data_list)