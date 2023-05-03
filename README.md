# DeepChange
# Reference Paper and code
Change Detection on Bi-temporal Remote Sensing Images using Dual-branch Multi-level Inter-temporal Network (TGARS 2023) [[paper](https://ieeexplore.ieee.org/document/10034787) and [code](https://github.com/ZhengJianwei2/DMINet)]
# 1. Environment Setup
This code has been executed on a workstation equipped with an Intel Xeon CPU E5-2690 v4 processor and NVIDIA TITAN V GPUs, which have a video memory of 12G. The code was run using Python 3.6, pytorch 1.9, CUDA 10.0, and cuDNN 7.6.
# 2. Dataset
- Levir-CD
- Levir-CD plus
- CLCD dataset
# 3. Setup instructions
```python
pip install -r requirements.txt
```
# 4. Train
```python
python main_cd.py
```
# 5. Test
```python
python eval_cd.py
```
