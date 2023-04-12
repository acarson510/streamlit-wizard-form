import streamlit as st 
from st_aggrid import AgGrid
import pandas as pd

if 'current_view' not in st.session_state:
    st.session_state['current_view'] = 'Grid'

if 'current_step' not in st.session_state:
    st.session_state['current_step'] = 1


def set_page_view(page):
    st.session_state['current_view'] = page
    st.session_state['current_step'] = 1         

def set_form_step(action,step=None):
    if action == 'Next':
        st.session_state['current_step'] = st.session_state['current_step'] + 1
    if action == 'Back':
        st.session_state['current_step'] = st.session_state['current_step'] - 1
    if action == 'Jump':
        st.session_state['current_step'] = step


##### wizard functions ####
def wizard_form_header():
    sf_header_cols = st.columns([1,1.75,1])
        
    with sf_header_cols[1]:            
        st.subheader('Load Data to Snowflake')
            
    # determines button color which should be red when user is on that given step
    wh_type = 'primary' if st.session_state['current_step'] == 1 else 'secondary'
    ff_type = 'primary' if st.session_state['current_step'] == 2 else 'secondary'
    lo_type = 'primary' if st.session_state['current_step'] == 3 else 'secondary'
    sf_type = 'primary' if st.session_state['current_step'] == 4 else 'secondary'

    step_cols = st.columns([.5,.85,.85,.85,.85,.5])    
    step_cols[1].button('Warehouses',on_click=set_form_step,args=['Jump',1],type=wh_type)
    step_cols[2].button('File Format',on_click=set_form_step,args=['Jump',2],type=ff_type)        
    step_cols[3].button('Load Options',on_click=set_form_step,args=['Jump',3],type=lo_type)      
    step_cols[4].button('Source Files',on_click=set_form_step,args=['Jump',4],type=sf_type)
        
### Replace Wizard Form Body with this ###
def wizard_form_body():
    st.write(st.session_state['current_step'])                   

def wizard_form_footer():    
    form_footer_container = st.empty()
    with form_footer_container.container():
        
        disable_back_button = True if st.session_state['current_step'] == 1 else False
        disable_next_button = True if st.session_state['current_step'] == 4 else False
        
        form_footer_cols = st.columns([5,1,1,1.75])
        
        form_footer_cols[0].button('Cancel',on_click=set_page_view,args=['Grid'])
        form_footer_cols[1].button('Back',on_click=set_form_step,args=['Back'],disabled=disable_back_button)
        form_footer_cols[2].button('Next',on_click=set_form_step,args=['Next'],disabled=disable_next_button)
    
        
        file_ready = False if st.session_state['queued_file'] is not None else True
        load_file = form_footer_cols[3].button('📤 Load Table',disabled=file_ready)   

### Replace Render Wizard View With This ###
def render_wizard_view():
    with st.expander('',expanded=True):
        wizard_form_header()
        st.markdown('---')
        wizard_form_body()
        st.markdown('---')
        wizard_form_footer()


##### grid functions ####
def get_table_grid():
	data = {   "Table Name": ["Product", "Employee", "Customer"] ,"Schema": ["Salesforce", "Salesforce", "Salesforce"],"Rows": [200, 300, 400]}
	df = pd.DataFrame(data=data)

	gridOptions = {
		"rowSelection": "single",        
    "columnDefs": [
	    {   "field": "Table Name", "checkboxSelection": True   },
      {   "field": "Schema"  },
      {   "field": "Rows" }
		]
	}

	return AgGrid(
        df,        
        gridOptions=gridOptions,
        fit_columns_on_grid_load=True,
        theme="balham"
    )

def render_grid_view():
    st.header('Streamlit Wizard Form')
    tables = get_table_grid()
    table_selected = True if len(tables['selected_rows']) == 0 else False
    
    if not table_selected:        
        st.session_state['table'] = tables['selected_rows'][0]['Table Name']
    st.button('Load Table',on_click=set_page_view,args=['Form'], disabled=table_selected,type='primary')

##### view rendering logic ####
if st.session_state['current_view'] == 'Grid':     
    render_grid_view()
else:
    render_wizard_view()
