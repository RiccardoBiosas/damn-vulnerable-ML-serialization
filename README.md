# Model Serialization Attacks PoC

## Install
- The project uses Poetry:
```sh
curl -sSL https://install.python-poetry.org | python3 -
```
- Install dependencies
```sh
poetry install
```

## Serialize/Deserialize the models
```sh
poetry run python unsafe_torch.py
poetry run python unsafe_tf.py
poetry run python unsafe_pickle.py
```

## Scan The Models
- **ModelScan**
```sh
poetry run modelscan -p damn_vuln_torch_model.pt
poetry run modelscan -p damn_vuln_tf_model.h5
poetry run modelscan -p damn_vuln_pickle_model.pkl
```

- **Fickling**
```sh
poetry run fickling --check-safety --print-result damn_vuln_torch_model.pt
poetry run fickling --check-safety --print-result damn_vuln_pickle_model.pkl
```
