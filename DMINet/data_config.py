
class DataConfig:
    data_name = ""
    root_dir = ""
    label_transform = "norm"
    def get_data_config(self, data_name):
        self.data_name = data_name
        #if data_name == 'LEVIR':
            #self.root_dir = 'D:/data/CD/LEVIR/'  # Your Path
            #self.root_dir = '/data/CD/LEVIR/'
            #self.root_dir = '/content/gdrive/MyDrive/Courses/CS_5824_AML/Project1/DMINet/data/CD/LEVIR/'
        #if data_name == 'LEVIR':
            #self.root_dir = 'D:/data/CD/LEVIR/'  # Your Path
            #self.root_dir = '/data/CD/LEVIR/'
            #self.root_dir = '/content/gdrive/MyDrive/Courses/CS_5824_AML/Project1/DMINet/data/CD/LEVIR_Plus/'
        if data_name == 'LEVIR':
            #self.root_dir = 'D:/data/CD/LEVIR/'  # Your Path
            #self.root_dir = '/data/CD/LEVIR/'
            self.root_dir = '/content/gdrive/MyDrive/Courses/CS_5824_AML/Project1/DMINet/data/CD/CLCD/'
        elif data_name == 'WHU':
            self.root_dir = 'D:/data/CD/WHU/'
        elif data_name == 'GT':
            self.root_dir = 'D:/data/CD/GT/'    
        elif data_name == 'quick_start':
            #self.root_dir = './samples/'
            self.root_dir = 'C:/Users/Sabiha/Downloads/DMINet-main/DMINet-main/samples/'
        else:
            raise TypeError('%s has not defined' % data_name)
        return self


if __name__ == '__main__':
    #data = DataConfig().get_data_config(data_name='LEVIR')
    data = DataConfig().get_data_config(data_name='LEVIR_Plus')

    #data = DataConfig().get_data_config(data_name='quick_start')
    # print(data.data_name)
    # print(data.root_dir)
    # print(data.label_transform)

