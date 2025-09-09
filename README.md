# pefe-agent

- [pefe-agent](#pefe-agent)
  - [Introduction](#introduction)
  - [Usage](#usage)
    - [Integration into an existing Feature Extractor](#integration-into-an-existing-feature-extractor)
    - [Get the loader ready](#get-the-loader-ready)
    - [Run the module](#run-the-module)


## Introduction

The library to integrate mass feature
extraction into any existing (Python)
feature extractor code.

Refer to [`pefe-loader`](https://github.com/pefe-system/pefe-loader)
to understand the architecture.

## Usage

### Integration into an existing Feature Extractor

Create a Python module that uses the feature
extractor to extract features from a PE file
with given path, like this:

```python
from pefe_agent.consumer import PEFEConsumer

class MyPEFEConsumer(PEFEConsumer):
    def handle_pe_file(self, path):
        feature_vector = self.extract_features_from_PE_file_at_path(path)
        # could be UUID or file hash or whatever,
        # should be unique
        id = self.generate_PE_file_id(path)

        return id, feature_vector

def main():
    name = "MyPEFEConsumer"
    MyPEFEConsumer(name).run()

if __name__ == "__main__":
    main()
```

You write the methods `extract_features_from_PE_file_at_path`
and `generate_PE_file_id` yourself, in alignment with
the feature extractor being integrated.

### Get the loader ready

As instructed in the documentation of `pefe-loader`,
configure and run a `pefe-loader` instance
so that it iterates over directories of benign and
malware PE files.

### Run the module

Remember the Python module that runs the feature
extractor - the one that you just created earlier?

In the same directory as that of this Python
module, create a new file named `config.json`.

Copy [everything from here](./config.example.json)
to that file and configure the variables as
appropriate. The loader host and port shall be the
same as what you have configured in `pefe-loader`
previously.

Then run the module.

For example,

- If that module is a single file named `ember2024pefe.py`
    in directory `$DIR`:

    - Create `config.json` under directory `$DIR`
    - Run

        ```sh
        cd $DIR
        python ember2024pefe.py
        ```

- If that module is a directory i.e. with `__init__.py`
    and `__main__.py` inside: suppose that directory's
    full path is `$DIR/ember2024pefe`:

    - Create `config.json` under directory `$DIR`
    - Run

        ```sh
        cd $DIR
        python -m ember2024pefe
        ```
