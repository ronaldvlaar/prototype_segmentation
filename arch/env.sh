export CITYSCAPES_DATASET='./Cityscapes'

#!/bin/bash -x
PWD=`pwd`
echo $PWD
activate () {
    . $PWD/Scripts/activate
}

activate