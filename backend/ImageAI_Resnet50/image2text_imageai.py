from imageai.Prediction import ImagePrediction
import os

def image2text(imagefile):
    execution_path = os.getcwd()
    prediction = ImagePrediction()
    prediction.setModelTypeAsResNet() # choose between Resnet, SqeezeNet, InceptionV3, DenseNet Model
    prediction.setModelPath(os.path.join(execution_path, "resnet50_weights_tf_dim_ordering_tf_kernels.h5")) #weight should be compatible with the model
    prediction.loadModel()

    predictions, probabilities = prediction.predictImage(os.path.join(execution_path, imagefile), result_count=5 )
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        print(eachPrediction, " : " , eachProbability)
    return predictions