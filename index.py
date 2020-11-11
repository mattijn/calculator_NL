import streamlit as st
from info import header
from info import relations_power_root_log
from info import usage_example
from calculator import calc

link = '[Numbers](https://homepages.cwi.nl/~steven/Talks/2019/11-21-dijkstra/Numbers.pdf)'
st.markdown((
    f'Deze pagina implementeert de rekenmachine zoals beschreven in het boek  {link}. '
    'Het boek _Numbers_ is geschreven door Steven Pemberton, onderzoeker aan CWI-Amsterdam.'
    ))

page_header = st.beta_expander("Klik voor meer infomatie over deze rekenmachine", expanded=False)
with page_header:
    header()

calc = calc()

page_rel_prl = st.beta_expander("Klik voor een overzicht van macht, wortel en log relaties", expanded=False)
with page_rel_prl:
    relations_power_root_log()

examples = st.beta_expander("Klik voor een voorbeeld hoe te gebruiken", expanded=False)
with examples:
    usage_example()