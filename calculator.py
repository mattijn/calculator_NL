import streamlit as st
import sessionstore
from evaluate import eval

store = sessionstore.get(display=[], eval=[], refresh=True)
  
def calc():
    global store
    def reset_store():
        global store
        store.display.clear()
        store.eval.clear()

    if store.refresh is True:
        reset_store()
        store.refresh = False

    def pop_store():
        global store
        if len(store.display):
            del store.display[-1]
            del store.eval[-1]
            display_string = ''.join(store.display)
            
            output_field.write(display_string)

    def append_store(item_disp, item_eval=None):
        global store
        store.display.append(item_disp)
        if not item_eval:
            item_eval = item_disp
        
        store.eval.append(item_eval)      
        output_field.write(''.join(store.display))    

    output, info_state, = st.beta_columns((3,3))
    output_field = output.empty()
    info_state.write('klik eerst op `AC`')

    answer, delete, ac = st.beta_columns((3,1,2))
    answer_field = answer.empty()
    del_buttion = delete.button('⌫')
    ac_button = ac.button('AC')

    seven, eight, nine, bracket_l, bracket_r, _ = st.beta_columns(6)
    seven_button = seven.button('7')
    eight_button = eight.button('8')
    nine_button = nine.button('9') 
    bracket_l_button = bracket_l.button('(')
    bracket_r_button = bracket_r.button(')')    
        
    four, five, six, pwr_up, pwr_down, pwr_db_down = st.beta_columns(6)
    four_button = four.button('4')
    five_button = five.button('5')
    six_button = six.button('6')
    pwr_up_button = pwr_up.button('↑') 
    pwr_down_button = pwr_down.button('↓')
    pwr_db_down_button = pwr_db_down.button('⇓')   

    one, two, three, multi, divi, _ = st.beta_columns(6)
    one_button = one.button('1')
    two_button = two.button('2')
    three_button = three.button('3')
    multi_button = multi.button('x')   
    divi_button = divi.button('÷')     

    zero, dot, equals, plus, minus, _ = st.beta_columns(6)
    zero_button = zero.button('0')
    dot_button = dot.button('.')
    equals_button = equals.button('=')
    plus_button = plus.button('+')
    minus_button = minus.button('-')   

    if ac_button:
        output_field.write('')
        answer_field.write(' ')
        reset_store()

    if del_buttion:
        pop_store()

    if one_button:
        append_store('1')

    if two_button:
        append_store('2')

    if three_button:
        append_store('3')

    if four_button:
        append_store('4')

    if five_button:
        append_store('5')

    if six_button:
        append_store('6')

    if seven_button:
        append_store('7')

    if eight_button:
        append_store('8')

    if nine_button:
        append_store('9')

    if zero_button:
        append_store('0')

    if dot_button:
        append_store('.') 

    if plus_button:
        append_store('+')

    if minus_button:
        append_store('-') 

    if multi_button:
        append_store('x', '*') 

    if divi_button:
        append_store('÷', '/')

    if pwr_up_button:
        append_store('↑')

    if pwr_down_button:
        append_store('↓')

    if pwr_db_down_button:
        append_store('⇓')

    if bracket_l_button:
        append_store('(')

    if bracket_r_button:
        append_store(')')        

    if equals_button:
        answer_field.write(eval(''.join(store.eval)))
        output_field.write(''.join(store.display))
    
# optrekken
# aftrekken
# vermenigvuldigen 
# delen
# macht omhoog
# macht omlaag
# dubbel macht omlaag