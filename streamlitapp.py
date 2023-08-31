import streamlit as st
import requests
import ipaddress

def get_client_ip():
    """Gets the IP address of the client."""
    client_ip = st.session_state['client_ip']
    if not client_ip:
        client_ip = request.remote_addr
        st.session_state['client_ip'] = client_ip
    return client_ip

def set_proxy(ip_address):
    """Sets the proxy IP address."""
    proxies = {'http': 'http://{}:80'.format(ip_address), 'https': 'https://{}:80'.format(ip_address)}
    requests.session().proxies = proxies

def scrape_data(url):
    """Scrape data from the specified URL."""
    set_proxy(get_client_ip())
    response = requests.get(url)
    return response.text

url = "https://www.screener.in/company/ADANIENT/consolidated/"
prox = get_client_ip()
st.write("Your IP is" + prox)


