import os
if 'CITYSCAPES_DATASET' in os.environ:
        csPath = os.environ['CITYSCAPES_DATASET']
        print(csPath)
