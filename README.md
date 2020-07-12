### Fine-tuned version RobBERT Dutch book reviews

In this repository you will fine the code used to fine tune RobBERT by Pieter Delobelle et al. on Dutch book reviews for my thesis on auditing algorithms.

The code to train the model can be found in `RobBERT-finetuned > finetune_dbrd.ipynb`.
The data used to train the model can be found in the data map. 
For testing, BERTje was used, the code to load in the model and test it on examples can be found in the file `test_bias.ipynb` in the RobBERT-finetuned folder.

The initial model is released under the MIT license and accompanied by the paper by Delobelle et al. 

```
@misc{delobelle2020robbert,
    title={RobBERT: a Dutch RoBERTa-based Language Model},
    author={Pieter Delobelle and Thomas Winters and Bettina Berendt},
    year={2020},
    eprint={2001.06286},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```