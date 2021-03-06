## Mineral Prediction App

Web app for basic mineral prediction using XPL, from eight classes using deep learning (transfer learning using MobileNet), the eight classes are:

- Biotite
- Hornblende
- Plagioclase
- Olivine
- Pyroxene
- Muscovite
- Quartz
- Alkali Feldspar

### Demo

Short demo of how it works:

<img src="demo_app.gif" width="750" height="480"/>

### Local use

Using streamlit as frontend, clone the repo and run it with the following command:

Requirements are:

- streamlit==0.61.0
- numpy==1.16.5
- pillow==7.2.0
- tensorflow

Alternatively run for the dependencies:

```bash
pip install -r requirements.txt
```

Clone the repo and run the following command:

```bash
streamlit run app.py
```

## Author

Iván E. Ferreira - Unal Bogotá

## License

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
