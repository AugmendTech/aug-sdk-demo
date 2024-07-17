# aug-sdk-demo

This project is a demo of the [aug-sdk](https://github.com/AugmendTech/aug-sdk) python package, showing how you can easily analyze videos with the Augmend API.

To use this project, create an API key at [https://augmend.com/settings](https://augmend.com/settings) and set this as the AUGMEND_API_KEY environment variable, or create a .env file with the same information.

You can run the project by installing the dependencies via pip or rye.

```
pip install -r requirements.txt
```

Then you can run the script via python:

```
cd src
python -m aug_sdk_demo myfile.mp4
```