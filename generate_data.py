from __future__ import print_function
import pandas as pd
import numpy as np
from PIL import Image
import os
from tqdm import tqdm


class Generate_data():
    def __init__(self, datapath):
        """
        Generate_data class
        Two methods to be used
        1-split_test
        2-save_images
        [Note] that you have to split the public and private from fer2013 file
        """
        self.data_path = datapath

    def split_test(self, train_filename = 'train', val_filename= 'val', test_filename = 'finaltest'):
        """
        Helper function to split the validation and test data from general test file as it contains (Public test, Private test)
            params:-
                data_path = path to the folder that contains the test data file
        """
        csv_path = self.data_path +"/"+ 'def.csv'
        test = pd.read_csv(csv_path)



        neutral=test[test.emotion==0]
        anger=test[test.emotion==1]
        contempt=test[test.emotion==2]
        disgust=test[test.emotion==3]
        fear=test[test.emotion==4]
        happy=test[test.emotion==5]
        sadness=test[test.emotion==6]
        surprise=test[test.emotion==7]

        total_len = len(test.index.values)

        neutral_len = len(neutral.index.values)
        anger_len = len(anger.index.values)
        contempt_len = len(contempt.index.values)
        disgust_len = len(disgust.index.values)
        fear_len = len(fear.index.values)
        happy_len = len(happy.index.values)
        sadness_len = len(sadness.index.values)
        surprise_len = len(surprise.index.values)

        train_perc=round(70/100*2909)
        val_perc=round(20/100*2909)
        test_perc=round(10/100*2909)


        training_data = pd.DataFrame(anger.iloc[:(round(17.3/100*train_perc)),:])
        training_data.to_csv(self.data_path+"/"+train_filename+".csv")

        training_data=pd.DataFrame(contempt.iloc[:round(4.1/100*train_perc),:])
        training_data.to_csv(self.data_path+"/"+train_filename+".csv", mode='a', header=False)

        training_data=pd.DataFrame(disgust.iloc[:round(14.6/100*train_perc),:])
        training_data.to_csv(self.data_path+"/"+train_filename+".csv", mode='a', header=False)

        training_data=pd.DataFrame(fear.iloc[:round(9.3/100*train_perc),:])
        training_data.to_csv(self.data_path+"/"+train_filename+".csv", mode='a', header=False)

        training_data=pd.DataFrame(happy.iloc[:round(22.7/100*train_perc),:])
        training_data.to_csv(self.data_path+"/"+train_filename+".csv", mode='a', header=False)

        training_data=pd.DataFrame(sadness.iloc[:round(9.4/100*train_perc),:])
        training_data.to_csv(self.data_path+"/"+train_filename+".csv", mode='a', header=False)

        training_data=pd.DataFrame(surprise.iloc[:round(22.6/100*train_perc),:])
        training_data.to_csv(self.data_path+"/"+train_filename+".csv", mode='a', header=False)




        validation_data = pd.DataFrame(anger.iloc[round(17.3/100*train_perc):round(17.3/100*train_perc)+round(17.3/100*val_perc),:])
        validation_data.to_csv(self.data_path+"/"+val_filename+".csv")

        validation_data=pd.DataFrame(contempt.iloc[round(4.1/100*train_perc):round(4.1/100*train_perc)+round(4.1/100*val_perc),:])
        validation_data.to_csv(self.data_path+"/"+val_filename+".csv", mode='a', header=False)

        validation_data=pd.DataFrame(disgust.iloc[round(14.6/100*train_perc):round(14.6/100*train_perc)+round(14.6/100*val_perc),:])
        validation_data.to_csv(self.data_path+"/"+val_filename+".csv", mode='a', header=False)

        validation_data=pd.DataFrame(fear.iloc[round(9.3/100*train_perc):round(9.3/100*train_perc)+round(9.3/100*val_perc),:])
        validation_data.to_csv(self.data_path+"/"+val_filename+".csv", mode='a', header=False)

        validation_data=pd.DataFrame(happy.iloc[round(22.7/100*train_perc):round(22.7/100*train_perc)+round(22.7/100*val_perc),:])
        validation_data.to_csv(self.data_path+"/"+val_filename+".csv", mode='a', header=False)

        validation_data=pd.DataFrame(sadness.iloc[round(9.4/100*train_perc):round(9.4/100*train_perc)+round(9.4/100*val_perc),:])
        validation_data.to_csv(self.data_path+"/"+val_filename+".csv", mode='a', header=False)

        validation_data=pd.DataFrame(surprise.iloc[round(22.6/100*train_perc):round(22.6/100*train_perc)+round(22.6/100*val_perc),:])
        validation_data.to_csv(self.data_path+"/"+val_filename+".csv", mode='a', header=False)





        test_data = pd.DataFrame(anger.iloc[round(17.3/100*train_perc)+round(17.3/100*val_perc):round(17.3/100*train_perc)+round(17.3/100*val_perc)+round(17.3/100*test_perc),:])
        test_data.to_csv(self.data_path+"/"+test_filename+".csv")

        test_data=pd.DataFrame(contempt.iloc[round(4.1/100*train_perc)+round(4.1/100*val_perc):round(4.1/100*train_perc)+round(4.1/100*val_perc)+round(4.1/100*test_perc),:])
        test_data.to_csv(self.data_path+"/"+test_filename+".csv", mode='a', header=False)

        test_data=pd.DataFrame(disgust.iloc[round(14.6/100*train_perc)+round(14.6/100*val_perc):round(14.6/100*train_perc)+round(14.6/100*val_perc)+round(14.6/100*test_perc),:])
        test_data.to_csv(self.data_path+"/"+test_filename+".csv", mode='a', header=False)

        test_data=pd.DataFrame(fear.iloc[round(9.3/100*train_perc)+round(9.3/100*val_perc):round(9.3/100*train_perc)+round(9.3/100*val_perc)+round(9.3/100*test_perc),:])
        test_data.to_csv(self.data_path+"/"+test_filename+".csv", mode='a', header=False)

        test_data=pd.DataFrame(happy.iloc[round(22.7/100*train_perc)+round(22.7/100*val_perc):round(22.7/100*train_perc)+round(22.7/100*val_perc)+round(22.7/100*test_perc),:])
        test_data.to_csv(self.data_path+"/"+test_filename+".csv", mode='a', header=False)

        test_data=pd.DataFrame(sadness.iloc[round(9.4/100*train_perc)+round(9.4/100*val_perc):round(9.4/100*train_perc)+round(9.4/100*val_perc)+round(9.4/100*test_perc),:])
        test_data.to_csv(self.data_path+"/"+test_filename+".csv", mode='a', header=False)

        test_data=pd.DataFrame(surprise.iloc[round(22.6/100*train_perc)+round(22.6/100*val_perc):round(22.6/100*train_perc)+round(22.6/100*val_perc)+round(22.6/100*test_perc),:])
        test_data.to_csv(self.data_path+"/"+test_filename+".csv", mode='a', header=False)

        print("Done splitting the test file into validation & final test file",validation_data)


    def str_to_image(self, str_img = ' '):
        '''
        Convert string pixels from the csv file into image object
            params:- take an image string
            return :- return PIL image object
        '''
        imgarray_str = str_img.split(' ')
        imgarray = np.asarray(imgarray_str,dtype=np.uint8).reshape(48,48)
        return Image.fromarray(imgarray)

    def save_images(self, datatype='train'):
        '''
        save_images is a function responsible for saving images from data files e.g(train, test) in a desired folder
            params:-
            datatype= str e.g (train, val, finaltest)
        '''
        foldername= self.data_path+"/"+datatype
        csvfile_path= self.data_path+"/"+datatype+'.csv'
        if not os.path.exists(foldername):
            os.mkdir(foldername)

        data = pd.read_csv(csvfile_path)
        images = data['pixels'] #dataframe to series pandas
        numberofimages = images.shape[0]
        for index in tqdm(range(numberofimages)):
            img = self.str_to_image(images[index])
            img.save(os.path.join(foldername,'{}{}.jpg'.format(datatype,index)),'JPEG')
        print('Done saving {} data'.format((foldername)))
