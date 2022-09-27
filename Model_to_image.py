import cv2
import joblib
import pickle
import numpy
from LoadData import LoadData


class Detection_tumor:
    def __init__(self, model = joblib.load('trained_model.sav')):
        self.data = LoadData ()
        self.patient_Information = self.data.get_Information()

        self.img = self.data.get_Image()
        self.img_cv = cv2.cvtColor(numpy.array(self.img.convert('RGB'))[:,:,::-1].copy(), cv2.COLOR_BGR2GRAY)
        self.model = model
        self.key = {0: 'No Tumor', 1: 'Pituriaty tumor', 2: 'Glioma tumor', 3: 'Meningioma tumor'}

    def prepare_image(self):
        self.prepare_image = cv2.resize(self.img_cv, (200,200))
        self.prepare_image = self.prepare_image.reshape(1,-1)/255
        return self.prepare_image

    def what_kind_tumor(self):
        return self.key[self.model.predict(Detection_tumor.prepare_image(self))[0]]

    def probability_diagnose(self):
        return round(self.model.predict_proba(Detection_tumor.prepare_image(self)).max() * 100,2)

    def array_probability(self):
        text = []
        data = self.model.predict_proba(Detection_tumor.prepare_image(self)) * 100
        for i in range(len(self.key)):
            text.append(str(self.key[i]) + ' : ' + str(round(data[0][i],2)) +" %" )
        return text

    def print_information(self):
        information = ("First name : " + self.patient_Information[1] +
                       "\n\nLast name : " + self.patient_Information[2] +
                       "\n\nAge : " + self.patient_Information[3] +
                        "\n\nDiagnose : " + self.what_kind_tumor() +
                       "\n\nProbabilities : " + str(self.probability_diagnose()) + " %" +
                       "\n\n" + self.array_probability()[0]+
                       "\n\n" +self.array_probability()[1] +
                       "\n\n" +self.array_probability()[2] +
                        "\n\n" + self.array_probability()[3]
                       )
        return information

    def get_image(self):
        return self.img


