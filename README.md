## Streamlit Wizard Form

A very simple Streamlit wizard form using session state to navigate along steps for data entry and loading. A few practical examples below including Snowflake's Classic Console Load Table wizard, a standard checkout form, and adding a custom animated spinner. While these are the examples I used, the pattern can transfer to almost any use case requiring more complex user input, which is better served from multiple views and a variation of widgets.

## Snowflake Table Loading Wizard

https://user-images.githubusercontent.com/104647198/219062371-f1834b0f-205a-49e7-9125-be1625cd9060.mp4

## Custom Animated Spinner

https://user-images.githubusercontent.com/15848721/229832305-39b7436f-b9cc-4e1f-93cc-9934b75380e8.mp4

## Checkout Form

https://user-images.githubusercontent.com/15848721/229832416-1a4a1ac0-147b-4b30-85f5-bc33ed3e6953.mp4

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
