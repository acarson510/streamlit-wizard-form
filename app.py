import streamlit as st 
from st_aggrid import AgGrid
import pandas as pd
import time

from streamlit_lottie import st_lottie
import requests
from PIL import Image


if 'current_view' not in st.session_state:
    st.session_state['current_view'] = 'Grid'

if 'current_step' not in st.session_state:
    st.session_state['current_step'] = 1

if 'queued_file' not in st.session_state:
    st.session_state['queued_file'] = 1

def set_page_view(page):
    st.session_state['current_step'] = 1 
    st.session_state['queued_file'] = None
    st.session_state['current_view'] = page      

def set_form_step(action,step=None):
    if action == 'Next':
        st.session_state['current_step'] = st.session_state['current_step'] + 1
    if action == 'Back':
        st.session_state['current_step'] = st.session_state['current_step'] - 1
    if action == 'Jump':
        st.session_state['current_step'] = step

### new ###
def render_animation():
    animation_response = requests.get('https://assets1.lottiefiles.com/packages/lf20_vykpwt8b.json')
    animation_json = dict()
    
    if animation_response.status_code == 200:
        animation_json = animation_response.json()
    else:
        print("Error in the URL")     
                           
    return st_lottie(animation_json,height=200,width=300)

def simulate_load_snowflake_table():
    success = False
    response_message = ''
    num_rows = 0     
    
    try:
        success = True        
        response_message = 'Success'
        num_rows = 2
    except Exception as e:
        response_message = e
        
    return success,response_message,num_rows

def checkout_form():
    with st.expander('',expanded=True):        
        
        options = ['Traveler Information','Room Information','Summary','Payment Information']        
        radio_cols = st.columns([.25,10])
        step = radio_cols[1].radio(label='',label_visibility='collapsed', options=options,horizontal=True,index=0)                
        if step == 'Traveler Information':
            st.markdown('##### Let\'s start with the basic details.')            
            name_cols = st.columns(2)
            name_cols[0].text_input('**Travler Name**', placeholder='First Name')
            name_cols[1].text_input('Last Name',label_visibility='hidden', placeholder='Last Name')
            st.text_input('**Traveler Email**',placeholder='📧 Your Email')
            f_cols = st.columns(2)                  
            f_cols[1].selectbox('**Traveler Origin**',options=['United States','Canada','Mexico'] )
            f_cols[0].date_input('**Traveler Date of Birth**')
            st.checkbox('Subscribe to our newsletter')
        if step == 'Room Information':
            date_cols =st.columns(3)
            date_cols[0].date_input('Check In Date')
            date_cols[1].date_input('Check Out Date')
            date_cols[2].selectbox('Room Type',options=['Standard','Deluxe','Suite'])
            st.markdown('---')
            option_cols = st.columns(2)
            with option_cols[0]:                                                                
                image = Image.open('assets/desert.jpg')
                st.image(image, caption='Our Desert View',use_column_width=True)
                st.write('**Room, 1 King Bed**')                
                dim_cols = st.columns(2)
                dim_cols[0].write('📏 550 sq ft')
                dim_cols[0].write('🌵 Desert View')
                dim_cols[1].write('👥 Sleeps 2')
                dim_cols[1].write('🛏️ King Size')          
                policy_cols = st.columns(2)          
                policy = policy_cols[0].radio('**Cancellation Policy**',options=['Non-Refundable','Fully Refundable'],horizontal=False,key='option1')
                delta_color, delta_val = ('off',0) if policy == 'Non-Refundable' else ('normal',50)
                base_price = 450
                price = base_price if policy == 'Non-Refundable' else base_price + delta_val                                
                policy_cols[1].metric('**Nightly Price**',value=f'$ {price}',delta_color=delta_color,delta=f'$ {delta_val}')
                st.button('Select',type='primary',key='select_1')
            with option_cols[1]:                
                image = Image.open('assets/ocean.jpg')
                st.image(image, caption='Our Ocean View',use_column_width=True)
                st.write('**Room, 2 Full Beds**')                
                dim_cols = st.columns(2)
                dim_cols[0].write('📏 600 sq ft')
                dim_cols[0].write('🏖️ Ocean View')
                dim_cols[1].write('👥 Sleeps 4')
                dim_cols[1].write('🛏️ Full Size')                                    
                policy_cols = st.columns(2)                
                policy = policy_cols[0].radio('**Cancellation Policy**',options=['Non-Refundable','Fully Refundable'],horizontal=False,key='option2')
                delta_color, delta_val = ('off',0) if policy == 'Non-Refundable' else ('normal',50)
                base_price = 450
                price = base_price if policy == 'Non-Refundable' else base_price + delta_val                
                policy_cols[1].metric('**Nightly Price**',value=f'$ {price}',delta_color=delta_color,delta=f'$ {delta_val}')#,label_visibility='hidden'
                st.button('Select',type='primary',key='select_2')                                  

        if step == 'Summary': 
            st.markdown('---')            
            st.write('**Traveler Information**')
            summ_cols = st.columns(2)           
            summ_cols[0].text_input('**Travler Full Name**', placeholder='First Name',disabled=True)            
            summ_cols[1].text_input('**Traveler Email**',placeholder='Your Email',disabled=True)       
            f_cols = st.columns(2)                  
            f_cols[1].text_input('**Traveler Origin**',disabled=True,placeholder='United States')
            f_cols[0].date_input('**Traveler Date of Birth**',disabled=True)                                         
            st.write('**Arrival & Departure Information**')
            date_cols =st.columns(2)
            date_cols[0].date_input('**Arrival Date**',disabled=True)
            date_cols[1].date_input('**Departure Date**',disabled=True)                        
            st.write('**Room Information**')
            room_cols = st.columns(2)
            room_cols[0].text_input('**Room Type**',disabled=True,placeholder='Standard')
            room_cols[1].text_input('**Beds**',disabled=True,placeholder='1 King')

        if step == 'Payment Information':
            st.text_input('**Credit Card Information**',placeholder='Card Number')
            exp_cols = st.columns(2)
            exp_cols[0].text_input('',placeholder='Expires',label_visibility='collapsed')
            exp_cols[1].text_input('',placeholder='CVV',label_visibility='collapsed')
            st.text_input('**Billing Address**',placeholder='Address 1')
            st.text_input('',placeholder='Address 2',label_visibility='collapsed')
            st.text_input('',placeholder='Postal Code',label_visibility='collapsed')
            footer_cols = st.columns([5,1])                 
            agreed = footer_cols[0].checkbox('I agree to terms and conditions')
            footer_cols[1].button('Submit',type='primary',key='submit_btn',disabled=not agreed)

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

    ###### Step 1: Warehouses ######
    if st.session_state['current_step'] == 1:            
        st.markdown('\n')
        st.markdown('\n')
        warehouses = ['DATA_LOADING_WH','ANALYTICS_WH','DATA_SCIENCE_WH']
        warehouse = st.selectbox('Which warehouse do you want to use to load the files?',options=warehouses,index=0)

    ###### Step 2: File Format ######
    if st.session_state['current_step'] == 2:
        st.markdown('\n')
        st.markdown('\n')
        file_format_cols = st.columns([9,1])                                
        file_format = file_format_cols[0].selectbox('File Format',options=['csv_format'])
        file_format_cols[1].markdown('\n')
        file_format_cols[1].markdown('\n')
        file_format_cols[1].button('➕')        
        show_sql = st.radio('Show SQL',options=['Yes','No'],index=1,horizontal=True)
        if show_sql == 'Yes':                
            code = f'''PUT file://<file_path>/<file_name> @{st.session_state['table']}/ \n\nCOPY INTO "SANDBOX"."DATA_LOADING"."{st.session_state['table']}" FROM @/ui1675186369009\nON_ERROR = 'SKIP_FILE_0' PURGE = TRUE;'''
            st.code(code, language='plsql')            

    ###### Step 3: Load Options ######            
    if st.session_state['current_step'] == 3:                      
        st.session_state['load_options'] = st.radio('What should the load do if it encounters an error while parsing a file?',
                options=[
                    'Do not load any data in the file',
                    'Stop loading, rollback and return the error',                        
                    'Continue loading valid data from the file',
                    'Do not load any data in the file if the error count exceeds:'
                    ],
                    index=1,
                    horizontal=False
            )
        threshold_disabled = True if st.session_state['load_options'] == 'Do not load any data in the file if the error count exceeds:' else False
        number_input_cols = st.columns(4)
        number_input_cols[0].number_input('File',step=1,label_visibility='collapsed',disabled=not threshold_disabled)      

    ###### Step 4: Source Files ######
    if st.session_state['current_step'] == 4:            
        source_file_container = st.empty()
        with source_file_container.container():
            st.markdown('\n')
            st.markdown('\n')                                
            st.session_state['queued_file'] = st.file_uploader('From where do you want to load files?')

            if st.session_state['queued_file'] is not None:
                table_rows = pd.read_csv(st.session_state['queued_file'])                      
            
    st.markdown('---')
    
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
         
    if load_file:
        source_file_container.empty()
        form_footer_container.empty()        
        with st.spinner('Loading file ...'):  
            time.sleep(3)                  
            success, response_message, num_rows = simulate_load_snowflake_table()
            file_name = st.session_state['queued_file'].name

            if success:                                                                                            
                st.success(f'✅  Successfully loaded {num_rows} rows from file {file_name}.')                    
            else:                         
                st.error(f'❌  Failed to load {num_rows} rows from file {file_name}.')
                                
            ok_cols = st.columns(8)
            ok_cols[0].button('OK',type='primary',on_click=set_page_view,args=['Grid'],use_container_width=True)                                          

def wizard_form_body_animation():

    ###### Step 1: Warehouses ######
    if st.session_state['current_step'] == 1:            
        st.markdown('\n')
        st.markdown('\n')
        warehouses = ['DATA_LOADING_WH','ANALYTICS_WH','DATA_SCIENCE_WH']        
        warehouse = st.selectbox('Which warehouse do you want to use to load the files?',options=warehouses,index=0)            

    ###### Step 2: File Format ######
    if st.session_state['current_step'] == 2:
        st.markdown('\n')
        st.markdown('\n')
        file_format_cols = st.columns([9,1])                                
        file_format = file_format_cols[0].selectbox('File Format',options=['csv_format'])
        file_format_cols[1].markdown('\n')
        file_format_cols[1].markdown('\n')
        file_format_cols[1].button('➕')        
        show_sql = st.radio('Show SQL',options=['Yes','No'],index=1,horizontal=True)
        if show_sql == 'Yes':                
            code = f'''PUT file://<file_path>/<file_name> @{st.session_state['table']}/ \n\nCOPY INTO "SANDBOX"."DATA_LOADING"."{st.session_state['table']}" FROM @/ui1675186369009\nON_ERROR = 'SKIP_FILE_0' PURGE = TRUE;'''
            st.code(code, language='plsql')            

    ###### Step 3: Load Options ######            
    if st.session_state['current_step'] == 3:                      
        st.session_state['load_options'] = st.radio('What should the load do if it encounters an error while parsing a file?',
                options=[
                    'Do not load any data in the file',
                    'Stop loading, rollback and return the error',                        
                    'Continue loading valid data from the file',
                    'Do not load any data in the file if the error count exceeds:'
                    ],
                    index=1,
                    horizontal=False
            )
        threshold_disabled = True if st.session_state['load_options'] == 'Do not load any data in the file if the error count exceeds:' else False
        number_input_cols = st.columns(4)
        number_input_cols[0].number_input('File',step=1,label_visibility='collapsed',disabled=not threshold_disabled)      

    ###### Step 4: Source Files ######
    if st.session_state['current_step'] == 4:            
        source_file_container = st.empty()
        with source_file_container.container():
            st.markdown('\n')
            st.markdown('\n')                                
            st.session_state['queued_file'] = st.file_uploader('From where do you want to load files?')

            if st.session_state['queued_file'] is not None:
                table_rows = pd.read_csv(st.session_state['queued_file'])                      
            
    st.markdown('---')
    
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
         
    if load_file:
        source_file_container.empty()
        form_footer_container.empty()
        response_container = st.empty()                                    
        with response_container.container():
            progress_bar_cols = st.columns([2,5,2])                                
            with progress_bar_cols[1]:                                                                            
                my_bar = st.progress(0, text='')
                render_animation()                    
                for percent_complete in range(100):
                    time.sleep(0.05)
                    my_bar.progress(percent_complete + 1, text='**Please hang on tight while your data loads to Snowflake.**')
                                        
        success, response_message, num_rows = simulate_load_snowflake_table() 
        
        with response_container.container():
            file_name = st.session_state['queued_file'].name
            if success:                                                                                            
                st.success(f'✅  Successfully loaded {num_rows} rows from file {file_name}.')                    
            else:                         
                st.error(f'❌  Failed to load {num_rows} rows from file {file_name}.')
                            
            ok_cols = st.columns(8)
            ok_cols[0].button('OK',type='primary',on_click=set_page_view,args=['Grid'],use_container_width=True)        

### Replace Render Wizard View With This ###
def render_wizard_view():
    with st.expander('',expanded=True):
        wizard_form_header()
        wizard_form_body()

def render_wizard_view_with_animation():
    with st.expander('',expanded=True):
        wizard_form_header()
        wizard_form_body_animation()

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
    header_cols = st.columns([1,6])    
    header_cols[0].image('assets/streamlit.png')
    header_cols[1].header('Streamlit Wizard Form')
    tables = get_table_grid()
    table_selected = True if len(tables['selected_rows']) == 0 else False
    
    if not table_selected:        
        st.session_state['table'] = tables['selected_rows'][0]['Table Name']
    st.button('Load Table',on_click=set_page_view,args=['Form'], disabled=table_selected,type='primary')

##### view rendering logic ####
if st.session_state['current_view'] == 'Grid':     
    render_grid_view()
else:
    form_example = st.selectbox('Which form example would you like to see?',options=['Snowflake Data Loader','Checkout Form'])
    if form_example == 'Snowflake Data Loader':
        render_wizard_view()
    else:
        checkout_form()
