## Streamlit Wizard Form

A very simple Streamlit wizard form using session state to navigate along steps for data entry and loading. A few practical examples below including Snowflake's Classic Console Load Table wizard, a standard checkout form, and adding a custom animated spinner. While these are the examples I used, the pattern can transfer to almost any use case requiring more complex user input, which is better served from multiple views and a variation of widgets.

_For further detail, please refer to the [Streamlit blog](https://blog.streamlit.io/streamlit-wizard-form-with-custom-animated-spinner/)_ or [Medium article](https://medium.com/streamlit/streamlit-wizard-and-custom-animated-spinner-2dcd52cccc65)_.


![wizard_main](https://github.com/acarson510/streamlit-wizard-form/assets/15848721/e33c6b5a-6074-4279-ad9d-9c7f13a0ca2f)

![checkout_form](https://github.com/acarson510/streamlit-wizard-form/assets/15848721/4fac7117-5f8d-4525-92d7-07be1598d79c)

## Setup Instructions

**Using Anaconda**

``` bash
conda create --name st_wizard_form python==3.8
```

``` bash
conda activate st_wizard_form 
```
---

**Install Dependencies**
```bash
pip install -r requirements.txt
```
---

**To Verify Streamlit**
```bash 
streamlit hello
```
**If verification succeded press CMD+C or CTRL + C to exit.** 

---

Start your app.
```bash 
streamlit run app.py
```
e enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
