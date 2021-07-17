import sqlite3
import streamlit as st
import hashlib
def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()
def check_hashes(password,hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False
conn=sqlite3.connect('data.db')
c=conn.cursor()
def create_usertable():
   
        
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT Primary Key,password TEXT,name TEXT,email_id EMAILS)')
def add_userdata(username,password,name,email):
    conn=sqlite3.connect('data.db')
    cur=conn.cursor()
    if cur.execute('SELECT * FROM userstable WHERE username=?',(username,)):
        if cur.fetchone():
            st.warning('Error User Already Exist Try with Another Username')
        else:
            conn.execute('INSERT INTO userstable(username,password,name,email_id) VALUES(?,?,?,?)',(username,password,name,email))
            st.success("You have successfully created a valid account")
            st.info("go to login menu to login")
            
    conn.commit()
    conn.close()
    
def login_user(username,password):
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
    data=c.fetchall()
    return data


def generate_login_block():
    block1 = st.empty()
    block2 = st.empty()

    return block1, block2


def clean_blocks(blocks):
    for block in blocks:
        block.empty()
def login1(blocks):
    blocks[0].markdown("""
            <style>
                input {
                    -webkit-text-security: disc;
                }
            </style>
        """, unsafe_allow_html=True)

    return blocks[1].text_input('USERNAME')





def login2(blocks):
    blocks[0].markdown("""
            <style>
                input {
                    -webkit-text-security: disc;
                }
            </style>
        """, unsafe_allow_html=True)

    return blocks[1].text_input('PASSWORD')



def main():
    st.title("Home budget prediction")
    menu = ["Login","SignUp"]
    choice = st.sidebar.selectbox("Menu",menu)
    if choice=='Login':
        st.subheader("Login Section")
        
        blk1=generate_login_block()
        blk2=generate_login_block()
        username=login1(blk1)
        password=login2(blk2)
        #username = st.sidebar.text_input("User Name")
        #password = st.sidebar.text_input("Password",type='password')
        if st.sidebar.checkbox("Login"):
            
            create_usertable()
            hashed_pswd = make_hashes(password)
            result=login_user(username,check_hashes(password, hashed_pswd))
            if result:
                
                st.success("Logged in as {}".format(username))
                clean_blocks(blk1)
                clean_blocks(blk2)
                st.write("Get your prediction now [link](https://share.streamlit.io/ameenafarooq/mini-project-sem-6/main/app2.py)")
            else:
                st.warning("Incorrect username/password")
    else:
        st.subheader("Create New Account")
        new_name=st.text_input("Name")
        new_email=st.text_input('Email Id')
        
        new_user = st.text_input("Username")
        new_password = st.text_input("Password",type='password')
        if st.button('SignUp'):
            create_usertable()
            add_userdata(new_user,make_hashes(new_password),new_name,new_email)
        
            
        
if __name__=='__main__':
    main()
    