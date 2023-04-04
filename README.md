## Streamlit Wizard Form

A very simple Streamlit wizard form using session state to navigate along  steps for data entry and loading. The example is modeled after the Classic Console’s Load Table wizard, but can be used in almost any use case requiring more complex  input which are better served from multiple views and a variation of widgets.

https://user-images.githubusercontent.com/104647198/219062371-f1834b0f-205a-49e7-9125-be1625cd9060.mp4


## Setup Instructions

A very simple Streamlit wizard form using session state to navigate along  steps for data entry and loading. The example is modeled after Snowflake's Classic Console’s Load Table wizard, but can be used in almost any use case requiring more complex user input which is better served from multiple views and a variation of widgets.

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
