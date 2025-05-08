## Download the dataset

CodeSearchNet dataset can be downloaded from [here](https://huggingface.co/datasets/code_search_net)
数据集放到 data 文件夹中，从 gz 中解压

## Install dependencies
conda install conda install pytorch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 pytorch-cuda=12.1 -c pytorch -c nvidia
conda install transformers
pip install -r requirements.txt
pip install accelerate==0.26.0

## mark
java
python mark.py --language java --dataset_name java --data_path /mnt/disk2/liwei/01-code/CodeMark-FSE/data/java/final/jsonl/train

python mark.py --language python --dataset_name python --data_path /mnt/disk2/liwei/01-code/CodeMark-FSE/data/python/final/jsonl/train


## train
```shell
nohup env CUDA_VISIBLE_DEVICES=2,3 python train.py --run_name=java_b1_100 --train_data_path=$PWD/dataset/java/java_b1_100.pickle --val_data_path=$PWD/data/java/final/jsonl/valid/java_valid_0.jsonl --batch_size=8 --epoch=10 --cache_path=$PWD/cached/gpt2 --output_path=$PWD/outputs/0421-2030-thirsty/models/gpt2_java_b1_100 --model=gpt2 --max_length=256 > $PWD/outputs/0421-2030-thirsty/logs/gpt2_java_b1_100.log 2>&1 &

nohup env CUDA_VISIBLE_DEVICES=4 python train.py --run_name=java_b1_100 --train_data_path=$PWD/dataset/java/java_b1_100.pickle --val_data_path=$PWD/data/java/final/jsonl/valid/java_valid_0.jsonl --batch_size=8 --epoch=25 --cache_path=$PWD/cached/t5 --output_path=$PWD/outputs/0421-2144-skinny/models/t5_java_b1_100 --model=t5 --max_length=256 > $PWD/outputs/0421-2144-skinny/logs/t5_java_b1_100 2>&1 &
```