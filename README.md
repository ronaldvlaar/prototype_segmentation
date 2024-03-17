The first dataset used is the Cityscapes dataset. This dataset can be downloaded from https://www.cityscapes-dataset.com/downloads/. The gtFine_trainvaltest.zip and leftlmgbit_trainvaltest.zip are needed. The domain is image segmentation.


The second dataset is an augmented version of the PASCAL VOC 2012 dataset. The domain is image segmentation. Instruction for downloading the data may be found here https://github.com/kazuto1011/deeplab-pytorch/blob/master/data/datasets/voc12/README.md. The augmented variant (SegmentationAug and SegmentationClassAug) should be downloaded.


The data will be used to train and evaluate a model for image segmentation. We want to improve the ProtoSeg (https://arxiv.org/pdf/2301.12276.pdf) baseline model for image segmentation. This model uses part-prototypes for making its predictions explainable, in contrast too deep learning methods like U-Net and DeepLab.
